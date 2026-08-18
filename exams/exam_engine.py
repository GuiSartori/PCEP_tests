# -*- coding: utf-8 -*-
"""
Shared exam engine for all PCEP mock exams.
Handles question display, user input, scoring, and results.
"""


def run_exam(questions, title="PCEP MOCK EXAM", description=""):
    """Run an interactive multiple-choice exam in the terminal.

    Args:
        questions: List of question dicts with keys:
            - pergunta (str): The question text
            - opcoes (list[str]): 4 options
            - resposta (str): Correct answer letter (A/B/C/D)
            - explicacao (str): Explanation shown after grading
        title: Exam title displayed in header
        description: Optional subtitle
    """
    print("\n" + "=" * 60)
    print(f"   {title}")
    if description:
        print(f"   {description}")
    print("=" * 60)
    print("   Answer with A, B, C, or D. Type 'quit' to exit.")
    print("=" * 60)

    user_answers = []
    total = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"\n{'-' * 60}")
        print(f"  QUESTION {i}/{total}")
        print(f"{'-' * 60}")
        print(f"\n{q['pergunta']}\n")

        letters = ["A", "B", "C", "D"]
        for j, option in enumerate(q["opcoes"]):
            print(f"    {letters[j]}. {option}")

        while True:
            resp = input("\n  Your answer (A/B/C/D): ").strip().upper()
            if resp in ("QUIT", "SAIR"):
                print("\n  Exam ended early.")
                if user_answers:
                    _show_results(user_answers, questions[:len(user_answers)], title)
                return
            if resp in letters:
                user_answers.append(resp)
                break
            print("  ! Invalid answer. Type A, B, C, or D.")

    _show_results(user_answers, questions, title)


def _show_results(user_answers, questions, title):
    """Display scoring results with explanations for every question."""
    total = len(questions)

    print("\n\n" + "=" * 60)
    print(f"   RESULTS - {title}")
    print("=" * 60)

    correct_count = 0
    for i, q in enumerate(questions):
        correct = q["resposta"]
        chosen = user_answers[i]
        is_correct = chosen == correct

        if is_correct:
            correct_count += 1
            status = "[OK]"
            print(f"  {status} Q{i+1:2d}: You answered {chosen} -> CORRECT")
        else:
            status = "[X]"
            print(f"  {status} Q{i+1:2d}: You answered {chosen} -> Correct: {correct}")

        print(f"       > {q['explicacao']}")

    percentage = (correct_count / total) * 100
    print(f"\n{'=' * 60}")
    print(f"  FINAL SCORE: {correct_count}/{total} ({percentage:.0f}%)")
    print("=" * 60)

    if percentage >= 70:
        print("  PASSED! (minimum 70%)")
    else:
        print("  Below 70%. Review the explanations above.")

    print("=" * 60 + "\n")


def validate_exam(questions):
    """Utility to check answer balance and question integrity.

    Run this during development to verify exams are balanced.
    """
    from collections import Counter

    answers = [q["resposta"] for q in questions]
    count = Counter(answers)
    total = len(questions)

    print(f"Total questions: {total}")
    print(f"Answer distribution: {dict(sorted(count.items()))}")

    # Check consecutive
    max_consec = 1
    current = 1
    for i in range(1, len(answers)):
        if answers[i] == answers[i - 1]:
            current += 1
            max_consec = max(max_consec, current)
        else:
            current = 1
    print(f"Max consecutive same letter: {max_consec}")

    # Warnings
    if total == 20:
        expected = 5
        for letter in "ABCD":
            if count.get(letter, 0) != expected:
                print(f"  WARNING: {letter} has {count.get(letter, 0)} (expected {expected})")

    if max_consec > 3:
        print("  WARNING: More than 3 consecutive same-letter answers")

    # Check required fields
    for i, q in enumerate(questions):
        for field in ("pergunta", "opcoes", "resposta", "explicacao"):
            if field not in q:
                print(f"  ERROR: Q{i+1} missing field '{field}'")
        if "opcoes" in q and len(q["opcoes"]) != 4:
            print(f"  ERROR: Q{i+1} has {len(q['opcoes'])} options (expected 4)")

    print("Validation complete.")
