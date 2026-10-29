# Synopsys / Ansys — Staff Engineer, AI/ML & Digital Twin (16469)

Prepared October 26, 2026 from the saved job requirements and current master libraries.

## Selection and fit

19 complete accomplishment IDs, each with its original heading and all original bullets, were resolved by Python. The selection file contains IDs only, plus target, summary and selected skills. Rheem, L&T and UTSA representation is preserved. The focus is Python automation, plant-model integration, neural surrogates, reduced-order models, digital twins and scientific computing, with additional software integration, classification algorithms and optimization evidence. Rheem EXP-001-B and EXP-001-C remain explicitly in development in their original wording.

EXP-004 meshing work was considered but omitted in favor of more direct requirements. No EXP-005 item met the exceptional-match gate. Demonstration IDs 5, 1 and 12 were resolved from the catalog without manually duplicating titles or URLs: system modeling, engineering software and research communication. The demonstrations are candidate-supplied; their content was not independently reviewed.

Scores use R = sum(weight x relevance) / sum(weight) and S = 0.80 R + 0.20 evidence strength. Per-keyword relevance and the full candidate ranking are in selection_scores.json. Direct requirements take precedence over these heuristic scores.

| Selected ID | R | Evidence | S |
|---|---:|---:|---:|
| EXP-001-A | 3.28 | 4.5 | 3.53 |
| EXP-001-D | 4.32 | 4.5 | 4.35 |
| EXP-001-B | 3.85 | 2.0 | 3.48 |
| EXP-001-C | 2.56 | 2.0 | 2.45 |
| EXP-001-G | 2.28 | 4.5 | 2.72 |
| EXP-002-C | 2.66 | 4.5 | 3.02 |
| EXP-002-G | 2.28 | 4.5 | 2.72 |
| EXP-002-E | 2.91 | 4.5 | 3.23 |
| EXP-002-F | 3.17 | 4.5 | 3.43 |
| EXP-002-B | 4.05 | 4.5 | 4.14 |
| EXP-002-D | 2.36 | 4.5 | 2.79 |
| EXP-003-G | 3.90 | 4.5 | 4.02 |
| EXP-003-E | 3.15 | 4.5 | 3.42 |
| EXP-003-F | 2.69 | 5.0 | 3.15 |
| EXP-003-D | 3.60 | 4.5 | 3.78 |
| EXP-003-H | 4.36 | 4.5 | 4.39 |
| EXP-003-A | 2.62 | 4.5 | 3.00 |
| EXP-003-C | 2.97 | 4.5 | 3.28 |
| EXP-003-B | 2.22 | 4.5 | 2.68 |

## Material gaps

The resume does not claim PyTorch, TensorFlow, scikit-learn, Kubernetes, AWS/Azure, optiSLang, modeFrontier, HEEDS, Twin Builder, Simulink or AMESim proficiency. Commercial AI deployment, broad feature-engineering practice, pre-sales ownership and staff-level customer-adoption leadership remain unestablished. The chronology supports a substantial research-plus-industry simulation background; it is not described as five years of industry experience. The employer must decide how research counts toward its experience requirement.

## Source discrepancies and handling

- The resolver expects EXP-001_Rheem_Project_Engineer_II.md, which is absent. A byte-identical temporary copy of the current EXP-001_Rheem_Project_Engineer_II_weighted_expanded.md was supplied under the expected filename using --libraries. The source library and resolver were not edited. A source hash manifest records the actual filename and validates unchanged bytes.
- The template fixes the Rheem title as Project Engineer; the library says Project Engineer II. The template fixes the research heading as Graduate Researcher / Resilient Extraterrestrial Habitats Institute, Dec 2019–Jan 2024; the profile describes a broader UTSA appointment Jan 2017–Jan 2024, and RETHi project dates May 2019–Feb 2024. Fixed template content was preserved; formal title and dates should be confirmed before applying.
- The template's personal email differs from the profile's academic email. The fixed template address was retained.
- EXP-002-C has a PID Control keyword but its achievement specifies PD control. The unsupported PID keyword received zero relevance and PID is not claimed.
- EXP-004-A contains a Scientific Computing weight of 10 outside the documented 1–5 scale. It was retained for audit but excluded from the scoring aggregate; that accomplishment was not selected.

## Build and validation

The supplied select_resume_content.py resolved headings, full bullet sets and demonstration URLs. The supplied build_resume.py produced grouped nested bullets. Shell access to installed pdfLaTeX and desktop capture were unavailable, so an official portable Tectonic compiler was used through a compiler adapter; compile.log is saved in the project output folder. The existing validate_resume.py passed with no errors or warnings.

Only generated demonstration macro routing was corrected to populate the template's earlier section and suppress its duplicate placeholder section; the empty optional-experience macro was made empty. No achievement prose was generated, edited or shortened. No font, margin or spacing changes were introduced. Template bytes remain unchanged: 10pt body, Letter, original 0.70in side / 0.62in top / 0.65in bottom margins.

The updated page-fill rule was already present in agents/resume_generator.md and was applied. Four selection revisions expanded the earlier 12-ID version to 19 IDs and reordered complete L&T accomplishment units to avoid a single-word continuation on page 2. Added IDs: EXP-001-C/G, EXP-002-B/D/G, EXP-003-B/C. All provide related model-updating, optimization, software/data integration or computational-modeling evidence; no EXP-005 content or artificial spacing was used.

Measured fill, defined as (lowest text bounding box minus top margin) divided by usable page height: page 1 = 99.8%, page 2 = 97.5%. The original 85-100% page-2 target is met. This measures vertical utilization rather than the fraction of pixels occupied by ink. Both pages remain inside their template margins, and no third page is present.

Final checks passed: exactly two Letter pages; unique IDs; exact resolver output; all source headings and bullets in order after typography/line-wrap normalization; grouped nested structure; searchable text; required fixed sections; exact visible and clickable demonstration URLs; no printed source IDs; unchanged libraries and template copy. Both final pages were visually inspected.
