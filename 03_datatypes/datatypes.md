# 🧱 Python Object Types / Data Types

This document captures my **hands-on practice with Python data types**, along with internal behavior, common operations, and real REPL observations.

---

## 1️⃣ Overview of Python Object Types

### Core Built-in Types

* **Numbers**: `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()`
* **String**: `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`
* **List**: `[1, [2, 'three'], 4.5]`, `list(range(10))`
* **Tuple**: `(1, 'spam', 4)`, `tuple('spam')`, `namedtuple`
* **Dictionary**: `{'food': 'spam', 'taste': 'yum'}`, `dict(hours=10)`
* **Set**: `set('abc')`, `{'a', 'b', 'c'}`
* **File**: `open('eggs.txt')`, `open(r'C:\\ham.bin', 'wb')`
* **Boolean**: `True`, `False`
* **NoneType**: `None`
* **Others**: Functions, Modules, Classes

### Advanced (Later Topics)

* Decorators
* Generators
* Iterators
* Metaprogramming

---

## 2️⃣ Numbers (int, float, power operations)

```python
2.5 * 2
```

```
5.0 - precision you see
```

```python
2 ** 4
```

```
16
```

### Large Integer Support (Big Integers)

```python
2 ** 400
```

Python supports **arbitrarily large integers** (limited by memory).

```python
2 ** 400hSDjhd
```

```
SyntaxError: invalid decimal literal
```

```python
2 ** 400154
```

```
ValueError: Exceeds the limit for integer string conversion
```

### Learning

* Python `int` has **no fixed size limit**
* Errors can occur during **string conversion**, not computation

---

## 3️⃣ Math & Random Modules

```python
import math
math.pi
```

```
3.141592653589793
```

```python
import random
random.random()
```

```
0.6078064495115358
```

### random.choice()

```python
random.choice({1,2,3,4,5})
```

```
TypeError: 'set' object is not subscriptable
```

```python
random.choice([1,2,3,4,5])
```

```
3
```

### Learning

* `random.choice()` works on **sequence types** (list, tuple)
* `set` is unordered and not indexable

---

## 4️⃣ Strings (Sequence Type)

```python
username = "chaiaurcode"
len(username)
```

```
11
```

### Indexing & Slicing

```python
username[0]
username[-1]
username[-2]
username[1:3]
```

```
'c'
'e'
'd'
'ha'
```

### String Introspection

```python
dir(username)
```

### Learning

* Strings are **immutable sequences**
* Support indexing, slicing, and many built-in methods

---

## 5️⃣ Lists (Mutable Sequence)

```python
mylist = [123, "chai", 3.14]
```

```python
len(mylist)
mylist[0]
mylist[1]
mylist[2]
```

```
3
123
'chail'
3.14
```

### Learning

* Lists can hold **mixed data types**
* Lists are **mutable**
* Index-based access

---

## 6️⃣ Dictionaries (Key-Value Mapping)

```python
dict = {'one':'lemon', 'two':'ginger', 'comic':'nagraj'}
```

```python
dict[0]
```

```
KeyError: 0
```

```python
dict['one']
dict['comic']
```

```
'lemon'
'nagraj'
```

### Learning

* Dictionary keys are used for access, not indexes
* Keys must be hashable

---

## 7️⃣ Common Errors Observed

* `SyntaxError` → invalid literals
* `TypeError` → unsupported operations on data types
* `KeyError` → invalid dictionary key
* `NameError` → variable not defined

---

## 8️⃣ Mutable vs Immutable Summary

| Type  | Mutable |
| ----- | ------- |
| int   | ❌ No    |
| float | ❌ No    |
| str   | ❌ No    |
| tuple | ❌ No    |
| list  | ✅ Yes   |
| dict  | ✅ Yes   |
| set   | ✅ Yes   |

---

## 9️⃣ Key Learnings Summary

* Python has rich built-in data types
* Integers support very large values
* Strings are immutable sequences
* Lists are mutable and ordered
* Dictionaries use key-based access
* Type errors explain incorrect usage clearly

---

