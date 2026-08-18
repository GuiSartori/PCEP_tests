# 📝 CORREÇÃO DETALHADA - SIMULADO PCEP 1

## ✅ Gabarito e Explicações

---

### **Questão 1**

**Pergunta:**
```python
x = 1
y = 2
x, y = y, x
print(x, y)
```

**Opções:**
- A. `2 1`
- B. `1 2`
- C. `1 1`
- D. `2 2`

**✅ Resposta Correta: A**

**📚 Explicação:**
Esta é uma técnica chamada **tuple unpacking** (desempacotamento de tupla) ou **swap simultâneo**. 

Em Python, a expressão `x, y = y, x` funciona assim:
1. O lado direito `y, x` cria uma tupla temporária `(2, 1)`
2. O lado esquerdo `x, y` desempacota essa tupla
3. `x` recebe o primeiro valor (2) e `y` recebe o segundo valor (1)

**Conceito:** Atribuição múltipla e tuple unpacking para troca de valores sem variável temporária.

---

### **Questão 2**

**Pergunta:**
O que o operador `//` faz em Python?

**Opções:**
- A. Divisão com resultado float
- B. Divisão inteira (floor division)
- C. Exponenciação
- D. Resto da divisão

**✅ Resposta Correta: B**

**📚 Explicação:**
O operador `//` realiza **divisão inteira** (floor division), que retorna apenas a parte inteira do resultado da divisão, arredondando para baixo.

Exemplos:
- `7 // 2` → `3` (não 3.5)
- `10 // 3` → `3` (não 3.333...)
- `9 // 2` → `4`

**Conceito:** Operadores aritméticos - divisão inteira vs divisão normal (`/`).

---

### **Questão 3**

**Pergunta:**
```python
print(2 ** 3 ** 2)
```

**Opções:**
- A. `64`
- B. `36`
- C. `512`
- D. `81`

**✅ Resposta Correta: C**

**📚 Explicação:**
O operador de exponenciação `**` é **associativo à direita**, ou seja, é avaliado da direita para a esquerda.

Portanto:
- `2 ** 3 ** 2` é interpretado como `2 ** (3 ** 2)`
- Primeiro calcula `3 ** 2 = 9`
- Depois calcula `2 ** 9 = 512`

**Conceito:** Precedência e associatividade de operadores - exponenciação é associativa à direita.

---

### **Questão 4**

**Pergunta:**
Qual é o tipo retornado por `type(3.0)`?

**Opções:**
- A. `<class 'int'>`
- B. `<class 'str'>`
- C. `<class 'double'>`
- D. `<class 'float'>`

**✅ Resposta Correta: D**

**📚 Explicação:**
Em Python, qualquer número com **ponto decimal** é tratado como `float`, mesmo que seja `.0`.

- `3` → `<class 'int'>`
- `3.0` → `<class 'float'>`
- `3.` → `<class 'float'>`

Python não tem tipo `double` (como em C/Java). O tipo `float` usa precisão dupla internamente.

**Conceito:** Tipos numéricos em Python - int vs float.

---

### **Questão 5**

**Pergunta:**
```python
x = "Python"
print(x[1:4])
```

**Opções:**
- A. `Pyt`
- B. `yth`
- C. `ytho`
- D. `Pyth`

**✅ Resposta Correta: B**

**📚 Explicação:**
O **slicing** de strings usa a notação `[início:fim]`, onde:
- O índice de início é **inclusivo**
- O índice de fim é **exclusivo**

Para a string `"Python"`:
- Índice 0: `P`
- Índice 1: `y`
- Índice 2: `t`
- Índice 3: `h`
- Índice 4: `o`
- Índice 5: `n`

`x[1:4]` pega os índices 1, 2 e 3 → `"yth"`

**Conceito:** Slicing (fatiamento) de strings - índices inclusivo/exclusivo.

---

### **Questão 6**

**Pergunta:**
Qual alternativa NÃO é um nome de variável válido?

**Opções:**
- A. `_valor`
- B. `valor2`
- C. `2valor`
- D. `valor_total`

**✅ Resposta Correta: C**

**📚 Explicação:**
Regras para nomes de variáveis em Python:
- ✅ Devem começar com **letra** ou **underscore** (`_`)
- ✅ Podem conter letras, números e underscores
- ❌ **Não podem começar com número**
- ❌ Não podem conter espaços ou caracteres especiais

`2valor` é inválido porque começa com número.

**Conceito:** Convenções de nomenclatura e identificadores válidos em Python.

---

### **Questão 7**

**Pergunta:**
```python
lista = [1, 2, 3, 4, 5]
print(lista[-2])
```

**Opções:**
- A. `5`
- B. `3`
- C. `2`
- D. `4`

**✅ Resposta Correta: D**

**📚 Explicação:**
Índices **negativos** contam de trás para frente:
- `lista[-1]` → último elemento (`5`)
- `lista[-2]` → penúltimo elemento (`4`)
- `lista[-3]` → antepenúltimo elemento (`3`)

**Conceito:** Indexação negativa em sequências (listas, tuplas, strings).

---

### **Questão 8**

**Pergunta:**
```python
print(bool(0), bool(""), bool([]))
```

**Opções:**
- A. `False False False`
- B. `True True True`
- C. `False True False`
- D. `True False True`

**✅ Resposta Correta: A**

**📚 Explicação:**
Em Python, certos valores são considerados **falsy** (equivalentes a `False`):
- Números zero: `0`, `0.0`, `0j`
- Sequências vazias: `""`, `[]`, `()`, `{}`
- `None`
- `False`

Todos os outros valores são **truthy** (equivalentes a `True`).

**Conceito:** Valores booleanos e truthiness/falsiness em Python.

---

### **Questão 9**

**Pergunta:**
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")
```

**Opções:**
- A. `1 2 3 4 5`
- B. `1 2 4`
- C. `0 1 2 4 5`
- D. `1 2 4 5`

**✅ Resposta Correta: D**

**📚 Explicação:**
O comando `continue` **pula o restante da iteração** e volta ao início do loop.

Execução passo a passo:
1. `i=0` → `i=1`, `i!=3` → imprime `1`
2. `i=1` → `i=2`, `i!=3` → imprime `2`
3. `i=2` → `i=3`, `i==3` → `continue` (pula o print)
4. `i=3` → `i=4`, `i!=3` → imprime `4`
5. `i=4` → `i=5`, `i!=3` → imprime `5`
6. `i=5`, não é `< 5`, loop termina

**Conceito:** Controle de fluxo - uso de `continue` em loops.

---

### **Questão 10**

**Pergunta:**
```python
def func(a, b=2):
    return a * b

print(func(3))
```

**Opções:**
- A. `6`
- B. `Erro: argumento faltando`
- C. `32`
- D. `5`

**✅ Resposta Correta: A**

**📚 Explicação:**
Funções podem ter **parâmetros com valores padrão**. Se o argumento não for fornecido, o valor padrão é usado.

- `b=2` define o valor padrão para `b`
- `func(3)` fornece apenas `a=3`
- `b` usa o valor padrão `2`
- Resultado: `3 * 2 = 6`

**Conceito:** Parâmetros opcionais e valores padrão em funções.

---

### **Questão 11**

**Pergunta:**
```python
nums = [1, 2, 3]
nums.append([4, 5])
print(len(nums))
```

**Opções:**
- A. `5`
- B. `3`
- C. `4`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
O método `append()` adiciona o objeto inteiro como **um único elemento** ao final da lista.

- Lista original: `[1, 2, 3]` (3 elementos)
- Após `append([4, 5])`: `[1, 2, 3, [4, 5]]` (4 elementos)
- A lista `[4, 5]` é adicionada como UM elemento

Se quisesse adicionar os elementos individualmente, deveria usar `extend([4, 5])`.

**Conceito:** Diferença entre `append()` (adiciona elemento) e `extend()` (adiciona elementos).

---

### **Questão 12**

**Pergunta:**
```python
x = 10
y = 3
print(x % y)
```

**Opções:**
- A. `3`
- B. `3.33`
- C. `0`
- D. `1`

**✅ Resposta Correta: D**

**📚 Explicação:**
O operador `%` (módulo) retorna o **resto da divisão inteira**.

- `10 ÷ 3 = 3` com resto `1`
- Portanto, `10 % 3 = 1`

Exemplos:
- `10 % 2 = 0` (10 é divisível por 2)
- `7 % 3 = 1`
- `15 % 4 = 3`

**Conceito:** Operador módulo (%) - resto da divisão.

---

### **Questão 13**

**Pergunta:**
Qual método remove E retorna o último elemento de uma lista?

**Opções:**
- A. `list.remove()`
- B. `list.pop()`
- C. `list.del()`
- D. `list.discard()`

**✅ Resposta Correta: B**

**📚 Explicação:**
Métodos de listas:
- **`pop()`**: Remove e **retorna** o último elemento (ou o índice especificado)
- **`remove(valor)`**: Remove a primeira ocorrência do valor (não retorna)
- **`del`**: Palavra-chave (não método) para deletar por índice
- **`discard()`**: Método de `set`, não de lista

Exemplo:
```python
lista = [1, 2, 3]
ultimo = lista.pop()  # ultimo = 3, lista = [1, 2]
```

**Conceito:** Métodos de manipulação de listas.

---

### **Questão 14**

**Pergunta:**
```python
text = "hello"
print(text.upper().count("L"))
```

**Opções:**
- A. `0`
- B. `1`
- C. `2`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Execução em cadeia (method chaining):
1. `text.upper()` → `"HELLO"`
2. `"HELLO".count("L")` → conta quantos `"L"` existem
3. Há 2 letras `L` em `"HELLO"`

**Importante:** O método `count()` é **case-sensitive** (diferencia maiúsculas de minúsculas).

**Conceito:** Métodos de strings - upper(), count() e method chaining.

---

### **Questão 15**

**Pergunta:**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

**Opções:**
- A. `[1, 2, 3]`
- B. `[4, 1, 2, 3]`
- C. `[1, 2, 3, 4]`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Quando fazemos `b = a`, **não criamos uma cópia** da lista. Criamos uma nova **referência** para a mesma lista na memória.

- `a` e `b` apontam para o **mesmo objeto** na memória
- Modificar `b` afeta `a` (porque são a mesma lista)

Para criar uma cópia independente:
```python
b = a.copy()  # ou b = a[:] ou b = list(a)
```

**Conceito:** Referências vs cópias - mutabilidade de listas.

---

### **Questão 16**

**Pergunta:**
```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

**Opções:**
- A. `2 4 6 8`
- B. `3 6 9`
- C. `2 5 8 11`
- D. `2 5 8`

**✅ Resposta Correta: D**

**📚 Explicação:**
A função `range(início, fim, passo)`:
- **início**: valor inicial (inclusivo) → `2`
- **fim**: valor final (exclusivo) → `10`
- **passo**: incremento → `3`

Sequência gerada:
- Começa em `2`
- Próximo: `2 + 3 = 5`
- Próximo: `5 + 3 = 8`
- Próximo: `8 + 3 = 11` (mas 11 ≥ 10, então para)

**Conceito:** Função range() com início, fim e passo.

---

### **Questão 17**

**Pergunta:**
```python
dicionario = {"a": 1, "b": 2, "c": 3}
print("b" in dicionario)
```

**Opções:**
- A. `True`
- B. `False`
- C. `2`
- D. `Erro`

**✅ Resposta Correta: A**

**📚 Explicação:**
O operador `in` verifica se uma **chave** existe no dicionário (não o valor).

- `"b" in dicionario` → `True` (porque "b" é uma chave)
- `2 in dicionario` → `False` (2 é um valor, não uma chave)
- `2 in dicionario.values()` → `True`

**Conceito:** Operador `in` com dicionários - verifica chaves.

---

### **Questão 18**

**Pergunta:**
```python
def func(lst):
    lst = [10, 20, 30]

minha_lista = [1, 2, 3]
func(minha_lista)
print(minha_lista)
```

**Opções:**
- A. `[10, 20, 30]`
- B. `[]`
- C. `[1, 2, 3]`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Quando **reatribuímos** o parâmetro dentro da função (`lst = [10, 20, 30]`), criamos uma **nova variável local** que não afeta o argumento original.

Se quisermos modificar a lista original, devemos usar métodos:
```python
def func(lst):
    lst.clear()
    lst.extend([10, 20, 30])
```

**Conceito:** Passagem por referência vs reatribuição - escopo de variáveis.

---

### **Questão 19**

**Pergunta:**
```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("erro")
else:
    print("ok")
finally:
    print("fim")
```

**Opções:**
- A. `erro ok fim`
- B. `ok fim`
- C. `erro fim`
- D. `Apenas erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Estrutura try-except-else-finally:
- **`try`**: bloco de código a ser testado
- **`except`**: executado se houver exceção → imprime `"erro"`
- **`else`**: executado se **NÃO** houver exceção (não executa neste caso)
- **`finally`**: **sempre** executado, independente de exceção → imprime `"fim"`

Como houve exceção, o `else` não executa.

**Conceito:** Tratamento de exceções - blocos try/except/else/finally.

---

### **Questão 20**

**Pergunta:**
```python
x = "abc"
y = x * 2
z = x + "2"
print(y, z)
```

**Opções:**
- A. `abc2 abcabc`
- B. `6 abc2`
- C. `Erro`
- D. `abcabc abc2`

**✅ Resposta Correta: D**

**📚 Explicação:**
Operações com strings:
- **Multiplicação** (`*`): Repete a string
  - `"abc" * 2` → `"abcabc"`
- **Concatenação** (`+`): Junta strings
  - `"abc" + "2"` → `"abc2"`

**Importante:** Não se pode multiplicar string por string ou somar string com número.

**Conceito:** Operações com strings - repetição e concatenação.

---

## 📊 Resumo dos Conceitos Abordados

| Conceito | Questões |
|----------|----------|
| Tuple unpacking / Swap | 1 |
| Operadores aritméticos | 2, 3, 12 |
| Tipos de dados | 4 |
| Slicing | 5, 16 |
| Nomenclatura de variáveis | 6 |
| Indexação negativa | 7 |
| Valores truthy/falsy | 8 |
| Controle de fluxo (continue) | 9 |
| Parâmetros padrão | 10 |
| Métodos de listas | 11, 13 |
| Métodos de strings | 14, 20 |
| Referências vs cópias | 15, 18 |
| Range() | 16 |
| Operador in | 17 |
| Tratamento de exceções | 19 |

---

**🎯 Critério de Aprovação:** Mínimo de 14 acertos (70%)

**📚 Dica de Estudo:** Revise os conceitos das questões que você errou e pratique com códigos similares!
