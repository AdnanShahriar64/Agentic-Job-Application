# Agent 2: Tailored Resume Content Generator

## Scope
Given a saved `job_requirements.json` OR an explicitly supplied job description, produce one job-specific `resume_content.json`, including selected demonstration titles AND complete explicit URLs. Build and validate the PDF with the existing Python scripts when requested. Do not search for unrelated jobs.

## Source files
Read `libraries/Candidate_profile.md`, `libraries/Summary_library.md`, `libraries/EXP-001_Rheem_Project_Engineer_II.md`, `libraries/EXP-002_LTTS_Senior_Simulation_Integration_Engineer.md`, `libraries/EXP-003_UTSA_Research.md`, `libraries/EXP-004_Universal_Real_Time_Power_Conversion.md`, `libraries/EXP-005_Selected_Earlier_Research_Projects.md`, `libraries/Technical_knowledge_library.md`, `libraries/Software_and_programming_skills_library.md`, and `libraries/Demonstration_links_library.json` (use actual files; flag missing paths). Do not edit them.

## Ranking and selection
Individually score evidence-based accomplishments using `score = 0.60*job_relevance + 0.25*intrinsic_importance + 0.15*evidence_strength` on 0-5 scales. Importance comes from the library; assess evidence strength from actual completion and verification. This is a decision aid, not an absolute rule. Preserve mandatory Rheem, L&T, and UTSA representation. Include EXP-004 when relevant; EXP-005 only on exceptionally strong/direct 5/5 job relevance and at most one item for a normal two-page resume. Combine overlapping project bullets when appropriate; preserve accomplishment IDs and truthful metrics. Never turn in-development work into completed work or disclosures into granted patents.

Select only relevant individual software skills supported by experience, not every item in a category. Select 3-5 demonstrations *when relevant and space permits*. Get URLs directly from `Demonstration_links_library.json`; preserve their bytes, show full visible URLs, and deduplicate aliases (links 3 and 14 were the same video). Do not invent or shorten URLs.


## Verbatim Achievement Preservation

All selected accomplishments must be copied verbatim from
the experience libraries.

1. Each accomplishment ID is an indivisible selection unit.
2. When selecting an accomplishment, copy ALL bullet points
   under its `Achievement:` field.
3. Preserve every word, sentence, punctuation mark,
   numerical result, and the original bullet order.
4. Never summarize, paraphrase, shorten, expand, merge,
   or rewrite achievement bullets.
5. Never select only some bullets from an accomplishment.
6. Do not include Importance, Domains, Keywords, or Status
   metadata in the printed resume.
7. Retain the original accomplishment ID for traceability.
8. Multiple bullets under one accomplishment ID must
   become separate resume bullets with the same source ID.
9. LaTeX escaping is permitted only if the displayed
   text remains identical to the original.
10. If an accomplishment does not fit, remove the entire
    accomplishment rather than deleting individual bullets.

Example:

If EXP-001-F contains four achievement bullets,
all four must appear in the resume, exactly as written.

If EXP-001-G contains one achievement bullet,
that entire bullet must appear unchanged.

Verbatim preservation takes precedence over
page utilization and accomplishment ranking.


## Resume content JSON contract
IMPORTANT: Generate fields in the schema understood by the actual `scripts/build_resume.py`. Its known example uses these exact top-level fields:

```json
{
  "experience": {
    "rheem": [
      {
        "source_id": "EXP-001-F",
        "text": "Invented a passive condensate entrainment and slinging system that uses fan-generated pressure differences to draw condensed water into the fan airflow path and improve condensate slinging performance."
      },
      {
        "source_id": "EXP-001-F",
        "text": "Performed CFD simulations to investigate airflow behavior, pressure distribution, and condensate entrainment mechanisms."
      },
      {
        "source_id": "EXP-001-F",
        "text": "Designed, fabricated, and iteratively refined 3D-printed prototypes to demonstrate the mechanism."
      },
      {
        "source_id": "EXP-001-F",
        "text": "Conducted experimental testing to validate condensate entrainment, slinging effectiveness, and overall system performance."
      }
    ]
  }
}
```

Examples are illustrative. Confirm optional-entry format in the current builder before using `other_experience`. Keep ID provenance in JSON; omit IDs from printed resume. If the builder expects another format, conform to its actual schema instead of guessing.


## Automatic Two-Page Resume Optimization

The final resume must contain exactly two US Letter pages.

After generating resume_content.json:

1. Execute build_resume.py.
2. Compile Resume_template.tex.
3. Run validate_resume.py.
4. Determine the actual PDF page count.

If the resume exceeds two pages:

1. Remove the lowest-ranked optional accomplishment
   as a complete unit.
2. Prefer removing less relevant accomplishments.
3. Remove optional demonstrations if necessary.
4. Remove low-relevance skills if necessary.
5. Never shorten, merge, or partially remove
   achievement bullets.

If the resume contains fewer than two pages:

1. Add the next highest-ranked relevant accomplishment.
2. Include ALL bullets belonging to that accomplishment.
3. Rebuild and check whether the new content fits.
4. If it causes overflow, try another relevant
   accomplishment with a smaller complete bullet set.
5. Repeat until the available page space is effectively
   utilized without generating a third page.

Perform a maximum of five content-revision attempts.

Preserve:
- Rheem, L&T, and UTSA employment representation.
- Fixed Education.
- Fixed contact information.
- Original achievement wording.
- Minimum 10 pt body font.
- Minimum 0.65-inch margins.

Do not insert artificial spacing or invent content
to fill empty areas.

If exactly two pages cannot be achieved, report
the limitation rather than altering accomplishments.

Validate the final PDF for page count, searchable text,
required headings, source IDs, URLs, and rendering.

