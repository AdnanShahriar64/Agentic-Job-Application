# Agent 1: Job Discovery and Requirements Extraction

## Scope
Search for relevant, current job postings; verify them; evaluate fit; and create machine-readable requirements for Agent 2. Do **not** generate resume JSON or LaTeX here.

## Candidate and priorities
Read `libraries/Candidate_profile.md` and relevant experience/skills libraries before searching. Target CFD, thermal, FEA, multiphysics, digital twin, simulation platform/software, computational mechanics, and R&D roles at appropriate seniority. Location preference: Remote US > San Antonio/Dallas area > Texas > other US locations. Where a regular search is requested, aim for 10 relevant jobs on Friday or 2 on other days, but do not pad with poor matches. These instructions do not schedule an unattended search.

## Search and verification
Use available authorized internet/job-search tools. Prefer original company career pages, confirm title, requisition, location, remote policy and application status when possible; record checked_at date. Reject duplicates. Do not invent salaries, visa policy, or missing fields. Mark uncertainty explicitly. If there is no browsing capability, explain that live verification was not possible.

## Requirements analysis
For each job extract exact text of core requirements where useful, grouped into `required`, `preferred`, and `responsibilities`. Add technical domains, explicit software, seniority and any clearly stated experience thresholds. Match demonstrable candidate strengths and gaps with evidence from source libraries, not just keyword overlap. Use an explanatory 0-100 match score only as a heuristic—not odds of being hired.

## Handoff contract
Create `jobs/<company_role>/job_requirements.json` with the following fields (null when unverified):

```json
{
  "company": "Example Company",
  "role": "Senior CFD Engineer",
  "job_url": "https://example.com/official-posting",
  "requisition": null,
  "location": "Dallas, TX",
  "work_arrangement": "hybrid",
  "salary": null,
  "checked_at": "2026-10-25",
  "required": ["CFD analysis", "Python"],
  "preferred": ["experimental testing"],
  "responsibilities": ["Develop and validate simulations"],
  "keywords": ["CFD", "Python", "validation"],
  "fit_score": 82,
  "fit_reasoning": "Strong CFD and engineering automation evidence",
  "gaps": [],
  "verification_notes": "Example data only; not an actual posting"
}
```

The above is illustrative only. Do not persist it as a real opportunity. Save each verified job separately. Present the posting URL and principal reasons for fit in the user-facing results. For the resume task, pass the exact saved job file path or its contents; don't expect a second session to know the first agent's private context.
