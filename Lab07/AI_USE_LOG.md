# AI USE LOG

- Course: SECB3203
- Assessment: Lab 7
- Student name: Seah Zhang Jian
- Matric no: A24CS0297
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 26 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-11-26 23:40
- Tool: Google (2026). Gemini. Retrieved 26 November 2026 from https://gemini.google.com
- Purpose: explain, tests-plan
- Prompt: Help me understand the OOP design requirements for Lab 7 DNASequence, BiologicalSample, and SampleCollection in models.py, and plan unit tests for composition and validation.
- Output: Explained read-only @property attributes without setters, pairing __eq__ and __hash__ on (name, sequence), returning defensive dict copies in .results, and testing duplicate IDs and TypeErrors.
- Verified by: ran python -m pytest and ruff check src in VS Code
- My change: Implemented DNASequence, BiologicalSample, and SampleCollection in src/models.py, wrote 3 unit tests in tests/test_lab07_models.py, and documented design decisions in README.md.
- Used in: src/models.py, tests/test_lab07_models.py, README.md