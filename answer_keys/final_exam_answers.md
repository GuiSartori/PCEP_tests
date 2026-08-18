# PCEP Final Exam — Answer Key & Explanations

**Format:** 30 questions · 40 minutes · Mirrors actual PCEP-30-02

## Quick Answer Key

| Q# | Answer | Block | Concept |
|----|--------|-------|---------|
| 1  | C | 1 | Scientific notation (2.5e3) |
| 2  | B | 1 | Binary/Octal/Hex literals |
| 3  | A | 1 | print() with sep and end |
| 4  | D | 1 | input() always returns str |
| 5  | D | 1 | Augmented assignment (//= and **=) |
| 6  | A | 1 | Chained relational operators |
| 7  | B | 1 | Bitwise operators (>> and &) |
| 8  | C | 2 | Nested if with boolean logic |
| 9  | B | 2 | while loop counter pattern |
| 10 | A | 2 | for loop with negative step |
| 11 | D | 2 | continue + break in while |
| 12 | C | 2 | Loop else clause (skipped by break) |
| 13 | A | 2 | Nested for building triangle pattern |
| 14 | D | 2 | range(1,10,2) with break |
| 15 | C | 2 | while True with break |
| 16 | B | 3 | list.pop(index) |
| 17 | D | 3 | List comprehension with filter |
| 18 | C | 3 | str.join() method |
| 19 | A | 3 | Negative indexing |
| 20 | B | 3 | dict.update() |
| 21 | D | 3 | Tuple element-by-element comparison |
| 22 | C | 3 | del on list slice |
| 23 | D | 4 | Function with *args |
| 24 | A | 4 | Function returning None implicitly |
| 25 | B | 4 | global keyword |
| 26 | C | 4 | Recursive factorial |
| 27 | A | 4 | Multiple except clauses (ValueError, TypeError) |
| 28 | D | 4 | try/finally without except |
| 29 | B | 4 | lambda with filter() |
| 30 | C | 4 | Scope shadowing (LEGB) |

## Answer Distribution

- **A**: 7 questions (Q3, Q6, Q10, Q13, Q19, Q24, Q27)
- **B**: 7 questions (Q2, Q7, Q9, Q16, Q20, Q25, Q29)
- **C**: 8 questions (Q1, Q8, Q12, Q15, Q18, Q22, Q26, Q30)
- **D**: 8 questions (Q4, Q5, Q11, Q14, Q17, Q21, Q23, Q28)

## Block Distribution

| Block | Questions | Count | Official Weight |
|-------|-----------|-------|-----------------|
| 1 - Fundamentals | Q1–Q7 | 7 | 18% |
| 2 - Control Flow | Q8–Q15 | 8 | 29% |
| 3 - Data Collections | Q16–Q22 | 7 | 25% |
| 4 - Functions & Exceptions | Q23–Q30 | 8 | 28% |

---

## Detailed Explanations

### Q1 — Scientific Notation
```python
x = 2.5e3
print(x)
```
**Answer: C** — `2500.0`

2.5e3 = 2.5 × 10³ = 2500.0. The `e` notation always produces a float.

**Key Takeaway:** `XeY` means X × 10^Y. Result is always float.

---

### Q2 — Binary/Octal/Hex Literals
```python
a = 0b1010  # binary
b = 0o12    # octal
c = 0xA     # hex
print(a == b == c)
```
**Answer: B** — `True`

All three represent the decimal number 10. Python evaluates them as equal integers.

**Key Takeaway:** `0b` = binary, `0o` = octal, `0x` = hex. They're just different ways to write integers.

---

### Q3 — print(sep/end)
```python
print("A", "B", "C", sep="-", end="!")
print("D")
```
**Answer: A** — `A-B-C!D`

sep="-" joins with dashes, end="!" replaces the newline. Next print starts right after "!", outputting "D" on the same line.

---

### Q4 — input() Returns str
**Answer: D** — `str`

`input()` always returns a string. Even if the user types `42`, the result is `"42"` not `42`.

---

### Q5 — Augmented Assignment
```python
x = 17
x //= 3  # 17 // 3 = 5
x **= 2  # 5 ** 2 = 25
```
**Answer: D** — `25`

---

### Q6 — Chained Comparisons
```python
x = 5
print(2 < x < 8)    # (2<5) and (5<8) → True
print(1 < x > 3)    # (1<5) and (5>3) → True
```
**Answer: A** — `True\nTrue`

Python allows chaining: `a < b < c` is equivalent to `(a < b) and (b < c)`.

---

### Q7 — Bitwise Operators
```python
x = 12  # binary: 1100
x >> 2  # shift right 2: 0011 = 3
x & 5   # 1100 & 0101 = 0100 = 4
```
**Answer: B** — `3 4`

---

### Q8 — Nested if with Boolean
```python
age = 25, has_id = False
# age >= 18 and has_id → True and False → False (first fails)
# elif age >= 18 → True → "need ID"
```
**Answer: C** — `need ID`

---

### Q9 — while Counter
```python
# count increments BEFORE adding to total
# Adds: 1+2+3+4+5 = 15
```
**Answer: B** — `15`

---

### Q10 — Negative Step Range
```python
range(10, 0, -3)  # 10, 7, 4, 1 (stops before 0)
```
**Answer: A** — `10 7 4 1`

---

### Q11 — continue + break in while
```python
# Skips even i, breaks when i > 7
# Prints odd numbers: 1, 3, 5, 7 (9 is odd but i>7 triggers break)
```
**Answer: D** — `1 3 5 7`

---

### Q12 — Loop else (skipped by break)
```python
# break at n=4 → else does NOT run
# print(n) → 4
```
**Answer: C** — `4`

---

### Q13 — Nested for Triangle
```python
# i=0: 1 star, i=1: 2 stars, i=2: 3 stars
```
**Answer: A** — `*\n**\n***`

---

### Q14 — range + break
```python
range(1, 10, 2)  # 1, 3, 5, 7, 9
# x=7: 7>6 → break. Only [1, 3, 5] appended.
```
**Answer: D** — `[1, 3, 5]`

---

### Q15 — while True + break
```python
# x: 2, 4, 6. When x=6: x>=6 → found=True, break
```
**Answer: C** — `6 True`

---

### Q16 — list.pop(index)
```python
items.pop(2)  # removes index 2 (value 30), returns it
```
**Answer: B** — `30 [10, 20, 40, 50]`

---

### Q17 — List Comprehension with Filter
```python
# Filter: x%2==0 keeps 2,4,6,8. Then *2: [4, 8, 12, 16]
```
**Answer: D** — `[4, 8, 12, 16]`

---

### Q18 — str.join()
```python
" | ".join(["hello", "world", "python"])
# → "hello | world | python"
```
**Answer: C** — `hello | world | python`

---

### Q19 — Negative Indexing
```python
data[-3] = 30 (third from end)
data[-1] = 50 (last)
```
**Answer: A** — `30 50`

---

### Q20 — dict.update()
```python
# Overwrites 'age' to 31, adds 'city'. Total: 3 keys.
```
**Answer: B** — `3 31`

---

### Q21 — Tuple Comparison
```python
(1, 5, 3) > (1, 5, 2)
# Compare element by element: 1==1, 5==5, 3>2 → True
```
**Answer: D** — `True`

---

### Q22 — del on Slice
```python
del data[2:5]  # removes indices 2,3,4 → values 2,3,4
# Remaining: [0, 1, 5, 6, 7]
```
**Answer: C** — `[0, 1, 5, 6, 7]`

---

### Q23 — *args
```python
# *args collects into tuple: (1,2,3,4). sum() = 10
```
**Answer: D** — `10`

---

### Q24 — Implicit None Return
```python
# greet() prints "Hi, Eve" but returns None
# print(result) → None
```
**Answer: A** — `Hi, Eve\nNone`

---

### Q25 — global Keyword
```python
# global counter allows modification. Two calls: 0+5+5 = 10
```
**Answer: B** — `10`

---

### Q26 — Recursive Factorial
```python
# 5! = 5×4×3×2×1 = 120
```
**Answer: C** — `120`

---

### Q27 — Multiple except
```python
# int("hello") → ValueError. Caught by first except clause (ValueError).
```
**Answer: A** — `caught`

---

### Q28 — try/finally without except
```python
# finally executes BEFORE return delivers the value
# Output: cleanup (from finally), then 5.0 (from print(result))
```
**Answer: D** — `cleanup\n5.0`

---

### Q29 — lambda + filter
```python
# filter keeps elements where x%3==0: 3 and 6
```
**Answer: B** — `[3, 6]`

---

### Q30 — Scope Shadowing
```python
# inner has local x=30, outer has local x=20, global x=10
# Each print sees its own scope's x
```
**Answer: C** — `30 20 10`

**Key Takeaway:** Each function scope creates its own variable. Inner scopes don't affect outer ones unless using `global` or `nonlocal`.
