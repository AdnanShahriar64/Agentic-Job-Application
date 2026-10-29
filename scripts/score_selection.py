#!/usr/bin/env python3
"""Compute accomplishment scores for one job, the same way every time.

The agent judges only how relevant each keyword is to the job (0-5) and the
evidence strength E (0-5). This script supplies the library weights, applies
the formula and the Career Focus bonus, and writes a ranked list.

    R = sum(weight * relevance) / sum(weight)      (weights from the libraries)
    S = 0.80 * R + 0.20 * E + focus bonus

Usage (from any directory):
    python scripts/score_selection.py jobs/<Company_Role>

Input  jobs/<Company_Role>/relevance.json:
{
  "focus_requested": ["FOCUS-AI"],
  "items": {
    "EXP-003-G": {"keyword_relevance": {"Neural Networks": 5, "Digital Twin": 4},
                  "evidence_strength": 4.5}
  }
}
Keywords left out of keyword_relevance count as relevance 0.

Output jobs/<Company_Role>/selection_scores.json, ranked by S.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from select_resume_content import FILES, HEADING_RE  # noqa: E402

KEYWORD_RE = re.compile(r'^\s*(?:\\)?-\s+(.+?)\s*:\s*(\d+(?:\.\d+)?)\s*$')
STATUS_RE = re.compile(r'status', re.I)
IN_DEVELOPMENT_MAX_E = 2.0
NOT_COMPLETE_RE = re.compile(r'\bin development\b|\bplanned\b|\bongoing\b|\bproposed\b|\bin progress\b', re.I)


def label(line):
    return re.sub(r'[\\*#_\s]', '', line).lower()


def load_library():
    """Return {id: {'keywords': {name: weight}, 'status': str}}."""
    index = {}
    for name in FILES.values():
        current, collecting = None, False
        for line in (ROOT / 'libraries' / name).read_text(encoding='utf-8-sig').splitlines():
            head = HEADING_RE.match(line)
            if head:
                current = head.group(1)
                index[current] = {'keywords': {}, 'status': ''}
                collecting = False
                continue
            if current is None:
                continue
            norm = label(line)
            if norm.startswith('weightedkeywords:'):
                collecting = True
                continue
            if norm.startswith('status:'):
                index[current]['status'] = re.sub(r'[\\*]', '', line).split(':', 1)[1].strip()
                collecting = False
                continue
            if norm.startswith('achievement:'):
                current = None  # keywords and status come before the achievement
                continue
            if collecting:
                m = KEYWORD_RE.match(line)
                if m:
                    weight = float(m.group(2))
                    if not 1 <= weight <= 5:
                        raise ValueError(f'{name}: {current} keyword "{m.group(1)}" has weight '
                                         f'{m.group(2)}; weights must be 1-5. Use Career Focus '
                                         'in Candidate_profile.md for extra emphasis.')
                    index[current]['keywords'][m.group(1)] = weight
    return index


def load_focus():
    text = (ROOT / 'libraries' / 'Candidate_profile.md').read_text(encoding='utf-8')
    focus = {}
    for line in text.splitlines():
        if line.startswith('| FOCUS-'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            fid, area, _signals, ids, bonus = cells[:5]
            focus[fid] = {'area': area, 'ids': [i.strip() for i in ids.split(',') if i.strip()],
                          'bonus': float(bonus)}
    return focus


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    folder = Path(sys.argv[1])
    if not folder.is_absolute():
        folder = ROOT / folder
    data = json.loads((folder / 'relevance.json').read_text(encoding='utf-8'))
    library, focus = load_library(), load_focus()
    errors, warnings, rows = [], [], []

    requested = data.get('focus_requested', [])
    for fid in requested:
        if fid not in focus:
            errors.append(f'Unknown focus ID {fid}; known: {sorted(focus)}')

    for eid, item in data.get('items', {}).items():
        if eid not in library:
            errors.append(f'Unknown accomplishment ID {eid}')
            continue
        weights = library[eid]['keywords']
        if not weights:
            errors.append(f'{eid} has no Weighted Keywords in its library')
            continue
        rel = item.get('keyword_relevance', {})
        for kw, r in rel.items():
            if kw not in weights:
                warnings.append(f'{eid}: "{kw}" is not one of its keywords (ignored)')
            elif not 0 <= r <= 5:
                errors.append(f'{eid}: relevance for "{kw}" must be 0-5')
        R = sum(w * rel.get(kw, 0) for kw, w in weights.items()) / sum(weights.values())
        E = float(item.get('evidence_strength', 0))
        status = library[eid]['status']
        if NOT_COMPLETE_RE.search(status) and E > IN_DEVELOPMENT_MAX_E:
            warnings.append(f'{eid} is "{status}"; evidence strength capped at {IN_DEVELOPMENT_MAX_E}')
            E = IN_DEVELOPMENT_MAX_E
        bonus = sum(focus[f]['bonus'] for f in requested if f in focus and eid in focus[f]['ids'])
        S = 0.80 * R + 0.20 * E + bonus
        rows.append({'id': eid, 'status': status, 'R': round(R, 3), 'E': E,
                     'focus_bonus': bonus, 'S': round(S, 3)})

    rows.sort(key=lambda r: -r['S'])
    for w in warnings:
        print('WARNING:', w)
    for e in errors:
        print('ERROR:', e)
    if errors:
        return 1
    (folder / 'selection_scores.json').write_text(
        json.dumps({'formula': 'S = 0.80*R + 0.20*E + focus bonus',
                    'focus_requested': requested, 'ranking': rows}, indent=2) + '\n',
        encoding='utf-8')
    print(f'{"ID":<11}{"R":>6}{"E":>6}{"bonus":>7}{"S":>7}  status')
    for r in rows:
        print(f'{r["id"]:<11}{r["R"]:>6.2f}{r["E"]:>6.1f}{r["focus_bonus"]:>7.2f}{r["S"]:>7.2f}  {r["status"]}')
    print('Wrote', folder / 'selection_scores.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
