# 📝 CORREÇÃO DETALHADA - SIMULADO PCEP 2 (Intermediário/Difícil)

## ✅ Gabarito e Explicações

---

### **Questão 1**

**Pergunta:**
```python
x = 1
y = 2
z = x
x = y
y = z
print(x, y, z)
```

**Opções:**
- A. `1 2 1`
- B. `2 1 2`
- C. `1 1 2`
- D. `2 1 1`

**✅ Resposta Correta: D**

**📚 Explicação:**
Este é um **swap manual** usando variável temporária, executado passo a passo:

Estado inicial:
- `x = 1`, `y = 2`

Passo a passo:
1. `z = x` → `z = 1` (salva o valor de x)
2. `x = y` → `x = 2` (x agora tem o valor de y)
3. `y = z` → `y = 1` (y agora tem o valor original de x)

Resultado final: `x=2, y=1, z=1` → imprime `2 1 1`

**Conceito:** Swap de variáveis usando variável temporária.

---

### **Questão 2**

**Pergunta:**
```python
print(2 ** 3 + 5 // 2 - 1 * 3)
```

**Opções:**
- A. `7`
- B. `8`
- C. `9`
- D. `10`

**✅ Resposta Correta: A**

**📚 Explicação:**
**Ordem de precedência** dos operadores (do maior para o menor):
1. `**` (exponenciação)
2. `*`, `/`, `//`, `%` (multiplicação, divisão)
3. `+`, `-` (adição, subtração)

Cálculo passo a passo:
1. `2 ** 3` = `8`
2. `5 // 2` = `2`
3. `1 * 3` = `3`
4. `8 + 2 - 3` = `7`

**Conceito:** Precedência de operadores aritméticos.

---

### **Questão 3**

**Pergunta:**
```python
s = "abcde"
print(s[::-1][1:4])
```

**Opções:**
- A. `bcd`
- B. `edc`
- C. `dcb`
- D. `cba`

**✅ Resposta Correta: C**

**📚 Explicação:**
Operações encadeadas:
1. `s[::-1]` → inverte a string → `"edcba"`
2. `[1:4]` → pega do índice 1 ao 3 → `"dcb"`

Detalhe: `[::-1]` usa passo negativo `-1` para inverter a sequência.

**Conceito:** Slicing avançado com passo negativo e encadeamento.

---

### **Questão 4**

**Pergunta:**
```python
x = [1, 2, 3]
y = x[:]
y.append(4)
print(x, y)
```

**Opções:**
- A. `[1, 2, 3, 4] [1, 2, 3, 4]`
- B. `[1, 2, 3] [1, 2, 3, 4]`
- C. `[1, 2, 3, 4] [1, 2, 3]`
- D. `Erro`

**✅ Resposta Correta: B**

**📚 Explicação:**
`x[:]` cria uma **cópia superficial** (shallow copy) da lista.

Diferença importante:
- `y = x` → referência (mesma lista)
- `y = x[:]` → cópia (listas independentes)

Outras formas de copiar:
```python
y = x.copy()
y = list(x)
y = x[:]
```

**Conceito:** Shallow copy vs referência - cópia de listas.

---

### **Questão 5**

**Pergunta:**
```python
def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))
print(f(2))
```

**Opções:**
- A. `[1]\n[2]`
- B. `[1, 2]\n[1, 2]`
- C. `Erro`
- D. `[1]\n[1, 2]`

**✅ Resposta Correta: D**

**📚 Explicação:**
⚠️ **Armadilha clássica do Python!**

Argumentos padrão **mutáveis** são criados **uma única vez** quando a função é definida, não a cada chamada.

Execução:
1. `f(1)` → `lst` é `[]`, adiciona 1 → retorna `[1]`
2. `f(2)` → `lst` ainda é `[1]` (mesma lista!), adiciona 2 → retorna `[1, 2]`

**Solução correta:**
```python
def f(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
```

**Conceito:** Armadilha de argumentos padrão mutáveis.

---

### **Questão 6**

**Pergunta:**
```python
a = "hello"
b = a.replace("l", "L", 1)
print(b)
```

**Opções:**
- A. `heLLo`
- B. `Hello`
- C. `hELLO`
- D. `heLlo`

**✅ Resposta Correta: D**

**📚 Explicação:**
O método `replace(old, new, count)` tem um terceiro parâmetro opcional:
- **`count`**: número máximo de substituições

`a.replace("l", "L", 1)`:
- Substitui apenas a **primeira** ocorrência de "l" por "L"
- `"hello"` → `"heLlo"` (só o primeiro "l" vira "L")

Sem o terceiro parâmetro, substituiria todas as ocorrências: `"heLLo"`.

**Conceito:** Método replace() com limite de substituições.

---

### **Questão 7**

**Pergunta:**
```python
x = 5
print(x == 5 and x is 5)
```

**Opções:**
- A. `True (mas comportamento depende da implementação)`
- B. `False`
- C. `Erro de sintaxe`
- D. `None`

**✅ Resposta Correta: A**

**📚 Explicação:**
Diferença entre `==` e `is`:
- **`==`**: compara **valores** (igualdade)
- **`is`**: compara **identidade** (mesmo objeto na memória)

**CPython** faz cache de inteiros pequenos (-5 a 256), então `x is 5` retorna `True` para esses valores.

⚠️ **Importante:** Este comportamento **não é garantido** pela especificação Python e pode variar entre implementações.

**Boa prática:** Use `is` apenas para comparar com `None`, `True`, `False`.

**Conceito:** Diferença entre == (igualdade) e is (identidade).

---

### **Questão 8**

**Pergunta:**
```python
d = {"a": 1, "b": 2}
d["c"] = d.get("c", 0) + 1
print(d)
```

**Opções:**
- A. `{'a': 1, 'b': 2, 'c': 0}`
- B. `{'a': 1, 'b': 2, 'c': 1}`
- C. `KeyError`
- D. `{'a': 1, 'b': 2}`

**✅ Resposta Correta: B**

**📚 Explicação:**
O método `get(chave, padrão)`:
- Retorna o valor da chave se existir
- Retorna o valor `padrão` se a chave não existir

Execução:
1. `d.get("c", 0)` → "c" não existe, retorna `0`
2. `0 + 1` = `1`
3. `d["c"] = 1` → cria a chave "c" com valor `1`

**Uso comum:** Contador de ocorrências sem verificar se a chave existe.

**Conceito:** Método get() de dicionários com valor padrão.

---

### **Questão 9**

**Pergunta:**
```python
x = [i ** 2 for i in range(5) if i % 2 != 0]
print(x)
```

**Opções:**
- A. `[0, 4, 16]`
- B. `[1, 4, 9]`
- C. `[1, 9]`
- D. `[0, 1, 4, 9, 16]`

**✅ Resposta Correta: C**

**📚 Explicação:**
**List comprehension** com filtro:

Estrutura: `[expressão for item in iterável if condição]`

Execução:
- `range(5)` → 0, 1, 2, 3, 4
- Filtro `if i % 2 != 0` → apenas ímpares → 1, 3
- `i ** 2` → 1² = 1, 3² = 9
- Resultado: `[1, 9]`

**Conceito:** List comprehension com condição de filtro.

---

### **Questão 10**

**Pergunta:**
```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
```

**Opções:**
- A. `TypeError: tupla é imutável`
- B. `(1, 2, [3, 4], 5)`
- C. `(1, 2, [3, 4, 5])`
- D. `(1, 2, [5, 3, 4])`

**✅ Resposta Correta: C**

**📚 Explicação:**
⚠️ **Conceito importante:**
- A **tupla** é imutável (não pode mudar seus elementos)
- Mas a **lista dentro** da tupla é mutável

`t[2]` retorna a lista `[3, 4]`, que pode ser modificada.

Analogia: A tupla é uma "caixa lacrada" que contém objetos. Você não pode trocar o que está na caixa, mas pode modificar o conteúdo de objetos mutáveis dentro dela.

**Conceito:** Imutabilidade de tuplas vs mutabilidade de elementos internos.

---

### **Questão 11**

**Pergunta:**
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    return x

print(outer())
```

**Opções:**
- A. `10`
- B. `5`
- C. `UnboundLocalError`
- D. `15`

**✅ Resposta Correta: D**

**📚 Explicação:**
A palavra-chave `nonlocal` permite modificar variáveis do **escopo externo** (mas não global).

Sem `nonlocal`:
```python
def inner():
    x += 5  # UnboundLocalError!
```

Com `nonlocal`:
```python
def inner():
    nonlocal x  # Modifica a variável do escopo outer
    x += 5  # Funciona! x passa de 10 para 15
```

**Conceito:** nonlocal - modificação de variáveis em escopos externos.

---

### **Questão 12**

**Pergunta:**
```python
print(list(zip([1, 2, 3], "ab")))
```

**Opções:**
- A. `[(1, 'a'), (2, 'b')]`
- B. `[(1, 'a'), (2, 'b'), (3, None)]`
- C. `[(1, 'a'), (2, 'b'), (3, '')]`
- D. `Erro`

**✅ Resposta Correta: A**

**📚 Explicação:**
A função `zip()` combina elementos de múltiplos iteráveis, mas **para no menor**.

Execução:
- Lista: `[1, 2, 3]` (3 elementos)
- String: `"ab"` (2 elementos)
- `zip()` para quando a string acaba
- Resultado: `[(1, 'a'), (2, 'b')]`

**Uso:** Iterar sobre múltiplas sequências simultaneamente.

**Conceito:** Função zip() - combinação de iteráveis.

---

### **Questão 13**

**Pergunta:**
```python
x = 10
def func():
    print(x)
x = 20
func()
```

**Opções:**
- A. `10`
- B. `Erro`
- C. `20`
- D. `None`

**✅ Resposta Correta: C**

**📚 Explicação:**
Python usa **late binding** (ligação tardia): a variável é resolvida no momento da **execução**, não da definição.

Sequência:
1. `x = 10` (define x)
2. `def func()` (define função, mas não executa)
3. `x = 20` (modifica x)
4. `func()` (executa → busca x **agora** → encontra 20)

**Conceito:** Late binding - resolução de variáveis no momento da execução.

---

### **Questão 14**

**Pergunta:**
```python
nums = [4, 2, 7, 1, 9]
result = sorted(nums, reverse=True)[:3]
print(result)
```

**Opções:**
- A. `[1, 2, 4]`
- B. `[4, 2, 7]`
- C. `[9, 7, 4, 2, 1]`
- D. `[9, 7, 4]`

**✅ Resposta Correta: D**

**📚 Explicação:**
Operações encadeadas:
1. `sorted(nums, reverse=True)` → ordena decrescente → `[9, 7, 4, 2, 1]`
2. `[:3]` → pega os 3 primeiros → `[9, 7, 4]`

**Diferença importante:**
- `sorted()` → retorna nova lista ordenada
- `list.sort()` → ordena in-place, retorna None

**Conceito:** Função sorted() com reverse e slicing.

---

### **Questão 15**

**Pergunta:**
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b, a - b)
```

**Opções:**
- A. `{2, 3} {1}`
- B. `{1, 4} {2, 3}`
- C. `{2, 3} {4}`
- D. `Erro`

**✅ Resposta Correta: A**

**📚 Explicação:**
Operações com **sets** (conjuntos):
- **`&`** (interseção): elementos em ambos → `{2, 3}`
- **`-`** (diferença): elementos em `a` mas não em `b` → `{1}`

Outras operações:
- `|` (união): todos elementos → `{1, 2, 3, 4}`
- `^` (diferença simétrica): elementos em apenas um → `{1, 4}`

**Conceito:** Operações de conjuntos (sets).

---

### **Questão 16**

**Pergunta:**
```python
class A:
    count = 0
    def __init__(self):
        A.count += 1

a = A()
b = A()
c = A()
print(A.count, a.count)
```

**Opções:**
- A. `3 1`
- B. `1 1`
- C. `3 3`
- D. `3 0`

**✅ Resposta Correta: C**

**📚 Explicação:**
`count` é um **atributo de classe** (compartilhado entre todas as instâncias).

Execução:
1. `a = A()` → `A.count` vira 1
2. `b = A()` → `A.count` vira 2
3. `c = A()` → `A.count` vira 3
4. `A.count` = 3
5. `a.count` acessa o atributo via instância → também retorna 3

**Diferença:**
- Atributo de **classe**: compartilhado
- Atributo de **instância**: individual (`self.count`)

**Conceito:** Atributos de classe vs atributos de instância.

---

### **Questão 17**

**Pergunta:**
```python
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

print(x)
```

**Opções:**
- A. `100`
- B. `99`
- C. `98`
- D. `-1`

**✅ Resposta Correta: B**

**📚 Explicação:**
Fluxo de execução:
1. `int("abc")` → **ValueError**
2. `except ValueError` captura → `x = -1`
3. `else` NÃO executa (houve exceção)
4. `finally` SEMPRE executa → `x = -1 + 100 = 99`

**Conceito:** Múltiplos except com else e finally.

---

### **Questão 18**

**Pergunta:**
```python
m = [[0]*3 for _ in range(3)]
m[0][1] = 5
print(m[1][1])
```

**Opções:**
- A. `5`
- B. `None`
- C. `0`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
List comprehension cria **listas independentes**:

`[[0]*3 for _ in range(3)]` cria:
```python
[
    [0, 0, 0],  # Lista independente
    [0, 0, 0],  # Lista independente
    [0, 0, 0]   # Lista independente
]
```

Modificar `m[0][1]` não afeta `m[1][1]`.

**Conceito:** List comprehension para matriz - listas independentes.

---

### **Questão 19**

**Pergunta:**
```python
m = [[0]*3] * 3
m[0][1] = 5
print(m[1][1])
```

**Opções:**
- A. `0`
- B. `5`
- C. `None`
- D. `Erro`

**✅ Resposta Correta: B**

**📚 Explicação:**
⚠️ **Armadilha!** Multiplicar lista cria **referências** para a mesma lista:

`[[0]*3] * 3` cria:
```python
[
    [0, 0, 0],  # ┐
    [0, 0, 0],  # ├─ MESMA lista na memória!
    [0, 0, 0]   # ┘
]
```

Modificar `m[0][1]` modifica **todas** as "linhas" porque são a mesma lista.

**Solução correta:** Usar list comprehension (questão 18).

**Conceito:** Armadilha de multiplicação de listas - referências compartilhadas.

---

### **Questão 20**

**Pergunta:**
```python
gen = (x for x in range(5))
next(gen)
next(gen)
print(list(gen))
```

**Opções:**
- A. `[0, 1, 2, 3, 4]`
- B. `[3, 4]`
- C. `Erro`
- D. `[2, 3, 4]`

**✅ Resposta Correta: D**

**📚 Explicação:**
**Generator** (gerador) usa parênteses `()` e é **lazy** (avalia sob demanda).

Execução:
1. `next(gen)` → consome e retorna 0
2. `next(gen)` → consome e retorna 1
3. `list(gen)` → consome o restante → `[2, 3, 4]`

**Diferença:**
- `[x for x in range(5)]` → lista completa (memória)
- `(x for x in range(5))` → generator (lazy, econômico)

**Conceito:** Generators - avaliação lazy e iteração.

---

## 📊 Resumo dos Conceitos Abordados

| Conceito | Questões |
|----------|----------|
| Swap e atribuições | 1 |
| Precedência de operadores | 2 |
| Slicing avançado | 3, 14 |
| Cópias vs referências | 4, 15, 18, 19 |
| Argumentos padrão mutáveis | 5 |
| Métodos de strings | 6 |
| Identidade vs igualdade | 7 |
| Métodos de dicionários | 8 |
| List comprehension | 9 |
| Mutabilidade e tuplas | 10 |
| Escopo (nonlocal) | 11 |
| Função zip() | 12 |
| Late binding | 13 |
| Operações com sets | 15 |
| Atributos de classe | 16 |
| Tratamento de exceções | 17 |
| Generators | 20 |

---

**🎯 Critério de Aprovação:** Mínimo de 14 acertos (70%)

**📚 Dica de Estudo:** Este simulado aborda conceitos intermediários/avançados. Pratique especialmente as armadilhas comuns (questões 5, 10, 19)!
