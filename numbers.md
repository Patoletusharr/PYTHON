# 🔢 Numbers in Python – Internal Working (In Depth)

This document explains **how numbers work internally in Python**, how Python relies on **C/C++ under the hood**, operator behavior, precision handling, and representation using `repr`, `str`, and `print`.

---

## 1️⃣ Numbers Are Objects in Python

In Python, **everything is an object**, including numbers.

```python
x = 10
```

Internally:

```
x ──► int object (10)
```

This is different from C/C++ where:

* Variables directly store values
* Memory layout is fixed by data type (`int`, `float`, etc.)

Python stores **numbers as heap objects** with metadata.

---

## 2️⃣ Most Data Types Behave Like Numbers

Many Python objects support **numeric-like behavior** using magic methods.

Examples:

```python
"chai" * 3
```

```
'chaichaichai'
```

```python
[1,2] * 2
```

```
[1, 2, 1, 2]
```

Why this works:

* Python calls internal methods like `__mul__()`
* Objects decide how `*`, `+`, etc. behave

📌 Operators are **method calls**, not hard-coded math.

---

## 3️⃣ Python vs C / C++ (Foundation Difference)

### C / C++

* Variables store raw values
* Data types have fixed memory size
* Arithmetic happens directly on CPU registers

### Python

* Python is written in **C (CPython)**
* Python integers, floats, strings are **C structures**
* Python uses C APIs to perform operations

Flow:

```
Python code
   ↓
C API calls (CPython)
   ↓
CPU execution
```

Python acts as a **high-level interface over C**.

---

## 4️⃣ Arithmetic Operators & Precedence

Supported operators:

* `+`  Addition
* `-`  Subtraction
* `*`  Multiplication
* `/`  True division
* `**` Power
* `%`  Modulus

### Operator Precedence

```python
x + y * z
```

Internally evaluated as:

```python
x + (y * z)
```

Example:

```python
x = 2
y = 3
z = 4
x + y * z
```

Result:

```
14
```

Why?

* `*` has higher precedence than `+`

---

## 5️⃣ Power & Large Numbers

```python
2 ** 400
```

* Python supports **arbitrarily large integers**
* No overflow like C/C++
* Limited only by memory

Internally:

* Uses dynamic memory allocation
* Handled by CPython's `PyLongObject`

---

## 6️⃣ Floating Point Precision Problem

```python
result = 1 / 3
result
```

Output:

```
0.3333333333333333
```

### Why This Happens

* Python uses **IEEE 754 double-precision floats**
* Same as C/C++ `double`
* Cannot represent some fractions exactly in binary

---

## 7️⃣ Handling Precision Correctly

### Using `round()`

```python
round(1/3, 2)
```

```
0.33
```

### Using `decimal` Module

```python
from decimal import Decimal, getcontext
getcontext().prec = 10
Decimal(1) / Decimal(3)
```

* Higher precision
* Slower but accurate
* Used in finance

---

## 8️⃣ `repr()` vs `str()` vs `print()`

```python
repr('chai')
```

```
"'chai'"
```

```python
str('chai')
```

```
'chai'
```

```python
print('chai')
```

```
chai
```

### Internal Meaning

| Function  | Purpose                       |
| --------- | ----------------------------- |
| `repr()`  | Unambiguous, developer-facing |
| `str()`   | Readable, user-facing         |
| `print()` | Calls `str()` internally      |

📌 `repr()` is used in debugging and REPL.

---

## 9️⃣ How Operators Are Actually Methods

```python
x + y
```

Internally:

```python
x.__add__(y)
```

This is why:

* Custom objects can override operators
* Python is highly extensible

---

## 🔑 Key Takeaways

* Numbers are full objects in Python
* Python delegates heavy work to C APIs
* Operators are method calls
* Python avoids overflow but trades speed
* Floating-point precision is a binary limitation
* `repr` and `str` serve different audiences

---

## 🔟 Math Functions: floor vs trunc

```python
import math
math.floor(3.7)    # 3
math.trunc(3.7)    # 3
math.trunc(-3.7)   # -3
math.floor(-3.7)   # -4
```

### Explanation

* `trunc()` removes the decimal part (towards zero)
* `floor()` always rounds **down** (towards −∞)

---

## 1️⃣1️⃣ Floating Point & Scientific Notation

```python
333333333333333333 * 2.1
```

```
7e+17
```

* Python may display large floats in **scientific notation**
* Actual value is approximate due to float precision

---

## 1️⃣2️⃣ Power, Integers & Complex Numbers

```python
2 * 200
2 ** 200
```

* `*` → multiplication
* `**` → exponentiation

```python
2 + 1j
2 + 1j * 3
(2 + 1j) * 3
```

### Explanation

* `j` represents imaginary unit
* Operator precedence applies (`*` before `+`)

---

## 1️⃣3️⃣ Binary, Octal & Hexadecimal Numbers

### What They Are

* **Binary (base 2)** → 0,1
* **Octal (base 8)** → 0–7
* **Hexadecimal (base 16)** → 0–9, A–F

```python
0b1000   # binary → 8
0o20     # octal → 16
0xFF     # hex → 255
```

### Conversions

```python
oct(64)
hex(64)
bin(64)
```

```python
int('64', 8)
int('64', 16)
int('1000', 2)
```

### Learning

* Base defines how digits are interpreted
* Invalid digits cause `ValueError`

---

## 1️⃣4️⃣ Bitwise Operations

```python
x = 1
x << 2   # 4
x | 2    # 3
```

### Explanation

* `<<` left shift (binary shift)
* `|` bitwise OR

---

## 1️⃣5️⃣ Random Numbers

```python
import random
random.random()
random.randint(1,10)
```

```python
l1 = ['lemon', 'masala', 'ginger']
random.choice(l1)
random.shuffle(l1)
```

### Explanation

* Pseudo-random numbers (algorithm based)
* `shuffle()` modifies list in-place

---

## 1️⃣6️⃣ Floating Point Precision Problem

```python
0.1 + 0.1 + 0.1
0.1 + 0.1 + 0.4
```

### Why This Happens

* Binary cannot exactly represent decimal fractions

---

## 1️⃣7️⃣ Decimal & Fraction for Accuracy

```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
```

```python
from fractions import Fraction
Fraction(2,7)
```

* `Decimal` → financial accuracy
* `Fraction` → rational numbers

---

## 1️⃣8️⃣ Set Operations

```python
setone = {1,2,3,4}
setone & {1,3}
setone | {1,3,7}
setone - {1,2,3,4}
```

---

## 1️⃣9️⃣ Boolean as Numbers

```python
True == 1
True + 4
```

### Explanation

* `True` → 1
* `False` → 0
* Boolean is subclass of `int`

---

📌 *This file explains numbers and arithmetic as part of Python internal working.*
