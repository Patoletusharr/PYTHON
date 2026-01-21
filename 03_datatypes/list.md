# 🧺 Python Lists – Basics & Internal Working

This file documents **Python list operations** using real REPL commands, outputs, and explanations.
It also explains **how lists work internally** (mutability, references, copying).

---

## 1️⃣ Creating & Printing Lists

```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)
```

```
['Black', 'Green', 'Oolong', 'White']
```

---

## 2️⃣ Indexing Lists

```python
tea_varieties[1]
```

```
'Green'
```

```python
tea_varieties[-1]
```

```
'White'
```

### Learning

* Lists support **positive and negative indexing**

---

## 3️⃣ Slicing Lists

```python
tea_varieties[2:]
```

```
['Oolong', 'White']
```

```python
tea_varieties[0:2]
```

```
['Black', 'Green']
```

```python
tea_varieties[0:4:1]
```

```
['Black', 'Green', 'Oolong', 'White']
```

---

## 4️⃣ Modifying List Elements (Mutability)

```python
tea_varieties[3] = "Herbal"
tea_varieties
```

```
['Black', 'Green', 'Oolong', 'Herbal']
```

### Internal Working

* Lists are **mutable**
* Elements can be modified in place
* Same list object is updated

---

## 5️⃣ Slice Assignment (Important Concept)

```python
tea_varieties = ['Black', 'Green', 'Oolong', 'Herbal']
tea_varieties[1:2] = "Lemon"
tea_varieties
```

```
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
```

### Explanation

* Right side must be **iterable**
* String is iterable → split into characters

---

### Correct Slice Assignment

```python
tea_varieties = ['Black', 'Green', 'Oolong', 'Herbal']
tea_varieties[1:2] = ["Lemon"]
tea_varieties
```

```
['Black', 'Lemon', 'Oolong', 'Herbal']
```

---

## 6️⃣ Inserting via Empty Slice

```python
tea_varieties[1:1] = ["test", "test"]
tea_varieties
```

```
['Black', 'test', 'test', 'White', 'Robust', 'Herbal']
```

### Learning

* Empty slice allows **inserting without replacement**

---

## 7️⃣ Iterating Over Lists

```python
for tea in tea_varieties:
    print(tea)
```

```python
for tea in tea_varieties:
    print(tea, end='-')
```

```
Black-test-test-White-Robust-Herbal-
```

### Learning

* Default `print()` ends with `\n`
* `end` parameter controls output format

---

## 8️⃣ Checking Membership

```python
"Oolong" in tea_varieties
```

```
True
```

---

## 9️⃣ List Methods

### append()

```python
tea_varieties.append("Oolong")
tea_varieties
```

```
['Black', 'test', 'test', 'White', 'Robust', 'Herbal', 'Oolong']
```

### pop()

```python
tea_varieties.pop()
```

```
'Oolong'
```

### remove()

```python
tea_varieties.remove("test")
tea_varieties
```

```
['Black', 'test', 'White', 'Robust', 'Herbal']
```

### insert()

```python
tea_varieties.insert(1, "Oolong")
tea_varieties
```

```
['Black', 'Oolong', 'White', 'Robust']
```

---

## 🔟 List References & Copying

```python
tea_varieties_copy = tea_varieties
tea_varieties_copy is tea_varieties
```

```
True
```

### Explanation

* Both variables point to **same list object**
* Changes affect both

---

### Shallow Copy

```python
tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy is tea_varieties
```

```
False
```

```python
tea_varieties_copy.append("coffee")
```

```python
tea_varieties
tea_varieties_copy
```

```
['Black', 'Oolong', 'White', 'Robust', 'Lemon', 'Gram', 'Gram']
['Black', 'Oolong', 'White', 'Robust', 'Lemon', 'Gram', 'Gram', 'coffee']
```

---

## 1️⃣1️⃣ List Comprehension

```python
squared_num = [x**2 for x in range(10)]
squared_num
```

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
cube_num = [y**3 for y in range(10)]
cube_num
```

```
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

---

## 🧠 Internal Working Summary

* Lists are **mutable objects** stored on heap
* Variables store references, not values
* Assignment copies references, not data
* `.copy()` creates a new list object
* Slice assignment modifies list in place

---

## ✅ Key Takeaways

* Lists support indexing, slicing, and mutation
* Be careful with slice assignment
* Understand reference vs copy
* List comprehensions are concise and fast

---