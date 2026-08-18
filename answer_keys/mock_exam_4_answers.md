# 📝 DETAILED ANSWER KEY - PCEP MOCK EXAM 4 (Intermediate/Hard)

## ✅ Answer Key & Explanations

---

### **Question 1**

**Code:**
```python
x = 1
y = 2
z = x
x = y
y = z
print(x, y, z)
```

**Options:**
- A. `1 2 1`
- B. `2 1 2`
- C. `1 1 2`
- D. `2 1 1`

**✅ Correct Answer: D**

**📚 Explanation:**
This is a **manual swap** using a temporary variable, executed step by step:

Initial state:
- `x = 1`, `y = 2`

Step-by-step:
1. `z = x` → `z = 1` (saves x's value)
2. `x = y` → `x = 2` (x now has y's value)
3. `y = z` → `y = 1` (y now has x's original value)

Final result: `x=2, y=1, z=1` → prints `2 1 1`

**Concept:** Variable swap using a temporary variable.

---

### **Question 2**

**Code:**
```python
print(2 ** 3 + 5 // 2 - 1 * 3)
```

**Options:**
- A. `7`
- B. `8`
- C. `9`
- D. `10`

**✅ Correct Answer: A**

**📚 Explanation:**
**Operator precedence** (highest to lowest):
1. `**` (exponentiation)
2. `*`, `/`, `//`, `%` (multiplication, division)
3. `+`, `-` (addition, subtraction)

Step-by-step calculation:
1. `2 ** 3` = `8`
2. `5 // 2` = `2`
3. `1 * 3` = `3`
4. `8 + 2 - 3` = `7`

**Concept:** Arithmetic operator precedence.

---

### **Question 3**

**Code:**
```python
s = "abcde"
print(s[::-1][1:4])
```

**Options:**
- A. `bcd`
- B. `edc`
- C. `dcb`
- D. `cba`

**✅ Correct Answer: C**

**📚 Explanation:**
Chained operations:
1. `s[::-1]` → reverses the string → `"edcba"`
2. `[1:4]` → takes indices 1 to 3 → `"dcb"`

Detail: `[::-1]` uses negative step `-1` to reverse the sequence.

**Concept:** Advanced slicing with negative step and chaining.

---

### **Question 4**

**Code:**
```python
x = [1, 2, 3]
y = x[:]
y.append(4)
print(x, y)
```

**Options:**
- A. `[1, 2, 3, 4] [1, 2, 3, 4]`
- B. `[1, 2, 3] [1, 2, 3, 4]`
- C. `[1, 2, 3, 4] [1, 2, 3]`
- D. `Error`

**✅ Correct Answer: B**

**📚 Explanation:**
`x[:]` creates a **shallow copy** of the list.

Important difference:
- `y = x` → reference (same list)
- `y = x[:]` → copy (independent lists)

Other ways to copy:
```python
y = x.copy()
y = list(x)
y = x[:]
```

**Concept:** Shallow copy vs reference — list copying.

---

### **Question 5**

**Code:**
```python
def f(x, lst=[]):
    lst.append(x)
    return lst

print(f(1))
print(f(2))
```

**Options:**
- A. `[1]\n[2]`
- B. `[1, 2]\n[1, 2]`
- C. `Error`
- D. `[1]\n[1, 2]`

**✅ Correct Answer: D**

**📚 Explanation:**
⚠️ **Classic Python pitfall!**

Mutable **default arguments** are created **once** when the function is defined, not on each call.

Execution:
1. `f(1)` → `lst` is `[]`, appends 1 → returns `[1]`
2. `f(2)` → `lst` is still `[1]` (same list!), appends 2 → returns `[1, 2]`

**Correct solution:**
```python
def f(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
```

**Concept:** Mutable default argument pitfall.

---

### **Question 6**

**Code:**
```python
a = "hello"
b = a.replace("l", "L", 1)
print(b)
```

**Options:**
- A. `heLLo`
- B. `Hello`
- C. `hELLO`
- D. `heLlo`

**✅ Correct Answer: D**

**📚 Explanation:**
The `replace(old, new, count)` method has an optional third parameter:
- **`count`**: maximum number of replacements

`a.replace("l", "L", 1)`:
- Replaces only the **first** occurrence of "l" with "L"
- `"hello"` → `"heLlo"` (only the first "l" becomes "L")

Without the third parameter, it would replace all occurrences: `"heLLo"`.

**Concept:** replace() method with replacement limit.

---

### **Question 7**

**Code:**
```python
x = 5
print(x == 5 and x is 5)
```

**Options:**
- A. `True (but behavior is implementation-dependent)`
- B. `False`
- C. `Syntax error`
- D. `None`

**✅ Correct Answer: A**

**📚 Explanation:**
Difference between `==` and `is`:
- **`==`**: compares **values** (equality)
- **`is`**: compares **identity** (same object in memory)

**CPython** caches small integers (-5 to 256), so `x is 5` returns `True` for these values.

⚠️ **Important:** This behavior **is not guaranteed** by the Python specification and may vary between implementations.

**Best practice:** Use `is` only to compare with `None`, `True`, `False`.

**Concept:** Difference between == (equality) and is (identity).

---

### **Question 8**

**Code:**
```python
d = {"a": 1, "b": 2}
d["c"] = d.get("c", 0) + 1
print(d)
```

**Options:**
- A. `{'a': 1, 'b': 2, 'c': 0}`
- B. `{'a': 1, 'b': 2, 'c': 1}`
- C. `KeyError`
- D. `{'a': 1, 'b': 2}`

**✅ Correct Answer: B**

**📚 Explanation:**
The `get(key, default)` method:
- Returns the key's value if it exists
- Returns the `default` value if the key doesn't exist

Execution:
1. `d.get("c", 0)` → "c" doesn't exist, returns `0`
2. `0 + 1` = `1`
3. `d["c"] = 1` → creates key "c" with value `1`

**Common usage:** Occurrence counter without checking if key exists.

**Concept:** dict.get() method with default value.

---

### **Question 9**

**Code:**
```python
x = [i ** 2 for i in range(5) if i % 2 != 0]
print(x)
```

**Options:**
- A. `[0, 4, 16]`
- B. `[1, 4, 9]`
- C. `[1, 9]`
- D. `[0, 1, 4, 9, 16]`

**✅ Correct Answer: C**

**📚 Explanation:**
**List comprehension** with filter:

Structure: `[expression for item in iterable if condition]`

Execution:
- `range(5)` → 0, 1, 2, 3, 4
- Filter `if i % 2 != 0` → only odd numbers → 1, 3
- `i ** 2` → 1² = 1, 3² = 9
- Result: `[1, 9]`

**Concept:** List comprehension with filter condition.

---

### **Question 10**

**Code:**
```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
```

**Options:**
- A. `TypeError: tuple is immutable`
- B. `(1, 2, [3, 4], 5)`
- C. `(1, 2, [3, 4, 5])`
- D. `(1, 2, [5, 3, 4])`

**✅ Correct Answer: C**

**📚 Explanation:**
⚠️ **Important concept:**
- The **tuple** is immutable (cannot change its elements)
- But the **list inside** the tuple is mutable

`t[2]` returns the list `[3, 4]`, which can be modified.

Analogy: The tuple is a "sealed box" containing objects. You can't swap what's in the box, but you can modify the contents of mutable objects inside it.

**Concept:** Tuple immutability vs mutability of internal elements.

---

### **Question 11**

**Code:**
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

**Options:**
- A. `10`
- B. `5`
- C. `UnboundLocalError`
- D. `15`

**✅ Correct Answer: D**

**📚 Explanation:**
The `nonlocal` keyword allows modifying variables from the **enclosing scope** (but not global).

Without `nonlocal`:
```python
def inner():
    x += 5  # UnboundLocalError!
```

With `nonlocal`:
```python
def inner():
    nonlocal x  # Modifies the variable from outer's scope
    x += 5  # Works! x goes from 10 to 15
```

**Concept:** nonlocal — modifying variables in enclosing scopes.

---

### **Question 12**

**Code:**
```python
print(list(zip([1, 2, 3], "ab")))
```

**Options:**
- A. `[(1, 'a'), (2, 'b')]`
- B. `[(1, 'a'), (2, 'b'), (3, None)]`
- C. `[(1, 'a'), (2, 'b'), (3, '')]`
- D. `Error`

**✅ Correct Answer: A**

**📚 Explanation:**
The `zip()` function combines elements from multiple iterables, but **stops at the shortest**.

Execution:
- List: `[1, 2, 3]` (3 elements)
- String: `"ab"` (2 elements)
- `zip()` stops when the string runs out
- Result: `[(1, 'a'), (2, 'b')]`

**Usage:** Iterate over multiple sequences simultaneously.

**Concept:** zip() function — combining iterables.

---

### **Question 13**

**Code:**
```python
x = 10
def func():
    print(x)
x = 20
func()
```

**Options:**
- A. `10`
- B. `Error`
- C. `20`
- D. `None`

**✅ Correct Answer: C**

**📚 Explanation:**
Python uses **late binding**: the variable is resolved at **execution** time, not at definition time.

Sequence:
1. `x = 10` (defines x)
2. `def func()` (defines function, doesn't execute)
3. `x = 20` (modifies x)
4. `func()` (executes → looks up x **now** → finds 20)

**Concept:** Late binding — variable resolution at execution time.

---

### **Question 14**

**Code:**
```python
nums = [4, 2, 7, 1, 9]
result = sorted(nums, reverse=True)[:3]
print(result)
```

**Options:**
- A. `[1, 2, 4]`
- B. `[4, 2, 7]`
- C. `[9, 7, 4, 2, 1]`
- D. `[9, 7, 4]`

**✅ Correct Answer: D**

**📚 Explanation:**
Chained operations:
1. `sorted(nums, reverse=True)` → sorts descending → `[9, 7, 4, 2, 1]`
2. `[:3]` → takes first 3 → `[9, 7, 4]`

**Important difference:**
- `sorted()` → returns a new sorted list
- `list.sort()` → sorts in-place, returns None

**Concept:** sorted() function with reverse and slicing.

---

### **Question 15**

**Code:**
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b, a - b)
```

**Options:**
- A. `{2, 3} {1}`
- B. `{1, 4} {2, 3}`
- C. `{2, 3} {4}`
- D. `Error`

**✅ Correct Answer: A**

**📚 Explanation:**
**Set** operations:
- **`&`** (intersection): elements in both → `{2, 3}`
- **`-`** (difference): elements in `a` but not in `b` → `{1}`

Other operations:
- `|` (union): all elements → `{1, 2, 3, 4}`
- `^` (symmetric difference): elements in only one → `{1, 4}`

**Concept:** Set operations.

---

### **Question 16**

**Code:**
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

**Options:**
- A. `3 1`
- B. `1 1`
- C. `3 3`
- D. `3 0`

**✅ Correct Answer: C**

**📚 Explanation:**
`count` is a **class attribute** (shared between all instances).

Execution:
1. `a = A()` → `A.count` becomes 1
2. `b = A()` → `A.count` becomes 2
3. `c = A()` → `A.count` becomes 3
4. `A.count` = 3
5. `a.count` accesses the attribute via instance → also returns 3

**Difference:**
- **Class** attribute: shared
- **Instance** attribute: individual (`self.count`)

**Concept:** Class attributes vs instance attributes.

---

### **Question 17**

**Code:**
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

**Options:**
- A. `100`
- B. `99`
- C. `98`
- D. `-1`

**✅ Correct Answer: B**

**📚 Explanation:**
Execution flow:
1. `int("abc")` → **ValueError**
2. `except ValueError` catches it → `x = -1`
3. `else` does NOT execute (exception occurred)
4. `finally` ALWAYS executes → `x = -1 + 100 = 99`

**Concept:** Multiple except with else and finally.

---

### **Question 18**

**Code:**
```python
m = [[0]*3 for _ in range(3)]
m[0][1] = 5
print(m[1][1])
```

**Options:**
- A. `5`
- B. `None`
- C. `0`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
List comprehension creates **independent lists**:

`[[0]*3 for _ in range(3)]` creates:
```python
[
    [0, 0, 0],  # Independent list
    [0, 0, 0],  # Independent list
    [0, 0, 0]   # Independent list
]
```

Modifying `m[0][1]` does not affect `m[1][1]`.

**Concept:** List comprehension for matrices — independent lists.

---

### **Question 19**

**Code:**
```python
m = [[0]*3] * 3
m[0][1] = 5
print(m[1][1])
```

**Options:**
- A. `0`
- B. `5`
- C. `None`
- D. `Error`

**✅ Correct Answer: B**

**📚 Explanation:**
⚠️ **Pitfall!** Multiplying a list creates **references** to the same list:

`[[0]*3] * 3` creates:
```python
[
    [0, 0, 0],  # ┐
    [0, 0, 0],  # ├─ SAME list in memory!
    [0, 0, 0]   # ┘
]
```

Modifying `m[0][1]` modifies **all** "rows" because they are the same list.

**Correct solution:** Use list comprehension (question 18).

**Concept:** List multiplication pitfall — shared references.

---

### **Question 20**

**Code:**
```python
gen = (x for x in range(5))
next(gen)
next(gen)
print(list(gen))
```

**Options:**
- A. `[0, 1, 2, 3, 4]`
- B. `[3, 4]`
- C. `Error`
- D. `[2, 3, 4]`

**✅ Correct Answer: D**

**📚 Explanation:**
A **generator** uses parentheses `()` and is **lazy** (evaluates on demand).

Execution:
1. `next(gen)` → consumes and returns 0
2. `next(gen)` → consumes and returns 1
3. `list(gen)` → consumes the rest → `[2, 3, 4]`

**Difference:**
- `[x for x in range(5)]` → full list (memory)
- `(x for x in range(5))` → generator (lazy, memory-efficient)

**Concept:** Generators — lazy evaluation and iteration.

---

## 📊 Concepts Summary

| Concept | Questions |
|---------|-----------|
| Swap and assignments | 1 |
| Operator precedence | 2 |
| Advanced slicing | 3, 14 |
| Copies vs references | 4, 15, 18, 19 |
| Mutable default arguments | 5 |
| String methods | 6 |
| Identity vs equality | 7 |
| Dictionary methods | 8 |
| List comprehension | 9 |
| Mutability and tuples | 10 |
| Scope (nonlocal) | 11 |
| zip() function | 12 |
| Late binding | 13 |
| Set operations | 15 |
| Class attributes | 16 |
| Exception handling | 17 |
| Generators | 20 |

---

**🎯 Passing Score:** Minimum 14 correct answers (70%)

**📚 Study Tip:** This mock exam covers intermediate/advanced concepts. Focus especially on common pitfalls (questions 5, 10, 19)!
