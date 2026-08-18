# PCEP-30-02 Study Kit

Practice exams and study material for the **Python Certified Entry-Level Python Programmer** (PCEP-30-02) certification from the Python Institute.

## What's Inside

- **5 mock exams** (20 questions each) at progressive difficulty levels
- **1 final exam** (30 questions) — mirrors the real PCEP-30-02 format exactly
- **1 concept checklist** (76 questions) — identifies your knowledge gaps by topic
- **Detailed answer keys** with explanations for every question
- **Study guide** covering all exam domains
- **Shared exam engine** — DRY architecture, easy to extend

## Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USER/pcep-study-kit.git
cd pcep-study-kit

# Run a mock exam (pick your level)
python exams/mock_exam_1.py     # Easy
python exams/mock_exam_2.py     # Realistic
python exams/mock_exam_3.py     # Medium
python exams/mock_exam_4.py     # Intermediate/Hard
python exams/mock_exam_5.py     # Hard (edge cases)

# Run the final exam (30 questions, simulates the real test)
python exams/final_exam.py

# Run the concept gap finder (76 questions by topic)
python exams/checklist.py
```

> Requires **Python 3.6+**. No external dependencies.

## Project Structure

```
pcep-study-kit/
├── exams/                        # Executable exams
│   ├── exam_engine.py            # Shared engine (display, scoring, validation)
│   ├── mock_exam_1.py            # Easy - fundamentals
│   ├── mock_exam_2.py            # Realistic - calibrated to actual exam
│   ├── mock_exam_3.py            # Medium - balanced review
│   ├── mock_exam_4.py            # Intermediate/Hard
│   ├── mock_exam_5.py            # Hard - edge cases & pitfalls
│   ├── final_exam.py             # 30 questions - full exam simulation
│   ├── checklist.py              # 76-question concept diagnostic
│   └── __init__.py
│
├── answer_keys/                  # Detailed answer keys (markdown)
│   ├── mock_exam_1_answers.md
│   ├── mock_exam_2_answers.md
│   ├── mock_exam_3_answers.md
│   ├── mock_exam_4_answers.md
│   ├── mock_exam_5_answers.md
│   └── final_exam_answers.md
│
├── content/                      # Study material
│   └── pcep_study_guide.md       # Full content overview by domain
│
├── .kiro/steering/               # AI steering rules (for generating new exams)
│   └── pcep-mock-exams.md
│
├── .gitignore
└── README.md
```

## Suggested Study Path

```
1. Read content/pcep_study_guide.md (overview of all topics)
2. Run exams/checklist.py (identify weak spots)
3. Study weak areas using the study guide
4. Progress through exams in order:
   mock_exam_1 → mock_exam_2 → mock_exam_3 → mock_exam_4 → mock_exam_5
5. Take the final_exam.py as your dress rehearsal
6. Score 70%+ consistently? You're ready for the real thing.
```

## Exam Difficulty Progression

| # | Exam | Difficulty | Questions | Focus |
|---|------|-----------|-----------|-------|
| 1 | mock_exam_1 | Easy | 20 | Core syntax, direct output |
| 2 | mock_exam_2 | Realistic | 20 | Calibrated to actual PCEP level |
| 3 | mock_exam_3 | Medium | 20 | Balanced review all domains |
| 4 | mock_exam_4 | Intermediate/Hard | 20 | Subtle behaviors |
| 5 | mock_exam_5 | Hard | 20 | Edge cases (harder than real exam) |
| F | final_exam | **Realistic** | **30** | **Full simulation (same as real exam)** |
| C | checklist | Mixed | 76 | One question per concept |

## About the PCEP-30-02 Exam

| Detail | Value |
|--------|-------|
| Duration | 40 minutes (+5 min NDA/tutorial) |
| Questions | 30 |
| Format | Multiple-choice, drag & drop, gap-fill, code insertion |
| Passing Score | **70%** |
| Prerequisite | None |
| Validity | Lifetime |
| Cost | ~$59 USD |

### Exam Blocks (Official Syllabus)

| Block | Topic | Items | Weight |
|-------|-------|-------|--------|
| 1 | Computer Programming & Python Fundamentals | 7 | 18% |
| 2 | Control Flow — Conditionals & Loops | 8 | 29% |
| 3 | Data Collections — Lists, Tuples, Dicts, Strings | 7 | 25% |
| 4 | Functions & Exceptions | 8 | 28% |

Source: [pythoninstitute.org/pcep-exam-syllabus](https://pythoninstitute.org/pcep-exam-syllabus)

## Design Principles

- **Balanced answers** — Every exam distributes answers evenly (A/B/C/D) to prevent guessing bias
- **No repeated questions** — Each exam tests unique code patterns
- **Explanations always shown** — Learn from every question, right or wrong
- **Progressive difficulty** — Start easy, build confidence, tackle edge cases last
- **Shared engine** — Adding new exams requires only writing questions; the engine handles the rest
- **Realistic final exam** — Same question count, block distribution, and difficulty as the real PCEP

## Contributing / Adding a New Exam

1. Create `exams/mock_exam_N.py` following the template in `.kiro/steering/pcep-mock-exams.md`
2. Ensure balanced answer distribution and no repeated concepts
3. Create `answer_keys/mock_exam_N_answers.md` with full explanations
4. Validate with:
   ```bash
   python -c "import os; os.chdir('exams'); from exam_engine import validate_exam; exec(open('mock_exam_N.py', encoding='utf-8').read().replace('from exam_engine import run_exam','').split('if __name__')[0]); validate_exam(questoes)"
   ```

## License

This is open study material. The PCEP certification and syllabus are owned by the Python Institute / OpenEDG.

---

*Good luck on your exam!* 🐍
