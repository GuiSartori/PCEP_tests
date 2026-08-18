# PCEP Mock Exam 5 — Answer Key & Explanations

**Difficulty:** Realistic (calibrated to actual PCEP-30-02 exam level)

## Quick Answer Key

| Q# | Answer | Block | Concept |
|----|--------|-------|---------|
| 1  | C | 1 | Operator precedence (**, %, +, -) |
| 2  | D | 1 | Floor division (//) and modulo (%) |
| 3  | B | 1 | String * precedence over + |
| 4  | A | 1 | Type casting with int() — truncation |
| 5  | B | 1 | Boolean and operator |
| 6  | A | 1 | Bitwise OR operator |
| 7  | A | 2 | if/elif/else branching |
| 8  | C | 2 | while loop — final value of counter |
| 9  | D | 2 | for loop sum with range() |
| 10 | B | 2 | break exits loop immediately |
| 11 | A | 2 | Nested loop iteration count |
| 12 | C | 3 | List positive and negative indexing |
| 13 | D | 3 | List slicing (exclusive end) |
| 14 | A | 3 | list.insert() method |
| 15 | B | 3 | dict.keys() method |
| 16 | C | 3 | Tuple concatenation and len() |
| 17 | D | 3 | str.split() — element count |
| 18 | B | 4 | Function return value |
| 19 | D | 4 | Local vs global scope |
| 20 | C | 4 | try/except ValueError |

## Answer Distribution

- **A**: 5 questions (Q4, Q6, Q7, Q11, Q14)
- **B**: 5 questions (Q3, Q5, Q10, Q15, Q18)
- **C**: 5 questions (Q1, Q8, Q12, Q16, Q20)
- **D**: 5 questions (Q2, Q9, Q13, Q17, Q19)

## Block Coverage

| Block | Questions | Weight on Real Exam |
|-------|-----------|-------------------|
| 1 - Fundamentals | Q1–Q6 (6 questions) | 18% |
| 2 - Control Flow | Q7–Q11 (5 questions) | 29% |
| 3 - Data Collections | Q12–Q17 (6 questions) | 25% |
| 4 - Functions & Exceptions | Q18–Q20 (3 questions) | 28% |

---

## Detailed Explanations

### Q1 — Operator Precedence

```python
print(2 ** 3 + 5 % 3 - 1)
```

**Correct Answer: C** — `9`

**Step-by-step:**
1. `**` first: 2³ = 8
2. `%` next: 5 % 3 = 2
3. Left-to-right: 8 + 2 - 1 = 9

**Key Takeaway:** Precedence order: `**` > `* / // %` > `+ -`

---

### Q2 — Floor Division and Modulo

```python
x = 15
print(x // 4, x % 4)
```

**Correct Answer: D** — `3 3`

**Step-by-step:**
- 15 // 4 = 3 (rounds down to nearest integer)
- 15 % 4 = 3 (remainder: 15 - 4×3 = 3)

**Key Takeaway:** `//` gives the quotient, `%` gives the remainder. Together they fully decompose a division.

---

### Q3 — String Operator Precedence

```python
x = "ab" + "cd" * 2
print(x)
```

**Correct Answer: B** — `abcdcd`

**Step-by-step:**
1. `*` has higher precedence: "cd" * 2 = "cdcd"
2. Then `+`: "ab" + "cdcd" = "abcdcd"

**Key Takeaway:** String `*` (repetition) binds tighter than `+` (concatenation), just like numeric operators.

---

### Q4 — Type Casting with int()

```python
x = int(3.7) + int("5")
print(x)
```

**Correct Answer: A** — `8`

**Step-by-step:**
- `int(3.7)` = 3 (truncates toward zero, does NOT round)
- `int("5")` = 5
- 3 + 5 = 8

**Key Takeaway:** `int()` truncates floats (removes decimal part). It does not round.

---

### Q5 — Boolean Operators

```python
x = 5
y = 10
print(x > 3 and y < 8)
```

**Correct Answer: B** — `False`

**Step-by-step:**
- x > 3 → 5 > 3 → True
- y < 8 → 10 < 8 → False
- True and False → False

**Key Takeaway:** `and` requires BOTH operands to be True. One False makes the whole expression False.

---

### Q6 — Bitwise OR

```python
x = 5
y = 3
print(x | y)
```

**Correct Answer: A** — `7`

**Step-by-step:**
- 5 in binary: 101
- 3 in binary: 011
- OR: 111 = 7

**Key Takeaway:** `|` (OR) sets a bit to 1 if EITHER operand has a 1 in that position.

---

### Q7 — if/elif/else

```python
x = 7
if x > 10:
    print("high")
elif x > 5:
    print("mid")
else:
    print("low")
```

**Correct Answer: A** — `mid`

**Step-by-step:**
- 7 > 10? No
- 7 > 5? Yes → print "mid" and stop

**Key Takeaway:** elif branches are checked in order; only the FIRST true branch executes.

---

### Q8 — while Loop Final Value

```python
x = 0
while x < 4:
    x += 1
print(x)
```

**Correct Answer: C** — `4`

**Step-by-step:**
- x: 0→1→2→3→4
- At x=4: condition 4 < 4 is False → exit
- print(x) → 4

**Key Takeaway:** The variable retains its final value after the loop exits.

---

### Q9 — for Loop Sum

```python
total = 0
for i in range(1, 5):
    total += i
print(total)
```

**Correct Answer: D** — `10`

**Step-by-step:**
- range(1, 5) produces: 1, 2, 3, 4
- Sum: 1 + 2 + 3 + 4 = 10

**Key Takeaway:** `range(start, stop)` — stop is EXCLUSIVE. range(1,5) does NOT include 5.

---

### Q10 — break Statement

```python
for i in range(1, 6):
    if i % 3 == 0:
        break
    print(i, end=" ")
```

**Correct Answer: B** — `1 2`

**Step-by-step:**
- i=1: 1%3=1 ≠ 0 → print 1
- i=2: 2%3=2 ≠ 0 → print 2
- i=3: 3%3=0 → break (exits immediately)

**Key Takeaway:** `break` exits the loop entirely. Code after break in the loop body doesn't execute.

---

### Q11 — Nested Loop Count

```python
count = 0
for i in range(3):
    for j in range(2):
        count += 1
print(count)
```

**Correct Answer: A** — `6`

**Explanation:** Outer: 3 iterations × Inner: 2 iterations = 6 total increments.

**Key Takeaway:** Nested loops multiply: outer_count × inner_count = total iterations.

---

### Q12 — List Indexing

```python
nums = [10, 20, 30, 40, 50]
print(nums[1] + nums[-1])
```

**Correct Answer: C** — `70`

**Step-by-step:**
- nums[1] = 20 (index 1, second element)
- nums[-1] = 50 (last element)
- 20 + 50 = 70

**Key Takeaway:** Negative indices count from the end. -1 is last, -2 is second-to-last, etc.

---

### Q13 — List Slicing

```python
data = [1, 2, 3, 4, 5, 6]
print(data[2:5])
```

**Correct Answer: D** — `[3, 4, 5]`

**Step-by-step:**
- Indices 2, 3, 4 (5 is exclusive)
- Values at those indices: 3, 4, 5

**Key Takeaway:** `list[start:end]` — start is inclusive, end is exclusive.

---

### Q14 — list.insert()

```python
my_list = [3, 1, 4, 1, 5]
my_list.insert(2, 99)
print(my_list)
```

**Correct Answer: A** — `[3, 1, 99, 4, 1, 5]`

**Explanation:** insert(index, value) places the value AT that index, shifting everything else right.

**Key Takeaway:** `insert(i, x)` — x goes at position i; existing elements move right.

---

### Q15 — dict.keys()

```python
data = {"Peter": 30, "Paul": 31}
print(list(data.keys()))
```

**Correct Answer: B** — `['Peter', 'Paul']`

**Explanation:** `keys()` returns a view of dictionary keys. `list()` converts it to a list.

**Key Takeaway:** `keys()` → keys, `values()` → values, `items()` → (key, value) tuples.

---

### Q16 — Tuple Concatenation

```python
t1 = (1, 2, 3)
t2 = t1 + (4, 5)
print(len(t2))
```

**Correct Answer: C** — `5`

**Explanation:** Tuples support `+` for concatenation. (1,2,3) + (4,5) = (1,2,3,4,5). Length = 5.

**Key Takeaway:** Tuples are immutable but support concatenation (creates a new tuple).

---

### Q17 — str.split()

```python
s = "Hello, World!"
parts = s.split(",")
print(len(parts))
```

**Correct Answer: D** — `2`

**Explanation:** Splitting "Hello, World!" at "," produces ['Hello', ' World!'] — 2 elements.

**Key Takeaway:** split(delimiter) divides the string at each occurrence of the delimiter.

---

### Q18 — Function Return

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result * 2)
```

**Correct Answer: B** — `14`

**Step-by-step:**
- add(3, 4) returns 7
- 7 * 2 = 14

**Key Takeaway:** `return` sends a value back to the caller. That value can be used in expressions.

---

### Q19 — Local vs Global Scope

```python
x = 5
def modify():
    x = 10
    return x

modify()
print(x)
```

**Correct Answer: D** — `5`

**Explanation:** `x = 10` inside the function creates a LOCAL variable. The global `x` is unchanged. The function's return value is not captured.

**Key Takeaway:** Assignment inside a function creates a local variable by default. Use `global` to modify the global.

---

### Q20 — try/except

```python
try:
    value = int("hello")
except ValueError:
    value = -1
print(value)
```

**Correct Answer: C** — `-1`

**Explanation:** `int("hello")` raises ValueError. The except block catches it and assigns -1 to value.

**Key Takeaway:** `except ExceptionType:` catches only that specific exception type. Code continues normally after the except block.
