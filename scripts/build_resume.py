#!/usr/bin/env python3
"""Build a tailored PDF resume from validated JSON and a fixed LaTeX template.

No third-party Python packages required for building. Requires pdflatex on PATH.
Works with the supplied Resume_template.tex macros.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

# Folder containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

# Parent folder = Resume_Automation
ROOT = SCRIPT_DIR.parent

LIBRARIES = ROOT / "libraries"
TEMPLATE = ROOT / "Resume_template.tex"
OUTPUT = ROOT / "output"


MACROS = ('ResumeSummary', 'ResumeSkills', 'RheemBullets', 'LTTSBullets',
          'UTSABullets', 'OtherExperience', 'Demonstrations')
REQUIRED_EMPLOYERS = ('rheem', 'ltts', 'utsa')
SPECIAL = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
           '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
           '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
UNICODE = {'–': '--', '—': '---', '−': '-', '“': '``', '”': "''",
           '‘': '`', '’': "'", '…': r'\ldots{}', '≥': r'$\geq$',
           '≤': r'$\leq$', '°': r'$^\circ$', '×': r'$\times$',
           '±': r'$\pm$', 'α': r'$\alpha$', 'β': r'$\beta$',
           'μ': r'$\mu$', 'ω': r'$\omega$', '²': r'$^2$', '³': r'$^3$',
           ' ': ' ', '→': r'$\rightarrow$'}

def tex_escape(value):
    if not isinstance(value, str):
        raise ValueError('Expected a plain text string.')
    return ''.join(UNICODE.get(ch, SPECIAL.get(ch, ch)) for ch in value)

def text(value, where):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{where} must contain nonempty text')
    if any(ord(c) < 32 and c not in '\n\t' for c in value):
        raise ValueError(f'{where} contains control characters')
    return value.strip()

def url_tex(value):
    url = text(value, 'demonstration URL')
    p = urlparse(url)
    if p.scheme not in ('http', 'https') or not p.netloc or any(c in url for c in '{}\\\n\r\t '):
        raise ValueError('Invalid or unsafe demonstration URL: ' + url)
    return r'\url{' + url + '}'

def expand_experience_bullets(data):
    """Flatten grouped achievement bullets, preserving accomplishment and bullet order.

    Supported input entries:
      {"source_id": "EXP-001-F", "text": "One original bullet."}
      {"source_id": "EXP-001-F", "bullets": ["First bullet.", "Second bullet."]}

    The existing repeated-source_id format stays valid. Returns a new data object,
    leaving the caller's original JSON unmodified.
    """
    if not isinstance(data, dict):
        raise ValueError('JSON root must be an object')
    result = dict(data)
    experience = data.get('experience')
    if not isinstance(experience, dict):
        return result  # Standard validation will provide the actionable error.
    expanded = dict(experience)
    for employer, entries in experience.items():
        if not isinstance(entries, list):
            continue
        output_entries = []
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                output_entries.append(entry)
                continue
            has_text = 'text' in entry
            has_bullets = 'bullets' in entry
            if has_text == has_bullets:
                raise ValueError(
                    f'experience.{employer}[{i}] must have exactly one of '
                    "'text' or 'bullets'"
                )
            if has_bullets:
                bullets = entry['bullets']
                if not isinstance(bullets, list) or not bullets:
                    raise ValueError(f'experience.{employer}[{i}].bullets must be a nonempty array')
                for j, bullet in enumerate(bullets):
                    text(bullet, f'experience.{employer}[{i}].bullets[{j}]')
                    # Do not strip or rewrite the source bullet.
                    output_entries.append({'source_id': entry.get('source_id'), 'text': bullet})
            else:
                output_entries.append(entry.copy())
        expanded[employer] = output_entries
    result['experience'] = expanded
    return result


def validate_content(data):
    if not isinstance(data, dict):
        raise ValueError('JSON root must be an object')
    text(data.get('summary'), 'summary')
    skills = data.get('skills')
    if not isinstance(skills, list) or not skills:
        raise ValueError('skills must be a nonempty array of {category, items}')
    for i, skill in enumerate(skills):
        if not isinstance(skill, dict):
            raise ValueError(f'skills[{i}] must be an object')
        text(skill.get('category'), f'skills[{i}].category')
        if not isinstance(skill.get('items'), list) or not skill['items']:
            raise ValueError(f'skills[{i}].items must be a nonempty array')
        for value in skill['items']:
            text(value, 'skill item')
    experience = data.get('experience')
    if not isinstance(experience, dict):
        raise ValueError('experience must be an object with rheem/ltts/utsa arrays')
    for name in REQUIRED_EMPLOYERS:
        entries = experience.get(name)
        if not isinstance(entries, list) or not entries:
            raise ValueError(f'experience.{name} requires at least one bullet')
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                raise ValueError(f'experience.{name}[{i}] must be an object')
            source = text(entry.get('source_id'), f'{name}[{i}].source_id')
            if not re.fullmatch(r'EXP-00[1-5]-[A-Z][0-9]*', source):
                raise ValueError(f'Invalid source ID: {source}')
            text(entry.get('text'), f'{name}[{i}].text')
    others = data.get('other_experience', [])
    if not isinstance(others, list):
        raise ValueError('other_experience must be an array')
    for entry in others:
        if not isinstance(entry, dict):
            raise ValueError('other_experience entries must be objects')
        for key in ('heading', 'source_id'):
            text(entry.get(key), 'other_experience.' + key)
        if 'bullets' in entry:
            if not isinstance(entry['bullets'], list) or not entry['bullets']:
                raise ValueError('other_experience.bullets must be nonempty')
            for bullet in entry['bullets']:
                text(bullet, 'other_experience.bullets')
        else:
            text(entry.get('text'), 'other_experience.text')
    demos = data.get('demonstrations', [])
    if not isinstance(demos, list):
        raise ValueError('demonstrations must be an array')
    seen = set()
    for d in demos:
        if not isinstance(d, dict):
            raise ValueError('demonstration entries must be objects')
        text(d.get('title'), 'demonstration title')
        url_tex(d.get('url'))
        if d['url'] in seen:
            raise ValueError('Duplicate demonstration URL: ' + d['url'])
        seen.add(d['url'])
    return True

def make_macros(data):
    validate_content(expand_experience_bullets(data))
    skills = '\n'.join(r'\textbf{' + tex_escape(x['category']) + ':} ' +
                       tex_escape(', '.join(x['items'])) + r'\par' for x in data['skills'])
    def bullet_list(name):
        # Grouped IDs become a heading bullet with every original achievement as
        # an indented child bullet. Legacy flat entries still compile as before.
        output = []
        for entry in data['experience'][name]:
            if 'bullets' in entry:
                output.append(r'\item \textbf{' + tex_escape(entry['heading']) + '}')
                output.append(r'\begin{itemize}[leftmargin=1.3em,topsep=1pt,itemsep=1pt]')
                output.extend(r'\item ' + tex_escape(b) for b in entry['bullets'])
                output.append(r'\end{itemize}')
            else:
                output.append(r'\item ' + tex_escape(entry['text']))
        return '\n'.join(output)
    others = ''
    if data.get('other_experience'):
        other_parts = []
        for entry in data['other_experience']:
            other_parts.append(r'\textbf{' + tex_escape(entry['heading']) + r'}\par')
            if 'bullets' in entry:
                other_parts.append(r'\begin{itemize}[leftmargin=1.4em,topsep=1pt,itemsep=1pt]')
                other_parts.extend(r'\item '+tex_escape(b) for b in entry['bullets'])
                other_parts.append(r'\end{itemize}')
            else:
                other_parts.append(tex_escape(entry['text']) + r'\par')
        others = '\n'.join(other_parts)
    demos = ''
    if data.get('demonstrations'):
        demos = '\n'.join(tex_escape(d['title']) + ': ' + url_tex(d['url']) + r'\par'
                          for d in data['demonstrations'])
    bodies = (tex_escape(data['summary']), skills, bullet_list('rheem'),
              bullet_list('ltts'), bullet_list('utsa'), others, demos)
    # An empty body must stay truly empty so the template's \\ifdefempty checks work.
    return '% Generated. Do not edit manually. Edit resume_content.json instead.\n' + '\n\n'.join(
        '\\renewcommand{\\' + macro + '}{' + ('\n' + body + '\n' if body.strip() else '') + '}'
        for macro, body in zip(MACROS, bodies)) + '\n'

def compile_latex(template, content, dest, compiler):
    dest.mkdir(parents=True, exist_ok=True)
    # Copy template under fixed name because it imports resume_content.tex.
    target = dest / 'Resume_template.tex'
    shutil.copy2(template, target)
    (dest / 'resume_content.tex').write_text(content, encoding='utf-8')
    binary = shutil.which(compiler)
    if not binary:
        raise RuntimeError(f'{compiler} not found. Install MiKTeX/TeX Live and add it to PATH.')
    for attempt in range(2):
        result = subprocess.run([binary, '-interaction=nonstopmode', '-halt-on-error',
                                 '-file-line-error', target.name], cwd=dest,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, encoding='utf-8', errors='replace', timeout=120)
        (dest / 'compile.log').write_text(result.stdout, encoding='utf-8')
        if result.returncode:
            raise RuntimeError('LaTeX compilation failed; inspect ' + str(dest / 'compile.log') +
                               '\n' + '\n'.join(result.stdout.splitlines()[-25:]))
    pdf = dest / 'Resume_template.pdf'
    if not pdf.exists():
        raise RuntimeError('pdflatex exited without creating a PDF')
    output = dest / 'Resume.pdf'
    shutil.copy2(pdf, output)
    return output

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', required=True, type=Path, help='resume_content.json')
    ap.add_argument('--template', type=Path, default=TEMPLATE)
    ap.add_argument('--output', type=Path, default=Path('output/current'))
    ap.add_argument('--compiler', default='pdflatex')
    ap.add_argument('--skip-validate', action='store_true', help='Skip PDF validation (not recommended)')
    args = ap.parse_args()

    # Resolve paths relative to the project root
    def resolve_path(path):
        path = Path(path)
        if not path.is_absolute():
            path = ROOT / path
        return path.resolve()

    args.input = resolve_path(args.input)
    args.template = resolve_path(args.template)
    args.output = resolve_path(args.output)

    try:
        original_data = json.loads(args.input.read_text(encoding='utf-8'))
        data = original_data
        validate_content(expand_experience_bullets(data))
        if not args.template.exists():
            raise ValueError('Missing LaTeX template: ' + str(args.template))
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / 'resume_content.json').write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        pdf = compile_latex(args.template, make_macros(data), args.output, args.compiler)
        print('Compiled:', pdf)
        if not args.skip_validate:
            from validate_resume import validate_pdf
            report = validate_pdf(pdf, expand_experience_bullets(data), args.output / 'compile.log')
            (args.output / 'validation_report.json').write_text(
                json.dumps(report, indent=2), encoding='utf-8')
            print('Validation:', 'PASS' if report['passed'] else 'FAIL')
            for message in report['errors']:
                print('ERROR:', message)
            for message in report['warnings']:
                print('WARNING:', message)
            if not report['passed']:
                return 2
        return 0
    except (ValueError, OSError, RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
