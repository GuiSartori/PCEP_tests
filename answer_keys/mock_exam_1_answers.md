# 📝 DETAILED ANSWER KEY - PCEP MOCK EXAM 1

## ✅ Answer Key & Explanations

---

### **Question 1**

**Code:**
```python
x = 1
y = 2
x, y = y, x
print(x, y)
```

**Options:**
- A. `2 1`
- B. `1 2`
- C. `1 1`
- D. `2 2`

**✅ Correct Answer: A**

**📚 Explanation:**
This technique is called **tuple unpacking** or **simultaneous swap**.

In Python, the expression `x, y = y, x` works like this:
1. The right-hand side `y, x` creates a temporary tuple `(2, 1)`
2. The left-hand side `x, y` unpacks that tuple
3. `x` gets the first value (2) and `y` gets the second value (1)

**Concept:** Multiple assignment and tuple unpacking for swapping values without a temporary variable.

---

### **Question 2**

**Question:**
What does the `//` operator do in Python?

**Options:**
- A. Division with float result
- B. Floor division (integer division)
- C. Exponentiation
- D. Remainder of division

**✅ Correct Answer: B**

**📚 Explanation:**
The `//` operator performs **floor division**, which returns only the integer part of the division result, rounding down.

Examples:
- `7 // 2` → `3` (not 3.5)
- `10 // 3` → `3` (not 3.333...)
- `9 // 2` → `4`

**Concept:** Arithmetic operators — floor division vs normal division (`/`).

---

### **Question 3**

**Code:**
```python
print(2 ** 3 ** 2)
```

**Options:**
- A. `64`
- B. `36`
- C. `512`
- D. `81`

**✅ Correct Answer: C**

**📚 Explanation:**
The exponentiation operator `**` is **right-associative**, meaning it evaluates from right to left.

Therefore:
- `2 ** 3 ** 2` is interpreted as `2 ** (3 ** 2)`
- First computes `3 ** 2 = 9`
- Then computes `2 ** 9 = 512`

**Concept:** Operator precedence and associativity — exponentiation is right-associative.

---

### **Question 4**

**Question:**
What is the type returned by `type(3.0)`?

**Options:**
- A. `<class 'int'>`
- B. `<class 'str'>`
- C. `<class 'double'>`
- D. `<class 'float'>`

**✅ Correct Answer: D**

**📚 Explanation:**
In Python, any number with a **decimal point** is treated as `float`, even if it's `.0`.

- `3` → `<class 'int'>`
- `3.0` → `<class 'float'>`
- `3.` → `<class 'float'>`

Python does not have a `double` type (unlike C/Java). The `float` type uses double precision internally.

**Concept:** Numeric types in Python — int vs float.

---

### **Question 5**

**Code:**
```python
x = "Python"
print(x[1:4])
```

**Options:**
- A. `Pyt`
- B. `yth`
- C. `ytho`
- D. `Pyth`

**✅ Correct Answer: B**

**📚 Explanation:**
String **slicing** uses the notation `[start:end]`, where:
- The start index is **inclusive**
- The end index is **exclusive**

For the string `"Python"`:
- Index 0: `P`
- Index 1: `y`
- Index 2: `t`
- Index 3: `h`
- Index 4: `o`
- Index 5: `n`

`x[1:4]` takes indices 1, 2, and 3 → `"yth"`

**Concept:** String slicing — inclusive start / exclusive end.

---

### **Question 6**

**Question:**
Which option is NOT a valid variable name?

**Options:**
- A. `_valor`
- B. `valor2`
- C. `2valor`
- D. `valor_total`

**✅ Correct Answer: C**

**📚 Explanation:**
Rules for variable names in Python:
- ✅ Must start with a **letter** or **underscore** (`_`)
- ✅ Can contain letters, numbers, and underscores
- ❌ **Cannot start with a number**
- ❌ Cannot contain spaces or special characters

`2valor` is invalid because it starts with a number.

**Concept:** Naming conventions and valid identifiers in Python.

---

### **Question 7**

**Code:**
```python
lista = [1, 2, 3, 4, 5]
print(lista[-2])
```

**Options:**
- A. `5`
- B. `3`
- C. `2`
- D. `4`

**✅ Correct Answer: D**

**📚 Explanation:**
**Negative** indices count from the end:
- `lista[-1]` → last element (`5`)
- `lista[-2]` → second-to-last element (`4`)
- `lista[-3]` → third-to-last element (`3`)

**Concept:** Negative indexing in sequences (lists, tuples, strings).

---

### **Question 8**

**Code:**
```python
print(bool(0), bool(""), bool([]))
```

**Options:**
- A. `False False False`
- B. `True True True`
- C. `False True False`
- D. `True False True`

**✅ Correct Answer: A**

**📚 Explanation:**
In Python, certain values are considered **falsy** (equivalent to `False`):
- Zero numbers: `0`, `0.0`, `0j`
- Empty sequences: `""`, `[]`, `()`, `{}`
- `None`
- `False`

All other values are **truthy** (equivalent to `True`).

**Concept:** Boolean values and truthiness/falsiness in Python.

---

### **Question 9**

**Code:**
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")
```

**Options:**
- A. `1 2 3 4 5`
- B. `1 2 4`
- C. `0 1 2 4 5`
- D. `1 2 4 5`

**✅ Correct Answer: D**

**📚 Explanation:**
The `continue` statement **skips the rest of the current iteration** and goes back to the top of the loop.

Step-by-step execution:
1. `i=0` → `i=1`, `i!=3` → prints `1`
2. `i=1` → `i=2`, `i!=3` → prints `2`
3. `i=2` → `i=3`, `i==3` → `continue` (skips print)
4. `i=3` → `i=4`, `i!=3` → prints `4`
5. `i=4` → `i=5`, `i!=3` → prints `5`
6. `i=5`, not `< 5`, loop ends

**Concept:** Control flow — using `continue` in loops.

---

### **Question 10**

**Code:**
```python
def func(a, b=2):
    return a * b

print(func(3))
```

**Options:**
- A. `6`
- B. `Error: missing argument`
- C. `32`
- D. `5`

**✅ Correct Answer: A**

**📚 Explanation:**
Functions can have **parameters with default values**. If the argument is not provided, the default value is used.

- `b=2` sets the default value for `b`
- `func(3)` provides only `a=3`
- `b` uses the default value `2`
- Result: `3 * 2 = 6`

**Concept:** Optional parameters and default values in functions.

---

### **Question 11**

**Code:**
```python
nums = [1, 2, 3]
nums.append([4, 5])
print(len(nums))
```

**Options:**
- A. `5`
- B. `3`
- C. `4`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
The `append()` method adds the entire object as **a single element** to the end of the list.

- Original list: `[1, 2, 3]` (3 elements)
- After `append([4, 5])`: `[1, 2, 3, [4, 5]]` (4 elements)
- The list `[4, 5]` is added as ONE element

To add elements individually, use `extend([4, 5])`.

**Concept:** Difference between `append()` (adds one element) and `extend()` (adds multiple elements).

---

### **Question 12**

**Code:**
```python
x = 10
y = 3
print(x % y)
```

**Options:**
- A. `3`
- B. `3.33`
- C. `0`
- D. `1`

**✅ Correct Answer: D**

**📚 Explanation:**
The `%` (modulo) operator returns the **remainder of integer division**.

- `10 ÷ 3 = 3` with remainder `1`
- Therefore, `10 % 3 = 1`

Examples:
- `10 % 2 = 0` (10 is divisible by 2)
- `7 % 3 = 1`
- `15 % 4 = 3`

**Concept:** Modulo operator (%) — remainder of division.

---

### **Question 13**

**Question:**
Which method removes AND returns the last element of a list?

**Options:**
- A. `list.remove()`
- B. `list.pop()`
- C. `list.del()`
- D. `list.discard()`

**✅ Correct Answer: B**

**📚 Explanation:**
List methods:
- **`pop()`**: Removes and **returns** the last element (or the element at a specified index)
- **`remove(value)`**: Removes the first occurrence of the value (does not return it)
- **`del`**: Keyword (not a method) for deleting by index
- **`discard()`**: Method of `set`, not of list

Example:
```python
my_list = [1, 2, 3]
last = my_list.pop()  # last = 3, my_list = [1, 2]
```

**Concept:** List manipulation methods.

---

### **Question 14**

**Code:**
```python
text = "hello"
print(text.upper().count("L"))
```

**Options:**
- A. `0`
- B. `1`
- C. `2`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
Method chaining execution:
1. `text.upper()` → `"HELLO"`
2. `"HELLO".count("L")` → counts how many `"L"` exist
3. There are 2 letters `L` in `"HELLO"`

**Important:** The `count()` method is **case-sensitive**.

**Concept:** String methods — upper(), count() and method chaining.

---

### **Question 15**

**Code:**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

**Options:**
- A. `[1, 2, 3]`
- B. `[4, 1, 2, 3]`
- C. `[1, 2, 3, 4]`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
When we do `b = a`, we do **not create a copy** of the list. We create a new **reference** to the same list in memory.

- `a` and `b` point to the **same object** in memory
- Modifying `b` affects `a` (because they are the same list)

To create an independent copy:
```python
b = a.copy()  # or b = a[:] or b = list(a)
```

**Concept:** References vs copies — list mutability.

---

### **Question 16**

**Code:**
```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

**Options:**
- A. `2 4 6 8`
- B. `3 6 9`
- C. `2 5 8 11`
- D. `2 5 8`

**✅ Correct Answer: D**

**📚 Explanation:**
The `range(start, stop, step)` function:
- **start**: initial value (inclusive) → `2`
- **stop**: final value (exclusive) → `10`
- **step**: increment → `3`

Generated sequence:
- Starts at `2`
- Next: `2 + 3 = 5`
- Next: `5 + 3 = 8`
- Next: `8 + 3 = 11` (but 11 ≥ 10, so it stops)

**Concept:** range() function with start, stop, and step.

---

### **Question 17**

**Code:**
```python
dicionario = {"a": 1, "b": 2, "c": 3}
print("b" in dicionario)
```

**Options:**
- A. `True`
- B. `False`
- C. `2`
- D. `Error`

**✅ Correct Answer: A**

**📚 Explanation:**
The `in` operator checks if a **key** exists in the dictionary (not the value).

- `"b" in dicionario` → `True` (because "b" is a key)
- `2 in dicionario` → `False` (2 is a value, not a key)
- `2 in dicionario.values()` → `True`

**Concept:** `in` operator with dictionaries — checks keys.

---

### **Question 18**

**Code:**
```python
def func(lst):
    lst = [10, 20, 30]

minha_lista = [1, 2, 3]
func(minha_lista)
print(minha_lista)
```

**Options:**
- A. `[10, 20, 30]`
- B. `[]`
- C. `[1, 2, 3]`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
When we **reassign** the parameter inside the function (`lst = [10, 20, 30]`), we create a **new local variable** that does not affect the original argument.

To modify the original list, use methods:
```python
def func(lst):
    lst.clear()
    lst.extend([10, 20, 30])
```

**Concept:** Pass by reference vs reassignment — variable scope.

---

### **Question 19**

**Code:**
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

**Options:**
- A. `erro ok fim`
- B. `ok fim`
- C. `erro fim`
- D. `Only erro`

**✅ Correct Answer: C**

**📚 Explanation:**
try-except-else-finally structure:
- **`try`**: code block to be tested
- **`except`**: executed if an exception occurs → prints `"erro"`
- **`else`**: executed if **NO** exception occurs (does not execute here)
- **`finally`**: **always** executed, regardless of exceptions → prints `"fim"`

Since an exception occurred, the `else` block does not execute.

**Concept:** Exception handling — try/except/else/finally blocks.

---

### **Question 20**

**Code:**
```python
x = "abc"
y = x * 2
z = x + "2"
print(y, z)
```

**Options:**
- A. `abc2 abcabc`
- B. `6 abc2`
- C. `Error`
- D. `abcabc abc2`

**✅ Correct Answer: D**

**📚 Explanation:**
String operations:
- **Multiplication** (`*`): Repeats the string
  - `"abc" * 2` → `"abcabc"`
- **Concatenation** (`+`): Joins strings
  - `"abc" + "2"` → `"abc2"`

**Important:** You cannot multiply string by string or add string with number.

**Concept:** String operations — repetition and concatenation.

---

## 📊 Concepts Summary

| Concept | Questions |
|---------|-----------|
| Tuple unpacking / Swap | 1 |
| Arithmetic operators | 2, 3, 12 |
| Data types | 4 |
| Slicing | 5, 16 |
| Variable naming | 6 |
| Negative indexing | 7 |
| Truthy/falsy values | 8 |
| Control flow (continue) | 9 |
| Default parameters | 10 |
| List methods | 11, 13 |
| String methods | 14, 20 |
| References vs copies | 15, 18 |
| Range() | 16 |
| in operator | 17 |
| Exception handling | 19 |

---

**🎯 Passing Score:** Minimum 14 correct answers (70%)

**📚 Study Tip:** Review the concepts from questions you got wrong and practice with similar code!
