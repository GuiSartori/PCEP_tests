# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   PCEP MOCK EXAM 1 — Easy (Fundamentals)                    ║
║   20 Multiple Choice Questions · Core syntax & basics       ║
║   Balanced answers: A=5, B=5, C=5, D=5                     ║
╚══════════════════════════════════════════════════════════════╝
"""

from exam_engine import run_exam

questoes = [
    {
        "pergunta": """What is the output of the following code?

    x = 1
    y = 2
    x, y = y, x
    print(x, y)""",
        "opcoes": ['2 1', '1 2', '1 1', '2 2'],
        "resposta": "A",
        "explicacao": 'Swap with tuple unpacking: x receives y (2), y receives x (1).'
    },
    {
        "pergunta": """What does the // operator do in Python?""",
        "opcoes": ['Division with float result', 'Integer division (floor division)', 'Exponentiation', 'Modulo (remainder)'],
        "resposta": "B",
        "explicacao": '// performs integer division, rounding down.'
    },
    {
        "pergunta": """What is the output?

    print(2 ** 3 ** 2)""",
        "opcoes": ['64', '36', '512', '81'],
        "resposta": "C",
        "explicacao": '** is right-associative: 2 ** (3**2) = 2**9 = 512.'
    },
    {
        "pergunta": """What is the type returned by type(3.0)?""",
        "opcoes": ["<class 'int'>", "<class 'str'>", "<class 'double'>", "<class 'float'>"],
        "resposta": "D",
        "explicacao": '3.0 has a decimal point, so it is a float.'
    },
    {
        "pergunta": """What is the output?

    x = "Python"
    print(x[1:4])""",
        "opcoes": ['Pyt', 'yth', 'ytho', 'Pyth'],
        "resposta": "B",
        "explicacao": "Slice [1:4] takes indices 1, 2, 3 → 'y', 't', 'h'."
    },
    {
        "pergunta": """Which option is NOT a valid variable name?""",
        "opcoes": ['_valor', 'valor2', '2valor', 'valor_total'],
        "resposta": "C",
        "explicacao": 'Variables cannot start with a number.'
    },
    {
        "pergunta": """What is the output?

    lista = [1, 2, 3, 4, 5]
    print(lista[-2])""",
        "opcoes": ['5', '3', '2', '4'],
        "resposta": "D",
        "explicacao": 'Index -2 is the second-to-last element → 4.'
    },
    {
        "pergunta": """What is the output?

    print(bool(0), bool(""), bool([]))""",
        "opcoes": ['False False False', 'True True True', 'False True False', 'True False True'],
        "resposta": "A",
        "explicacao": '0, empty string, and empty list are all falsy → False.'
    },
    {
        "pergunta": """What is printed?

    i = 0
    while i < 5:
        i += 1
        if i == 3:
            continue
        print(i, end=" ")""",
        "opcoes": ['1 2 3 4 5', '1 2 4', '0 1 2 4 5', '1 2 4 5'],
        "resposta": "D",
        "explicacao": 'continue skips the print when i==3. Prints 1 2 4 5.'
    },
    {
        "pergunta": """What is the output?

    def func(a, b=2):
        return a * b

    print(func(3))""",
        "opcoes": ['6', 'Error: missing argument', '32', '5'],
        "resposta": "A",
        "explicacao": 'b has default value 2, so func(3) = 3 * 2 = 6.'
    },
    {
        "pergunta": """What is the output?

    nums = [1, 2, 3]
    nums.append([4, 5])
    print(len(nums))""",
        "opcoes": ['5', '3', '4', 'Error'],
        "resposta": "C",
        "explicacao": 'append adds [4,5] as ONE element. len = 4.'
    },
    {
        "pergunta": """What is the output?

    x = 10
    y = 3
    print(x % y)""",
        "opcoes": ['3', '3.33', '0', '1'],
        "resposta": "D",
        "explicacao": '10 % 3 = 1 (remainder of the division).'
    },
    {
        "pergunta": """Which method removes AND returns the last element of a list?""",
        "opcoes": ['list.remove()', 'list.pop()', 'list.del()', 'list.discard()'],
        "resposta": "B",
        "explicacao": 'pop() removes and returns the last element (or the specified index).'
    },
    {
        "pergunta": """What is the output?

    text = "hello"
    print(text.upper().count("L"))""",
        "opcoes": ['0', '1', '2', 'Error'],
        "resposta": "C",
        "explicacao": "'HELLO'.count('L') → finds 2 occurrences of 'L'."
    },
    {
        "pergunta": """What is the output?

    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)""",
        "opcoes": ['[1, 2, 3]', '[4, 1, 2, 3]', '[1, 2, 3, 4]', 'Error'],
        "resposta": "C",
        "explicacao": 'b = a creates a reference (not a copy). Both point to the same list.'
    },
    {
        "pergunta": """What is the output?

    for i in range(2, 10, 3):
        print(i, end=" ")""",
        "opcoes": ['2 4 6 8', '3 6 9', '2 5 8 11', '2 5 8'],
        "resposta": "D",
        "explicacao": 'range(2, 10, 3) → starts at 2, step 3, stops before 10: 2, 5, 8.'
    },
    {
        "pergunta": """What is printed?

    dicionario = {"a": 1, "b": 2, "c": 3}
    print("b" in dicionario)""",
        "opcoes": ['True', 'False', '2', 'Error'],
        "resposta": "A",
        "explicacao": "'in' checks the KEYS of the dictionary. 'b' is a key."
    },
    {
        "pergunta": """What is the output?

    def func(lst):
        lst = [10, 20, 30]

    minha_lista = [1, 2, 3]
    func(minha_lista)
    print(minha_lista)""",
        "opcoes": ['[10, 20, 30]', '[1, 2, 3]', '[]', 'Error'],
        "resposta": "B",
        "explicacao": 'Reassigning lst inside the function creates a local variable. It does not affect the original.'
    },
    {
        "pergunta": """What is the output?

    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("error")
    else:
        print("ok")
    finally:
        print("end")""",
        "opcoes": ['error end', 'ok end', 'error ok end', 'Only error'],
        "resposta": "A",
        "explicacao": 'Exception caught → else does NOT execute. finally ALWAYS executes.'
    },
    {
        "pergunta": """What is the output?

    x = "abc"
    y = x * 2
    z = x + "2"
    print(y, z)""",
        "opcoes": ['abc2 abcabc', 'abcabc abc2', 'Error', '6 abc2'],
        "resposta": "B",
        "explicacao": "'abc' * 2 = 'abcabc'. 'abc' + '2' = 'abc2'."
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 1", "20 Questions - Fundamentals")
