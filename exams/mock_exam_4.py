# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   PCEP MOCK EXAM 4 — Intermediate/Hard                      ║
║   20 Multiple Choice Questions · Subtle behaviors           ║
║   Balanced answers: A=5, B=5, C=5, D=5                     ║
╚══════════════════════════════════════════════════════════════╝
"""

from exam_engine import run_exam

questoes = [
    {
        "pergunta": """What is the output?

    x = 1
    y = 2
    z = x
    x = y
    y = z
    print(x, y, z)""",
        "opcoes": ['1 2 1', '2 1 2', '1 1 2', '2 1 1'],
        "resposta": "D",
        "explicacao": 'z=1, x=2, y=z=1. Manual swap: x=2, y=1, z=1.'
    },
    {
        "pergunta": """What is the output?

    print(2 ** 3 + 5 // 2 - 1 * 3)""",
        "opcoes": ['7', '8', '9', '10'],
        "resposta": "A",
        "explicacao": 'Precedence: (2**3) + (5//2) - (1*3) = 8 + 2 - 3 = 7.'
    },
    {
        "pergunta": """What is the output?

    s = "abcde"
    print(s[::-1][1:4])""",
        "opcoes": ['bcd', 'edc', 'dcb', 'cba'],
        "resposta": "C",
        "explicacao": "s[::-1] = 'edcba'. [1:4] = 'dcb'."
    },
    {
        "pergunta": """What is the output?

    x = [1, 2, 3]
    y = x[:]
    y.append(4)
    print(x, y)""",
        "opcoes": ['[1, 2, 3, 4] [1, 2, 3, 4]', '[1, 2, 3] [1, 2, 3, 4]', '[1, 2, 3, 4] [1, 2, 3]', 'Error'],
        "resposta": "B",
        "explicacao": 'x[:] creates a COPY. Modifying y does not affect x.'
    },
    {
        "pergunta": """What is the output?

    def f(x, lst=[]):
        lst.append(x)
        return lst

    print(f(1))
    print(f(2))""",
        "opcoes": ['[1] then [2]', '[1, 2] then [1, 2]', 'Error', '[1] then [1, 2]'],
        "resposta": "D",
        "explicacao": 'Mutable default argument is shared between calls. The same list persists.'
    },
    {
        "pergunta": """What is the output?

    a = "hello"
    b = a.replace("l", "L", 1)
    print(b)""",
        "opcoes": ['heLLo', 'Hello', 'hELLO', 'heLlo'],
        "resposta": "D",
        "explicacao": "The third argument limits to 1 replacement. Only the first 'l' becomes 'L'."
    },
    {
        "pergunta": """What happens?

    x = 5
    print(x == 5 and x is 5)""",
        "opcoes": ['True (but behavior is implementation-dependent)', 'False', 'Syntax error', 'None'],
        "resposta": "A",
        "explicacao": "CPython caches small ints (-5 to 256), so 'is' returns True, but this is not guaranteed."
    },
    {
        "pergunta": """What is the output?

    d = {"a": 1, "b": 2}
    d["c"] = d.get("c", 0) + 1
    print(d)""",
        "opcoes": ["{'a': 1, 'b': 2, 'c': 0}", "{'a': 1, 'b': 2, 'c': 1}", 'KeyError', "{'a': 1, 'b': 2}"],
        "resposta": "B",
        "explicacao": "get('c', 0) returns 0 (default). 0 + 1 = 1. Creates key 'c' with value 1."
    },
    {
        "pergunta": """What is the output?

    x = [i ** 2 for i in range(5) if i % 2 != 0]
    print(x)""",
        "opcoes": ['[0, 4, 16]', '[1, 4, 9]', '[1, 9]', '[0, 1, 4, 9, 16]'],
        "resposta": "C",
        "explicacao": 'Odd numbers in range(5): 1, 3. Squares: 1, 9.'
    },
    {
        "pergunta": """What is the output?

    t = (1, 2, [3, 4])
    t[2].append(5)
    print(t)""",
        "opcoes": ['TypeError: tuple is immutable', '(1, 2, [3, 4], 5)', '(1, 2, [3, 4, 5])', '(1, 2, [5, 3, 4])'],
        "resposta": "C",
        "explicacao": 'The tuple is immutable, but the LIST inside it is mutable. We can modify the list contents.'
    },
    {
        "pergunta": """What is the output?

    def outer():
        x = 10
        def inner():
            nonlocal x
            x += 5
        inner()
        return x

    print(outer())""",
        "opcoes": ['10', '5', 'UnboundLocalError', '15'],
        "resposta": "D",
        "explicacao": 'nonlocal allows modifying x from the enclosing scope. 10 + 5 = 15.'
    },
    {
        "pergunta": """What is the output?

    print(list(zip([1, 2, 3], "ab")))""",
        "opcoes": ["[(1, 'a'), (2, 'b')]", "[(1, 'a'), (2, 'b'), (3, None)]", "[(1, 'a'), (2, 'b'), (3, '')]", 'Error'],
        "resposta": "A",
        "explicacao": 'zip stops at the shortest iterable. Result has only 2 elements.'
    },
    {
        "pergunta": """What is the output?

    x = 10
    def func():
        print(x)
    x = 20
    func()""",
        "opcoes": ['10', 'Error', '20', 'None'],
        "resposta": "C",
        "explicacao": 'func() looks up x at EXECUTION time (not definition time). x is already 20.'
    },
    {
        "pergunta": """What is the output?

    nums = [4, 2, 7, 1, 9]
    result = sorted(nums, reverse=True)[:3]
    print(result)""",
        "opcoes": ['[1, 2, 4]', '[4, 2, 7]', '[9, 7, 4, 2, 1]', '[9, 7, 4]'],
        "resposta": "D",
        "explicacao": 'sorted reverse → [9,7,4,2,1]. Slice [:3] → [9, 7, 4].'
    },
    {
        "pergunta": """What is the output?

    a = {1, 2, 3}
    b = {2, 3, 4}
    print(a & b, a - b)""",
        "opcoes": ['{2, 3} {1}', '{1, 4} {2, 3}', '{2, 3} {4}', 'Error'],
        "resposta": "A",
        "explicacao": '& is intersection: {2,3}. - is difference: elements in a not in b: {1}.'
    },
    {
        "pergunta": """What is the output?

    class A:
        count = 0
        def __init__(self):
            A.count += 1

    a = A()
    b = A()
    c = A()
    print(A.count, a.count)""",
        "opcoes": ['3 1', '1 1', '3 3', '3 0'],
        "resposta": "C",
        "explicacao": 'count is a class attribute, shared. Each __init__ increments it. a.count accesses via the class → 3.'
    },
    {
        "pergunta": """What is the output?

    try:
        x = int("abc")
    except ValueError:
        x = -1
    except TypeError:
        x = -2
    else:
        x = 0
    finally:
        x += 100

    print(x)""",
        "opcoes": ['100', '99', '98', '-1'],
        "resposta": "B",
        "explicacao": 'ValueError caught → x=-1. else does NOT execute. finally always runs → x = -1 + 100 = 99.'
    },
    {
        "pergunta": """What is the output?

    m = [[0]*3 for _ in range(3)]
    m[0][1] = 5
    print(m[1][1])""",
        "opcoes": ['0', 'None', '5', 'Error'],
        "resposta": "A",
        "explicacao": 'List comprehension creates independent lists. m[0] and m[1] are different objects.'
    },
    {
        "pergunta": """What is the output?

    m = [[0]*3] * 3
    m[0][1] = 5
    print(m[1][1])""",
        "opcoes": ['0', '5', 'None', 'Error'],
        "resposta": "B",
        "explicacao": 'Multiplying a list creates REFERENCES. m[0], m[1], m[2] are the SAME list. Changing one changes all.'
    },
    {
        "pergunta": """What is the output?

    gen = (x for x in range(5))
    next(gen)
    next(gen)
    print(list(gen))""",
        "opcoes": ['[0, 1, 2, 3, 4]', '[2, 3, 4]', 'Error', '[3, 4]'],
        "resposta": "B",
        "explicacao": 'next() consumes 0 and 1. list() consumes the rest: [2, 3, 4].'
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 4", "20 Questions - Intermediate/Hard")
