# Agent 2 — ID-Based Tailored Resume Selector

## Purpose
Select relevant *accomplishment IDs*, rather than recreating, rewriting, or copying accomplishment text. Python is the sole source of achievement text in the final resume.

## Sources
Read `libraries/Candidate_profile.md`, `libraries/Summary_library.md`, the five `libraries/EXP-00*.md` career libraries, skill libraries, `libraries/Demonstration_links_library.json`, and supplied `job_requirements.json` or job description. Never alter master libraries during a job application.

## Ranking
Each accomplishment has `Weighted Keywords` (weights 1–5), `Status`, and `Achievement`. No overall `Importance` or `Domains` field is required.

1. Analyze mandatory and preferred requirements.
2. Decide which Career Focus areas (table in `libraries/Candidate_profile.md`) the job asks for, judged by meaning. List none if it asks for none.
3. For the candidate accomplishments, judge each weighted keyword's job relevance r (0–5), grounded in the actual `Achievement` text, and the evidence strength E (0–5) from completed/validated work and status. Write these to `jobs/<company_role>/relevance.json`. Do **not** write weights, R or S yourself.
4. Run `python scripts/score_selection.py jobs/<company_role>`. It takes the weights from the libraries, computes R = sum(weight × r) / sum(weight) and S = 0.80 R + 0.20 E + focus bonus, caps E at 2 for in-development work, and writes the ranking to `selection_scores.json`.
5. Use the ranking as the starting order, not a hard gate. The focus bonus only reorders; it never allows a claim the Achievement text does not support.
6. Prioritize direct matches to mandatory requirements; never invent qualifications.
7. Preserve mandatory Rheem, L&T, UTSA representation. Consider EXP-004 where useful. EXP-005 remains exceptional-match only, job relevance 5/5, maximum one selected entry without explicit override.

## Immutable achievement rule
**Never generate or edit any `Achievement:` text yourself.** Do not write achievement prose to `resume_selection.json`. Each selected accomplishment is an indivisible ID. The Python resolver reads its original heading and ALL original bullets from the respective Markdown file. Bullets must remain in the original sequence and appear as nested sub-bullets under the accomplishment heading. Do not omit, merge, shorten or paraphrase bullets. Metadata (weighted keywords and status) is not printed.

## Output selection file
Write `jobs/<company_role>/resume_selection.json` with:

```json
{
  "target_company": "Example Company",
  "target_role": "Simulation Engineer",
  "summary": "Concise factual summary relevant to the job.",
  "skills": [{"category": "Numerical simulation", "items": ["FEM", "CFD"]}],
  "experience": {
    "rheem": ["EXP-001-F", "EXP-001-G"],
    "ltts": ["EXP-002-C"],
    "utsa": ["EXP-003-F"],
    "other": ["EXP-004-A"]
  },
  "demonstration_ids": [1, 2]
}
```

Only write: target company, target role, factual summary, selected skills, selected accomplishment IDs in desired display order, and demonstration IDs. Do not duplicate achievement bullets, titles, or URLs manually. The resolver fetches those fields by ID.

## Deterministic generation
From project root, run:

```powershell
python scripts/select_resume_content.py --selection jobs/Company_Position/resume_selection.json --output jobs/Company_Position/resume_content.json
python scripts/build_resume.py --input jobs/Company_Position/resume_content.json --output output/Company_Position
```

Use the supplied updated `build_resume.py` supporting the grouped format:
`{"source_id":"EXP-001-F", "heading":"...", "bullets":["...", "..."]}`. The builder prints the heading as a main bullet and the achievement bullets as sub-bullets, while keeping their exact source wording after necessary LaTeX escaping. For demonstrations, resolver reads full exact URLs from `Demonstration_links_library.json`.

## Page fitting
Target exactly two US Letter pages. If overflow occurs, remove a complete lower-priority ID; if underfilled, add an entire additional relevant ID. Change only the ID lists, optional skills or demonstration IDs. Do not rewrite selected achievements or alter font/margins. Limit to five selection revisions. Report if the target is unattainable without compromising relevance or readability.

After achieving two pages, continue optimizing page utilization. Target approximately 85–100% of the usable height on page 2.

If page 2 remains underfilled, add the next highest-ranked relevant accomplishment ID, including its complete original heading and all bullets. Rebuild and measure again.

If an addition creates a third page, try a smaller complete accomplishment or replace a lower-ranked selection. Continue for up to five selection revisions.

Preserve original wording, font size, margins, and readable spacing. Never use irrelevant content or artificial spacing to reach the fill target. Report when relevant source material cannot meet it.

## Validation
Verify IDs exist, no ID is duplicated, mandatory employers are represented, printed bullets match source bullet text and ordering, PDF is extractable, demonstration URLs are clickable, page count is exactly two, and no factual claims are invented. Check `compile.log` and validation results. If a date/title/status discrepancy is discovered, report it; do not silently change the source file.
