# Bitwise Operators — PCEP-30-02 Study Guide

## What Are Bitwise Operators?

Bitwise operators work on the **binary (base-2) representation** of integers, manipulating individual bits. Python has 6 bitwise operators:

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | 1 only if BOTH bits are 1 |
| `\|` | OR | 1 if EITHER bit is 1 |
| `^` | XOR | 1 if bits are DIFFERENT |
| `~` | NOT | Flips all bits (inverts) |
| `<<` | Left shift | Shifts bits left (multiplies by 2ⁿ) |
| `>>` | Right shift | Shifts bits right (divides by 2ⁿ) |

---

## Converting Decimal to Binary (Mental Math)

Powers of 2 to memorize:

```
2⁰ = 1
2¹ = 2
2² = 4
2³ = 8
2⁴ = 16
2⁵ = 32
2⁶ = 64
2⁷ = 128
```

To convert a number to binary, find which powers of 2 sum to it:

```
13 = 8 + 4 + 1 = 2³ + 2² + 2⁰ → 1101
 7 = 4 + 2 + 1 = 2² + 2¹ + 2⁰ → 0111
10 = 8 + 2     = 2³ + 2¹       → 1010
 5 = 4 + 1     = 2² + 2⁰       → 0101
 3 = 2 + 1     = 2¹ + 2⁰       → 0011
 6 = 4 + 2     = 2² + 2¹       → 0110
```

Python helper: `bin(13)` → `'0b1101'`

---

## Operator 1: AND (`&`)

**Rule:** Result bit is 1 only if BOTH input bits are 1.

```
Truth table:
  0 & 0 = 0
  0 & 1 = 0
  1 & 0 = 0
  1 & 1 = 1    ← only case that produces 1
```

**Example:** `5 & 3`

```
  5 = 101
  3 = 011
  -------
  &   001 = 1
```

**Use case:** Masking — extracting specific bits from a number.

---

## Operator 2: OR (`|`)

**Rule:** Result bit is 1 if EITHER (or both) input bits are 1.

```
Truth table:
  0 | 0 = 0    ← only case that produces 0
  0 | 1 = 1
  1 | 0 = 1
  1 | 1 = 1
```

**Example:** `5 | 3`

```
  5 = 101
  3 = 011
  -------
  |   111 = 7
```

**Use case:** Setting (turning on) specific bits.

---

## Operator 3: XOR (`^`)

**Rule:** Result bit is 1 if the bits are DIFFERENT.

```
Truth table:
  0 ^ 0 = 0
  0 ^ 1 = 1
  1 ^ 0 = 1
  1 ^ 1 = 0    ← same bits cancel out
```

**Example:** `5 ^ 3`

```
  5 = 101
  3 = 011
  -------
  ^   110 = 6
```

**Special property:** `x ^ x = 0` (any number XORed with itself is 0)

---

## Operator 4: NOT (`~`)

**Rule:** Flips every bit. In Python, `~x = -(x + 1)` due to two's complement representation.

```
~0  = -1
~1  = -2
~5  = -6
~-1 = 0
```

**Formula:** `~x = -(x + 1)`

**Why?** Python uses two's complement for negative numbers, so flipping all bits of `x` gives `-(x+1)`.

---

## Operator 5: Left Shift (`<<`)

**Rule:** Shifts all bits left by n positions. Empty positions filled with 0.

**Effect:** Multiplies by 2ⁿ.

```
5 << 1:
  5  = 101
  << 1010 = 10    (5 × 2 = 10)

5 << 2:
  5  = 101
  << 10100 = 20   (5 × 4 = 20)

3 << 3:
  3  = 11
  << 11000 = 24   (3 × 8 = 24)
```

**Quick formula:** `x << n = x × 2ⁿ`

---

## Operator 6: Right Shift (`>>`)

**Rule:** Shifts all bits right by n positions. Bits that fall off are discarded.

**Effect:** Integer divides by 2ⁿ (floor division).

```
10 >> 1:
  10 = 1010
  >>  0101 = 5    (10 // 2 = 5)

20 >> 2:
  20 = 10100
  >>   00101 = 5  (20 // 4 = 5)

7 >> 1:
  7  = 111
  >>  011 = 3     (7 // 2 = 3, the last bit is lost)
```

**Quick formula:** `x >> n = x // 2ⁿ`

---

## Precedence (from highest to lowest)

```
~       (NOT — unary, highest)
<<  >>  (shifts)
&       (AND)
^       (XOR)
|       (OR — lowest among bitwise)
```

Within expressions with arithmetic:
```
**  >  ~ (unary)  >  * / // %  >  + -  >  << >>  >  &  >  ^  >  |  >  comparisons  >  not  >  and  >  or
```

---

## Common Patterns for the PCEP Exam

### Pattern 1: Determine the result of a bitwise expression

```python
# Convert both to binary, apply operator, convert back
print(12 & 10)   # 1100 & 1010 = 1000 = 8
print(12 | 10)   # 1100 | 1010 = 1110 = 14
print(12 ^ 10)   # 1100 ^ 1010 = 0110 = 6
```

### Pattern 2: Shift as multiply/divide

```python
print(1 << 4)    # 1 × 2⁴ = 16
print(32 >> 3)   # 32 // 2³ = 4
```

### Pattern 3: NOT with formula

```python
print(~7)        # -(7+1) = -8
print(~0)        # -(0+1) = -1
print(~-5)       # -(-5+1) = 4
```

---

## Practice Exercises

Solve each one mentally first, then verify with Python.

### Exercise 1: Basic AND

```python
# What is the output?
print(7 & 5)
```

<details>
<summary>Answer</summary>

```
7 = 111
5 = 101
&   101 = 5
```
Answer: **5**
</details>

---

### Exercise 2: Basic OR

```python
# What is the output?
print(6 | 3)
```

<details>
<summary>Answer</summary>

```
6 = 110
3 = 011
|   111 = 7
```
Answer: **7**
</details>

---

### Exercise 3: XOR

```python
# What is the output?
print(9 ^ 5)
```

<details>
<summary>Answer</summary>

```
9 = 1001
5 = 0101
^   1100 = 12
```
Answer: **12**
</details>

---

### Exercise 4: NOT

```python
# What is the output?
print(~3)
```

<details>
<summary>Answer</summary>

`~3 = -(3+1) = -4`

Answer: **-4**
</details>

---

### Exercise 5: Left Shift

```python
# What is the output?
print(3 << 4)
```

<details>
<summary>Answer</summary>

`3 × 2⁴ = 3 × 16 = 48`

Answer: **48**
</details>

---

### Exercise 6: Right Shift

```python
# What is the output?
print(100 >> 3)
```

<details>
<summary>Answer</summary>

`100 // 2³ = 100 // 8 = 12`

Answer: **12**
</details>

---

### Exercise 7: Combined Expression

```python
# What is the output?
x = 12
print(x >> 2 & 3)
```

<details>
<summary>Answer</summary>

Precedence: `>>` before `&`.
1. `12 >> 2` = 12 // 4 = 3
2. `3 & 3` = 3

Answer: **3**
</details>

---

### Exercise 8: OR then shift

```python
# What is the output?
print((5 | 2) << 1)
```

<details>
<summary>Answer</summary>

1. `5 | 2`: 101 | 010 = 111 = 7
2. `7 << 1`: 7 × 2 = 14

Answer: **14**
</details>

---

### Exercise 9: XOR self-canceling

```python
# What is the output?
a = 42
print(a ^ a)
```

<details>
<summary>Answer</summary>

Any number XORed with itself = 0.

Answer: **0**
</details>

---

### Exercise 10: Multi-operator

```python
# What is the output?
a = 0b1100   # 12
b = 0b1010   # 10
print(a & b, a | b, a ^ b)
```

<details>
<summary>Answer</summary>

```
a = 1100
b = 1010
& = 1000 = 8
| = 1110 = 14
^ = 0110 = 6
```
Answer: **8 14 6**
</details>

---

### Exercise 11: Negative NOT

```python
# What is the output?
print(~(-10))
```

<details>
<summary>Answer</summary>

`~(-10) = -(-10 + 1) = -(-9) = 9`

Answer: **9**
</details>

---

### Exercise 12: Chained shifts

```python
# What is the output?
print(2 << 3 >> 1)
```

<details>
<summary>Answer</summary>

Left-to-right (same precedence):
1. `2 << 3` = 2 × 8 = 16
2. `16 >> 1` = 16 // 2 = 8

Answer: **8**
</details>

---

## Quick Reference Card (for exam day)

```
AND (&):  Only 1s survive        → makes numbers smaller or equal
OR  (|):  All 1s combined        → makes numbers bigger or equal
XOR (^):  Different bits = 1     → x^x=0, x^0=x
NOT (~):  ~x = -(x+1)           → flips sign and subtracts 1
<<  :     x << n = x * 2^n      → shift left = multiply by power of 2
>>  :     x >> n = x // 2^n     → shift right = divide by power of 2
```

**Exam tip:** When you see a bitwise question, immediately convert both numbers to binary (4-bit is usually enough), apply the truth table column by column, then convert back to decimal.
