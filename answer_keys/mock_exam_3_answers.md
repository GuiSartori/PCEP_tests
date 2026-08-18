# 📝 CORREÇÃO DETALHADA - SIMULADO PCEP 3 (Revisão Geral)

## ✅ Gabarito e Explicações

---

### **Questão 1**

**Pergunta:**
```python
x = "Python"
print(x[-3:])
```

**Opções:**
- A. `Pyt`
- B. `tho`
- C. `on`
- D. `hon`

**✅ Resposta Correta: D**

**📚 Explicação:**
Slicing com índice negativo:
- `x[-3:]` → do 3º elemento de trás para frente até o fim

String `"Python"`:
- Índice -6: `P`
- Índice -5: `y`
- Índice -4: `t`
- Índice -3: `h` ← começa aqui
- Índice -2: `o`
- Índice -1: `n`

Resultado: `"hon"`

**Conceito:** Slicing com índices negativos.

---

### **Questão 2**

**Pergunta:**
```python
print(isinstance(True, int))
```

**Opções:**
- A. `False`
- B. `TypeError`
- C. `True`
- D. `None`

**✅ Resposta Correta: C**

**📚 Explicação:**
Em Python, `bool` é uma **subclasse** de `int`!

Implicações:
- `True` == `1` → `True`
- `False` == `0` → `True`
- `True + True` → `2`
- `False * 10` → `0`

Hierarquia de tipos:
```
object
  └─ int
      └─ bool
```

**Conceito:** bool é subclasse de int - hierarquia de tipos.

---

### **Questão 3**

**Pergunta:**
```python
a = [1, 2, 3, 4, 5]
b = a[1:4]
b[0] = 99
print(a[1])
```

**Opções:**
- A. `99`
- B. `2`
- C. `1`
- D. `Erro`

**✅ Resposta Correta: B**

**📚 Explicação:**
**Slicing cria uma nova lista** (cópia dos elementos).

Execução:
1. `b = a[1:4]` → `b = [2, 3, 4]` (nova lista)
2. `b[0] = 99` → `b = [99, 3, 4]`
3. `a` permanece inalterado: `[1, 2, 3, 4, 5]`
4. `a[1]` = `2`

**Diferença:**
- `b = a[1:4]` → cópia (independente)
- `b = a` → referência (compartilhado)

**Conceito:** Slicing cria cópias, não referências.

---

### **Questão 4**

**Pergunta:**
```python
d = {}
d[1] = "a"
d["1"] = "b"
d[1.0] = "c"
print(len(d))
```

**Opções:**
- A. `1`
- B. `2`
- C. `3`
- D. `Erro`

**✅ Resposta Correta: B**

**📚 Explicação:**
Em Python, `1` e `1.0` são considerados **iguais**:
- `1 == 1.0` → `True`
- `hash(1) == hash(1.0)` → `True`

Portanto, são a **mesma chave** no dicionário!

Execução:
1. `d[1] = "a"` → `{1: "a"}`
2. `d["1"] = "b"` → `{1: "a", "1": "b"}` (chave diferente!)
3. `d[1.0] = "c"` → `{1: "c", "1": "b"}` (sobrescreve 1)

Resultado: 2 chaves → `len(d) = 2`

**Conceito:** Equivalência entre int e float em dicionários.

---

### **Questão 5**

**Pergunta:**
```python
def f(a, b, c=3, d=4):
    return a + b + c + d

print(f(1, 2, d=10))
```

**Opções:**
- A. `16`
- B. `20`
- C. `10`
- D. `Erro`

**✅ Resposta Correta: A**

**📚 Explicação:**
Chamada com **argumentos posicionais e nomeados**:
- `a = 1` (posicional)
- `b = 2` (posicional)
- `c = 3` (valor padrão, não fornecido)
- `d = 10` (nomeado, sobrescreve o padrão)

Soma: `1 + 2 + 3 + 10 = 16`

**Conceito:** Argumentos posicionais, nomeados e valores padrão.

---

### **Questão 6**

**Pergunta:**
```python
for i in range(5):
    if i == 3:
        break
else:
    print("else")
print(i)
```

**Opções:**
- A. `else\n3`
- B. `else\n4`
- C. `4`
- D. `3`

**✅ Resposta Correta: D**

**📚 Explicação:**
O bloco `else` de um loop **só executa se o loop completar normalmente** (sem `break`).

Execução:
1. `i=0`, `i=1`, `i=2` → loop continua
2. `i=3` → `break` → sai do loop
3. `else` NÃO executa (loop foi interrompido)
4. `print(i)` → imprime `3`

**Importante:** A variável do loop (`i`) persiste após o loop!

**Conceito:** Cláusula else em loops - break impede execução.

---

### **Questão 7**

**Pergunta:**
```python
s = "hello world"
print(s.split())
```

**Opções:**
- A. `['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']`
- B. `['hello', 'world']`
- C. `['hello world']`
- D. `('hello', 'world')`

**✅ Resposta Correta: B**

**📚 Explicação:**
`split()` sem argumentos:
- Separa por **qualquer whitespace** (espaços, tabs, newlines)
- Remove whitespace extra automaticamente
- Retorna uma **lista**

Exemplos:
- `"hello world".split()` → `['hello', 'world']`
- `"a  b   c".split()` → `['a', 'b', 'c']`
- `"hello world".split(' ')` → `['hello', 'world']`

**Conceito:** Método split() - separação por whitespace.

---

### **Questão 8**

**Pergunta:**
```python
x = lambda a, b: a if a > b else b
print(x(5, 8))
```

**Opções:**
- A. `5`
- B. `True`
- C. `Erro`
- D. `8`

**✅ Resposta Correta: D**

**📚 Explicação:**
**Lambda** é uma função anônima de uma linha.

Equivalente a:
```python
def x(a, b):
    if a > b:
        return a
    else:
        return b
```

Execução:
- `x(5, 8)` → `5 > 8` é `False`
- Retorna `b` → `8`

**Uso:** Funções simples em `map()`, `filter()`, `sorted()`, etc.

**Conceito:** Funções lambda e expressão condicional ternária.

---

### **Questão 9**

**Pergunta:**
```python
nums = [1, 2, 3, 4, 5]
print(nums[::2])
```

**Opções:**
- A. `[1, 3, 5]`
- B. `[2, 4]`
- C. `[1, 2]`
- D. `[5, 3, 1]`

**✅ Resposta Correta: A**

**📚 Explicação:**
Slicing com passo: `[início:fim:passo]`
- `[::2]` → do início ao fim, de 2 em 2

Execução:
- Índice 0: `1` ✓
- Índice 1: `2` (pula)
- Índice 2: `3` ✓
- Índice 3: `4` (pula)
- Índice 4: `5` ✓

Resultado: `[1, 3, 5]`

**Conceito:** Slicing com step (passo).

---

### **Questão 10**

**Pergunta:**
```python
x = 5
def f():
    global x
    x = 10
f()
print(x)
```

**Opções:**
- A. `5`
- B. `Erro`
- C. `10`
- D. `None`

**✅ Resposta Correta: C**

**📚 Explicação:**
A palavra-chave `global` permite **modificar variáveis globais** dentro de funções.

Sem `global`:
```python
def f():
    x = 10  # Cria variável LOCAL, não afeta a global
```

Com `global`:
```python
def f():
    global x  # Modifica a variável GLOBAL
    x = 10
```

**Conceito:** Palavra-chave global - modificação de variáveis globais.

---

### **Questão 11**

**Pergunta:**
```python
print("abc" * 0)
```

**Opções:**
- A. `abc`
- B. `0`
- C. `Erro`
- D. `''` (string vazia)

**✅ Resposta Correta: D**

**📚 Explicação:**
Multiplicar string por número inteiro:
- `"abc" * 3` → `"abcabcabc"`
- `"abc" * 1` → `"abc"`
- `"abc" * 0` → `""` (string vazia)
- `"abc" * -1` → `""` (também vazia)

**Conceito:** Repetição de strings - casos especiais (0 e negativos).

---

### **Questão 12**

**Pergunta:**
```python
lst = [3, 1, 4, 1, 5]
lst.sort()
lst.reverse()
print(lst[0])
```

**Opções:**
- A. `5`
- B. `1`
- C. `3`
- D. `4`

**✅ Resposta Correta: A**

**📚 Explicação:**
Métodos que modificam a lista **in-place**:

Execução:
1. `lst.sort()` → `[1, 1, 3, 4, 5]` (ordena crescente)
2. `lst.reverse()` → `[5, 4, 3, 1, 1]` (inverte)
3. `lst[0]` → `5`

**Importante:** Ambos os métodos retornam `None`, não a lista!

**Conceito:** Métodos in-place - sort() e reverse().

---

### **Questão 13**

**Pergunta:**
```python
t = (1, 2, 3)
t[0] = 10
```

**Opções:**
- A. `t se torna (10, 2, 3)`
- B. `TypeError: tuplas são imutáveis`
- C. `t se torna [10, 2, 3]`
- D. `IndexError`

**✅ Resposta Correta: B**

**📚 Explicação:**
Tuplas são **imutáveis** - não é possível modificar seus elementos.

Operações permitidas:
- ✅ `t[0]` (acessar)
- ✅ `t + (4,)` (criar nova tupla)
- ✅ `t * 2` (criar nova tupla)
- ❌ `t[0] = 10` (modificar) → **TypeError**

**Exceção:** Se a tupla contém objetos mutáveis (como listas), esses objetos internos podem ser modificados.

**Conceito:** Imutabilidade de tuplas.

---

### **Questão 14**

**Pergunta:**
```python
d = {"x": 1, "y": 2, "z": 3}
print(list(d.values()))
```

**Opções:**
- A. `['x', 'y', 'z']`
- B. `[('x',1), ('y',2), ('z',3)]`
- C. `[1, 2, 3]`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Métodos de dicionários:
- **`keys()`**: retorna as chaves → `dict_keys(['x', 'y', 'z'])`
- **`values()`**: retorna os valores → `dict_values([1, 2, 3])`
- **`items()`**: retorna pares (chave, valor) → `dict_items([('x', 1), ...])`

`list(d.values())` converte para lista → `[1, 2, 3]`

**Conceito:** Métodos de dicionários - keys(), values(), items().

---

### **Questão 15**

**Pergunta:**
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("erro")
else:
    print("ok")
finally:
    print("fim")
```

**Opções:**
- A. `erro fim`
- B. `fim`
- C. `ok fim`
- D. `ok`

**✅ Resposta Correta: C**

**📚 Explicação:**
Estrutura completa de tratamento de exceções:

- **`try`**: código a ser testado
- **`except`**: executado SE houver exceção
- **`else`**: executado SE NÃO houver exceção → imprime `"ok"`
- **`finally`**: **SEMPRE** executado → imprime `"fim"`

Como `10 / 2` não gera exceção, o `else` é executado.

**Conceito:** Blocos try/except/else/finally - fluxo completo.

---

### **Questão 16**

**Pergunta:**
```python
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z[-1], len(z))
```

**Opções:**
- A. `3 6`
- B. `6 3`
- C. `6 6`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
Operador `+` com listas realiza **concatenação**:

Execução:
1. `z = x + y` → `[1, 2, 3, 4, 5, 6]`
2. `z[-1]` → último elemento → `6`
3. `len(z)` → comprimento → `6`

Saída: `6 6`

**Conceito:** Concatenação de listas com operador +.

---

### **Questão 17**

**Pergunta:**
```python
x = "abcdef"
print(x[1::2])
```

**Opções:**
- A. `ace`
- B. `abcdef`
- C. `bce`
- D. `bdf`

**✅ Resposta Correta: D**

**📚 Explicação:**
Slicing `[início::passo]`:
- Começa no índice 1 (`b`)
- Vai até o fim
- Passo 2 (pega de 2 em 2)

String `"abcdef"`:
- Índice 1: `b` ✓
- Índice 2: `c` (pula)
- Índice 3: `d` ✓
- Índice 4: `e` (pula)
- Índice 5: `f` ✓

Resultado: `"bdf"`

**Conceito:** Slicing com início e passo.

---

### **Questão 18**

**Pergunta:**
```python
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

print(f(6))
```

**Opções:**
- A. `5`
- B. `8`
- C. `13`
- D. `21`

**✅ Resposta Correta: B**

**📚 Explicação:**
Esta é a **sequência de Fibonacci** implementada recursivamente.

Sequência:
- f(0) = 0
- f(1) = 1
- f(2) = f(1) + f(0) = 1 + 0 = 1
- f(3) = f(2) + f(1) = 1 + 1 = 2
- f(4) = f(3) + f(2) = 2 + 1 = 3
- f(5) = f(4) + f(3) = 3 + 2 = 5
- f(6) = f(5) + f(4) = 5 + 3 = **8**

**Conceito:** Recursão - Fibonacci.

---

### **Questão 19**

**Pergunta:**
```python
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
a.update(b)
print(a)
```

**Opções:**
- A. `{'a': 1, 'b': 2, 'c': 4}`
- B. `{'b': 3, 'c': 4}`
- C. `{'a': 1, 'b': 3, 'c': 4}`
- D. `Erro`

**✅ Resposta Correta: C**

**📚 Explicação:**
O método `update()` **mescla** dicionários:
- Adiciona novas chaves
- **Sobrescreve** chaves existentes

Execução:
1. `a = {"a": 1, "b": 2}`
2. `a.update({"b": 3, "c": 4})`
   - Adiciona `"c": 4`
   - Sobrescreve `"b": 2` → `"b": 3`
3. Resultado: `{"a": 1, "b": 3, "c": 4}`

**Conceito:** Método update() de dicionários - mesclagem.

---

### **Questão 20**

**Pergunta:**
```python
items = ["a", "b", "c"]
result = list(enumerate(items, start=1))
print(result[1])
```

**Opções:**
- A. `(2, 'b')`
- B. `(1, 'a')`
- C. `(0, 'b')`
- D. `(1, 'b')`

**✅ Resposta Correta: A**

**📚 Explicação:**
`enumerate(iterável, start=n)` retorna tuplas (índice, valor):

Execução:
1. `enumerate(items, start=1)`:
   - `(1, 'a')`
   - `(2, 'b')`
   - `(3, 'c')`
2. `list(...)` → `[(1, 'a'), (2, 'b'), (3, 'c')]`
3. `result[1]` → segundo elemento → `(2, 'b')`

**Uso comum:** Loop com contador personalizado:
```python
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

**Conceito:** Função enumerate() com start personalizado.

---

## 📊 Resumo dos Conceitos Abordados

| Conceito | Questões |
|----------|----------|
| Slicing (básico e avançado) | 1, 3, 9, 17 |
| Hierarquia de tipos | 2 |
| Equivalência em dicionários | 4 |
| Argumentos de funções | 5 |
| Cláusula else em loops | 6 |
| Métodos de strings | 7 |
| Funções lambda | 8 |
| Escopo (global) | 10 |
| Operações com strings | 11 |
| Métodos in-place | 12 |
| Imutabilidade | 13 |
| Métodos de dicionários | 14, 19 |
| Tratamento de exceções | 15 |
| Concatenação de listas | 16 |
| Recursão | 18 |
| Enumerate | 20 |

---

## 🎯 Distribuição de Dificuldade

- **Básico** (8 questões): 1, 7, 9, 11, 12, 13, 14, 16
- **Intermediário** (8 questões): 3, 5, 6, 10, 15, 17, 19, 20
- **Avançado** (4 questões): 2, 4, 8, 18

---

**🎯 Critério de Aprovação:** Mínimo de 14 acertos (70%)

**📚 Dica de Estudo:** Este simulado oferece uma revisão equilibrada. Pratique os conceitos que você tem mais dificuldade!

---

## 📖 Recursos Adicionais

### Comandos úteis para praticar:
```python
# Slicing
s = "Python"
print(s[::-1])    # Inverter
print(s[::2])     # Pular elementos

# Dicionários
d = {"a": 1}
d.update({"b": 2})
print(d.get("c", 0))

# Listas
lst = [1, 2, 3]
lst.sort()
lst.reverse()

# Tratamento de exceções
try:
    # código
except Exception as e:
    # tratamento
else:
    # sem exceção
finally:
    # sempre executa
```
