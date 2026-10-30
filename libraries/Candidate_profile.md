# Candidate Profile — Adnan Shahriar

**Profile ID:** CAND-001  
**Purpose:** Authoritative candidate identity, career chronology, education, and general professional positioning for automated résumé tailoring.  
**Last updated:** October 24, 2026  
**Usage:** Read with the experience, technical knowledge, software, and demonstration libraries. Do not copy all fields into every résumé.

## Identity and Contact

- **Name:** Adnan Shahriar
- **Professional display name:** Adnan Shahriar, Ph.D.
- **Location:** San Antonio, TX, USA
- **Phone:** 210-803-5230
- **Email:** adnan.shahriar@my.utsa.edu
- **LinkedIn:** https://www.linkedin.com/in/adnan-shahriar/
- **Google Scholar:** https://scholar.google.com/citations?user=jF2HLEcAAAAJ&hl=en

## Professional Identity

**Primary background:** Mechanical engineering Ph.D. with professional and research experience spanning computational mechanics, CFD, FEA, thermal-fluid modeling, numerical solver development, digital twins, HVAC product R&D, engineering automation, and simulation software integration.

**Evidence-backed differentiators:**
- Developed custom finite element and multiphysics numerical solvers from first principles, including coupled structural, thermal, and fluid models.
- Developed and integrated physics-based models for NASA's Modular-Coupled Virtual Testbed (MCVT) and a structurally calibrated experimental digital twin.
- Developed real-time C/C++ HVAC plant simulation for John Deere SiL/HiL applications and supported embedded simulation infrastructure.
- Designed and experimentally evaluated HVAC aerodynamic and mechanical improvements at Rheem, combining CFD, FEA, rapid prototyping, and test validation.
- Developed custom engineering tools, including Python/CadQuery CAD automation, numerical optimization, meshing, and simulation workflows.
- Performed Eulerian CFD and coupled Eulerian–Lagrangian (CEL) fluid–structure interaction modeling for coastal bridge wave loading.

**Potential target role families:** CFD Engineer; FEA / Structural Simulation Engineer; Thermal / Thermo-Fluid Engineer; Simulation Software Engineer; Digital Twin / Systems Simulation Engineer; Mechanical / HVAC R&D Engineer; Computational Mechanics Research Engineer.

**Summary-writing rule:** Use the target job description to select relevant strengths. Do not represent all listed specialties as equally recent or equally deep, and do not assert years of specific-domain experience without checking the dated evidence.

## Career Focus

Areas the candidate wants emphasized. This is the **only** place to add extra emphasis — do not raise keyword weights above 5 in the experience libraries.

`scripts/score_selection.py` reads this table. When a job asks for a focus area (any of its job signals, judged by meaning, not exact words), each listed evidence ID gets the bonus added to its score S. IDs not listed get no bonus, and a focus area the job does not ask for gives no bonus. The bonus changes ranking only; it never allows claiming a capability the Achievement text does not show.

| Focus ID | Focus area | Job signals | Evidence IDs | Bonus |
|---|---|---|---|---|
| FOCUS-AI | AI/ML for engineering simulation | machine learning, AI, neural networks, surrogate models, data-driven design | EXP-003-G, EXP-001-B | 0.5 |
| FOCUS-THERMAL | Thermal management and thermal-fluid modeling | thermal management, heat transfer, cooling, thermal control, HVAC thermal | EXP-003-P, EXP-002-C, EXP-003-C, EXP-003-A | 0.5 |
| FOCUS-SCI | Scientific computing and numerical software | scientific computing, numerical methods, solver development, HPC | EXP-004-A, EXP-003-H, EXP-003-A | 0.5 |

Job discovery (Agent 1) should also rank a job higher when it asks for one of these focus areas and the overall match is otherwise comparable.

## Education

### Ph.D. in Mechanical Engineering
- **Institution:** The University of Texas at San Antonio (UTSA)
- **Graduated:** December 2023
- **GPA:** 3.94 (as listed in source résumé)
- **Dissertation:** Novel Finite Element Techniques to Expedite the Implementation and Computational Time of 3D Structural Models Showcased Through Space Habitat
- **Research focus:** Computational mechanics; FEM/XFEM; numerical methods; structural dynamics; multiphysics coupling; model order reduction; digital twin development.

### B.S. in Aeronautical Engineering (Aerospace Major)
- **Institution:** Military Institute of Science and Technology, Bangladesh
- **Graduated:** January 2015
- **GPA:** 3.36 (as listed in source résumé)

### Additional degree — requires confirmation before résumé use
- A prior career description mentions an **M.S. in Mechanical Engineering**, but the previously supplied résumé's education section did not give its institution or graduation date. Do not automatically add this degree to application-ready output until its details are confirmed.

## Employment and Research Chronology

| Entry ID | Organization and role | Dates | Source library |
| --- | --- | --- | --- |
| EXP-001 | Rheem Manufacturing / Friedrich Air Conditioning Division — Project Engineer II | March 2025–Present | `EXP-001_Rheem_Project_Engineer_II.md` |
| EXP-002 | L&T Technology Services — Senior Simulation Integration Engineer | January 2024–March 2025 | `EXP-002_LTTS_Senior_Simulation_Integration_Engineer.md` |
| EXP-003 | UTSA — Graduate Researcher (Postdoctoral Fellow title still to be confirmed) | March 2018–January 2024 | `EXP-003_UTSA_Research.md` |
| EXP-004 | Universal Real-Time Power Conversion LLC — Physics-Based Modeling and Simulation Engineer | June–September 2022 | `EXP-004_Universal_Real_Time_Power_Conversion.md` |
| EXP-005 | Selected earlier research and aerospace projects | Various dates | `EXP-005_Selected_Earlier_Research_Projects.md` |

**Chronology notes:**
- EXP-004 overlaps the UTSA research period; treat it as a concurrent short-term engagement, not a sequential role.
- The NASA RETHi project ran May 2019–February 2024 according to the research description; the stated UTSA appointment ends January 2024. Preserve both dates unless clarified; do not infer an employment extension.
- Confirm the exact formal appointment and dates associated with the term “Postdoctoral Fellow” before using it in an application.
- Scout Motors (December 2024–March 2025) and John Deere (January–November 2024) were **client assignments within L&T Technology Services**, not separate employers.

## Research Programs and Technical Highlights

- **NASA Resilient Extraterrestrial Habitats Institute (RETHi):** Finite element and coupled-physics solver development, MCVT system-of-systems integration, thermo-mechanical topology optimization, digital twin model updating, and damage surrogate modeling.
- **Coastal Bridge Hurricane Vulnerability Research:** Eulerian wave modeling, coupled Eulerian–Lagrangian FSI, structural response, and HPC simulation.
- **DOE / Savannah River Nuclear Solutions Materials Research:** TEM/HRTEM image analysis, 2D FFT, MoSe2 nanocrystal structural modeling, and molecular dynamics of Hg–steel interactions.
- **Additional Research:** Graphene–lipid membrane molecular dynamics; aircraft–runway dynamics; experimental airfoil aerodynamics; computational geometry.

**Research output:** A prior self-reported profile mentions more than 23 publications and approximately 145 citations. **These counts are historical and time-sensitive; verify against a current CV or Google Scholar before including numerical totals.**

## Teaching Experience

**Graduate Teaching Assistant — UTSA | January 2017–May 2019**

- **Numerical Methods:** Mentored 200+ undergraduate students; developed computational demonstrations and instructional resources involving numerical methods and visualization.
- **Mechatronics:** Mentored approximately 120 students using circuits, sensors, National Instruments myDAQ, Arduino, and animatronics projects.
- **Materials Engineering and Lab:** Mentored approximately 120 students in materials characterization and experimental laboratory procedures.

**Tailoring:** Normally omit detailed teaching bullets from an industry two-page résumé, except where instruction, technical communication, mentoring, laboratory leadership, or academic work is especially relevant.

## Selected Measurable Outcomes (Claims Must Retain Their Context)

- **Rheem fan shroud:** More than 80% improvement in airflow efficiency (CFM/W) versus previous design, based on prototype testing.
- **Rheem motor mount:** More than 50% reduction in structural material use while meeting stated stiffness and vibration requirements.
- **Rheem VPAK AHU:** Approximately 25% higher airflow compared with existing configuration.
- **Rheem front panel:** Approximately 60% higher airflow than baseline design.
- **Rheem intellectual property:** Four patent disclosures submitted; **not** equivalent to granted patents.

**Rule:** Detailed experience entries are authoritative for wording, project completion status, validation methods, and the exact claim. Do not convert prototype results into production-wide performance claims.

## Portfolio and Publication Links

- **LinkedIn:** https://www.linkedin.com/in/adnan-shahriar/
- **Google Scholar:** https://scholar.google.com/citations?user=jF2HLEcAAAAJ&hl=en
- **Demonstration catalog:** `Demonstration_links_library.json` (source for exact demonstration URLs, titles, IDs, and relevance metadata).

**Rule:** Select demonstrations based on the job rather than always displaying a fixed set. Preserve explicit URLs in the final résumé when selected.

## Resume Generation Constraints

- This file establishes identity, education, career chronology, and durable positioning; it is **not** a ready-made résumé or a replacement for detailed accomplishment libraries.
- Never invent degrees, professional certifications, patents, publications, employer titles, software proficiency, or quantitative results.
- Do not use personal or immigration details in the résumé unless explicitly requested and relevant to an application question.
- Keep the latest professional experience visible unless there is a compelling job-specific reason to omit an older, unrelated role.
- Prefer clear, plain ATS-friendly job titles and institution names; preserve formal titles when confirmed.
- If a claim in this profile differs from a detailed experience library, flag the discrepancy for verification rather than silently choosing a preferred version.
- A `Summary_library.md` may supply positioning language, but every factual summary claim must remain supported by this profile or the corresponding experience libraries.

## Items to Confirm or Update

- [ ] Whether to display the academic email above or a preferred personal email.
- [ ] Institution and graduation date for the reported M.S. in Mechanical Engineering.
- [ ] Official UTSA appointment title(s) and their dates, especially “Postdoctoral Fellow.”
- [ ] Research appointment end date versus RETHi project end date.
- [ ] Current publication and citation counts if used in applications.
- [ ] Any professional certification or software/hardware competency not already verified in the detailed libraries.
