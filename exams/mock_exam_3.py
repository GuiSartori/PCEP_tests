# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   PCEP MOCK EXAM 3 — Balanced Review                        ║
║   20 Multiple Choice Questions · All domains covered        ║
║   Balanced answers: A=5, B=5, C=5, D=5                     ║
╚══════════════════════════════════════════════════════════════╝
"""

from exam_engine import run_exam

questoes = [
    {
        "pergunta": """What is the output?

    x = "Python"
    print(x[-3:])""",
        "opcoes": ['Pyt', 'tho', 'on', 'hon'],
        "resposta": "D",
        "explicacao": "x[-3:] takes the last 3 characters: 'h', 'o', 'n' → 'hon'."
    },
    {
        "pergunta": """What is the output?

    print(isinstance(True, int))""",
        "opcoes": ['False', 'TypeError', 'True', 'None'],
        "resposta": "C",
        "explicacao": 'bool is a subclass of int in Python. isinstance(True, int) returns True.'
    },
    {
        "pergunta": """What is the output?

    a = [1, 2, 3, 4, 5]
    b = a[1:4]
    b[0] = 99
    print(a[1])""",
        "opcoes": ['99', '2', '1', 'Error'],
        "resposta": "B",
        "explicacao": 'Slicing creates a new list. Modifying b does not change a. a[1] remains 2.'
    },
    {
        "pergunta": """What is the output?

    d = {}
    d[1] = "a"
    d["1"] = "b"
    d[1.0] = "c"
    print(len(d))""",
        "opcoes": ['1', '2', '3', 'Error'],
        "resposta": "B",
        "explicacao": "In Python, 1 == 1.0 and hash(1) == hash(1.0), so d[1.0] overwrites d[1]. Keys: 1 and '1' → len = 2."
    },
    {
        "pergunta": """What is the output?

    def f(a, b, c=3, d=4):
        return a + b + c + d

    print(f(1, 2, d=10))""",
        "opcoes": ['16', '20', '10', 'Error'],
        "resposta": "A",
        "explicacao": 'a=1, b=2, c=3 (default), d=10. Sum: 1+2+3+10 = 16.'
    },
    {
        "pergunta": """What is printed?

    for i in range(5):
        if i == 3:
            break
    else:
        print("else")
    print(i)""",
        "opcoes": ['else then 3', 'else then 4', '4', '3'],
        "resposta": "D",
        "explicacao": 'break stops the loop AND prevents the else from executing. Then prints i=3.'
    },
    {
        "pergunta": """What is the output?

    s = "hello world"
    print(s.split())""",
        "opcoes": ["['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']", "['hello', 'world']", "['hello world']", "('hello', 'world')"],
        "resposta": "B",
        "explicacao": "split() without arguments splits by whitespace: ['hello', 'world']."
    },
    {
        "pergunta": """What is the output?

    x = lambda a, b: a if a > b else b
    print(x(5, 8))""",
        "opcoes": ['5', 'True', 'Error', '8'],
        "resposta": "D",
        "explicacao": 'The lambda returns the larger value. 8 > 5, so it returns 8.'
    },
    {
        "pergunta": """What is the output?

    nums = [1, 2, 3, 4, 5]
    print(nums[::2])""",
        "opcoes": ['[1, 3, 5]', '[2, 4]', '[1, 2]', '[5, 3, 1]'],
        "resposta": "A",
        "explicacao": '[::2] takes elements with step 2, starting from index 0: 1, 3, 5.'
    },
    {
        "pergunta": """What is the output?

    x = 5
    def f():
        global x
        x = 10
    f()
    print(x)""",
        "opcoes": ['5', 'Error', '10', 'None'],
        "resposta": "C",
        "explicacao": 'global allows modifying the global scope variable. x becomes 10.'
    },
    {
        "pergunta": """What is the output?

    print("abc" * 0)""",
        "opcoes": ['abc', '0', 'Error', "''  (empty string)"],
        "resposta": "D",
        "explicacao": "Multiplying a string by 0 results in an empty string ''."
    },
    {
        "pergunta": """What is the output?

    lst = [3, 1, 4, 1, 5]
    lst.sort()
    lst.reverse()
    print(lst[0])""",
        "opcoes": ['5', '1', '3', '4'],
        "resposta": "A",
        "explicacao": 'sort() → [1,1,3,4,5]. reverse() → [5,4,3,1,1]. lst[0] = 5.'
    },
    {
        "pergunta": """What happens when this is executed?

    t = (1, 2, 3)
    t[0] = 10""",
        "opcoes": ['t becomes (10, 2, 3)', 'TypeError: tuples are immutable', 't becomes [10, 2, 3]', 'IndexError'],
        "resposta": "B",
        "explicacao": 'Tuples are immutable. Attempting to assign to an index raises TypeError.'
    },
    {
        "pergunta": """What is the output?

    d = {"x": 1, "y": 2, "z": 3}
    print(list(d.values()))""",
        "opcoes": ["['x', 'y', 'z']", "[('x',1), ('y',2), ('z',3)]", '[1, 2, 3]', 'Error'],
        "resposta": "C",
        "explicacao": 'd.values() returns the dictionary values: 1, 2, 3.'
    },
    {
        "pergunta": """What is the output?

    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("error")
    else:
        print("ok")
    finally:
        print("end")""",
        "opcoes": ['error end', 'end', 'ok end', 'ok'],
        "resposta": "C",
        "explicacao": "No exception → else executes ('ok'). finally always executes ('end')."
    },
    {
        "pergunta": """What is the output?

    x = [1, 2, 3]
    y = [4, 5, 6]
    z = x + y
    print(z[-1], len(z))""",
        "opcoes": ['3 6', '6 3', '6 6', 'Error'],
        "resposta": "C",
        "explicacao": 'x + y = [1,2,3,4,5,6]. z[-1]=6, len(z)=6.'
    },
    {
        "pergunta": """What is the output?

    x = "abcdef"
    print(x[1::2])""",
        "opcoes": ['ace', 'abcdef', 'bce', 'bdf'],
        "resposta": "D",
        "explicacao": "[1::2] starts at index 1 with step 2: 'b','d','f' → 'bdf'."
    },
    {
        "pergunta": """What is the output?

    def f(n):
        if n <= 1:
            return n
        return f(n-1) + f(n-2)

    print(f(6))""",
        "opcoes": ['5', '8', '13', '21'],
        "resposta": "B",
        "explicacao": 'Recursive Fibonacci: f(6) = f(5)+f(4) = 5+3 = 8.'
    },
    {
        "pergunta": """What is the output?

    a = {"a": 1, "b": 2}
    b = {"b": 3, "c": 4}
    a.update(b)
    print(a)""",
        "opcoes": ["{'a': 1, 'b': 3, 'c': 4}", "{'b': 3, 'c': 4}", "{'a': 1, 'b': 2, 'c': 4}", 'Error'],
        "resposta": "A",
        "explicacao": "update() merges dictionaries. Existing keys are overwritten: 'b' becomes 3."
    },
    {
        "pergunta": """What is the output?

    items = ["a", "b", "c"]
    result = list(enumerate(items, start=1))
    print(result[1])""",
        "opcoes": ["(2, 'b')", "(1, 'a')", "(0, 'b')", "(1, 'b')"],
        "resposta": "A",
        "explicacao": "enumerate with start=1 → [(1,'a'),(2,'b'),(3,'c')]. Index [1] → (2, 'b')."
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 3", "20 Questions - Balanced Review")
