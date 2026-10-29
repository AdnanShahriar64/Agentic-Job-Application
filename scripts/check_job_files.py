#!/usr/bin/env python3
"""Check a job folder created by Agent 0 before building the resume.

Usage (from any directory):
    python scripts/check_job_files.py jobs/<Company_Role>

Checks job_posting.txt, job_requirements.json and resume_selection.json,
and does a dry run of the ID resolver. Exit code 0 = OK, 1 = errors.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from select_resume_content import FILES, build, extract_entries  # noqa: E402

REQ_KEYS = ['employer', 'job_title', 'location', 'employment_arrangement',
            'requisition_number', 'application_url', 'date_checked', 'posting_file',
            'eligibility_requirements', 'required_qualifications',
            'preferred_qualifications', 'main_responsibilities', 'technical_skills',
            'software_requirements', 'technical_keywords', 'qualification_gaps',
            'match_score']
PRIORITIES = {'Critical', 'High', 'Medium', 'Low'}
GAP_STATUS = {'Directly supported', 'Partially supported', 'Not established'}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    folder = Path(sys.argv[1])
    if not folder.is_absolute():
        folder = ROOT / folder
    errors, warnings = [], []

    def load(name):
        p = folder / name
        if not p.is_file():
            errors.append(f'Missing {name}')
            return None
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'{name} is not valid JSON: {exc}')
            return None

    # Known accomplishment IDs
    known = set()
    for name in FILES.values():
        known |= set(extract_entries(ROOT / 'libraries' / name))

    # 0. Library keyword weights must stay within 1-5
    try:
        from score_selection import load_library
        load_library()
    except ValueError as exc:
        errors.append(str(exc))

    # 1. Posting text
    posting = folder / 'job_posting.txt'
    if not posting.is_file():
        errors.append('Missing job_posting.txt')
    else:
        body = posting.read_text(encoding='utf-8').split('---', 1)[-1]
        if len(body.split()) < 80:
            warnings.append('job_posting.txt is very short; was the full posting captured?')

    # 2. Requirements
    req = load('job_requirements.json')
    if req is not None:
        for k in REQ_KEYS:
            if k not in req:
                errors.append(f'job_requirements.json missing key: {k}')
        for field in ('required_qualifications', 'preferred_qualifications'):
            for i, q in enumerate(req.get(field) or []):
                if not isinstance(q, dict) or q.get('priority') not in PRIORITIES:
                    errors.append(f'{field}[{i}] needs "text" and a priority in {sorted(PRIORITIES)}')
        for i, g in enumerate(req.get('qualification_gaps') or []):
            if g.get('status') not in GAP_STATUS:
                errors.append(f'qualification_gaps[{i}].status must be one of {sorted(GAP_STATUS)}')
            for eid in g.get('evidence_ids', []):
                if eid not in known:
                    errors.append(f'qualification_gaps[{i}] cites unknown ID {eid}')
        score = req.get('match_score')
        if score is not None and not (isinstance(score, (int, float)) and 0 <= score <= 100):
            errors.append('match_score must be a number from 0 to 100')
        if req.get('required_qualifications') == []:
            warnings.append('No required qualifications extracted')

    # 3. Selection
    sel = load('resume_selection.json')
    if sel is not None:
        exp = sel.get('experience', {})
        exp005 = [i for i in exp.get('other', []) if i.startswith('EXP-005')]
        if len(exp005) > 1:
            errors.append(f'More than one EXP-005 entry selected: {exp005}')
        if len(sel.get('demonstration_ids', [])) > 5:
            errors.append('More than 5 demonstrations selected')
        if not sel.get('summary', '').strip():
            errors.append('summary is empty')
        try:
            build(sel, ROOT / 'libraries')  # dry run: IDs, duplicates, employers, demos
        except (ValueError, KeyError, FileNotFoundError) as exc:
            errors.append(f'resume_selection.json: {exc}')

    for w in warnings:
        print('WARNING:', w)
    for e in errors:
        print('ERROR:', e)
    print('CHECK:', 'FAIL' if errors else 'PASS')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
