# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   PCEP MOCK EXAM 2 — Realistic Exam-Level Difficulty        ║
║   20 Multiple Choice Questions · Calibrated to actual PCEP  ║
║   Balanced answers: A=5, B=5, C=5, D=5                     ║
╚══════════════════════════════════════════════════════════════╝

Based on the official PCEP-30-02 syllabus from pythoninstitute.org.
Straightforward code tracing, not advanced tricks.
Passing score: 70%
"""

from exam_engine import run_exam

questoes = [
    # Q1 — Block 1: Numeric operators & precedence → Answer: C
    {
        "pergunta": """What is the output of the following code?

    print(2 ** 3 + 5 % 3 - 1)""",
        "opcoes": ["8", "10", "9", "7"],
        "resposta": "C",
        "explicacao": "Precedence: ** first → 2³=8. Then % → 5%3=2. Then left-to-right: 8+2-1 = 9."
    },
    # Q2 — Block 1: Floor division and modulo → Answer: D
    {
        "pergunta": """What is the output of the following code?

    x = 15
    print(x // 4, x % 4)""",
        "opcoes": ["4 3", "3.75 3", "3 0", "3 3"],
        "resposta": "D",
        "explicacao": "15 // 4 = 3 (floor division). 15 % 4 = 3 (remainder). Output: 3 3."
    },
    # Q3 — Block 1: String operator precedence → Answer: B
    {
        "pergunta": """What is the output of the following code?

    x = "ab" + "cd" * 2
    print(x)""",
        "opcoes": ["abcdabcd", "abcdcd", "ababcdcd", "abcabc"],
        "resposta": "B",
        "explicacao": "* has higher precedence than +. 'cd' * 2 = 'cdcd'. Then 'ab' + 'cdcd' = 'abcdcd'."
    },
    # Q4 — Block 1: Type casting with int() → Answer: A
    {
        "pergunta": """What is the output of the following code?

    x = int(3.7) + int("5")
    print(x)""",
        "opcoes": ["8", "9", "8.7", "Error"],
        "resposta": "A",
        "explicacao": "int(3.7) truncates to 3 (does NOT round). int('5') = 5. Sum: 3 + 5 = 8."
    },
    # Q5 — Block 1: Boolean operators → Answer: B
    {
        "pergunta": """What is the output of the following code?

    x = 5
    y = 10
    print(x > 3 and y < 8)""",
        "opcoes": ["True", "False", "5", "Error"],
        "resposta": "B",
        "explicacao": "x>3 is True, but y<8 is False (y=10). True and False evaluates to False."
    },
    # Q6 — Block 1: Bitwise operator → Answer: A
    {
        "pergunta": """What is the output of the following code?

    x = 5
    y = 3
    print(x | y)""",
        "opcoes": ["7", "3", "5", "1"],
        "resposta": "A",
        "explicacao": "5 = 101 in binary, 3 = 011. Bitwise OR: 101 | 011 = 111 = 7."
    },
    # Q7 — Block 2: if/elif/else → Answer: A
    {
        "pergunta": """What is the output of the following code?

    x = 7
    if x > 10:
        print("high")
    elif x > 5:
        print("mid")
    else:
        print("low")""",
        "opcoes": ["mid", "high", "low", "mid low"],
        "resposta": "A",
        "explicacao": "x=7: first condition (7>10) is False. Second (7>5) is True → prints 'mid'."
    },
    # Q8 — Block 2: while loop → Answer: C
    {
        "pergunta": """What is the output of the following code?

    x = 0
    while x < 4:
        x += 1
    print(x)""",
        "opcoes": ["3", "5", "4", "0"],
        "resposta": "C",
        "explicacao": "Loop: x goes 1→2→3→4. When x=4, condition 4<4 is False → loop exits. Prints 4."
    },
    # Q9 — Block 2: for loop sum → Answer: D
    {
        "pergunta": """What is the output of the following code?

    total = 0
    for i in range(1, 5):
        total += i
    print(total)""",
        "opcoes": ["15", "5", "6", "10"],
        "resposta": "D",
        "explicacao": "range(1,5) produces 1,2,3,4. Sum: 1+2+3+4 = 10."
    },
    # Q10 — Block 2: break statement → Answer: B
    {
        "pergunta": """What is the output of the following code?

    for i in range(1, 6):
        if i % 3 == 0:
            break
        print(i, end=" ")""",
        "opcoes": ["1 2 3", "1 2", "1 2 4 5", "1 2 3 4 5"],
        "resposta": "B",
        "explicacao": "i=1: 1%3≠0 → print 1. i=2: 2%3≠0 → print 2. i=3: 3%3==0 → break. Output: '1 2'."
    },
    # Q11 — Block 2: nested loop count → Answer: A
    {
        "pergunta": """What is the output of the following code?

    count = 0
    for i in range(3):
        for j in range(2):
            count += 1
    print(count)""",
        "opcoes": ["6", "5", "3", "2"],
        "resposta": "A",
        "explicacao": "Outer loop: 3 iterations. Inner loop: 2 per outer. Total: 3 × 2 = 6."
    },
    # Q12 — Block 3: List indexing → Answer: C
    {
        "pergunta": """What is the output of the following code?

    nums = [10, 20, 30, 40, 50]
    print(nums[1] + nums[-1])""",
        "opcoes": ["60", "30", "70", "80"],
        "resposta": "C",
        "explicacao": "nums[1] = 20 (second element). nums[-1] = 50 (last). 20 + 50 = 70."
    },
    # Q13 — Block 3: List slicing → Answer: D
    {
        "pergunta": """What is the output of the following code?

    data = [1, 2, 3, 4, 5, 6]
    print(data[2:5])""",
        "opcoes": ["[2, 3, 4, 5]", "[3, 4, 5, 6]", "[2, 3, 4]", "[3, 4, 5]"],
        "resposta": "D",
        "explicacao": "data[2:5] includes indices 2,3,4 → values [3, 4, 5]. End index is exclusive."
    },
    # Q14 — Block 3: List insert method → Answer: A
    {
        "pergunta": """What is the output of the following code?

    my_list = [3, 1, 4, 1, 5]
    my_list.insert(2, 99)
    print(my_list)""",
        "opcoes": [
            "[3, 1, 99, 4, 1, 5]",
            "[3, 99, 1, 4, 1, 5]",
            "[99, 3, 1, 4, 1, 5]",
            "[3, 1, 4, 99, 1, 5]"
        ],
        "resposta": "A",
        "explicacao": "insert(2, 99) inserts 99 at index 2, shifting existing elements right."
    },
    # Q15 — Block 3: Dictionary keys → Answer: B
    {
        "pergunta": """What is the output of the following code?

    data = {"Peter": 30, "Paul": 31}
    print(list(data.keys()))""",
        "opcoes": [
            "[30, 31]",
            "['Peter', 'Paul']",
            "[('Peter', 30), ('Paul', 31)]",
            "{'Peter', 'Paul'}"
        ],
        "resposta": "B",
        "explicacao": "keys() returns the dictionary keys. list() converts to list: ['Peter', 'Paul']."
    },
    # Q16 — Block 3: Tuple concatenation → Answer: C
    {
        "pergunta": """What is the output of the following code?

    t1 = (1, 2, 3)
    t2 = t1 + (4, 5)
    print(len(t2))""",
        "opcoes": ["3", "2", "5", "Error"],
        "resposta": "C",
        "explicacao": "Tuple concatenation: (1,2,3) + (4,5) = (1,2,3,4,5). Length is 5."
    },
    # Q17 — Block 3: String split → Answer: D
    {
        "pergunta": """What is the output of the following code?

    s = "Hello, World!"
    parts = s.split(",")
    print(len(parts))""",
        "opcoes": ["1", "13", "5", "2"],
        "resposta": "D",
        "explicacao": "split(',') splits at the comma into ['Hello', ' World!']. That's 2 elements."
    },
    # Q18 — Block 4: Function return value → Answer: B
    {
        "pergunta": """What is the output of the following code?

    def add(a, b):
        return a + b

    result = add(3, 4)
    print(result * 2)""",
        "opcoes": ["7", "14", "34", "Error"],
        "resposta": "B",
        "explicacao": "add(3,4) returns 7. Then 7 * 2 = 14."
    },
    # Q19 — Block 4: Variable scope → Answer: D
    {
        "pergunta": """What is the output of the following code?

    x = 5
    def modify():
        x = 10
        return x

    modify()
    print(x)""",
        "opcoes": ["10", "None", "Error", "5"],
        "resposta": "D",
        "explicacao": "x=10 inside modify() is LOCAL. The global x remains 5. modify()'s return value is not used."
    },
    # Q20 — Block 4: Exception handling → Answer: C
    {
        "pergunta": """What is the output of the following code?

    try:
        value = int("hello")
    except ValueError:
        value = -1
    print(value)""",
        "opcoes": ["hello", "0", "-1", "Error"],
        "resposta": "C",
        "explicacao": "int('hello') raises ValueError. The except block sets value=-1. Prints -1."
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 2", "20 Questions - Realistic Exam Level")
