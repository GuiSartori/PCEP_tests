# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   PCEP MOCK EXAM 5 — Hard Difficulty (Edge Cases)           ║
║   20 Multiple Choice Questions · Tricky behaviors           ║
║   Balanced answers: A=5, B=5, C=5, D=5                     ║
╚══════════════════════════════════════════════════════════════╝
"""

from exam_engine import run_exam

questoes = [
    {
        "pergunta": """What is the output?

    x = [1, 2, 3]
    y = x
    x += [4, 5]
    print(y)""",
        "opcoes": ['[1, 2, 3]', 'Error', '[4, 5, 1, 2, 3]', '[1, 2, 3, 4, 5]'],
        "resposta": "D",
        "explicacao": '+= on a list calls extend() IN PLACE (mutates the same object). y still references the same list, so y shows [1,2,3,4,5].'
    },
    {
        "pergunta": """What is the output?

    x = (1, 2, 3)
    y = x
    x += (4, 5)
    print(y)""",
        "opcoes": ['(1, 2, 3)', '(1, 2, 3, 4, 5)', 'Error: tuples are immutable', '(4, 5)'],
        "resposta": "A",
        "explicacao": '+= on a tuple creates a NEW tuple and rebinds x. y still points to the original (1,2,3). Tuples are immutable — no in-place modification.'
    },
    {
        "pergunta": """What is the output?

    def f(x=[]):
        x.append(len(x))
        return x

    f()
    f()
    print(f())""",
        "opcoes": ['[2]', '[0]', '[0, 1, 2]', 'Error'],
        "resposta": "C",
        "explicacao": 'Mutable default persists. 1st call appends 0→[0], 2nd appends 1→[0,1], 3rd appends 2→[0,1,2].'
    },
    {
        "pergunta": """What is the output?

    print(0.1 + 0.2 == 0.3)""",
        "opcoes": ['True', '0.30000000000000004', 'Error', 'False'],
        "resposta": "D",
        "explicacao": 'Floating-point: 0.1+0.2 = 0.30000000000000004, NOT equal to 0.3. Classic IEEE 754 precision issue.'
    },
    {
        "pergunta": """What is the output?

    nums = [1, 2, 3, 4, 5]
    nums[1:4] = [20, 30]
    print(nums)""",
        "opcoes": ['[1, 20, 30, 4, 5]', '[1, 20, 30, 5]', '[1, 20, 30, 3, 4, 5]', 'Error: size mismatch'],
        "resposta": "B",
        "explicacao": 'Slice assignment replaces indices 1,2,3 (three elements) with [20,30] (two elements). The list shrinks: [1, 20, 30, 5].'
    },
    {
        "pergunta": """What is the output?

    x = 10
    def outer():
        x = 20
        def inner():
            print(x)
        return inner

    fn = outer()
    x = 30
    fn()""",
        "opcoes": ['10', '30', '20', 'Error'],
        "resposta": "C",
        "explicacao": "inner() is a closure capturing x from outer()'s scope (x=20). The global x=30 doesn't affect the enclosed variable."
    },
    {
        "pergunta": """What is the output?

    d = {"a": 1, "b": 2, "c": 3}
    keys = list(d.keys())
    for k in keys:
        if d[k] % 2 != 0:
            del d[k]
    print(d)""",
        "opcoes": ["{'a': 1, 'c': 3}", 'Error: dictionary changed size during iteration', '{}', "{'b': 2}"],
        "resposta": "D",
        "explicacao": "We iterate over a COPY of keys (list(d.keys())), so deleting from d is safe. Removes odd values: only 'b':2 remains."
    },
    {
        "pergunta": """What is the output?

    result = []
    for i in range(4):
        result.append(lambda: i)
    print([f() for f in result])""",
        "opcoes": ['[0, 1, 2, 3]', '[3, 3, 3, 3]', '[4, 4, 4, 4]', 'Error'],
        "resposta": "B",
        "explicacao": "Late binding: lambdas capture the variable 'i', not its value at creation time. When called, i=3 (final loop value). All return 3."
    },
    {
        "pergunta": """What is the output?

    print(bool(""), bool(" "), bool("0"), bool([]))""",
        "opcoes": ['False True True False', 'False False False False', 'False True False False', 'False False True False'],
        "resposta": "A",
        "explicacao": "'' empty→False. ' ' non-empty→True. '0' non-empty string→True. [] empty→False."
    },
    {
        "pergunta": """What is the output?

    try:
        try:
            1 / 0
        except ZeroDivisionError:
            print("inner", end=" ")
            raise ValueError("oops")
    except ValueError:
        print("outer", end=" ")
    finally:
        print("done")""",
        "opcoes": ['inner done', 'outer done', 'inner outer', 'inner outer done'],
        "resposta": "D",
        "explicacao": "Inner catches ZeroDivisionError→'inner'. Raises ValueError→outer catches→'outer'. finally always runs→'done'."
    },
    {
        "pergunta": """What is the output?

    x = "python"
    print(x[100:200])""",
        "opcoes": ['IndexError', 'python', 'None', "'' (empty string)"],
        "resposta": "D",
        "explicacao": 'Slicing NEVER raises IndexError — out-of-range slices return empty sequence. x[100] (indexing) WOULD raise IndexError.'
    },
    {
        "pergunta": """What is the output?

    def f(a, b, /, c, *, d):
        return a + b + c + d

    print(f(1, 2, c=3, d=4))""",
        "opcoes": ['Error: invalid syntax', 'Error: positional-only after /', '10', 'Error: keyword-only before *'],
        "resposta": "C",
        "explicacao": '/ means a,b are positional-only. * means d is keyword-only. c can be either. f(1, 2, c=3, d=4) = 1+2+3+4 = 10.'
    },
    {
        "pergunta": """What is the output?

    nums = [5, 3, 8, 1, 9]
    result = nums.sort()
    print(result)""",
        "opcoes": ['[1, 3, 5, 8, 9]', 'Error', 'None', '(1, 3, 5, 8, 9)'],
        "resposta": "C",
        "explicacao": 'list.sort() sorts IN PLACE and returns None. Use sorted(nums) to get a new sorted list.'
    },
    {
        "pergunta": """What happens when you run this?

    d = {}
    d[(1, 2)] = "ok"
    d[[1, 2]] = "fail" """,
        "opcoes": ["TypeError: unhashable type: 'list'", 'd has two entries', 'The list key overwrites the tuple key', 'KeyError'],
        "resposta": "A",
        "explicacao": 'Tuples are hashable (valid dict keys). Lists are NOT hashable → TypeError on the second assignment.'
    },
    {
        "pergunta": """What is the output?

    x = [1, 2, 3]
    y = x
    x = x + [4, 5]
    print(y)""",
        "opcoes": ['[1, 2, 3, 4, 5]', '[1, 2, 3]', '[4, 5]', 'Error'],
        "resposta": "B",
        "explicacao": 'x = x + [...] creates a NEW list and rebinds x. Unlike +=, it does NOT mutate the original. y still points to [1,2,3].'
    },
    {
        "pergunta": """What is the output?

    print("ab" < "abc" < "b")""",
        "opcoes": ['False', 'True', 'Error: cannot chain on strings', 'True False'],
        "resposta": "B",
        "explicacao": "Lexicographic: 'ab'<'abc' (prefix is smaller) and 'abc'<'b' (first char 'a'<'b'). Both True → chained result is True."
    },
    {
        "pergunta": """What is the output?

    def gen():
        yield 10
        yield 20
        yield 30

    g = gen()
    next(g)
    next(g)
    print(next(g))""",
        "opcoes": ['10', '20', '30', 'StopIteration'],
        "resposta": "C",
        "explicacao": 'First next→10 (consumed), second next→20 (consumed), third next→30 (printed).'
    },
    {
        "pergunta": """What is the output?

    x = {"a": 1, "b": 2}
    y = {"b": 3, "c": 4}
    z = {**x, **y}
    print(z["b"], len(z))""",
        "opcoes": ['2 4', '3 3', '2 3', 'Error'],
        "resposta": "B",
        "explicacao": "Dict unpacking merges. Duplicate key 'b' — last one wins (y's value: 3). Total keys: a,b,c → len=3."
    },
    {
        "pergunta": """What is the result of: type("abc" * 0) and len("abc" * 0)?""",
        "opcoes": ["<class 'str'> and 0", "<class 'NoneType'> and 0", 'Error: cannot multiply by 0', "<class 'str'> and 3"],
        "resposta": "A",
        "explicacao": "'abc' * 0 = '' (empty string). It's still a str (type is <class 'str'>) with length 0."
    },
    {
        "pergunta": """What is the output?

    a, b = 1, 2
    a, b = b, a + b
    print(a, b)""",
        "opcoes": ['2 3', '2 4', '1 3', '3 2'],
        "resposta": "A",
        "explicacao": 'RHS evaluated first with original values: b=2, a+b=1+2=3. Then assigned: a=2, b=3. Output: 2 3.'
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 5", "20 Questions - Hard (Edge Cases)")
