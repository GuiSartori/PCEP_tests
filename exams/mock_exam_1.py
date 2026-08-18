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
        "pergunta": """Qual é o resultado do seguinte código?

    x = 1
    y = 2
    x, y = y, x
    print(x, y)""",
        "opcoes": ['2 1', '1 2', '1 1', '2 2'],
        "resposta": "A",
        "explicacao": 'Swap com tuple unpacking: x recebe y (2), y recebe x (1).'
    },
    {
        "pergunta": """O que o operador // faz em Python?""",
        "opcoes": ['Divisão com resultado float', 'Divisão inteira (floor division)', 'Exponenciação', 'Resto da divisão'],
        "resposta": "B",
        "explicacao": '// faz divisão inteira, arredondando para baixo.'
    },
    {
        "pergunta": """Qual é o resultado?

    print(2 ** 3 ** 2)""",
        "opcoes": ['64', '36', '512', '81'],
        "resposta": "C",
        "explicacao": '** é associativo à direita: 2 ** (3**2) = 2**9 = 512.'
    },
    {
        "pergunta": """Qual é o tipo retornado por type(3.0)?""",
        "opcoes": ["<class 'int'>", "<class 'str'>", "<class 'double'>", "<class 'float'>"],
        "resposta": "D",
        "explicacao": '3.0 tem ponto decimal, portanto é float.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = "Python"
    print(x[1:4])""",
        "opcoes": ['Pyt', 'yth', 'ytho', 'Pyth'],
        "resposta": "B",
        "explicacao": "Slice [1:4] pega índices 1, 2, 3 → 'y', 't', 'h'."
    },
    {
        "pergunta": """Qual alternativa NÃO é um nome de variável válido?""",
        "opcoes": ['_valor', 'valor2', '2valor', 'valor_total'],
        "resposta": "C",
        "explicacao": 'Variáveis não podem começar com número.'
    },
    {
        "pergunta": """Qual é o resultado?

    lista = [1, 2, 3, 4, 5]
    print(lista[-2])""",
        "opcoes": ['5', '3', '2', '4'],
        "resposta": "D",
        "explicacao": 'Índice -2 é o penúltimo elemento → 4.'
    },
    {
        "pergunta": """Qual é o resultado?

    print(bool(0), bool(""), bool([]))""",
        "opcoes": ['False False False', 'True True True', 'False True False', 'True False True'],
        "resposta": "A",
        "explicacao": '0, string vazia e lista vazia são todos falsy → False.'
    },
    {
        "pergunta": """O que é impresso?

    i = 0
    while i < 5:
        i += 1
        if i == 3:
            continue
        print(i, end=" ")""",
        "opcoes": ['1 2 3 4 5', '1 2 4', '0 1 2 4 5', '1 2 4 5'],
        "resposta": "D",
        "explicacao": 'continue pula o print quando i==3. Imprime 1 2 4 5.'
    },
    {
        "pergunta": """Qual é o resultado?

    def func(a, b=2):
        return a * b

    print(func(3))""",
        "opcoes": ['6', 'Erro: argumento faltando', '32', '5'],
        "resposta": "A",
        "explicacao": 'b tem valor padrão 2, então func(3) = 3 * 2 = 6.'
    },
    {
        "pergunta": """Qual é o resultado?

    nums = [1, 2, 3]
    nums.append([4, 5])
    print(len(nums))""",
        "opcoes": ['5', '3', '4', 'Erro'],
        "resposta": "C",
        "explicacao": 'append adiciona [4,5] como UM elemento. len = 4.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = 10
    y = 3
    print(x % y)""",
        "opcoes": ['3', '3.33', '0', '1'],
        "resposta": "D",
        "explicacao": '10 % 3 = 1 (resto da divisão).'
    },
    {
        "pergunta": """Qual método remove E retorna o último elemento de uma lista?""",
        "opcoes": ['list.remove()', 'list.pop()', 'list.del()', 'list.discard()'],
        "resposta": "B",
        "explicacao": 'pop() remove e retorna o último (ou o índice especificado).'
    },
    {
        "pergunta": """Qual é o resultado?

    text = "hello"
    print(text.upper().count("L"))""",
        "opcoes": ['0', '1', '2', 'Erro'],
        "resposta": "C",
        "explicacao": "'HELLO'.count('L') → encontra 2 ocorrências de 'L'."
    },
    {
        "pergunta": """Qual é o resultado?

    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)""",
        "opcoes": ['[1, 2, 3]', '[4, 1, 2, 3]', '[1, 2, 3, 4]', 'Erro'],
        "resposta": "C",
        "explicacao": 'b = a cria referência (não cópia). Ambos apontam para a mesma lista.'
    },
    {
        "pergunta": """Qual é o resultado?

    for i in range(2, 10, 3):
        print(i, end=" ")""",
        "opcoes": ['2 4 6 8', '3 6 9', '2 5 8 11', '2 5 8'],
        "resposta": "D",
        "explicacao": 'range(2, 10, 3) → começa em 2, passo 3, para antes de 10: 2, 5, 8.'
    },
    {
        "pergunta": """O que é impresso?

    dicionario = {"a": 1, "b": 2, "c": 3}
    print("b" in dicionario)""",
        "opcoes": ['True', 'False', '2', 'Erro'],
        "resposta": "A",
        "explicacao": "'in' verifica as CHAVES do dicionário. 'b' é uma chave."
    },
    {
        "pergunta": """Qual é o resultado?

    def func(lst):
        lst = [10, 20, 30]

    minha_lista = [1, 2, 3]
    func(minha_lista)
    print(minha_lista)""",
        "opcoes": ['[10, 20, 30]', '[1, 2, 3]', '[]', 'Erro'],
        "resposta": "B",
        "explicacao": 'Reatribuir lst dentro da função cria variável local. Não afeta a original.'
    },
    {
        "pergunta": """Qual é o resultado?

    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("erro")
    else:
        print("ok")
    finally:
        print("fim")""",
        "opcoes": ['erro fim', 'ok fim', 'erro ok fim', 'Apenas erro'],
        "resposta": "A",
        "explicacao": 'Exceção capturada → else NÃO executa. finally SEMPRE executa.'
    },
    {
        "pergunta": """Qual é o resultado?

    x = "abc"
    y = x * 2
    z = x + "2"
    print(y, z)""",
        "opcoes": ['abc2 abcabc', 'abcabc abc2', 'Erro', '6 abc2'],
        "resposta": "B",
        "explicacao": "'abc' * 2 = 'abcabc'. 'abc' + '2' = 'abc2'."
    },
]


if __name__ == "__main__":
    run_exam(questoes, "PCEP MOCK EXAM 1", "20 Questions - Fundamentals")
