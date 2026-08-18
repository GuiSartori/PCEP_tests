# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════╗
║   PCEP CONCEPT CHECKLIST — Knowledge Gap Diagnostic                 ║
║   One question per concept · Covers ALL PCEP-30-02 exam topics      ║
║   Organized by domain · Identifies your weak spots                  ║
╚══════════════════════════════════════════════════════════════════════╝
"""

questoes = [
    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 1: FUNDAMENTALS & BASIC OPERATIONS
    # ═══════════════════════════════════════════════════════════════

    # 1. Interpreted vs Compiled languages
    {
        "conceito": "Interpreted vs Compiled Languages",
        "dominio": "1 - Fundamentals",
        "pergunta": """Python is best described as:""",
        "opcoes": [
            "A compiled language like C",
            "An interpreted, high-level language",
            "A purely functional language",
            "A low-level assembly language"
        ],
        "resposta": "B",
        "explicacao": "Python is interpreted — source code is executed line by line by the interpreter, not compiled to machine code beforehand."
    },
    # 2. Python versions (2 vs 3)
    {
        "conceito": "Python 2 vs Python 3",
        "dominio": "1 - Fundamentals",
        "pergunta": """Which statement about Python 2 and Python 3 is TRUE?""",
        "opcoes": [
            "Python 2 and 3 are fully compatible",
            "print is a function in Python 3 but a statement in Python 2",
            "Python 2 uses f-strings",
            "Python 3 uses the 'print' statement"
        ],
        "resposta": "B",
        "explicacao": "In Python 3, print() is a function requiring parentheses. In Python 2, 'print' was a statement."
    },
    # 3. Literals — integer
    {
        "conceito": "Integer Literals",
        "dominio": "1 - Fundamentals",
        "pergunta": """Which of the following is NOT a valid integer literal in Python?

    a) 0o17
    b) 0x1F
    c) 0b1012
    d) 1_000_000""",
        "opcoes": [
            "0o17",
            "0x1F",
            "0b1012",
            "1_000_000"
        ],
        "resposta": "C",
        "explicacao": "0b prefix expects binary digits (0 and 1 only). '2' is invalid in binary. 0o is octal, 0x is hex, underscores are allowed separators."
    },
    # 4. Literals — float
    {
        "conceito": "Float Literals & Scientific Notation",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the value of: 3e2 + 1.5e-1?""",
        "opcoes": ["300.15", "30.15", "301.5", "300.015"],
        "resposta": "A",
        "explicacao": "3e2 = 3 × 10² = 300.0. 1.5e-1 = 1.5 × 10⁻¹ = 0.15. Sum = 300.15."
    },
    # 5. Literals — string (escape sequences)
    {
        "conceito": "String Escape Sequences",
        "dominio": "1 - Fundamentals",
        "pergunta": """What does print("Line1\\nLine2\\tEnd") output?""",
        "opcoes": [
            "Line1\\nLine2\\tEnd (literally)",
            "Line1 followed by newline, Line2 followed by tab, End",
            "Line1nLine2tEnd",
            "Error: invalid escape"
        ],
        "resposta": "B",
        "explicacao": "\\n is a newline character, \\t is a tab character. They produce actual whitespace in output."
    },
    # 6. Literals — boolean
    {
        "conceito": "Boolean Type & Truthiness",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: True + True + False?""",
        "opcoes": ["True", "2", "1", "Error"],
        "resposta": "B",
        "explicacao": "bool is a subclass of int. True=1, False=0. So 1 + 1 + 0 = 2."
    },
    # 7. Type function
    {
        "conceito": "type() Function",
        "dominio": "1 - Fundamentals",
        "pergunta": """What does type(4 / 2) return?""",
        "opcoes": [
            "<class 'int'>",
            "<class 'float'>",
            "<class 'str'>",
            "<class 'number'>"
        ],
        "resposta": "B",
        "explicacao": "The / operator ALWAYS returns a float in Python 3, even when the result is a whole number. 4/2 = 2.0."
    },
    # 8. Type casting / conversion
    {
        "conceito": "Type Casting (int, float, str)",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: int(3.9) + int("2")?""",
        "opcoes": ["5", "5.9", "6", "Error"],
        "resposta": "A",
        "explicacao": "int(3.9) truncates to 3 (not rounded). int('2') = 2. Sum = 5."
    },
    # 9. Variable naming rules
    {
        "conceito": "Variable Naming Rules",
        "dominio": "1 - Fundamentals",
        "pergunta": """Which is a valid Python variable name?""",
        "opcoes": ["2nd_place", "my-var", "_private", "class"],
        "resposta": "C",
        "explicacao": "Variables can start with _ or letter, not number or hyphen. 'class' is a reserved keyword."
    },
    # 10. Dynamic typing
    {
        "conceito": "Dynamic Typing",
        "dominio": "1 - Fundamentals",
        "pergunta": """What happens when you run:
    x = 5
    x = "hello"
    print(type(x))""",
        "opcoes": [
            "Error: cannot change type",
            "<class 'int'>",
            "<class 'str'>",
            "None"
        ],
        "resposta": "C",
        "explicacao": "Python is dynamically typed — variables can be reassigned to values of different types without error."
    },
    # 11. Arithmetic operators (+, -, *, /, //, %, **)
    {
        "conceito": "Arithmetic Operators",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: 17 // 3 and 17 % 3?""",
        "opcoes": ["5 and 2", "5.67 and 2", "6 and 2", "5 and 3"],
        "resposta": "A",
        "explicacao": "// is floor division: 17//3 = 5. % is modulo: 17%3 = 2 (remainder)."
    },
    # 12. Operator precedence
    {
        "conceito": "Operator Precedence",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: 2 + 3 * 4 ** 2 - 1?""",
        "opcoes": ["49", "79", "19", "48"],
        "resposta": "A",
        "explicacao": "Precedence: ** first → 4²=16, then * → 3×16=48, then + and - → 2+48-1 = 49."
    },
    # 13. Assignment operators (+=, -=, etc.)
    {
        "conceito": "Augmented Assignment Operators",
        "dominio": "1 - Fundamentals",
        "pergunta": """After running:
    x = 10
    x //= 3
    x += 1
What is x?""",
        "opcoes": ["3", "4", "5", "3.33"],
        "resposta": "B",
        "explicacao": "x //= 3 → 10//3 = 3. Then x += 1 → 3+1 = 4."
    },
    # 14. Comparison operators
    {
        "conceito": "Comparison Operators",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: 5 != 5.0?""",
        "opcoes": ["True", "False", "Error", "None"],
        "resposta": "B",
        "explicacao": "5 == 5.0 is True (Python compares values across int/float). So 5 != 5.0 is False."
    },
    # 15. Logical operators (and, or, not)
    {
        "conceito": "Logical Operators (and, or, not)",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: not False and True or False?""",
        "opcoes": ["True", "False", "None", "Error"],
        "resposta": "A",
        "explicacao": "Precedence: not > and > or. not False=True. True and True=True. True or False=True."
    },
    # 16. Bitwise operators
    {
        "conceito": "Bitwise Operators",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the result of: 6 & 3?""",
        "opcoes": ["2", "7", "1", "5"],
        "resposta": "A",
        "explicacao": "6 = 110 in binary, 3 = 011. Bitwise AND: 110 & 011 = 010 = 2."
    },
    # 17. input() function
    {
        "conceito": "input() Function",
        "dominio": "1 - Fundamentals",
        "pergunta": """If the user types 42, what is the type of: x = input("Enter: ")?""",
        "opcoes": [
            "<class 'int'>",
            "<class 'str'>",
            "<class 'float'>",
            "Depends on what is typed"
        ],
        "resposta": "B",
        "explicacao": "input() ALWAYS returns a string, regardless of what the user types. You must cast explicitly."
    },
    # 18. print() function (sep, end)
    {
        "conceito": "print() Parameters (sep, end)",
        "dominio": "1 - Fundamentals",
        "pergunta": """What is the output of: print(1, 2, 3, sep="-", end="!")?""",
        "opcoes": ["1 2 3!", "1-2-3!", "1-2-3\\n", "-1-2-3!"],
        "resposta": "B",
        "explicacao": "sep='-' replaces the default space between arguments. end='!' replaces the default newline."
    },
    # 19. Comments
    {
        "conceito": "Comments in Python",
        "dominio": "1 - Fundamentals",
        "pergunta": """Which creates a single-line comment in Python?""",
        "opcoes": ["// comment", "# comment", "/* comment */", "-- comment"],
        "resposta": "B",
        "explicacao": "Python uses # for single-line comments. The other syntaxes belong to other languages."
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 2: CONTROL FLOW
    # ═══════════════════════════════════════════════════════════════

    # 20. if statement
    {
        "conceito": "if Statement",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output?
    x = 15
    if x > 20:
        print("A")
    elif x > 10:
        print("B")
    elif x > 5:
        print("C")
    else:
        print("D")""",
        "opcoes": ["A", "B", "C", "B and C"],
        "resposta": "B",
        "explicacao": "x=15 fails first condition, passes 'x > 10', prints 'B' and stops (elif is exclusive)."
    },
    # 21. Nested if
    {
        "conceito": "Nested Conditionals",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output?
    x = 10
    if x > 5:
        if x > 15:
            print("high")
        else:
            print("mid")
    else:
        print("low")""",
        "opcoes": ["high", "mid", "low", "Error"],
        "resposta": "B",
        "explicacao": "x=10 > 5 (enters outer if), but 10 is NOT > 15, so inner else prints 'mid'."
    },
    # 22. while loop
    {
        "conceito": "while Loop",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output?
    n = 1
    while n < 16:
        n *= 2
    print(n)""",
        "opcoes": ["8", "16", "32", "15"],
        "resposta": "B",
        "explicacao": "n doubles: 1→2→4→8→16. At n=16, condition 16<16 is False, loop exits. n=16."
    },
    # 23. for loop with range()
    {
        "conceito": "for Loop with range()",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output of: print(list(range(1, 10, 3)))?""",
        "opcoes": ["[1, 4, 7]", "[1, 4, 7, 10]", "[3, 6, 9]", "[1, 3, 6, 9]"],
        "resposta": "A",
        "explicacao": "range(1, 10, 3): starts at 1, step 3, stops BEFORE 10. Values: 1, 4, 7."
    },
    # 24. break statement
    {
        "conceito": "break Statement",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output?
    for i in range(10):
        if i == 4:
            break
        print(i, end=" ")""",
        "opcoes": ["0 1 2 3", "0 1 2 3 4", "1 2 3 4", "0 1 2 3 4 5 6 7 8 9"],
        "resposta": "A",
        "explicacao": "Loop prints 0,1,2,3 then when i=4, break exits immediately before printing 4."
    },
    # 25. continue statement
    {
        "conceito": "continue Statement",
        "dominio": "2 - Control Flow",
        "pergunta": """What is the output?
    for i in range(6):
        if i % 2 == 0:
            continue
        print(i, end=" ")""",
        "opcoes": ["0 2 4", "1 3 5", "1 2 3 4 5", "2 4 6"],
        "resposta": "B",
        "explicacao": "continue skips even numbers (0,2,4). Only odd numbers (1,3,5) are printed."
    },
    # 26. pass statement
    {
        "conceito": "pass Statement",
        "dominio": "2 - Control Flow",
        "pergunta": """What does 'pass' do in Python?""",
        "opcoes": [
            "Exits the loop",
            "Skips to the next iteration",
            "Does nothing — acts as a placeholder",
            "Raises an exception"
        ],
        "resposta": "C",
        "explicacao": "'pass' is a null operation — it does nothing. Used as a placeholder where code is syntactically required."
    },
    # 27. for/else and while/else
    {
        "conceito": "Loop else Clause",
        "dominio": "2 - Control Flow",
        "pergunta": """When does the 'else' clause of a for/while loop execute?""",
        "opcoes": [
            "When the loop body raises an exception",
            "When the loop completes WITHOUT hitting a break",
            "When the loop condition is initially False",
            "After every iteration"
        ],
        "resposta": "B",
        "explicacao": "The else clause runs only if the loop finishes naturally (no break). If break is hit, else is skipped."
    },
    # 28. Nested loops
    {
        "conceito": "Nested Loops",
        "dominio": "2 - Control Flow",
        "pergunta": """How many times does 'X' print?
    for i in range(3):
        for j in range(4):
            print("X", end="")""",
        "opcoes": ["7", "12", "3", "4"],
        "resposta": "B",
        "explicacao": "Outer loop runs 3 times, inner loop runs 4 times each → 3 × 4 = 12."
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 3: DATA COLLECTIONS (Strings, Lists, Tuples, Dicts)
    # ═══════════════════════════════════════════════════════════════

    # 29. String indexing
    {
        "conceito": "String Indexing (positive & negative)",
        "dominio": "3 - Data Collections",
        "pergunta": """Given s = "Python", what is s[0] + s[-1]?""",
        "opcoes": ["Pn", "Py", "on", "yn"],
        "resposta": "A",
        "explicacao": "s[0] = 'P' (first char). s[-1] = 'n' (last char). Concatenation: 'Pn'."
    },
    # 30. String slicing
    {
        "conceito": "String Slicing",
        "dominio": "3 - Data Collections",
        "pergunta": """Given s = "abcdefgh", what is s[2:6]?""",
        "opcoes": ["cdef", "bcde", "cdefg", "bcdef"],
        "resposta": "A",
        "explicacao": "s[2:6] includes indices 2,3,4,5 → 'c','d','e','f' → 'cdef'."
    },
    # 31. String slicing with step
    {
        "conceito": "String Slicing with Step",
        "dominio": "3 - Data Collections",
        "pergunta": """Given s = "abcdefgh", what is s[::3]?""",
        "opcoes": ["adg", "ace", "beh", "adf"],
        "resposta": "A",
        "explicacao": "Step 3 starting from 0: indices 0,3,6 → 'a','d','g' → 'adg'."
    },
    # 32. String concatenation & repetition
    {
        "conceito": "String Concatenation & Repetition",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the result of: "ha" * 3 + "!"?""",
        "opcoes": ["hahaha!", "ha3!", "ha!ha!ha!", "Error"],
        "resposta": "A",
        "explicacao": "'ha' * 3 = 'hahaha'. Then + '!' = 'hahaha!'."
    },
    # 33. String immutability
    {
        "conceito": "String Immutability",
        "dominio": "3 - Data Collections",
        "pergunta": """What happens when you run: s = "hello"; s[0] = "H"?""",
        "opcoes": [
            "s becomes 'Hello'",
            "TypeError: strings are immutable",
            "s becomes 'HELLO'",
            "Nothing happens silently"
        ],
        "resposta": "B",
        "explicacao": "Strings are immutable in Python. You cannot assign to individual characters."
    },
    # 34. String methods (upper, lower, strip)
    {
        "conceito": "String Methods: upper(), lower(), strip()",
        "dominio": "3 - Data Collections",
        "pergunta": """What is "  Hello  ".strip().lower()?""",
        "opcoes": ["hello", "  hello  ", "Hello", "HELLO"],
        "resposta": "A",
        "explicacao": "strip() removes whitespace → 'Hello'. lower() converts to lowercase → 'hello'."
    },
    # 35. String methods (split, join)
    {
        "conceito": "String Methods: split() and join()",
        "dominio": "3 - Data Collections",
        "pergunta": """What is "-".join("abc".split())?""",
        "opcoes": ["a-b-c", "abc", "a-bc", "-abc-"],
        "resposta": "B",
        "explicacao": "'abc'.split() with no spaces returns ['abc']. Joining one element: 'abc'."
    },
    # 36. String methods (find, replace, count)
    {
        "conceito": "String Methods: find(), replace(), count()",
        "dominio": "3 - Data Collections",
        "pergunta": """What is "banana".count("an")?""",
        "opcoes": ["1", "2", "3", "0"],
        "resposta": "B",
        "explicacao": "'banana' contains 'an' at positions 1 and 3 (non-overlapping). Count = 2."
    },
    # 37. String formatting (f-strings)
    {
        "conceito": "f-string Formatting",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the output of:
    name = "World"
    print(f"Hello, {name}!")""",
        "opcoes": ["Hello, {name}!", "Hello, World!", "f'Hello, World!'", "Error"],
        "resposta": "B",
        "explicacao": "f-strings evaluate expressions inside {} at runtime. {name} becomes 'World'."
    },
    # 38. String 'in' operator
    {
        "conceito": "Membership Test with 'in' (Strings)",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the result of: "py" in "python"?""",
        "opcoes": ["False", "True", "Error", "None"],
        "resposta": "B",
        "explicacao": "'in' checks substring presence. 'py' is found at the beginning of 'python'."
    },
    # 39. List creation and indexing
    {
        "conceito": "List Creation & Indexing",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the output of:
    lst = [10, 20, 30, 40, 50]
    print(lst[1], lst[-2])""",
        "opcoes": ["10 40", "20 40", "20 50", "10 50"],
        "resposta": "B",
        "explicacao": "lst[1] = 20 (second element). lst[-2] = 40 (second from end)."
    },
    # 40. List slicing
    {
        "conceito": "List Slicing",
        "dominio": "3 - Data Collections",
        "pergunta": """What is [0, 1, 2, 3, 4, 5][1:5:2]?""",
        "opcoes": ["[1, 3]", "[1, 2, 3, 4]", "[0, 2, 4]", "[1, 3, 5]"],
        "resposta": "A",
        "explicacao": "[1:5:2] starts at index 1, ends before 5, step 2. Indices 1,3 → values [1, 3]."
    },
    # 41. List mutability
    {
        "conceito": "List Mutability (vs String Immutability)",
        "dominio": "3 - Data Collections",
        "pergunta": """After running: lst = [1, 2, 3]; lst[1] = 99 — what is lst?""",
        "opcoes": ["[1, 2, 3]", "Error: lists are immutable", "[1, 99, 3]", "[99, 2, 3]"],
        "resposta": "C",
        "explicacao": "Lists are mutable — you can assign to individual indices. lst becomes [1, 99, 3]."
    },
    # 42. list.append() vs list.extend()
    {
        "conceito": "append() vs extend()",
        "dominio": "3 - Data Collections",
        "pergunta": """After:
    a = [1, 2]
    a.append([3, 4])
    b = [1, 2]
    b.extend([3, 4])
What are len(a) and len(b)?""",
        "opcoes": ["3 and 4", "4 and 4", "3 and 3", "4 and 3"],
        "resposta": "A",
        "explicacao": "append adds the list as ONE element (len=3). extend adds each element individually (len=4)."
    },
    # 43. list.insert()
    {
        "conceito": "list.insert()",
        "dominio": "3 - Data Collections",
        "pergunta": """After: lst = [1, 3, 4]; lst.insert(1, 2) — what is lst?""",
        "opcoes": ["[1, 2, 3, 4]", "[2, 1, 3, 4]", "[1, 3, 2, 4]", "[1, 3, 4, 2]"],
        "resposta": "A",
        "explicacao": "insert(1, 2) inserts value 2 at index 1, shifting others right. Result: [1, 2, 3, 4]."
    },
    # 44. list.remove() vs list.pop()
    {
        "conceito": "remove() vs pop()",
        "dominio": "3 - Data Collections",
        "pergunta": """Given lst = [5, 3, 5, 7]. After lst.remove(5), what is lst?""",
        "opcoes": ["[3, 7]", "[3, 5, 7]", "[5, 3, 7]", "Error"],
        "resposta": "B",
        "explicacao": "remove() deletes only the FIRST occurrence of the value. [5, 3, 5, 7] → [3, 5, 7]."
    },
    # 45. list.sort() vs sorted()
    {
        "conceito": "sort() vs sorted()",
        "dominio": "3 - Data Collections",
        "pergunta": """What does list.sort() return?""",
        "opcoes": ["A new sorted list", "None (sorts in place)", "The original list", "A tuple"],
        "resposta": "B",
        "explicacao": "sort() modifies the list in-place and returns None. sorted() returns a NEW sorted list."
    },
    # 46. List comprehension
    {
        "conceito": "List Comprehension",
        "dominio": "3 - Data Collections",
        "pergunta": """What is [x*2 for x in range(4)]?""",
        "opcoes": ["[0, 2, 4, 6]", "[2, 4, 6, 8]", "[0, 1, 2, 3]", "[1, 2, 3, 4]"],
        "resposta": "A",
        "explicacao": "range(4) = 0,1,2,3. Each multiplied by 2: [0, 2, 4, 6]."
    },
    # 47. List references vs copies
    {
        "conceito": "List References vs Copies",
        "dominio": "3 - Data Collections",
        "pergunta": """After:
    a = [1, 2, 3]
    b = a
    b.append(4)
What is a?""",
        "opcoes": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4, 1, 2, 3]", "Error"],
        "resposta": "B",
        "explicacao": "b = a creates a REFERENCE, not a copy. Both point to the same list object."
    },
    # 48. del statement on lists
    {
        "conceito": "del Statement",
        "dominio": "3 - Data Collections",
        "pergunta": """After: lst = [1, 2, 3, 4, 5]; del lst[1:3] — what is lst?""",
        "opcoes": ["[1, 4, 5]", "[1, 2, 5]", "[2, 3]", "[1, 3, 4, 5]"],
        "resposta": "A",
        "explicacao": "del lst[1:3] removes indices 1 and 2 (values 2, 3). Result: [1, 4, 5]."
    },
    # 49. Tuple creation and properties
    {
        "conceito": "Tuple Creation & Immutability",
        "dominio": "3 - Data Collections",
        "pergunta": """Which creates a single-element tuple?""",
        "opcoes": ["t = (1)", "t = (1,)", "t = [1]", "t = tuple[1]"],
        "resposta": "B",
        "explicacao": "(1) is just the integer 1 in parentheses. The trailing comma (1,) makes it a tuple."
    },
    # 50. Tuple unpacking
    {
        "conceito": "Tuple Unpacking",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the output?
    a, b, c = (10, 20, 30)
    print(b)""",
        "opcoes": ["10", "20", "30", "(10, 20, 30)"],
        "resposta": "B",
        "explicacao": "Tuple unpacking assigns each element to the corresponding variable. b gets 20."
    },
    # 51. Dictionary creation
    {
        "conceito": "Dictionary Creation",
        "dominio": "3 - Data Collections",
        "pergunta": """Which is a valid dictionary?""",
        "opcoes": [
            "{1: 'a', 2: 'b'}",
            "{[1,2]: 'a'}",
            "{'a', 'b', 'c'}",
            "{1; 'a', 2; 'b'}"
        ],
        "resposta": "A",
        "explicacao": "Dicts use {key: value}. Lists can't be keys (unhashable). {'a','b','c'} is a set."
    },
    # 52. Dictionary access ([], get())
    {
        "conceito": "Dictionary Access: [] vs get()",
        "dominio": "3 - Data Collections",
        "pergunta": """Given d = {"a": 1}. What is the difference between d["b"] and d.get("b")?""",
        "opcoes": [
            "Both return None",
            "d['b'] raises KeyError; d.get('b') returns None",
            "Both raise KeyError",
            "d['b'] returns None; d.get('b') raises KeyError"
        ],
        "resposta": "B",
        "explicacao": "[] raises KeyError if key is missing. get() returns None (or a default value) instead."
    },
    # 53. Dictionary methods (keys, values, items)
    {
        "conceito": "Dictionary Methods: keys(), values(), items()",
        "dominio": "3 - Data Collections",
        "pergunta": """What does dict.items() return?""",
        "opcoes": [
            "A list of keys",
            "A list of values",
            "A view of (key, value) tuples",
            "A new dictionary"
        ],
        "resposta": "C",
        "explicacao": "items() returns a view object containing (key, value) pairs as tuples."
    },
    # 54. Dictionary 'in' operator
    {
        "conceito": "Membership Test 'in' for Dictionaries",
        "dominio": "3 - Data Collections",
        "pergunta": """Given d = {"x": 10, "y": 20}. What does '10 in d' evaluate to?""",
        "opcoes": ["True", "False", "Error", "10"],
        "resposta": "B",
        "explicacao": "'in' checks KEYS of a dictionary by default, not values. 10 is not a key."
    },
    # 55. Dictionary iteration
    {
        "conceito": "Iterating Over Dictionaries",
        "dominio": "3 - Data Collections",
        "pergunta": """What does this loop iterate over?
    d = {"a": 1, "b": 2}
    for x in d:
        print(x)""",
        "opcoes": ["Values (1, 2)", "Keys ('a', 'b')", "Tuples (('a',1), ('b',2))", "Indices (0, 1)"],
        "resposta": "B",
        "explicacao": "Iterating directly over a dict yields its KEYS. Use .values() or .items() for others."
    },
    # 56. 'in' operator for lists
    {
        "conceito": "Membership Test 'in' for Lists",
        "dominio": "3 - Data Collections",
        "pergunta": """What is the result of: 3 in [1, 2, [3, 4]]?""",
        "opcoes": ["True", "False", "Error", "[3, 4]"],
        "resposta": "B",
        "explicacao": "'in' checks top-level elements only. The list contains 1, 2, and [3,4] — not 3 directly."
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 4: FUNCTIONS AND EXCEPTIONS
    # ═══════════════════════════════════════════════════════════════

    # 57. Function definition (def)
    {
        "conceito": "Function Definition with def",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is wrong with this code?
    def greet:
        print("Hello")""",
        "opcoes": [
            "Nothing, it works",
            "Missing parentheses after function name",
            "Missing return statement",
            "Incorrect indentation"
        ],
        "resposta": "B",
        "explicacao": "Function definitions require parentheses: def greet(): — even with no parameters."
    },
    # 58. return statement
    {
        "conceito": "return Statement",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What does a function return if it has no return statement?""",
        "opcoes": ["0", "'' (empty string)", "None", "Error"],
        "resposta": "C",
        "explicacao": "Functions without an explicit return statement implicitly return None."
    },
    # 59. Multiple return values
    {
        "conceito": "Returning Multiple Values",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the type of the result?
    def f():
        return 1, 2, 3
    result = f()""",
        "opcoes": ["list", "tuple", "int", "dict"],
        "resposta": "B",
        "explicacao": "Returning comma-separated values implicitly creates a tuple: (1, 2, 3)."
    },
    # 60. Positional arguments
    {
        "conceito": "Positional Arguments",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    def sub(a, b):
        return a - b
    print(sub(10, 3))""",
        "opcoes": ["-7", "7", "13", "Error"],
        "resposta": "B",
        "explicacao": "Positional: a=10, b=3. Returns 10 - 3 = 7."
    },
    # 61. Keyword arguments
    {
        "conceito": "Keyword Arguments",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    def sub(a, b):
        return a - b
    print(sub(b=10, a=3))""",
        "opcoes": ["7", "-7", "13", "Error"],
        "resposta": "B",
        "explicacao": "Keyword args: a=3, b=10 (order doesn't matter). Returns 3 - 10 = -7."
    },
    # 62. Default parameter values
    {
        "conceito": "Default Parameter Values",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    def power(base, exp=2):
        return base ** exp
    print(power(3))""",
        "opcoes": ["6", "9", "8", "Error"],
        "resposta": "B",
        "explicacao": "exp defaults to 2. power(3) = 3 ** 2 = 9."
    },
    # 63. Mutable default argument pitfall
    {
        "conceito": "Mutable Default Argument Pitfall",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is printed on the second call?
    def add(item, lst=[]):
        lst.append(item)
        return lst
    add(1)
    print(add(2))""",
        "opcoes": ["[2]", "[1, 2]", "Error", "None"],
        "resposta": "B",
        "explicacao": "Mutable defaults persist between calls. The same list object is reused: [1] → [1, 2]."
    },
    # 64. Local vs global scope
    {
        "conceito": "Local vs Global Scope",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    x = 10
    def f():
        x = 20
        print(x)
    f()
    print(x)""",
        "opcoes": ["20 20", "20 10", "10 10", "Error"],
        "resposta": "B",
        "explicacao": "Inside f(), x=20 is LOCAL. Outside, global x remains 10. Output: 20 then 10."
    },
    # 65. global keyword
    {
        "conceito": "global Keyword",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    x = 1
    def f():
        global x
        x = 99
    f()
    print(x)""",
        "opcoes": ["1", "99", "Error", "None"],
        "resposta": "B",
        "explicacao": "'global x' allows the function to modify the module-level x. After f(), x = 99."
    },
    # 66. Recursion
    {
        "conceito": "Recursion",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    print(factorial(5))""",
        "opcoes": ["24", "120", "60", "5"],
        "resposta": "B",
        "explicacao": "5! = 5×4×3×2×1 = 120. The base case returns 1 when n <= 1."
    },
    # 67. Lambda functions
    {
        "conceito": "Lambda Functions",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    double = lambda x: x * 2
    print(double(7))""",
        "opcoes": ["7", "14", "Error", "x * 2"],
        "resposta": "B",
        "explicacao": "Lambda creates an anonymous function. double(7) = 7 * 2 = 14."
    },
    # 68. try/except basic
    {
        "conceito": "try/except Basic Structure",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("caught")""",
        "opcoes": ["10/0 then caught", "caught", "Error crashes program", "0"],
        "resposta": "B",
        "explicacao": "Division by zero raises ZeroDivisionError, which is caught. Prints 'caught'."
    },
    # 69. Multiple except blocks
    {
        "conceito": "Multiple except Blocks",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is the output?
    try:
        x = int("abc")
    except ValueError:
        print("val")
    except TypeError:
        print("type")""",
        "opcoes": ["type", "val", "val type", "Error"],
        "resposta": "B",
        "explicacao": "int('abc') raises ValueError (not TypeError). The matching except block prints 'val'."
    },
    # 70. else clause in try
    {
        "conceito": "try/except/else",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """When does the 'else' clause in try/except execute?""",
        "opcoes": [
            "When an exception occurs",
            "Always, after try",
            "Only when NO exception occurs in try",
            "Before the try block"
        ],
        "resposta": "C",
        "explicacao": "The else clause runs only when the try block completes WITHOUT raising any exception."
    },
    # 71. finally clause
    {
        "conceito": "finally Clause",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """What is special about the 'finally' clause?""",
        "opcoes": [
            "It runs only when an exception occurs",
            "It runs only when no exception occurs",
            "It ALWAYS runs, regardless of whether an exception occurred",
            "It replaces the except clause"
        ],
        "resposta": "C",
        "explicacao": "'finally' ALWAYS executes — whether the try succeeded, an exception was caught, or even if a return was hit."
    },
    # 72. ValueError
    {
        "conceito": "ValueError Exception",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """Which operation raises a ValueError?""",
        "opcoes": [
            "int('hello')",
            "1 / 0",
            "lst[100]",
            "'a' + 1"
        ],
        "resposta": "A",
        "explicacao": "int('hello') can't convert 'hello' to int → ValueError. 1/0→ZeroDivisionError, lst[100]→IndexError, 'a'+1→TypeError."
    },
    # 73. TypeError
    {
        "conceito": "TypeError Exception",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """Which operation raises a TypeError?""",
        "opcoes": [
            "int('3')",
            "'text' + 5",
            "x = 10 / 3",
            "len([1,2,3])"
        ],
        "resposta": "B",
        "explicacao": "You cannot concatenate str and int directly. 'text' + 5 raises TypeError."
    },
    # 74. IndexError
    {
        "conceito": "IndexError Exception",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """Given lst = [1, 2, 3]. Which raises IndexError?""",
        "opcoes": ["lst[2]", "lst[-1]", "lst[3]", "lst[0]"],
        "resposta": "C",
        "explicacao": "Valid indices are -3 to 2 for a 3-element list. lst[3] is out of range → IndexError."
    },
    # 75. KeyError
    {
        "conceito": "KeyError Exception",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """Given d = {"a": 1}. What raises KeyError?""",
        "opcoes": ["d['a']", "d.get('b')", "d['b']", "'a' in d"],
        "resposta": "C",
        "explicacao": "d['b'] accesses a non-existent key directly → KeyError. get() returns None instead."
    },
    # 76. ZeroDivisionError
    {
        "conceito": "ZeroDivisionError",
        "dominio": "4 - Functions & Exceptions",
        "pergunta": """Which operations raise ZeroDivisionError? (pick the correct one)""",
        "opcoes": [
            "Only 1/0",
            "1/0 and 1//0 and 1%0",
            "Only 1/0 and 1//0",
            "None — Python returns infinity"
        ],
        "resposta": "B",
        "explicacao": "All division-related operators (/, //, %) raise ZeroDivisionError when dividing by zero."
    },
]


# ════════════════════════════════════════════════════════════════
# EXECUTION ENGINE
# ════════════════════════════════════════════════════════════════

def rodar_checklist():
    print("\n" + "═" * 70)
    print("   PCEP CONCEPT CHECKLIST — Knowledge Gap Diagnostic")
    print("   76 Questions · One per concept · All PCEP-30-02 domains")
    print("═" * 70)
    print("   Answer with A, B, C, or D. Type 'quit' to exit early.")
    print("═" * 70)

    respostas_usuario = []
    total = len(questoes)
    dominio_atual = ""

    for i, q in enumerate(questoes, 1):
        # Print domain header when it changes
        if q["dominio"] != dominio_atual:
            dominio_atual = q["dominio"]
            print(f"\n{'═' * 70}")
            print(f"   DOMAIN: {dominio_atual.upper()}")
            print(f"{'═' * 70}")

        print(f"\n{'─' * 70}")
        print(f"  Q{i}/{total} — [{q['conceito']}]")
        print(f"{'─' * 70}")
        print(f"\n{q['pergunta']}\n")

        letras = ["A", "B", "C", "D"]
        for j, opcao in enumerate(q["opcoes"]):
            print(f"    {letras[j]}. {opcao}")

        while True:
            resp = input(f"\n  Your answer (A/B/C/D): ").strip().upper()
            if resp == "QUIT":
                print("\n  Checklist ended early.")
                if respostas_usuario:
                    mostrar_resultado(respostas_usuario, questoes[:len(respostas_usuario)])
                return
            if resp in letras:
                respostas_usuario.append(resp)
                break
            print("  ⚠ Invalid answer. Type A, B, C or D.")

    mostrar_resultado(respostas_usuario, questoes)


def mostrar_resultado(respostas_usuario, questoes_respondidas):
    print("\n\n" + "═" * 70)
    print("   RESULTS — CONCEPT CHECKLIST")
    print("═" * 70)

    acertos = 0
    gaps = []  # Track weak concepts

    dominio_scores = {}  # {domain: [correct, total]}

    for i, q in enumerate(questoes_respondidas):
        correta = q["resposta"]
        escolhida = respostas_usuario[i]
        status = "✅" if escolhida == correta else "❌"

        # Track domain scores
        dom = q["dominio"]
        if dom not in dominio_scores:
            dominio_scores[dom] = [0, 0]
        dominio_scores[dom][1] += 1

        if escolhida == correta:
            acertos += 1
            dominio_scores[dom][0] += 1
        else:
            gaps.append(q)
            print(f"  {status} Q{i+1:2d} [{q['conceito']}]")
            print(f"       You: {escolhida} → Correct: {correta}")
            print(f"       💡 {q['explicacao']}")

    total = len(questoes_respondidas)
    percentual = (acertos / total) * 100

    # Domain breakdown
    print(f"\n{'═' * 70}")
    print("   SCORE BY DOMAIN")
    print(f"{'═' * 70}")
    for dom, (correct, tot) in dominio_scores.items():
        pct = (correct / tot) * 100 if tot > 0 else 0
        bar = "█" * int(pct // 5) + "░" * (20 - int(pct // 5))
        status_icon = "✅" if pct >= 70 else "⚠️" if pct >= 50 else "❌"
        print(f"  {status_icon} {dom:<30} {correct:2d}/{tot:2d} ({pct:5.1f}%) {bar}")

    # Overall score
    print(f"\n{'═' * 70}")
    print(f"  OVERALL SCORE: {acertos}/{total} ({percentual:.0f}%)")
    print(f"{'═' * 70}")

    if percentual >= 70:
        print("  🎉 PASSING SCORE (minimum 70%)")
    else:
        print("  📚 Below 70%. Focus on the gaps identified above.")

    # Knowledge gaps summary
    if gaps:
        print(f"\n{'═' * 70}")
        print(f"   KNOWLEDGE GAPS — Concepts to review ({len(gaps)} gaps)")
        print(f"{'═' * 70}")
        for g in gaps:
            print(f"  • [{g['dominio']}] {g['conceito']}")

    print(f"{'═' * 70}\n")


if __name__ == "__main__":
    rodar_checklist()
