# Automated Resume Builder

This project uses your **fixed** `Resume_template.tex` and a job-specific `resume_content.json` to generate `resume_content.tex` and a PDF. The name/contact/links/education and mandatory employer headings remain in the fixed template.

## Requirements

- Python 3.9+
- MiKTeX or TeX Live with `pdflatex` available on the command line
- PDF validation: `python -m pip install pymupdf` (alternative: `python -m pip install pypdf`)

## Windows PowerShell quick start

From the directory containing these files:

```powershell
python -m pip install pymupdf
python build_resume.py --input resume_content_example.json --template Resume_template.tex --output output\test
```

Output files: `output/test/Resume.pdf`, `resume_content.tex`, `resume_content.json`, `compile.log`, and `validation_report.json`.

To validate an existing PDF:

```powershell
python validate_resume.py --pdf output\test\Resume.pdf --json output\test\resume_content.json --log output\test\compile.log
```

## JSON format

Copy `resume_content_example.json` and replace summary, skills, and experience bullet text. The required employer arrays are `rheem`, `ltts`, and `utsa`; each item requires `source_id` and `text`. Optional `other_experience` items require `source_id`, `heading`, and `text`. Optional `demonstrations` require `title` and full `url`.

Codex should select relevant content from the libraries and create this JSON. The builder does **not** automatically rank or write accomplishments, nor can it independently verify factual accuracy of a rewritten bullet. The `source_id` field is an audit trail. Check sources when reviewing. 

The sample is an abbreviated **test**, not a full two-page tailored résumé. The script will reject a PDF longer than two pages, but it will not automatically shorten it. If more than two pages, revise the JSON and rebuild.

## Notes

- **Keep `Resume_template.tex` fixed.** The builder writes only an output copy, not your source template.
- Do not insert raw LaTeX into plain-text JSON fields: the builder escapes special characters automatically.
- URLs must be valid HTTP(S) URLs and are emitted with `\url{...}`.
- PDF content and visual layout should still be reviewed by a person, especially line wrapping, overflow warnings, and truthfulness of the claims.
- If you edited the fixed template on your PC since downloading it, replace the packaged `Resume_template.tex` with your current version before running the builder.
