# Lennox Advanced Technology Engineer — 2026-54642

Prepared October 27, 2026, from the saved job analysis and current master libraries.

## Selection and fit

18 complete accomplishment IDs produce 21 original achievement bullets. Python resolved every heading, all bullets in their original order, and demonstration titles/URLs; the agent wrote only ID selections, a factual summary and selected skills. All three mandatory employment sections remain. The selected evidence emphasizes HVAC product R&D, CFD/FEA, component material analysis, prototyping, laboratory testing, vibration, DFM, scientific programming and thermal-fluid models. EXP-001-F retains all four original bullets. Four submitted patent disclosures remain disclosures, not granted patents; prototype performance is not described as production-wide performance.

EXP-004 preprocessing work was considered but omitted in favor of directly relevant HVAC work. No EXP-005 accomplishment met the exceptional-match gate. Demonstrations 8, 6 and 5 cover HVAC duct CFD, thermal optimization and coupled-system/structural modeling. They are candidate-supplied and were not independently reviewed.

## Ranking

R = sum(weight x semantic relevance) / sum(weight); S = 0.80 R + 0.20 evidence strength. Scores are selection aids, not hiring probabilities. Per-keyword decisions and the complete ranking are saved in selection_scores.json.

| Selected ID | R | Evidence | S |
|---|---:|---:|---:|
| EXP-001-E | 5.00 | 4.5 | 4.90 |
| EXP-001-F | 4.72 | 4.5 | 4.68 |
| EXP-001-J | 3.44 | 4.5 | 3.65 |
| EXP-001-I | 4.71 | 4.5 | 4.67 |
| EXP-001-O | 4.15 | 4.5 | 4.22 |
| EXP-001-N | 4.04 | 4.5 | 4.13 |
| EXP-001-L | 5.00 | 4.5 | 4.90 |
| EXP-001-M | 4.24 | 4.5 | 4.29 |
| EXP-001-A | 4.07 | 4.5 | 4.15 |
| EXP-001-G | 4.72 | 4.5 | 4.68 |
| EXP-001-H | 3.25 | 4.5 | 3.50 |
| EXP-001-P | 3.15 | 4.5 | 3.42 |
| EXP-002-C | 2.94 | 4.5 | 3.25 |
| EXP-002-B | 3.66 | 4.5 | 3.83 |
| EXP-003-A | 3.62 | 4.5 | 3.80 |
| EXP-003-E | 2.77 | 4.5 | 3.12 |
| EXP-003-C | 3.91 | 4.5 | 4.03 |
| EXP-003-F | 3.18 | 5.0 | 3.54 |

## Gaps and source discrepancies

- Lennox specifies a mechanical engineering bachelor's degree. The documented bachelor's is aeronautical engineering and the PhD is mechanical engineering. Both degrees are shown accurately; employer acceptance of that combination must be confirmed.
- Formal FMEA, low-GWP refrigerant/energy-code expertise, DOE regulatory application, supplier-management scope and independent multi-project budget ownership are not established and are not claimed.
- The fixed template says Project Engineer at Rheem; the library says Project Engineer II. It lists Graduate Researcher / Resilient Extraterrestrial Habitats Institute for Dec 2019–Jan 2024; the profile describes a broader UTSA appointment Jan 2017–Jan 2024 and RETHi project May 2019–Feb 2024. Fixed template text was retained; the discrepancies need confirmation before applying. The template's personal email was preserved instead of the profile's academic email.
- The resolver expects an absent older Rheem filename. Its --libraries option was pointed at a byte-identical temporary snapshot of the current expanded library under the expected name. The original libraries and resolver were not edited; source hashes were checked.
- A resolver boundary issue was detected for EXP-001-R: it collected trailing tailoring notes beneath the final accomplishment. That ID was excluded entirely. No tailoring metadata or partial accomplishment appears in the final resume.
- EXP-002-C's PID keyword conflicts with the PD-controller achievement. PID received no relevance and is not claimed. EXP-004-A has a weight of 10 outside the documented 1–5 range; it was excluded from the score aggregate and the accomplishment was not selected.

## Build, page utilization and validation

The supplied select_resume_content.py and build_resume.py generated the grouped content and LaTeX. The existing validator passed without errors or warnings. An official portable Tectonic compiler was used through the established adapter because installed pdfLaTeX is inaccessible from this shell. compile.log is retained in the project output folder.

Three selection revisions added two directly relevant material/vibration accomplishments, rejected the resolver-boundary case, and reordered complete IDs to avoid splitting a long accomplishment at the page break. The final result has exactly two US Letter pages: page 1 fills 99.4% and page 2 fills 98.1% of usable vertical height. The measure runs from the original top margin to the lowest text bounding box, divided by usable page height; it is not ink-pixel density.

No original achievement wording, font, margins or spacing was changed. The template copy is byte-identical: 10pt body; original 0.70in side, 0.62in top and 0.65in bottom margins. Only generated macro routing populates the template's existing demonstrations section and suppresses its duplicate placeholder/empty optional-experience heading.

Checks passed for valid unique IDs, mandatory employers, exact resolver output, source bullet wording and order, grouped nested bullets, searchable text, required headings, absence of printed source IDs, all exact visible/clickable demonstration URLs, unchanged libraries/template, two Letter pages and the 85–100% page-2 fill target. Both final rendered pages were inspected.
