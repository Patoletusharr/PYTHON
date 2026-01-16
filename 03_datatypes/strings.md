# 🔤 Python Strings – Basics & Internal Working

This file documents **Python string operations** with **REPL commands, outputs**, and **internal behavior** (immutability, memory, references).

---

## 1️⃣ Creating & Printing Strings

```python
chai = "lemon chai"
chai
```

```
'lemon chai'
```

```python
print(chai)
```

```
lemon chai
```

---

## 2️⃣ Indexing Strings

```python
chai[0]
```

```
'l'
```

```python
chai[7]
```

```
'h'
```

---

## 3️⃣ Slicing Strings

```python
chai[0:6]
```

```
'lemon'
```

### Slice Syntax

```
string[start : end : step]
```

```python
num_list = "0123456789"
num_list[:]
```

```
'0123456789'
```

```python
num_list[:2]
```

```
'01'
```

```python
num_list[3:]
```

```
'3456789'
```

```python
num_list[3:9]
```

```
'345678'
```

```python
num_list[0:7:2]
```

```
'0246'
```

```python
num_list[0:7:3]
```

```
'036'
```

---

## 4️⃣ String Methods

```python
chai.upper()
```

```
'LEMON CHAI'
```

```python
chai.lower()
```

```
'lemon chai'
```

```python
chai = "   garam chai  "
chai.strip()
```

```
'garam chai'
```

```python
chai.replace("garam", "masala")
```

```
'   masala chai  '
```

---

## 5️⃣ String Immutability (Internal Working)

```python
chai
```

```
'   garam chai  '
```

* Strings are **immutable**
* Methods return **new string objects**
* Original string remains unchanged
* Old objects are garbage-collected when references drop to zero

---

## 6️⃣ Splitting Strings

```python
chai = "Lemon, Ginger, Masala, Mint"
chai.split(", ")
```

```
['Lemon', 'Ginger', 'Masala', 'Mint']
```

---

## 7️⃣ Searching in Strings

```python
chai = "Masala Chai"
chai.find("Chai")
```

```
7
```

```python
chai.find("chai")
```

```
-1
```

```python
chai = "Masala Chai Chai Chai"
chai.count("Chai")
```

```
3
```

---

## 8️⃣ String Formatting

```python
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
order.format(quantity, chai_type)
```

```
'I ordered 2 cups of Masala chai'
```

---

## 9️⃣ Joining Strings

```python
chai_variety = ["lemon", "Masala", "Ginger"]
"".join(chai_variety)
```

```
'lemonMasalaGinger'
```

```python
" ".join(chai_variety)
```

```
'lemon Masala Ginger'
```

```python
", ".join(chai_variety)
```

```
'lemon, Masala, Ginger'
```

---

## 🔟 Length & Iteration

```python
len(chai)
```

```
21
```

```python
for letter in chai:
    print(letter)
```

```
M
a
s
a
l
a

C
h
a
i

C
h
a
i

C
h
a
i
```

---

## 1️⃣1️⃣ Escape Sequences

```python
chai = "Masala\nChai"
print(chai)
```

```
Masala
Chai
```

---

## 1️⃣2️⃣ Raw Strings

```python
chai = r"Masala\nchai"
print(chai)
```

```
Masala\nchai
```

```python
chai = r"c:\user\pwd"
print(chai)
```

```
c:\user\pwd
```

---

## 1️⃣3️⃣ Quotes Inside Strings

```python
chai = "He said, \"Masala chai is awesome\""
chai
```

```
'He said, "Masala chai is awesome"'
```

---

## 1️⃣4️⃣ Membership Operator (`in`)

```python
chai = "Masala Chai"
"Masala" in chai
```

```
True
```

```python
"Masalaa" in chai
```

```
False
```

---

## 🧠 Internal Summary

* Strings are **immutable Unicode objects**
* Stored in heap memory
* Variables store **references**, not values
* Any modification creates a **new object**
* Python may optimize strings using **interning**

---

## ✅ Key Takeaways

* Strings behave like sequences
* Cannot be modified in place
* All string methods return new objects
* Safe and predictable memory behavior

---
