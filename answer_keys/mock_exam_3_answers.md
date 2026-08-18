# 📝 DETAILED ANSWER KEY - PCEP MOCK EXAM 3 (Balanced Review)

## ✅ Answer Key & Explanations

---

### **Question 1**

**Code:**
```python
x = "Python"
print(x[-3:])
```

**Options:**
- A. `Pyt`
- B. `tho`
- C. `on`
- D. `hon`

**✅ Correct Answer: D**

**📚 Explanation:**
Slicing with negative index:
- `x[-3:]` → from the 3rd element from the end to the end

String `"Python"`:
- Index -6: `P`
- Index -5: `y`
- Index -4: `t`
- Index -3: `h` ← starts here
- Index -2: `o`
- Index -1: `n`

Result: `"hon"`

**Concept:** Slicing with negative indices.

---

### **Question 2**

**Code:**
```python
print(isinstance(True, int))
```

**Options:**
- A. `False`
- B. `TypeError`
- C. `True`
- D. `None`

**✅ Correct Answer: C**

**📚 Explanation:**
In Python, `bool` is a **subclass** of `int`!

Implications:
- `True` == `1` → `True`
- `False` == `0` → `True`
- `True + True` → `2`
- `False * 10` → `0`

Type hierarchy:
```
object
  └─ int
      └─ bool
```

**Concept:** bool is a subclass of int — type hierarchy.

---

### **Question 3**

**Code:**
```python
a = [1, 2, 3, 4, 5]
b = a[1:4]
b[0] = 99
print(a[1])
```

**Options:**
- A. `99`
- B. `2`
- C. `1`
- D. `Error`

**✅ Correct Answer: B**

**📚 Explanation:**
**Slicing creates a new list** (a copy of elements).

Execution:
1. `b = a[1:4]` → `b = [2, 3, 4]` (new list)
2. `b[0] = 99` → `b = [99, 3, 4]`
3. `a` remains unchanged: `[1, 2, 3, 4, 5]`
4. `a[1]` = `2`

**Difference:**
- `b = a[1:4]` → copy (independent)
- `b = a` → reference (shared)

**Concept:** Slicing creates copies, not references.

---

### **Question 4**

**Code:**
```python
d = {}
d[1] = "a"
d["1"] = "b"
d[1.0] = "c"
print(len(d))
```

**Options:**
- A. `1`
- B. `2`
- C. `3`
- D. `Error`

**✅ Correct Answer: B**

**📚 Explanation:**
In Python, `1` and `1.0` are considered **equal**:
- `1 == 1.0` → `True`
- `hash(1) == hash(1.0)` → `True`

Therefore, they are the **same key** in the dictionary!

Execution:
1. `d[1] = "a"` → `{1: "a"}`
2. `d["1"] = "b"` → `{1: "a", "1": "b"}` (different key!)
3. `d[1.0] = "c"` → `{1: "c", "1": "b"}` (overwrites key 1)

Result: 2 keys → `len(d) = 2`

**Concept:** Equivalence between int and float as dictionary keys.

---

### **Question 5**

**Code:**
```python
def f(a, b, c=3, d=4):
    return a + b + c + d

print(f(1, 2, d=10))
```

**Options:**
- A. `16`
- B. `20`
- C. `10`
- D. `Error`

**✅ Correct Answer: A**

**📚 Explanation:**
Call with **positional and keyword arguments**:
- `a = 1` (positional)
- `b = 2` (positional)
- `c = 3` (default value, not provided)
- `d = 10` (keyword, overrides default)

Sum: `1 + 2 + 3 + 10 = 16`

**Concept:** Positional arguments, keyword arguments, and default values.

---

### **Question 6**

**Code:**
```python
for i in range(5):
    if i == 3:
        break
else:
    print("else")
print(i)
```

**Options:**
- A. `else\n3`
- B. `else\n4`
- C. `4`
- D. `3`

**✅ Correct Answer: D**

**📚 Explanation:**
The `else` block of a loop **only executes if the loop completes normally** (without `break`).

Execution:
1. `i=0`, `i=1`, `i=2` → loop continues
2. `i=3` → `break` → exits loop
3. `else` does NOT execute (loop was interrupted)
4. `print(i)` → prints `3`

**Important:** The loop variable (`i`) persists after the loop!

**Concept:** else clause in loops — break prevents execution.

---

### **Question 7**

**Code:**
```python
s = "hello world"
print(s.split())
```

**Options:**
- A. `['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']`
- B. `['hello', 'world']`
- C. `['hello world']`
- D. `('hello', 'world')`

**✅ Correct Answer: B**

**📚 Explanation:**
`split()` without arguments:
- Splits on **any whitespace** (spaces, tabs, newlines)
- Removes extra whitespace automatically
- Returns a **list**

Examples:
- `"hello world".split()` → `['hello', 'world']`
- `"a  b   c".split()` → `['a', 'b', 'c']`
- `"hello world".split(' ')` → `['hello', 'world']`

**Concept:** split() method — splitting by whitespace.

---

### **Question 8**

**Code:**
```python
x = lambda a, b: a if a > b else b
print(x(5, 8))
```

**Options:**
- A. `5`
- B. `True`
- C. `Error`
- D. `8`

**✅ Correct Answer: D**

**📚 Explanation:**
**Lambda** is a one-line anonymous function.

Equivalent to:
```python
def x(a, b):
    if a > b:
        return a
    else:
        return b
```

Execution:
- `x(5, 8)` → `5 > 8` is `False`
- Returns `b` → `8`

**Usage:** Simple functions in `map()`, `filter()`, `sorted()`, etc.

**Concept:** Lambda functions and ternary conditional expression.

---

### **Question 9**

**Code:**
```python
nums = [1, 2, 3, 4, 5]
print(nums[::2])
```

**Options:**
- A. `[1, 3, 5]`
- B. `[2, 4]`
- C. `[1, 2]`
- D. `[5, 3, 1]`

**✅ Correct Answer: A**

**📚 Explanation:**
Slicing with step: `[start:stop:step]`
- `[::2]` → from start to end, every 2nd element

Execution:
- Index 0: `1` ✓
- Index 1: `2` (skipped)
- Index 2: `3` ✓
- Index 3: `4` (skipped)
- Index 4: `5` ✓

Result: `[1, 3, 5]`

**Concept:** Slicing with step.

---

### **Question 10**

**Code:**
```python
x = 5
def f():
    global x
    x = 10
f()
print(x)
```

**Options:**
- A. `5`
- B. `Error`
- C. `10`
- D. `None`

**✅ Correct Answer: C**

**📚 Explanation:**
The `global` keyword allows **modifying global variables** inside functions.

Without `global`:
```python
def f():
    x = 10  # Creates a LOCAL variable, doesn't affect the global
```

With `global`:
```python
def f():
    global x  # Modifies the GLOBAL variable
    x = 10
```

**Concept:** global keyword — modifying global variables.

---

### **Question 11**

**Code:**
```python
print("abc" * 0)
```

**Options:**
- A. `abc`
- B. `0`
- C. `Error`
- D. `''` (empty string)

**✅ Correct Answer: D**

**📚 Explanation:**
Multiplying string by integer:
- `"abc" * 3` → `"abcabcabc"`
- `"abc" * 1` → `"abc"`
- `"abc" * 0` → `""` (empty string)
- `"abc" * -1` → `""` (also empty)

**Concept:** String repetition — special cases (0 and negatives).

---

### **Question 12**

**Code:**
```python
lst = [3, 1, 4, 1, 5]
lst.sort()
lst.reverse()
print(lst[0])
```

**Options:**
- A. `5`
- B. `1`
- C. `3`
- D. `4`

**✅ Correct Answer: A**

**📚 Explanation:**
Methods that modify the list **in-place**:

Execution:
1. `lst.sort()` → `[1, 1, 3, 4, 5]` (ascending order)
2. `lst.reverse()` → `[5, 4, 3, 1, 1]` (reversed)
3. `lst[0]` → `5`

**Important:** Both methods return `None`, not the list!

**Concept:** In-place methods — sort() and reverse().

---

### **Question 13**

**Code:**
```python
t = (1, 2, 3)
t[0] = 10
```

**Options:**
- A. `t becomes (10, 2, 3)`
- B. `TypeError: tuples are immutable`
- C. `t becomes [10, 2, 3]`
- D. `IndexError`

**✅ Correct Answer: B**

**📚 Explanation:**
Tuples are **immutable** — you cannot modify their elements.

Allowed operations:
- ✅ `t[0]` (access)
- ✅ `t + (4,)` (create new tuple)
- ✅ `t * 2` (create new tuple)
- ❌ `t[0] = 10` (modify) → **TypeError**

**Exception:** If the tuple contains mutable objects (like lists), those internal objects can be modified.

**Concept:** Tuple immutability.

---

### **Question 14**

**Code:**
```python
d = {"x": 1, "y": 2, "z": 3}
print(list(d.values()))
```

**Options:**
- A. `['x', 'y', 'z']`
- B. `[('x',1), ('y',2), ('z',3)]`
- C. `[1, 2, 3]`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
Dictionary methods:
- **`keys()`**: returns the keys → `dict_keys(['x', 'y', 'z'])`
- **`values()`**: returns the values → `dict_values([1, 2, 3])`
- **`items()`**: returns (key, value) pairs → `dict_items([('x', 1), ...])`

`list(d.values())` converts to list → `[1, 2, 3]`

**Concept:** Dictionary methods — keys(), values(), items().

---

### **Question 15**

**Code:**
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

**Options:**
- A. `erro fim`
- B. `fim`
- C. `ok fim`
- D. `ok`

**✅ Correct Answer: C**

**📚 Explanation:**
Complete exception handling structure:

- **`try`**: code to be tested
- **`except`**: executed IF an exception occurs
- **`else`**: executed IF NO exception occurs → prints `"ok"`
- **`finally`**: **ALWAYS** executed → prints `"fim"`

Since `10 / 2` does not raise an exception, the `else` block executes.

**Concept:** try/except/else/finally blocks — complete flow.

---

### **Question 16**

**Code:**
```python
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z[-1], len(z))
```

**Options:**
- A. `3 6`
- B. `6 3`
- C. `6 6`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
The `+` operator with lists performs **concatenation**:

Execution:
1. `z = x + y` → `[1, 2, 3, 4, 5, 6]`
2. `z[-1]` → last element → `6`
3. `len(z)` → length → `6`

Output: `6 6`

**Concept:** List concatenation with + operator.

---

### **Question 17**

**Code:**
```python
x = "abcdef"
print(x[1::2])
```

**Options:**
- A. `ace`
- B. `abcdef`
- C. `bce`
- D. `bdf`

**✅ Correct Answer: D**

**📚 Explanation:**
Slicing `[start::step]`:
- Starts at index 1 (`b`)
- Goes to the end
- Step 2 (takes every 2nd)

String `"abcdef"`:
- Index 1: `b` ✓
- Index 2: `c` (skipped)
- Index 3: `d` ✓
- Index 4: `e` (skipped)
- Index 5: `f` ✓

Result: `"bdf"`

**Concept:** Slicing with start and step.

---

### **Question 18**

**Code:**
```python
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

print(f(6))
```

**Options:**
- A. `5`
- B. `8`
- C. `13`
- D. `21`

**✅ Correct Answer: B**

**📚 Explanation:**
This is the **Fibonacci sequence** implemented recursively.

Sequence:
- f(0) = 0
- f(1) = 1
- f(2) = f(1) + f(0) = 1 + 0 = 1
- f(3) = f(2) + f(1) = 1 + 1 = 2
- f(4) = f(3) + f(2) = 2 + 1 = 3
- f(5) = f(4) + f(3) = 3 + 2 = 5
- f(6) = f(5) + f(4) = 5 + 3 = **8**

**Concept:** Recursion — Fibonacci.

---

### **Question 19**

**Code:**
```python
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
a.update(b)
print(a)
```

**Options:**
- A. `{'a': 1, 'b': 2, 'c': 4}`
- B. `{'b': 3, 'c': 4}`
- C. `{'a': 1, 'b': 3, 'c': 4}`
- D. `Error`

**✅ Correct Answer: C**

**📚 Explanation:**
The `update()` method **merges** dictionaries:
- Adds new keys
- **Overwrites** existing keys

Execution:
1. `a = {"a": 1, "b": 2}`
2. `a.update({"b": 3, "c": 4})`
   - Adds `"c": 4`
   - Overwrites `"b": 2` → `"b": 3`
3. Result: `{"a": 1, "b": 3, "c": 4}`

**Concept:** dict.update() method — merging dictionaries.

---

### **Question 20**

**Code:**
```python
items = ["a", "b", "c"]
result = list(enumerate(items, start=1))
print(result[1])
```

**Options:**
- A. `(2, 'b')`
- B. `(1, 'a')`
- C. `(0, 'b')`
- D. `(1, 'b')`

**✅ Correct Answer: A**

**📚 Explanation:**
`enumerate(iterable, start=n)` returns tuples (index, value):

Execution:
1. `enumerate(items, start=1)`:
   - `(1, 'a')`
   - `(2, 'b')`
   - `(3, 'c')`
2. `list(...)` → `[(1, 'a'), (2, 'b'), (3, 'c')]`
3. `result[1]` → second element → `(2, 'b')`

**Common usage:** Loop with custom counter:
```python
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

**Concept:** enumerate() function with custom start.

---

## 📊 Concepts Summary

| Concept | Questions |
|---------|-----------|
| Slicing (basic and advanced) | 1, 3, 9, 17 |
| Type hierarchy | 2 |
| Dictionary key equivalence | 4 |
| Function arguments | 5 |
| else clause in loops | 6 |
| String methods | 7 |
| Lambda functions | 8 |
| Scope (global) | 10 |
| String operations | 11 |
| In-place methods | 12 |
| Immutability | 13 |
| Dictionary methods | 14, 19 |
| Exception handling | 15 |
| List concatenation | 16 |
| Recursion | 18 |
| Enumerate | 20 |

---

## 🎯 Difficulty Distribution

- **Basic** (8 questions): 1, 7, 9, 11, 12, 13, 14, 16
- **Intermediate** (8 questions): 3, 5, 6, 10, 15, 17, 19, 20
- **Advanced** (4 questions): 2, 4, 8, 18

---

**🎯 Passing Score:** Minimum 14 correct answers (70%)

**📚 Study Tip:** This mock exam offers a balanced review. Focus on the concepts you find most challenging!

---

## 📖 Additional Resources

### Useful commands to practice:
```python
# Slicing
s = "Python"
print(s[::-1])    # Reverse
print(s[::2])     # Skip elements

# Dictionaries
d = {"a": 1}
d.update({"b": 2})
print(d.get("c", 0))

# Lists
lst = [1, 2, 3]
lst.sort()
lst.reverse()

# Exception handling
try:
    # code
except Exception as e:
    # handle
else:
    # no exception
finally:
    # always executes
```
