# Resume automation coordinator

These are instructions, not a guarantee of autonomous subagent execution. Pick the workflow that matches the request.

## Workflow A — The user gives a job link or pastes a job description

Read `agents/Agent_0_job_intake.md` and follow it. It creates every JSON file for that job and builds the resume. Then, if the user wants a cover letter, read `agents/Agent_3_cover_letter_generator.md` and follow it.

## Workflow B — The user asks to find jobs

Read `agents/Agent1_job_discovery.md` and follow its instructions, then read `agents/Agent_2_resume_generator.md` and follow its instructions, then read `agents/Agent_3_cover_letter_generator.md` and follow its instructions.


## Save all application deliverables under <project root>/output/<company_role>/. If write access is unavailable, request access rather than using another output folder.

## Local LaTeX Compilation Environment

- The operating system is Windows.
- The LaTeX distribution is MiKTeX.
- The compiler is pdflatex.
- The resume source is Resume_template.tex.
- Use the Python build_resume.py script to compile resumes.
- Run all commands from the Resume_Depo project root.
- Keep generated files inside the project's output folder.
- Check pdflatex availability using:
  where.exe pdflatex
  pdflatex --version
- Do not launch TeXstudio or other GUI LaTeX editors
  for automated PDF generation.
- If pdflatex is not found, report its missing PATH
  configuration instead of modifying the template.
- If MiKTeX needs access outside the workspace,
  request authorization for that operation.
- Never silently bypass Codex sandbox restrictions.
- Do not modify MiKTeX installation or configuration
  unless explicitly authorized.

