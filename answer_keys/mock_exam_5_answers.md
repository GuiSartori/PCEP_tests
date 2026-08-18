# 📝 DETAILED ANSWER KEY - PCEP MOCK EXAM 5 (Hard)

**Difficulty:** Hard (edge cases & pitfalls — harder than the real exam)

## ✅ Quick Answer Key

| Q# | Answer | Concept |
|----|--------|---------|
| 1  | D | += on list (in-place mutation via extend) |
| 2  | A | += on tuple (creates new object, rebinds) |
| 3  | C | Mutable default argument accumulation |
| 4  | D | Float precision (IEEE 754) |
| 5  | B | Slice assignment changes list size |
| 6  | C | Closure captures enclosing scope variable |
| 7  | D | Safe dict deletion iterating over keys copy |
| 8  | B | Late binding in lambda inside loop |
| 9  | A | Truthiness of " " and "0" (non-empty strings) |
| 10 | D | Nested try/except with re-raise |
| 11 | D | Slicing never raises IndexError |
| 12 | C | Positional-only (/) and keyword-only (*) params |
| 13 | C | sort() returns None (in-place) |
| 14 | A | Lists as dict keys → TypeError (unhashable) |
| 15 | B | x = x + [...] rebinds vs += mutates |
| 16 | D | Chained string comparison (lexicographic) |
| 17 | C | Generator next() consumes values |
| 18 | B | Dict unpacking with ** (last wins) |
| 19 | A | String * 0 → empty string (still str type) |
| 20 | A | Tuple unpacking: RHS evaluated before assignment |

## Answer Distribution

- **A**: 5 questions (Q2, Q9, Q14, Q19, Q20)
- **B**: 4 questions (Q5, Q8, Q15, Q18)
- **C**: 5 questions (Q3, Q6, Q12, Q13, Q17)
- **D**: 6 questions (Q1, Q4, Q7, Q10, Q11, Q16)

> **Note:** Distribution is A=5, B=4, C=5, D=6 — slight imbalance. This should be corrected if the exam is regenerated.

---

## 📚 Detailed Explanations

### Q1 — += on List (In-Place Mutation)

```python
x = [1, 2, 3]
y = x
x += [4, 5]
print(y)
```

**✅ Correct Answer: D** — `[1, 2, 3, 4, 5]`

**📚 Explanation:** When you use `+=` on a list, Python calls `list.extend()` internally, which modifies the list **in place**. Since `y` is a reference to the same list object as `x`, the mutation is visible through `y`.

**Key Takeaway:** `+=` on mutable objects (lists) mutates in place; on immutable objects (tuples, strings) it creates a new object.

---

### Q2 — += on Tuple (Creates New Object)

```python
x = (1, 2, 3)
y = x
x += (4, 5)
print(y)
```

**✅ Correct Answer: A** — `(1, 2, 3)`

**📚 Explanation:** Tuples are immutable. `+=` on a tuple creates a **new** tuple `(1,2,3,4,5)` and rebinds `x` to it. `y` still references the original tuple `(1,2,3)`.

**Key Takeaway:** Same operator (`+=`) has different behavior depending on mutability of the object.

---

### Q3 — Mutable Default Argument Accumulation

```python
def f(x=[]):
    x.append(len(x))
    return x

f()
f()
print(f())
```

**✅ Correct Answer: C** — `[0, 1, 2]`

**📚 Explanation:** The default `[]` is created once at function definition time. Each call mutates the same list:
- 1st call: len=0, append(0) → [0]
- 2nd call: len=1, append(1) → [0, 1]
- 3rd call: len=2, append(2) → [0, 1, 2]

**Key Takeaway:** Never use mutable objects as default arguments unless you intend shared state. Use `None` + conditional instead.

---

### Q4 — Float Precision (IEEE 754)

```python
print(0.1 + 0.2 == 0.3)
```

**✅ Correct Answer: D** — `False`

**📚 Explanation:** Floating-point numbers use binary representation (IEEE 754). `0.1 + 0.2` evaluates to `0.30000000000000004`, not exactly `0.3`.

**Key Takeaway:** Never compare floats with `==`. Use `math.isclose()` or compare with a tolerance.

---

### Q5 — Slice Assignment Changes List Size

```python
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30]
print(nums)
```

**✅ Correct Answer: B** — `[1, 20, 30, 5]`

**📚 Explanation:** Slice assignment replaces elements at indices 1, 2, 3 (three elements) with a two-element list `[20, 30]`. The list shrinks from 5 to 4 elements.

**Key Takeaway:** Slice assignment can change the size of a list — the replacement doesn't need to match the slice length.

---

### Q6 — Closure Captures Enclosing Scope

```python
x = 10
def outer():
    x = 20
    def inner():
        print(x)
    return inner

fn = outer()
x = 30
fn()
```

**✅ Correct Answer: C** — `20`

**📚 Explanation:** `inner()` is a closure that captures `x` from `outer()`'s local scope (where `x=20`). Changes to the global `x` don't affect the enclosed `x`.

**Key Takeaway:** Closures capture variables from their enclosing scope (LEGB: Local → Enclosing → Global → Built-in).

---

### Q7 — Safe Dict Deletion with Keys Copy

```python
d = {"a": 1, "b": 2, "c": 3}
keys = list(d.keys())
for k in keys:
    if d[k] % 2 != 0:
        del d[k]
print(d)
```

**✅ Correct Answer: D** — `{'b': 2}`

**📚 Explanation:** By iterating over `list(d.keys())` (a snapshot copy), we can safely delete from `d` during iteration. Odd values (1, 3) are removed, leaving only `'b': 2`.

**Key Takeaway:** Never modify a dict while iterating over it directly. Iterate over a copy of keys instead.

---

### Q8 — Late Binding in Lambda Loop

```python
result = []
for i in range(4):
    result.append(lambda: i)
print([f() for f in result])
```

**✅ Correct Answer: B** — `[3, 3, 3, 3]`

**📚 Explanation:** Lambdas capture the **variable** `i`, not its value at creation time. When called after the loop, `i` has its final value (3). All lambdas return 3.

**Key Takeaway:** To capture the current value, use a default argument: `lambda i=i: i`.

---

### Q9 — Truthiness of Non-Empty Strings

```python
print(bool(""), bool(" "), bool("0"), bool([]))
```

**✅ Correct Answer: A** — `False True True False`

**📚 Explanation:**
- `""` → empty string → False
- `" "` → contains a space character → non-empty → True
- `"0"` → contains character '0' → non-empty → True
- `[]` → empty list → False

**Key Takeaway:** Any non-empty string is truthy, including `" "` and `"0"`. Only `""` is falsy.

---

### Q10 — Nested try/except with Re-raise

```python
try:
    try:
        1 / 0
    except ZeroDivisionError:
        print("inner", end=" ")
        raise ValueError("oops")
except ValueError:
    print("outer", end=" ")
finally:
    print("done")
```

**✅ Correct Answer: D** — `inner outer done`

**📚 Explanation:**
1. Inner try: `1/0` raises ZeroDivisionError → caught → prints "inner"
2. `raise ValueError` propagates to outer try → caught → prints "outer"
3. `finally` always executes → prints "done"

**Key Takeaway:** You can catch one exception and raise a different one. `finally` runs regardless.

---

### Q11 — Slicing Never Raises IndexError

```python
x = "python"
print(x[100:200])
```

**✅ Correct Answer: D** — `'' (empty string)`

**📚 Explanation:** Slicing gracefully handles out-of-range indices by clamping them to the sequence boundaries. Result is an empty string.

**Key Takeaway:** `x[100]` raises IndexError, but `x[100:200]` returns `''`. Slicing is forgiving, indexing is strict.

---

### Q12 — Positional-Only and Keyword-Only Parameters

```python
def f(a, b, /, c, *, d):
    return a + b + c + d

print(f(1, 2, c=3, d=4))
```

**✅ Correct Answer: C** — `10`

**📚 Explanation:**
- `/` makes `a`, `b` positional-only (cannot use `a=1`)
- `*` makes `d` keyword-only (must use `d=4`)
- `c` can be either positional or keyword
- `1 + 2 + 3 + 4 = 10`

**Key Takeaway:** `/` separates positional-only params (left); `*` separates keyword-only params (right).

---

### Q13 — sort() Returns None

```python
nums = [5, 3, 8, 1, 9]
result = nums.sort()
print(result)
```

**✅ Correct Answer: C** — `None`

**📚 Explanation:** `list.sort()` sorts the list **in place** and returns `None`. If you need a sorted copy, use `sorted(nums)`.

**Key Takeaway:** In-place methods (`sort()`, `reverse()`, `append()`) return `None`. They modify the object directly.

---

### Q14 — Lists as Dict Keys (Unhashable)

```python
d = {}
d[(1, 2)] = "ok"
d[[1, 2]] = "fail"
```

**✅ Correct Answer: A** — `TypeError: unhashable type: 'list'`

**📚 Explanation:** Dictionary keys must be hashable. Tuples are hashable (immutable), lists are not (mutable). Using a list as a key raises TypeError.

**Key Takeaway:** Only immutable, hashable types can be dict keys: int, float, str, tuple (with hashable elements), frozenset.

---

### Q15 — x = x + [...] Rebinds vs += Mutates

```python
x = [1, 2, 3]
y = x
x = x + [4, 5]
print(y)
```

**✅ Correct Answer: B** — `[1, 2, 3]`

**📚 Explanation:** `x = x + [4, 5]` creates a **new list** and rebinds `x` to it. The original list (still referenced by `y`) is unchanged.

**Key Takeaway:** `x += [...]` mutates in place (extend). `x = x + [...]` creates a new list (rebind). Different behavior!

---

### Q16 — Chained String Comparison

```python
print("ab" < "abc" < "b")
```

**✅ Correct Answer: D** — `True`

**📚 Explanation:** Python evaluates chained comparisons as `("ab" < "abc") and ("abc" < "b")`:
- `"ab" < "abc"` → True (prefix is always smaller)
- `"abc" < "b"` → True (first char 'a' < 'b')
- Both True → result is True

**Key Takeaway:** String comparison is lexicographic (character by character). A shorter prefix is always "less than" a longer string with the same prefix.

---

### Q17 — Generator next() Consumes Values

```python
def gen():
    yield 10
    yield 20
    yield 30

g = gen()
next(g)
next(g)
print(next(g))
```

**✅ Correct Answer: C** — `30`

**📚 Explanation:** Each `next()` call advances the generator to the next `yield`:
- 1st `next(g)` → yields 10 (discarded)
- 2nd `next(g)` → yields 20 (discarded)
- 3rd `next(g)` → yields 30 (printed)

**Key Takeaway:** Generators are lazy iterators — values are consumed one at a time and can't be "rewound."

---

### Q18 — Dict Unpacking with **

```python
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z["b"], len(z))
```

**✅ Correct Answer: B** — `3 3`

**📚 Explanation:** Dict unpacking merges dictionaries. When keys collide, the **last** one wins. `"b"` appears in both — `y`'s value (3) overwrites `x`'s (2). Total unique keys: a, b, c → len=3.

**Key Takeaway:** `{**d1, **d2}` merges dicts; later dicts overwrite earlier ones for duplicate keys.

---

### Q19 — String Multiplication by 0

```python
type("abc" * 0)  # and
len("abc" * 0)
```

**✅ Correct Answer: A** — `<class 'str'> and 0`

**📚 Explanation:** `"abc" * 0` produces an empty string `""`. It's still of type `str`, just with length 0.

**Key Takeaway:** Multiplying a string by 0 gives an empty string (not None, not error). The type is preserved.

---

### Q20 — Tuple Unpacking: RHS Evaluated First

```python
a, b = 1, 2
a, b = b, a + b
print(a, b)
```

**✅ Correct Answer: A** — `2 3`

**📚 Explanation:** Python evaluates the entire right-hand side **before** any assignment:
- RHS: `b` = 2, `a + b` = 1 + 2 = 3 → tuple (2, 3)
- Then assigns: `a = 2`, `b = 3`

**Key Takeaway:** In tuple unpacking, the RHS is fully evaluated with the original values before any LHS assignment occurs.

---

## 📊 Concepts Summary

| Concept | Questions |
|---------|-----------|
| In-place mutation vs rebinding | 1, 2, 15 |
| Mutable default arguments | 3 |
| Floating-point precision | 4 |
| Slice assignment | 5 |
| Closures and scope | 6 |
| Safe dict iteration | 7 |
| Late binding | 8 |
| Truthiness/falsiness | 9 |
| Nested exceptions | 10 |
| Slicing vs indexing | 11 |
| Advanced function parameters | 12 |
| In-place methods | 13 |
| Hashability | 14 |
| String comparison | 16 |
| Generators | 17 |
| Dict unpacking | 18 |
| String operations | 19 |
| Tuple unpacking | 20 |

---

**🎯 Passing Score:** Minimum 14 correct answers (70%)

**📚 Study Tip:** This mock exam is harder than the real test! If you score 70%+ here, you're well-prepared for the PCEP.
