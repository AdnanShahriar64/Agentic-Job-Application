#!/usr/bin/env python3
"""Validate generated résumé PDF (pip install pymupdf, or pip install pypdf)."""
import argparse
import json
import re
import sys
from pathlib import Path

def extract_pdf(pdf):
    try:
        import fitz
        doc = fitz.open(str(pdf))
        return len(doc), '\n'.join(page.get_text() for page in doc), 'PyMuPDF'
    except ImportError:
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(pdf))
            return len(reader.pages), '\n'.join(p.extract_text() or '' for p in reader.pages), 'pypdf'
        except ImportError:
            raise RuntimeError('PDF validation requires: pip install pymupdf (or pypdf)')

def normalize(s):
    return re.sub(r'\s+', ' ', s).lower()

def validate_pdf(pdf, data=None, log=None):
    errors, warnings = [], []
    if not pdf.exists() or pdf.stat().st_size < 1000:
        return dict(passed=False, errors=['PDF missing or unusually small'], warnings=[], pages=0)
    try:
        pages, content, extractor = extract_pdf(pdf)
    except Exception as exc:
        return dict(passed=False, errors=['Cannot parse PDF: '+str(exc)], warnings=[], pages=0)
    if pages > 2:
        errors.append(f'PDF contains {pages} pages (limit: 2)')
    if not content.strip() or len(content) < 250:
        errors.append('Insufficient text extracted: check ATS readability')
    for label in ('Rheem Manufacturing', 'Technology Services', 'Extraterrestrial Habitats',
                  'EDUCATION', 'Shahriar', 'LinkedIn', 'GitHub', 'Google Scholar'):
        if normalize(label) not in normalize(content):
            errors.append('Missing expected fixed header/section: ' + label)
    if 'Insert job-specific' in content or 'Insert selected' in content:
        errors.append('Unresolved template placeholders detected')
    if data:
        for label in [x['category'] for x in data['skills']]:
            if normalize(label) not in normalize(content):
                warnings.append('Skill category not found in extracted PDF: '+label)
        for d in data.get('demonstrations', []):
            # URLs may wrap into multiple lines in PDF text.
            compact = re.sub(r'\s+', '', content)
            if re.sub(r'\s+', '', d['url']) not in compact:
                warnings.append('Demonstration URL may be wrapped/omitted: '+d['url'])
    if log and Path(log).exists():
        logtext = Path(log).read_text(encoding='utf-8', errors='replace')
        if 'Overfull \\hbox' in logtext or 'Overfull \\vbox' in logtext:
            warnings.append('Overfull box reported by TeX; inspect rendered PDF')
    return dict(passed=not errors, errors=errors, warnings=warnings,
                pages=pages, pdf_text_characters=len(content), extraction_backend=extractor)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pdf', required=True, type=Path)
    ap.add_argument('--json', type=Path, help='Optional resume_content.json')
    ap.add_argument('--log', type=Path)
    args = ap.parse_args()
    data = json.loads(args.json.read_text(encoding='utf-8')) if args.json else None
    report = validate_pdf(args.pdf, data, args.log)
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] else 2

if __name__ == '__main__':
    sys.exit(main())
