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
        "pergunta": """Qual é o resultado?

    x = 1
    y = 2
    z = x
    x = y
    y = z
    print(x, y, z)""",
        "opcoes": ['1 2 1', '2 1 2', '1 1 2', '2 1 1'],
        "resposta": "D",
        "explicacao": 'z=1, x=2, y=z=1. Swap manual: x=2, y=1, z=1.'
    },
    {
        "pergunta": """Qual é o resultado?

    print(2 ** 3 + 5 // 2 - 1 * 3)""",
        "opcoes": ['7', '8', '9', '10'],
        "resposta": "A",
        "explicacao": 'Precedência: (2**3) + (5//2) - (1*3) = 8 + 2 - 3 = 7.'
    },
    {
        "pergunta": """Qual é o resultado?

    s = "abcde"
    print(s[::-1][1:4])""",
        "opcoes": ['bcd', 'edc', 'dcb', 'cba'],
        "resposta": "C",
        "explicacao": "s[::-1] = 'edcba'. [1:4] = 'dcb'."
    },
    {
        "pergunta": """Qual é o resultado?

    x = [1, 2, 3]
    y = x[:]
    y.append(4)
    print(x, y)""",
        "opcoes": ['[1, 2, 3, 4] [1, 2, 3, 4]', '[1, 2, 3] [1, 2, 3, 4]', '[1, 2, 3, 4] [1, 2, 3]', 'Erro'],
        "resposta": "B",
        "explicacao": 'x[:] cria uma CÓPIA. Modificar y não afeta x.'
    },
    {
        "pergunta": """Qual é o resultado?

    def f(x, lst=[]):
        lst.append(x)
        return lst

    print(f(1))
    print(f(2))""",
        "opcoes": ['[1]\\n[2]', '[1, 2]\\n[1, 2]', 'Erro', '[1]\\n[1, 2]'],
        "resposta": "D",
        "explicacao": 'Argumento padrão mutável é compartilhado entre chamadas. A mesma lista persiste.'
    },
    {
        "pergunta": """Qual é o resultado?

    a = "hello"
    b = a.replace("l", "L", 1)
    print(b)""",
        "opcoes": ['heLLo', 'Hello', 'hELLO', 'heLlo'],
        "resposta": "D",
        "explicacao": "O terceiro argumento limita a 1 substituição. Só o primeiro 'l' vira 'L'."
    },
    {
        "pergunta": """O que acontece?

    x = 5
    print(x == 5 and x is 5)""",
        "opcoes": ['True (mas comportamento depende da implementação)', 'False', 'Erro de sintaxe', 'None'],
        "resposta": "A",
        "explicacao": "CPython faz cache de ints pequenos (-5 a 256), então 'is' retorna True, mas não é garantido."
    },
    {
        "pergunta": """Qual é o resultado?

    d = {"a": 1, "b": 2}
    d["c"] = d.get("c", 0) + 1
    print(d)""",
        "opcoes": ["{'a': 1, 'b': 2, 'c': 0}", "{'a': 1, 'b': 2, 'c': 1}", 'KeyError', "{'a': 1, 'b': 2}"],
        "resposta": "B",
        "explicacao": "get('c', 0) retorna 0 (padrão). 0 + 1 = 1. Cria chave 'c' com valor 1."
    },
    {
        "pergunta": """Qual é o resultado?

    x = [i ** 2 for i in range(5) if i % 2 != 0]
    print(x)""",
        "opcoes": ['[0, 4, 16]', '[1, 4, 9]', '[1, 9]', '[0, 1, 4, 9, 16]'],
        "resposta": "C",
        "explicacao": 'range(5) ímpares: 1, 3. Quadrados: 1, 9.'
    },
    {
        "pergunta": """Qual é o resultado?

    t = (1, 2, [3, 4])
    t[2].append(5)
    print(t)""",
        "opcoes": ['TypeError: tupla é imutável', '(1, 2, [3, 4], 5)', '(1, 2, [3, 4, 5])', '(1, 2, [5, 3, 4])'],
        "resposta": "C",
        "explicacao": 'A tupla é imutável, mas a LISTA dentro dela é mutável. Podemos alterar o conteúdo da lista.'
    },
    {
        "pergunta": """Qual é o resultado?

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
        "explicacao": 'nonlocal permite modificar x do escopo externo. 10 + 5 = 15.'
    },
    {
        "pergunta": """Qual é o resultado?

    print(list(zip([1, 2, 3], "ab")))""",
        "opcoes": ["[(1, 'a'), (2, 'b')]", "[(1, 'a'), (2, 'b'), (3, None)]", "[(1, 'a'), (2, 'b'), (3, '')]", 'Erro'],
        "resposta": "A",
        "explicacao": 'zip para no menor iterável. Resultado tem apenas 2 elementos.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = 10
    def func():
        print(x)
    x = 20
    func()""",
        "opcoes": ['10', 'Erro', '20', 'None'],
        "resposta": "C",
        "explicacao": 'func() busca x no momento da EXECUÇÃO (não da definição). x já vale 20.'
    },
    {
        "pergunta": """Qual é o resultado?

    nums = [4, 2, 7, 1, 9]
    result = sorted(nums, reverse=True)[:3]
    print(result)""",
        "opcoes": ['[1, 2, 4]', '[4, 2, 7]', '[9, 7, 4, 2, 1]', '[9, 7, 4]'],
        "resposta": "D",
        "explicacao": 'sorted reverse → [9,7,4,2,1]. Slice [:3] → [9, 7, 4].'
    },
    {
        "pergunta": """Qual é o resultado?

    a = {1, 2, 3}
    b = {2, 3, 4}
    print(a & b, a - b)""",
        "opcoes": ['{2, 3} {1}', '{1, 4} {2, 3}', '{2, 3} {4}', 'Erro'],
        "resposta": "A",
        "explicacao": '& é interseção: {2,3}. - é diferença: elementos em a que não estão em b: {1}.'
    },
    {
        "pergunta": """Qual é o resultado?

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
        "explicacao": 'count é atributo de classe, compartilhado. Cada __init__ incrementa. a.count acessa via classe → 3.'
    },
    {
        "pergunta": """Qual é o resultado?

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
        "explicacao": 'ValueError capturado → x=-1. else NÃO executa. finally sempre → x = -1 + 100 = 99.'
    },
    {
        "pergunta": """Qual é o resultado?

    m = [[0]*3 for _ in range(3)]
    m[0][1] = 5
    print(m[1][1])""",
        "opcoes": ['0', 'None', '5', 'Erro'],
        "resposta": "A",
        "explicacao": 'List comprehension cria listas independentes. m[0] e m[1] são objetos diferentes.'
    },
    {
        "pergunta": """Qual é o resultado?

    m = [[0]*3] * 3
    m[0][1] = 5
    print(m[1][1])""",
        "opcoes": ['0', '5', 'None', 'Erro'],
        "resposta": "B",
        "explicacao": 'Multiplicar lista cria REFERÊNCIAS. m[0], m[1], m[2] são a MESMA lista. Mudar uma muda todas.'
    },
    {
        "pergunta": """Qual é o resultado?

    gen = (x for x in range(5))
    next(gen)
    next(gen)
    print(list(gen))""",
        "opcoes": ['[0, 1, 2, 3, 4]', '[2, 3, 4]', 'Erro', '[3, 4]'],
        "resposta": "B",
        "explicacao": 'next() consome 0 e 1. list() consome o restante: [2, 3, 4].'
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 4", "20 Questions - Intermediate/Hard")
