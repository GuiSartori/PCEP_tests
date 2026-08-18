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
        "pergunta": """Qual é o resultado?

    x = "Python"
    print(x[-3:])""",
        "opcoes": ['Pyt', 'tho', 'on', 'hon'],
        "resposta": "D",
        "explicacao": "x[-3:] pega os últimos 3 caracteres: 'h', 'o', 'n' → 'hon'."
    },
    {
        "pergunta": """Qual é o resultado?

    print(isinstance(True, int))""",
        "opcoes": ['False', 'TypeError', 'True', 'None'],
        "resposta": "C",
        "explicacao": 'bool é subclasse de int em Python. isinstance(True, int) retorna True.'
    },
    {
        "pergunta": """Qual é o resultado?

    a = [1, 2, 3, 4, 5]
    b = a[1:4]
    b[0] = 99
    print(a[1])""",
        "opcoes": ['99', '2', '1', 'Erro'],
        "resposta": "B",
        "explicacao": 'Slicing cria uma nova lista. Modificar b não altera a. a[1] continua sendo 2.'
    },
    {
        "pergunta": """Qual é o resultado?

    d = {}
    d[1] = "a"
    d["1"] = "b"
    d[1.0] = "c"
    print(len(d))""",
        "opcoes": ['1', '2', '3', 'Erro'],
        "resposta": "B",
        "explicacao": "Em Python, 1 == 1.0 e hash(1) == hash(1.0), então d[1.0] sobrescreve d[1]. Chaves: 1 e '1' → len = 2."
    },
    {
        "pergunta": """Qual é o resultado?

    def f(a, b, c=3, d=4):
        return a + b + c + d

    print(f(1, 2, d=10))""",
        "opcoes": ['16', '20', '10', 'Erro'],
        "resposta": "A",
        "explicacao": 'a=1, b=2, c=3 (padrão), d=10. Soma: 1+2+3+10 = 16.'
    },
    {
        "pergunta": """O que é impresso?

    for i in range(5):
        if i == 3:
            break
    else:
        print("else")
    print(i)""",
        "opcoes": ['else\\n3', 'else\\n4', '4', '3'],
        "resposta": "D",
        "explicacao": 'break interrompe o loop E impede o else de executar. Depois imprime i=3.'
    },
    {
        "pergunta": """Qual é o resultado?

    s = "hello world"
    print(s.split())""",
        "opcoes": ["['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']", "['hello', 'world']", "['hello world']", "('hello', 'world')"],
        "resposta": "B",
        "explicacao": "split() sem argumento separa por espaço: ['hello', 'world']."
    },
    {
        "pergunta": """Qual é o resultado?

    x = lambda a, b: a if a > b else b
    print(x(5, 8))""",
        "opcoes": ['5', 'True', 'Erro', '8'],
        "resposta": "D",
        "explicacao": 'A lambda retorna o maior valor. 8 > 5, então retorna 8.'
    },
    {
        "pergunta": """Qual é o resultado?

    nums = [1, 2, 3, 4, 5]
    print(nums[::2])""",
        "opcoes": ['[1, 3, 5]', '[2, 4]', '[1, 2]', '[5, 3, 1]'],
        "resposta": "A",
        "explicacao": '[::2] pega elementos com passo 2, começando do índice 0: 1, 3, 5.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = 5
    def f():
        global x
        x = 10
    f()
    print(x)""",
        "opcoes": ['5', 'Erro', '10', 'None'],
        "resposta": "C",
        "explicacao": 'global permite modificar a variável do escopo global. x passa a valer 10.'
    },
    {
        "pergunta": """Qual é o resultado?

    print("abc" * 0)""",
        "opcoes": ['abc', '0', 'Erro', "''  (string vazia)"],
        "resposta": "D",
        "explicacao": "Multiplicar string por 0 resulta em string vazia ''."
    },
    {
        "pergunta": """Qual é o resultado?

    lst = [3, 1, 4, 1, 5]
    lst.sort()
    lst.reverse()
    print(lst[0])""",
        "opcoes": ['5', '1', '3', '4'],
        "resposta": "A",
        "explicacao": 'sort() → [1,1,3,4,5]. reverse() → [5,4,3,1,1]. lst[0] = 5.'
    },
    {
        "pergunta": """O que acontece ao executar?

    t = (1, 2, 3)
    t[0] = 10""",
        "opcoes": ['t se torna (10, 2, 3)', 'TypeError: tuplas são imutáveis', 't se torna [10, 2, 3]', 'IndexError'],
        "resposta": "B",
        "explicacao": 'Tuplas são imutáveis. Tentar atribuir a um índice gera TypeError.'
    },
    {
        "pergunta": """Qual é o resultado?

    d = {"x": 1, "y": 2, "z": 3}
    print(list(d.values()))""",
        "opcoes": ["['x', 'y', 'z']", "[('x',1), ('y',2), ('z',3)]", '[1, 2, 3]', 'Erro'],
        "resposta": "C",
        "explicacao": 'd.values() retorna os valores do dicionário: 1, 2, 3.'
    },
    {
        "pergunta": """Qual é o resultado?

    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("erro")
    else:
        print("ok")
    finally:
        print("fim")""",
        "opcoes": ['erro fim', 'fim', 'ok fim', 'ok'],
        "resposta": "C",
        "explicacao": "Sem exceção → else executa ('ok'). finally sempre executa ('fim')."
    },
    {
        "pergunta": """Qual é o resultado?

    x = [1, 2, 3]
    y = [4, 5, 6]
    z = x + y
    print(z[-1], len(z))""",
        "opcoes": ['3 6', '6 3', '6 6', 'Erro'],
        "resposta": "C",
        "explicacao": 'x + y = [1,2,3,4,5,6]. z[-1]=6, len(z)=6.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = "abcdef"
    print(x[1::2])""",
        "opcoes": ['ace', 'abcdef', 'bce', 'bdf'],
        "resposta": "D",
        "explicacao": "[1::2] começa no índice 1 com passo 2: 'b','d','f' → 'bdf'."
    },
    {
        "pergunta": """Qual é o resultado?

    def f(n):
        if n <= 1:
            return n
        return f(n-1) + f(n-2)

    print(f(6))""",
        "opcoes": ['5', '8', '13', '21'],
        "resposta": "B",
        "explicacao": 'Fibonacci recursivo: f(6) = f(5)+f(4) = 5+3 = 8.'
    },
    {
        "pergunta": """Qual é o resultado?

    a = {"a": 1, "b": 2}
    b = {"b": 3, "c": 4}
    a.update(b)
    print(a)""",
        "opcoes": ["{'a': 1, 'b': 3, 'c': 4}", "{'b': 3, 'c': 4}", "{'a': 1, 'b': 2, 'c': 4}", 'Erro'],
        "resposta": "A",
        "explicacao": "update() mescla dicionários. Chaves existentes são sobrescritas: 'b' vira 3."
    },
    {
        "pergunta": """Qual é o resultado?

    items = ["a", "b", "c"]
    result = list(enumerate(items, start=1))
    print(result[1])""",
        "opcoes": ["(2, 'b')", "(1, 'a')", "(0, 'b')", "(1, 'b')"],
        "resposta": "A",
        "explicacao": "enumerate com start=1 → [(1,'a'),(2,'b'),(3,'c')]. Índice [1] → (2, 'b')."
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 3", "20 Questions - Balanced Review")
