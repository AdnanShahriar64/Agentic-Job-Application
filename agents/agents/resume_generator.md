# Agent 2: Tailored Resume Content Generator

## Scope
Given a saved `job_requirements.json` OR an explicitly supplied job description, produce one job-specific `resume_content.json`, including selected demonstration titles AND complete explicit URLs. Build and validate the PDF with the existing Python scripts when requested. Do not search for unrelated jobs.

## Source files
Read `libraries/Candidate_profile.md`, `libraries/Summary_library.md`, `libraries/EXP-001_Rheem_Project_Engineer_II.md`, `libraries/EXP-002_LTTS_Senior_Simulation_Integration_Engineer.md`, `libraries/EXP-003_UTSA_Research.md`, `libraries/EXP-004_Universal_Real_Time_Power_Conversion.md`, `libraries/EXP-005_Selected_Earlier_Research_Projects.md`, `libraries/Technical_knowledge_library.md`, `libraries/Software_and_programming_skills_library.md`, and `libraries/Demonstration_links_library.json` (use actual files; flag missing paths). Do not edit them.

## Ranking and selection
Individually score evidence-based accomplishments using `score = 0.60*job_relevance + 0.25*intrinsic_importance + 0.15*evidence_strength` on 0-5 scales. Importance comes from the library; assess evidence strength from actual completion and verification. This is a decision aid, not an absolute rule. Preserve mandatory Rheem, L&T, and UTSA representation. Include EXP-004 when relevant; EXP-005 only on exceptionally strong/direct 5/5 job relevance and at most one item for a normal two-page resume. Combine overlapping project bullets when appropriate; preserve accomplishment IDs and truthful metrics. Never turn in-development work into completed work or disclosures into granted patents.

Select only relevant individual software skills supported by experience, not every item in a category. Select 3-5 demonstrations *when relevant and space permits*. Get URLs directly from `Demonstration_links_library.json`; preserve their bytes, show full visible URLs, and deduplicate aliases (links 3 and 14 were the same video). Do not invent or shorten URLs.

## Resume content JSON contract
IMPORTANT: Generate fields in the schema understood by the actual `scripts/build_resume.py`. Its known example uses these exact top-level fields:

```json
{
  "target_company": "Example Company",
  "target_role": "Senior CFD Engineer",
  "summary": "Evidence-grounded tailored summary.",
  "skills": [{"category": "Simulation", "items": ["CFD", "FEA"]}],
  "experience": {
    "rheem": [{"source_id": "EXP-001-E", "text": "Grounded bullet text."}],
    "ltts": [{"source_id": "EXP-002-C", "text": "Grounded bullet text."}],
    "utsa": [{"source_id": "EXP-003-J", "text": "Grounded bullet text."}]
  },
  "other_experience": [],
  "demonstrations": [
    {"id": 7, "title": "CFD and bridge structural analysis", "url": "https://youtu.be/DTQD6CamibM"}
  ]
}
```

Examples are illustrative. Confirm optional-entry format in the current builder before using `other_experience`. Keep ID provenance in JSON; omit IDs from printed resume. If the builder expects another format, conform to its actual schema instead of guessing.

## Build and quality checks
Use `scripts/build_resume.py` (input job-specific JSON, template `Resume_template.tex`, output folder under `output/<company_role>/`) and `scripts/validate_resume.py`. The fixed header/contact links, education and employment titles/dates come from `Resume_template.tex`, not the candidate profile. Do not rewrite the template. Compile via available pdfLaTeX/MiKTeX. Ensure valid LaTeX escaping and URL rendering in the Python builder.

Target exactly **two US Letter pages**. On 3+ pages: shorten verbose bullets, merge overlap, remove low-value optional material/demonstrations, preserve fixed sections. On 1 page: expand substantiated detail/add high-relevance material (not padding or fabricated claims). Max 5 content revisions. Maintain >=10pt body and >=0.65in margins; no arbitrary negative spacing or forced blank pages. If exactly two pages is not possible with high-quality relevant content, report it. Verify searchable text, required headings, URLs, source IDs, page count, and visually inspect page rendering where possible. Do not claim successful validation based only on the compiler exit code.

Output a resume PDF, the selected JSON, and a short traceability/fit/gap report. If the job file doesn't exist, ask for or work from the supplied job description; do not fabricate one.
