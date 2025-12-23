# 🔒 Immutable Objects in Python (Internal Working)

This document explains **immutability in Python** using hands-on REPL examples and Python’s internal memory model.
The focus is on **how variables work**, **object references**, and **why values don’t change unexpectedly**.

---

## 🧠 Core Idea

> **Python variables do not store values. They store references to objects.**

Objects live in memory. Variables are just labels pointing to those objects.

```
variable ──► object (in memory)
```

---

## 🧪 Example 1: String Immutability

```python
username = "tushar"
username = "sushant"
```

### Internal Working

Step 1:

```
username ──► "tushar"
```

Step 2:

```
username ──► "sushant"
"tushar" (unchanged object)
```

### Key Points

* Strings are **immutable**
* Python does **not modify** existing strings
* A new string object is created on reassignment

---

## 🧪 Example 2: Integer Immutability & References

```python
x = 10
y = x
x = 15
```

### Internal Working

After assignment:

```
x ──► 10
y ──► 10
```

After reassignment:

```
x ──► 15
y ──► 10
```

### Why `y` Did Not Change

* Integers are immutable
* `x = 15` creates a **new integer object**
* `y` still points to the old object `10`

---

## 🔍 Verifying with `id()`

```python
x = 10
y = x
id(x) == id(y)
```

Output:

```
True
```

```python
x = 15
id(x) == id(y)
```

Output:

```
False
```

✔ Confirms new object creation

---

## 🔁 Why Python Uses Immutability

* Prevents accidental data changes
* Enables memory optimizations
* Makes code safer and predictable
* Helps Python cache small integers and strings

---

## 🧠 Mutable vs Immutable Objects

| Type  | Mutable | Example      |
| ----- | ------- | ------------ |
| int   | ❌ No    | `10`         |
| str   | ❌ No    | `"chai"`     |
| tuple | ❌ No    | `(1,2)`      |
| list  | ✅ Yes   | `[1,2]`      |
| dict  | ✅ Yes   | `{ "a": 1 }` |
| set   | ✅ Yes   | `{1,2}`      |

---

## 🧠 One-Line Mental Model

> **Reassignment changes the reference, not the object.**

---

## 🎯 Interview-Ready Explanation

> In Python, immutable objects such as integers and strings cannot be modified in place. When reassigned, Python creates a new object and updates the variable reference, while other references to the original object remain unchanged.

---


