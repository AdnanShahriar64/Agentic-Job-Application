#!/usr/bin/env python3
"""Resolve accomplishment IDs to verbatim Markdown achievement bullets.

Run from any working directory; paths are relative to Resume_Depo root.
The agent selects IDs only. This script owns the extraction.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    'EXP-001': 'EXP-001_Rheem_Project_Engineer_II.md',
    'EXP-002': 'EXP-002_LTTS_Senior_Simulation_Integration_Engineer.md',
    'EXP-003': 'EXP-003_UTSA_Research.md',
    'EXP-004': 'EXP-004_Universal_Real_Time_Power_Conversion.md',
    'EXP-005': 'EXP-005_Selected_Earlier_Research_Projects.md',
    'EXP-006': 'EXP-006_UTSA_Teaching_Experience.md',
}

EMPLOYER_FOR = {'EXP-001':'rheem','EXP-002':'ltts','EXP-003':'utsa'}

ID_RE = re.compile(r'EXP-00[1-6]-[A-Z][0-9]*')

HEADING_RE = re.compile(
    r'^\s*\**\s*#{3,6}\s+'
    r'(EXP-00[1-6]-[A-Z][0-9]*)'
    r'\s*:\s*(.+?)\s*\**\s*$'
)

BULLET_RE = re.compile(r'^\s*(?:\\)?-\s+(.+?)\s*$')


def path_from_root(p):
    p=Path(p)
    return p if p.is_absolute() else ROOT/p


def label(line):
    """Recognize Markdown labels despite literal backslash-escaped asterisks."""
    return re.sub(r'[\\*#_\s]', '', line).lower()


def extract_entries(path):
    source = path.read_text(encoding='utf-8-sig').splitlines()
    out = {}
    current_id = None
    current_heading = None
    collecting = False
    bullets = []

    def finish():
        if current_id is not None:
            if not bullets:
                raise ValueError(f'{path.name}: {current_id} has no Achievement bullets')
            if current_id in out:
                raise ValueError(f'{path.name}: repeated ID {current_id}')
            out[current_id] = {'heading': current_heading, 'bullets': list(bullets)}

    for line in source + ['## END OF SOURCE']:
        head = HEADING_RE.match(line)
        if head:
            finish()
            current_id, current_heading = head.group(1), head.group(2).strip()
            collecting = False
            bullets = []
            continue
        # Once the next top-level section begins, stop looking for bullets.
        # Headings may be wrapped in bold markers (e.g. "**## Tailoring Notes**").
        if line.lstrip().lstrip('*').lstrip().startswith('#') and current_id and not head:
            finish()
            current_id = None
            current_heading = None
            bullets = []
            collecting = False
            continue
        if current_id is None:
            continue
        normalized = label(line)
        if normalized.startswith('achievement:'):
            collecting = True
            continue
        if collecting:
            match = BULLET_RE.match(line)
            if match:
                bullets.append(match.group(1))
            elif normalized.startswith(('status:', 'weightedkeywords:', 'technicaldetails:', 'importance:', 'domains:')):
                collecting = False
    return out


def build(selection, libdir):
    chosen = selection.get('experience')
    if not isinstance(chosen, dict):
        raise ValueError('Selection requires experience object')
    index = {}
    for prefix, name in FILES.items():
        path = libdir / name
        if not path.is_file():
            raise FileNotFoundError(f'Missing library: {path}')
        entries = extract_entries(path)
        for eid, record in entries.items():
            if eid in index:
                raise ValueError(f'Duplicate accomplishment ID: {eid}')
            index[eid] = record

    result = {
        'target_company': selection.get('target_company', ''),
        'target_role': selection.get('target_role', ''),
        'summary': selection['summary'],
        'skills': selection['skills'],
        'experience': {'rheem':[], 'ltts':[], 'utsa':[]},
        'other_experience': [],
        'demonstrations': []
    }
    seen = set()
    for employer, ids in chosen.items():
        if employer not in {'rheem', 'ltts', 'utsa', 'other'}:
            raise ValueError('Unknown experience group: ' + employer)
        if not isinstance(ids, list):
            raise ValueError(f'experience.{employer} must be an array of IDs')
        for eid in ids:
            if not isinstance(eid,str) or not ID_RE.fullmatch(eid):
                raise ValueError('Invalid accomplishment ID: ' + repr(eid))
            if eid not in index:
                raise ValueError(f'Unknown accomplishment ID: {eid}')
            if eid in seen:
                raise ValueError(f'Accomplishment selected more than once: {eid}')
            seen.add(eid)
            actual = EMPLOYER_FOR.get(eid[:7], 'other')
            if employer != actual:
                raise ValueError(f'{eid} belongs to {actual}, not {employer}')
            entry = {'source_id': eid, 'heading': index[eid]['heading'], 'bullets': index[eid]['bullets']}
            if employer == 'other':
                if eid.startswith('EXP-006-'):
                    entry['heading'] = (
                        'Graduate Teaching Assistant | UTSA | '
                        'Jan 2017–May 2019 — ' + entry['heading']
                    )
                result['other_experience'].append(entry)
            else:
                result['experience'][employer].append(entry)
    for employer in ['rheem','ltts','utsa']:
        if not result['experience'][employer]:
            raise ValueError(f'Mandatory employer {employer} must have an accomplishment')

    demos_path = libdir / 'Demonstration_links_library.json'
    demos = json.loads(demos_path.read_text(encoding='utf-8'))['demonstrations']
    by_id = {str(d['id']): d for d in demos}
    used_urls = set()
    for did in selection.get('demonstration_ids', []):
        d = by_id.get(str(did))
        if d is None:
            raise ValueError(f'Unknown demonstration ID: {did}')
        if d['url'] in used_urls:
            continue
        result['demonstrations'].append({k:d[k] for k in ('id','title','url')})
        used_urls.add(d['url'])
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--selection',type=Path,required=True)
    p.add_argument('--libraries',type=Path,default=Path('libraries'))
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    selection=json.loads(path_from_root(args.selection).read_text(encoding='utf-8'))
    content=build(selection,path_from_root(args.libraries))
    dest=path_from_root(args.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Wrote',dest)
    for group,entries in content['experience'].items():
        print(group, [(e['source_id'],len(e['bullets'])) for e in entries])

if __name__ == '__main__':
    main()
