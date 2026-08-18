# -*- coding: utf-8 -*-
"""
PCEP FINAL EXAM — Full Certification Simulation
30 Questions in 40 minutes · Mirrors actual PCEP-30-02
Block 1: 7 questions · Block 2: 8 questions
Block 3: 7 questions · Block 4: 8 questions
"""

from exam_engine import run_exam

questoes = [
    # ══════════════════════════════════════════════════════════════
    # Block 1: Fundamentals (Q1-Q7)
    # ══════════════════════════════════════════════════════════════
    {
        # Q1 — Scientific notation → answer: C
        "pergunta": """What is the value of x after this code executes?

    x = 2.5e3
    print(x)""",
        "opcoes": ["25000.0", "2.53", "2500.0", "253"],
        "resposta": "C",
        "explicacao": "2.5e3 is scientific notation meaning 2.5 × 10³ = 2500.0. The result is a float."
    },
    {
        # Q2 — Binary/Octal/Hex literals → answer: B
        "pergunta": """What is the output?

    a = 0b1010
    b = 0o12
    c = 0xA
    print(a == b == c)""",
        "opcoes": ["False", "True", "Error: invalid literal", "None"],
        "resposta": "B",
        "explicacao": "0b1010 (binary) = 10, 0o12 (octal) = 10, 0xA (hex) = 10. All equal, so True."
    },
    {
        # Q3 — print(sep/end) → answer: A
        "pergunta": """What is the output?

    print("A", "B", "C", sep="-", end="!")
    print("D")""",
        "opcoes": ["A-B-C!D", "A B C!D", "A-B-C! D", "A-B-C!\\nD"],
        "resposta": "A",
        "explicacao": "sep='-' joins with dashes, end='!' replaces the newline. Next print starts right after '!', outputting 'D' on the same line."
    },
    {
        # Q4 — input() returns str → answer: D
        "pergunta": """What is the type of x after this code runs?

    x = input("Enter: ")
    # User types: 42""",
        "opcoes": ["int", "float", "depends on what is typed", "str"],
        "resposta": "D",
        "explicacao": "input() ALWAYS returns a string, regardless of what the user types. To get int, you must use int(input(...))."
    },
    {
        # Q5 — Augmented assignment (//= and **=) → answer: D
        "pergunta": """What is the value of x?

    x = 17
    x //= 3
    x **= 2
    print(x)""",
        "opcoes": ["36", "9", "28", "25"],
        "resposta": "D",
        "explicacao": "17 // 3 = 5 (floor division), then 5 ** 2 = 25 (exponentiation)."
    },
    {
        # Q6 — Relational operator chaining → answer: A
        "pergunta": """What is the output?

    x = 5
    print(2 < x < 8)
    print(1 < x > 3)""",
        "opcoes": ["True then True", "True then False", "False then True", "Error"],
        "resposta": "A",
        "explicacao": "Python supports chained comparisons. 2 < 5 < 8 → True. 1 < 5 > 3 means (1<5) and (5>3) → True."
    },
    {
        # Q7 — Bitwise operators → answer: B
        "pergunta": """What is the output?

    x = 12
    print(x >> 2, x & 5)""",
        "opcoes": ["6 4", "3 4", "3 0", "48 5"],
        "resposta": "B",
        "explicacao": "12 in binary is 1100. Right shift by 2: 0011 = 3. Bitwise AND: 1100 & 0101 = 0100 = 4. Output: 3 4."
    },

    # ══════════════════════════════════════════════════════════════
    # Block 2: Control Flow (Q8-Q15)
    # ══════════════════════════════════════════════════════════════
    {
        # Q8 — Nested if with multiple conditions → answer: C
        "pergunta": """What is the output?

    age = 25
    has_id = False
    if age >= 18 and has_id:
        print("allowed")
    elif age >= 18:
        print("need ID")
    else:
        print("denied")""",
        "opcoes": ["allowed", "denied", "need ID", "Error"],
        "resposta": "C",
        "explicacao": "age >= 18 is True but has_id is False, so first condition fails. elif (age >= 18) is True → 'need ID'."
    },
    {
        # Q9 — while with counter pattern → answer: B
        "pergunta": """What is the output?

    count = 0
    total = 0
    while count < 5:
        count += 1
        total += count
    print(total)""",
        "opcoes": ["10", "15", "14", "20"],
        "resposta": "B",
        "explicacao": "count increments first each iteration: adds 1+2+3+4+5 = 15."
    },
    {
        # Q10 — for with negative step range → answer: A
        "pergunta": """What is the output?

    for i in range(10, 0, -3):
        print(i, end=" ")""",
        "opcoes": ["10 7 4 1", "10 7 4", "7 4 1", "10 7 4 1 -2"],
        "resposta": "A",
        "explicacao": "range(10, 0, -3) produces 10, 7, 4, 1. Stops before reaching 0."
    },
    {
        # Q11 — continue inside while → answer: D
        "pergunta": """What is the output?

    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue
        if i > 7:
            break
        print(i, end=" ")""",
        "opcoes": ["1 3 5 7 9", "1 2 3 4 5 6 7", "1 3 5", "1 3 5 7"],
        "resposta": "D",
        "explicacao": "continue skips even numbers. When i=9, i>7 triggers break. Odd numbers 1, 3, 5, 7 are printed before break."
    },
    {
        # Q12 — loop else clause → answer: C
        "pergunta": """What is the output?

    for n in range(2, 6):
        if n == 4:
            break
    else:
        print("done")
    print(n)""",
        "opcoes": ["done followed by 4", "done followed by 3", "4", "3"],
        "resposta": "C",
        "explicacao": "The loop breaks at n=4, so else does NOT execute (else runs only on normal completion). print(n) outputs 4."
    },
    {
        # Q13 — nested for building pattern → answer: A
        "pergunta": """What pattern does this code print?

    for i in range(3):
        for j in range(i + 1):
            print("*", end="")
        print()""",
        "opcoes": ["* then ** then ***", "*** then ** then *", "* then * then *", "** then ** then **"],
        "resposta": "A",
        "explicacao": "i=0: 1 star. i=1: 2 stars. i=2: 3 stars. Builds a growing triangle: *, **, ***."
    },
    {
        # Q14 — range() with all 3 args + break → answer: D
        "pergunta": """What is the output?

    result = []
    for x in range(1, 10, 2):
        if x > 6:
            break
        result.append(x)
    print(result)""",
        "opcoes": ["[1, 3, 5, 7]", "[1, 3, 5, 7, 9]", "[2, 4, 6]", "[1, 3, 5]"],
        "resposta": "D",
        "explicacao": "range(1,10,2) gives 1,3,5,7,9. When x=7, 7>6 triggers break. Only 1, 3, 5 were appended."
    },
    {
        # Q15 — while True with break → answer: C
        "pergunta": """What is the output?

    found = False
    x = 0
    while True:
        x += 2
        if x >= 6:
            found = True
            break
    print(x, found)""",
        "opcoes": ["6 False", "8 True", "6 True", "4 True"],
        "resposta": "C",
        "explicacao": "Loop adds 2 each iteration: x=2, 4, 6. When x=6, x>=6 is True → found=True, break. Output: 6 True."
    },

    # ══════════════════════════════════════════════════════════════
    # Block 3: Data Collections (Q16-Q22)
    # ══════════════════════════════════════════════════════════════
    {
        # Q16 — list.pop() with index → answer: B
        "pergunta": """What is the output?

    items = [10, 20, 30, 40, 50]
    removed = items.pop(2)
    print(removed, items)""",
        "opcoes": ["20 [10, 30, 40, 50]", "30 [10, 20, 40, 50]", "30 [10, 20, 30, 40]", "50 [10, 20, 30, 40]"],
        "resposta": "B",
        "explicacao": "pop(2) removes and returns the element at index 2, which is 30. The list becomes [10, 20, 40, 50]."
    },
    {
        # Q17 — list comprehension with condition → answer: D
        "pergunta": """What is the output?

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    result = [x * 2 for x in nums if x % 2 == 0]
    print(result)""",
        "opcoes": ["[2, 4, 6, 8, 10, 12, 14, 16]", "[1, 4, 3, 8, 5, 12, 7, 16]", "[2, 4, 6, 8]", "[4, 8, 12, 16]"],
        "resposta": "D",
        "explicacao": "The condition filters even numbers (2,4,6,8), then each is multiplied by 2: [4, 8, 12, 16]."
    },
    {
        # Q18 — string .join() → answer: C
        "pergunta": """What is the output?

    words = ["hello", "world", "python"]
    result = " | ".join(words)
    print(result)""",
        "opcoes": ["hello world python", "hello|world|python", "hello | world | python", "[hello, world, python]"],
        "resposta": "C",
        "explicacao": "join() uses the string ' | ' (with spaces) as separator between each list element."
    },
    {
        # Q19 — negative index on list → answer: A
        "pergunta": """What is the output?

    data = [10, 20, 30, 40, 50]
    print(data[-3], data[-1])""",
        "opcoes": ["30 50", "20 40", "40 50", "20 50"],
        "resposta": "A",
        "explicacao": "Negative indexing: -1 is last (50), -3 is third from end (30). Output: 30 50."
    },
    {
        # Q20 — dict.update() → answer: B
        "pergunta": """What is the output?

    info = {"name": "Alice", "age": 30}
    info.update({"age": 31, "city": "NYC"})
    print(len(info), info["age"])""",
        "opcoes": ["2 30", "3 31", "3 30", "2 31"],
        "resposta": "B",
        "explicacao": "update() merges: 'age' is overwritten to 31, 'city' is added. Total keys: 3. info['age'] = 31."
    },
    {
        # Q21 — tuple comparison → answer: D
        "pergunta": """What is the output?

    t1 = (1, 5, 3)
    t2 = (1, 5, 2)
    print(t1 > t2)""",
        "opcoes": ["False", "Error: tuples not comparable", "None", "True"],
        "resposta": "D",
        "explicacao": "Tuple comparison is element-by-element. First elements equal (1==1), second equal (5==5), third: 3 > 2 → True."
    },
    {
        # Q22 — del on list slice → answer: C
        "pergunta": """What is the output?

    data = [0, 1, 2, 3, 4, 5, 6, 7]
    del data[2:5]
    print(data)""",
        "opcoes": ["[0, 1, 2, 5, 6, 7]", "[2, 3, 4]", "[0, 1, 5, 6, 7]", "[0, 1, 6, 7]"],
        "resposta": "C",
        "explicacao": "del data[2:5] removes elements at indices 2, 3, 4 (values 2, 3, 4). Remaining: [0, 1, 5, 6, 7]."
    },

    # ══════════════════════════════════════════════════════════════
    # Block 4: Functions & Exceptions (Q23-Q30)
    # ══════════════════════════════════════════════════════════════
    {
        # Q23 — function with *args → answer: D
        "pergunta": """What is the output?

    def total(*args):
        return sum(args)

    print(total(1, 2, 3, 4))""",
        "opcoes": ["[1, 2, 3, 4]", "(1, 2, 3, 4)", "Error: too many arguments", "10"],
        "resposta": "D",
        "explicacao": "*args collects positional arguments into a tuple. sum((1,2,3,4)) = 10."
    },
    {
        # Q24 — function returning None implicitly → answer: A
        "pergunta": """What is the output?

    def greet(name):
        print(f"Hi, {name}")

    result = greet("Eve")
    print(result)""",
        "opcoes": ["Hi, Eve then None", "Hi, Eve then Hi, Eve", "None", "Hi, Eve"],
        "resposta": "A",
        "explicacao": "greet() prints 'Hi, Eve' but has no return statement, so it returns None. print(result) outputs None."
    },
    {
        # Q25 — global keyword → answer: B
        "pergunta": """What is the output?

    counter = 0

    def increment():
        global counter
        counter += 5

    increment()
    increment()
    print(counter)""",
        "opcoes": ["0", "10", "5", "Error: cannot modify global"],
        "resposta": "B",
        "explicacao": "The global keyword allows modifying the module-level variable. Two calls add 5 each: 0 + 5 + 5 = 10."
    },
    {
        # Q26 — recursive function → answer: C
        "pergunta": """What is the output?

    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(factorial(5))""",
        "opcoes": ["24", "60", "120", "5"],
        "resposta": "C",
        "explicacao": "5! = 5 × 4 × 3 × 2 × 1 = 120. Base case: factorial(1) returns 1."
    },
    {
        # Q27 — multiple except catching → answer: A
        "pergunta": """What is the output?

    try:
        x = int("hello")
    except ValueError:
        print("caught")
    except TypeError:
        print("type error")
    except Exception:
        print("general")""",
        "opcoes": ["caught", "general", "type error", "Error"],
        "resposta": "A",
        "explicacao": "int('hello') raises ValueError. The first except clause catches it specifically, so 'caught' is printed."
    },
    {
        # Q28 — try/finally without except → answer: D
        "pergunta": """What is the output?

    def divide(a, b):
        try:
            return a / b
        finally:
            print("cleanup")

    result = divide(10, 2)
    print(result)""",
        "opcoes": ["5.0 then cleanup", "cleanup only", "Error: finally without except", "cleanup then 5.0"],
        "resposta": "D",
        "explicacao": "finally always executes, even when return is used. 'cleanup' prints before the value is returned. Then print(result) outputs 5.0."
    },
    {
        # Q29 — lambda with filter → answer: B
        "pergunta": """What is the output?

    nums = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 3 == 0, nums))
    print(result)""",
        "opcoes": ["[1, 2, 4, 5]", "[3, 6]", "[0, 0]", "[False, False, True, False, False, True]"],
        "resposta": "B",
        "explicacao": "filter() keeps elements where the lambda returns True. x % 3 == 0 is True for 3 and 6."
    },
    {
        # Q30 — scope shadowing → answer: C
        "pergunta": """What is the output?

    x = 10

    def outer():
        x = 20
        def inner():
            x = 30
            print(x)
        inner()
        print(x)

    outer()
    print(x)""",
        "opcoes": ["10 20 30", "30 30 30", "30 20 10", "20 20 10"],
        "resposta": "C",
        "explicacao": "Each function has its own local x (scope shadowing). inner prints 30, outer prints 20, global prints 10."
    },
]

if __name__ == "__main__":
    run_exam(questoes, "PCEP FINAL EXAM", "30 Questions · 40 min · Full Certification Simulation")
