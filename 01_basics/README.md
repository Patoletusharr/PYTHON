# 🐍 Python Basics – Learning Journey (01_basics)

This README documents my hands-on Python learning, focusing on Python internals, REPL usage, imports, errors, and execution flow.

---

## 1️⃣ Python BTS (Behind the Scenes)

```
Code → Bytecode (mostly hidden) → Python Virtual Machine (PVM)
```

### Step 1: Compile to Bytecode

* Python source code (`.py`) is compiled into bytecode
* Bytecode is low-level and platform-independent
* Syntax checking and parsing happen at this stage
* Bytecode executes faster than raw source code
* `.pyc` files are compiled Python files (frozen binaries)

---

## 2️⃣ Running Python Scripts (First Interaction)

```bash
python hello_chai.py
```

```
chai aur code
4
```

### Learnings

* Python executes files top to bottom
* Top-level code runs immediately
* Output appears during import because of top-level execution

---

## 3️⃣ Entering Python REPL (Interactive Mode)

```bash
python
```

### Math Operations

```python
2 * 2
3 + 5
```

```
4
8
```

### String Operations

```python
"tushar" * 4
```

```
'tushartushartushartushar'
```

### Learnings

* Python evaluates expressions instantly
* Strings support multiplication

---

## 4️⃣ Variables & Dynamic Typing

```python
score = 100
score
```

```
100
```

### Learnings

* Python is dynamically typed
* Variable types are inferred at runtime

---

## 5️⃣ Errors Faced & Fixes

### NameError

```python
print(tushar)
```

```
NameError: name 'tushar' is not defined
```

```python
print("tushar")
```

### Learnings

* Variables must exist before use
* Strings must be quoted

---

### IndentationError

```python
for c in "chai":
print(c)
```

```
IndentationError: expected an indented block
```

```python
for c in "chai":
    print(c)
```

```
c
h
a
i
```

### Learnings

* Indentation is syntax, not style
* Python uses indentation instead of braces

---

## 6️⃣ Using Built-in Modules

```python
import os
os.getcwd()
```

```
C:\Users\DELL\Documents\Python\01_basics
```

### Learnings

* Python provides built-in modules
* `os` helps interact with the operating system

---

## 7️⃣ Importing Custom Python Files

```python
import hello_chai
```

```
chai aur code
4
```

### Learnings

* Import runs a file once per session
* Top-level code executes during import

---

## 8️⃣ Reloading a Module

```python
from importlib import reload
reload(hello_chai)
```

```
chai aur code
4
```

### Learnings

* Reload is useful after code changes
* Forces Python to re-run the module

---

## 9️⃣ Accessing Module Attributes

```python
hello_chai.chai("mint chai")
```

```
mint chai
```

```python
hello_chai.chai_one
```

```
'lemon tea'
```

```python
hello_chai.chai_onee
```

```
AttributeError: module 'hello_chai' has no attribute 'chai_onee'
```

### Learnings

* Only defined attributes can be accessed
* Python provides clear runtime errors

---

## 🔟 Understanding **pycache**

```
hello_chai.cpython-311.pyc
```

* Stores compiled bytecode
* Created only for imported files
* `311` indicates Python version
* Improves execution speed

---

## 1️⃣1️⃣ Python Virtual Machine (PVM)

* Executes bytecode line by line
* Runtime engine of Python
* Makes Python an interpreted language

---

## 1️⃣2️⃣ Python Execution Flow

```
Source Code (.py)
      ↓
Bytecode (.pyc)
      ↓
Python Virtual Machine (PVM)
```

---

## 1️⃣3️⃣ Python Implementations

* CPython
* PyPy
* Jython
* IronPython
* Stackless Python

---

## 1️⃣4️⃣ Summary

* Python scripts execution
* REPL usage
* Variables and strings
* Indentation and loops
* Error handling
* Imports and reloads
* Bytecode and PVM

---
