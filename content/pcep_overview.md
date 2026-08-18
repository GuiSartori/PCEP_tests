# Simulado PCEP – Certified Entry-Level Python Programmer
## 20 Questões de Múltipla Escolha

---

### Questão 1
Qual é o resultado do seguinte código?

```python
x = 1
y = 2
x, y = y, x
print(x, y)
```

A. `1 2`  
B. `2 1`  
C. `1 1`  
D. `2 2`  

---

### Questão 2
O que o operador `//` faz em Python?

A. Divisão com resultado float  
B. Divisão inteira (floor division)  
C. Exponenciação  
D. Resto da divisão  

---

### Questão 3
Qual é o resultado?

```python
print(2 ** 3 ** 2)
```

A. `64`  
B. `512`  
C. `36`  
D. `81`  

---

### Questão 4
Qual é o tipo de dado retornado pela expressão `type(3.0)`?

A. `<class 'int'>`  
B. `<class 'float'>`  
C. `<class 'str'>`  
D. `<class 'double'>`  

---

### Questão 5
Qual é o resultado?

```python
x = "Python"
print(x[1:4])
```

A. `Pyt`  
B. `yth`  
C. `ytho`  
D. `Pyth`  

---

### Questão 6
Qual alternativa NÃO é um nome de variável válido em Python?

A. `_valor`  
B. `valor2`  
C. `2valor`  
D. `valor_total`  

---

### Questão 7
Qual é o resultado?

```python
lista = [1, 2, 3, 4, 5]
print(lista[-2])
```

A. `5`  
B. `4`  
C. `3`  
D. `2`  

---

### Questão 8
Qual é o resultado?

```python
print(bool(0), bool(""), bool([]))
```

A. `True True True`  
B. `False False False`  
C. `False True False`  
D. `True False True`  

---

### Questão 9
Quantas vezes o loop executa?

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

A. 5 vezes (imprime 1, 2, 3, 4, 5)  
B. 4 vezes (imprime 1, 2, 4, 5)  
C. 3 vezes (imprime 1, 2, 4)  
D. 5 vezes (imprime 0, 1, 2, 4, 5)  

---

### Questão 10
O que acontece ao executar?

```python
def func(a, b=2):
    return a * b

print(func(3))
```

A. Erro: argumento faltando  
B. `6`  
C. `32`  
D. `5`  

---

### Questão 11
Qual é o resultado?

```python
nums = [1, 2, 3]
nums.append([4, 5])
print(len(nums))
```

A. `5`  
B. `4`  
C. `3`  
D. Erro  

---

### Questão 12
Qual é o resultado?

```python
x = 10
y = 3
print(x % y)
```

A. `3`  
B. `1`  
C. `3.33`  
D. `0`  

---

### Questão 13
Qual método remove E retorna o último elemento de uma lista?

A. `list.remove()`  
B. `list.pop()`  
C. `list.del()`  
D. `list.discard()`  

---

### Questão 14
Qual é o resultado?

```python
text = "hello"
print(text.upper().count("L"))
```

A. `0`  
B. `2`  
C. `1`  
D. Erro  

---

### Questão 15
Qual é o resultado?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

A. `[1, 2, 3]`  
B. `[1, 2, 3, 4]`  
C. `[4, 1, 2, 3]`  
D. Erro  

---

### Questão 16
Qual é o resultado?

```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

A. `2 5 8`  
B. `2 4 6 8`  
C. `3 6 9`  
D. `2 5 8 11`  

---

### Questão 17
O que o seguinte código imprime?

```python
dicionario = {"a": 1, "b": 2, "c": 3}
print("b" in dicionario)
```

A. `True`  
B. `False`  
C. `2`  
D. Erro  

---

### Questão 18
Qual é o resultado?

```python
def func(lst):
    lst = [10, 20, 30]

minha_lista = [1, 2, 3]
func(minha_lista)
print(minha_lista)
```

A. `[10, 20, 30]`  
B. `[1, 2, 3]`  
C. `[]`  
D. Erro  

---

### Questão 19
Qual é o resultado?

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

A. `erro fim`  
B. `erro ok fim`  
C. `ok fim`  
D. Apenas `erro`  

---

### Questão 20
Qual é o resultado?

```python
x = "abc"
y = x * 2
z = x + "2"
print(y, z)
```

A. `abcabc abc2`  
B. `abc2 abcabc`  
C. `6 abc2`  
D. Erro  

---

## GABARITO

| # | Resposta | Explicação resumida |
|---|----------|---------------------|
| 1 | B | Swap com tuple unpacking |
| 2 | B | `//` é divisão inteira |
| 3 | B | `**` é associativo à direita: `2 ** (3**2)` = `2**9` = 512 |
| 4 | B | `3.0` é float |
| 5 | B | Slice [1:4] → índices 1, 2, 3 → "yth" |
| 6 | C | Variável não pode começar com número |
| 7 | B | Índice -2 é o penúltimo → 4 |
| 8 | B | 0, string vazia e lista vazia são todos falsy |
| 9 | B | `continue` pula o print quando i==3, imprime 1, 2, 4, 5 |
| 10 | B | `b` tem valor padrão 2, então 3*2=6 |
| 11 | B | `append` adiciona a lista como UM elemento → len = 4 |
| 12 | B | 10 % 3 = 1 (resto) |
| 13 | B | `pop()` remove e retorna o último |
| 14 | B | "HELLO".count("L") → 2 |
| 15 | B | `b = a` cria referência, não cópia |
| 16 | A | range(2, 10, 3) → 2, 5, 8 |
| 17 | A | `in` verifica chaves do dicionário |
| 18 | B | Reatribuir `lst` dentro da função não afeta a variável externa |
| 19 | A | Exceção capturada → `else` não executa → `finally` sempre executa |
| 20 | A | `"abc" * 2` = "abcabc", `"abc" + "2"` = "abc2" |
