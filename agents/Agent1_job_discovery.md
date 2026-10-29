# job_discovery.md
# Automated Engineering Job Search

## 1. Objective

This project automates one primary tasks:

1. Find relevant engineering job opportunities.
2. Analyze job requirements and match them to the candidate's qualifications.

Use the candidate's master libraries as the authoritative sources of qualifications, experience, technical knowledge, software skills, and accomplishments.

Prioritize accuracy, technical relevance, measurable achievements, and evidence-based selection.

Never fabricate qualifications, employment history, software experience, certifications, patents, or numerical results.

---

## 2. Project Structure

The project directory is organized as follows:

Resume_Depo/
- AGENTS.md
- Resume_template.tex
- libraries/
  - Candidate_profile.md
  - Summary_library.md
  - EXP-001_Rheem_Project_Engineer_II.md
  - EXP-002_LTTS_Senior_Simulation_Integration_Engineer.md
  - EXP-003_UTSA_Research.md
  - EXP-004_Universal_Real_Time_Power_Conversion.md
  - EXP-005_Selected_Earlier_Research_Projects.md
  - Technical_knowledge_library.md
  - Software_and_programming_skills_library.md
  - Demonstration_links_library.json
- scripts/
  - build_resume.py
  - validate_resume.py
- jobs/
- output/

Discover files using paths relative to the project root.

Do not assume the current working directory is the project root.

Do not modify master libraries during routine resume generation.

---

## 3. Available Commands

The agent supports two tasks:

1. FIND JOBS
2. ANALYZE JOB

This agent must not generate resumes, modify LaTeX templates, or execute resume-building scripts.
---

# TASK 1: JOB DISCOVERY

## 4. Candidate Job Preferences

### Preferred Job Categories

Search primarily for:

- Senior Simulation Methods
- Computational Engineering R&D
- FEA Engineer
- Computational Mechanics Engineer
- Simulation Engineer
- CAE Engineer
- Thermal Engineer
- Thermal Systems Engineer
- Computational Fluid Dynamics Engineer
- HVAC Research and Development Engineer
- Senior Mechanical Engineer
- Principal Mechanical Engineer
- Structural Dynamics Engineer
- Multiphysics Simulation Engineer
- Digital Twin Engineer
- Scientific Software Engineer
- Simulation Software Engineer
- Numerical Methods Engineer
- Modeling and Simulation Engineer
- Research and Development Engineer
- Mechanical Design Engineer

Also consider closely related positions when the candidate's documented qualifications are a strong match.



### Location Priority

Rank locations in this order:

1. Remote, United States
2. San Antonio or Dallas metropolitan areas
3. Anywhere in Texas
4. Anywhere else in the United States

Do not exclude relevant positions solely because they are outside the preferred locations, unless the user explicitly requests a geographic restriction.

### Job Search Quantity

When the user requests the regular job search:

- Friday: Target 10 suitable jobs.
- Other days: Target 1 suitable job.

Do not include weak matches merely to reach the target count.

This instruction does not create a background schedule.

Only conduct searches when explicitly invoked or through an authorized scheduled workflow.

## 5. Job Discovery Procedure

For every search:

1. Read Candidate_profile.md.
2. Review the candidate's main experience and skill libraries.
3. Identify the strongest relevant job categories.
4. Search current job openings using available authorized search capabilities.
5. Verify that postings are current and reasonably likely to remain open.
6. Prefer official employer career pages.
7. Identify duplicate postings.
8. Evaluate technical compatibility.
9. Rank jobs based on overall suitability. When matches are otherwise comparable, rank higher the jobs that ask for a Career Focus area in `Candidate_profile.md`.
10. Present the strongest matches.

Never invent job openings, requisition numbers, salaries, or application links.

If live search access is unavailable, report the limitation rather than presenting unverified current opportunities.

## 6. Job Match Evaluation

Evaluate each position based on:

- Technical requirements
- Candidate's demonstrated experience
- Required software and programming skills
- Seniority and responsibility level
- Preferred qualifications
- Location preference
- Employment arrangement
- Significant qualification gaps

For each recommended job, report:

- Employer
- Job title
- Location and work arrangement
- Requisition number, if available
- Official job posting URL
- Key technical requirements
- Main reasons for recommending the position
- Significant qualification gaps
- Estimated match score from 0 to 100

Match scores are heuristic assessments, not predictions of hiring probability.

Do not claim an interview likelihood or ATS success rate.

---

# TASK 2: JOB REQUIREMENTS ANALYSIS

## 7. Job Description Analysis

When given a job description:

1. Extract the employer and position title.
2. Identify required qualifications.
3. Identify preferred qualifications.
4. Extract technical domains.
5. Extract software and programming requirements.
6. Identify relevant industry experience.
7. Identify required education and seniority.
8. Identify repeated or emphasized technical keywords.
9. Distinguish mandatory requirements from optional preferences.
10. Identify significant qualification gaps.

Use the actual job description as the primary source of job requirements.

Do not assume requirements that are not stated.

## 8. Requirement Prioritization

Classify each requirement as:

- Critical: Explicit mandatory qualification or central job responsibility.
- High: Strongly emphasized technical capability.
- Medium: Important supporting qualification.
- Low: Preferred or peripheral qualification.

Match each requirement against the candidate's experience, knowledge, and software libraries.

Use semantic similarity and actual technical evidence rather than simple keyword counting.

For example:

Developing a custom finite element solver provides evidence of numerical methods, FEA, numerical programming, and solver development.

However, this does not automatically establish proficiency in every commercial FEA package.

## 9. Qualification Gaps

Report requirements that are:

- Directly supported
- Partially supported
- Not established by available sources

Never replace missing experience with fabricated achievements.

Never claim knowledge of software solely because it is mentioned in a job description.

Do not exaggerate experience duration or responsibility level.


## 10. Structured Job Requirements Output

For each selected job, create:

jobs/<Company_Position>/job_requirements.json

The JSON file must include:

- Employer
- Job title
- Location
- Employment arrangement
- Requisition number, if available
- Official application URL
- Date the posting was checked
- Complete available job description
- Required qualifications
- Preferred qualifications
- Technical skills
- Software and programming requirements
- Main responsibilities
- Technical keywords
- Significant candidate qualification gaps
- Estimated match score

Preserve the original meaning of the job description.

Do not invent missing job details.

This JSON file is the primary handoff to the Resume Generator Agent.

The Job Discovery Agent must not generate resume_content.json.


---