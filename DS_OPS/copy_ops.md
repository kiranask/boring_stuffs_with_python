# Python Copy Operations Deep Dive
Principal SDET Interview Notes

---

# Why Copy Matters

Many engineers think:

```python
a = [10, 20]
b = a
```

means:
“b is a copy”

WRONG.

Python only copies the reference.

Memory:

a ----+
      |
      v
   [10, 20]
      ^
      |
b ----+

Both variables point to SAME object.

---

# Assignment (NOT Copy)

Code:
```python
a = [10, 20]
b = a
```

Result:
```python
a = [10, 20]
b = [10, 20]
```

Looks same.

But same object.

Now:

```python
b.append(30)
```

What happens:
Python modifies shared list.

Result:
```python
a = [10, 20, 30]
b = [10, 20, 30]
```

Why?
Same reference.

---

# Shallow Copy

Code:
```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
```

Question:
Did Python copy everything?

NO.

What happens:
- new outer list created
- inner objects reused

Memory:

original
   |
   v
+------------------+
| outer list A     |
+------------------+
    |         |
    v         v
  [1,2]     [3,4]

shallow
   |
   v
+------------------+
| outer list B     |
+------------------+
    |         |
    v         v
  [1,2]     [3,4]

Important:
Inner lists are SHARED.

---

# Modify Nested Object in Shallow Copy

Code:
```python
shallow[0].append(99)
```

What happens:
Python follows:

```python
shallow[0]
```

This points to:
```python
[1,2]
```

Same object as:
```python
original[0]
```

append changes shared object.

Result:
```python
original = [[1, 2, 99], [3, 4]]
shallow  = [[1, 2, 99], [3, 4]]
```

Why?
Nested reference shared.

---

# Modify Outer Shallow Object

Code:
```python
shallow.append(["NEW"])
```

What happens:
Only shallow outer list changes.

Result:
```python
original = [[1, 2, 99], [3, 4]]

shallow = [[1, 2, 99], [3, 4], ["NEW"]]
```

Why?
Outer containers are separate.

---

# Deep Copy

Code:
```python
import copy

deep = copy.deepcopy(original)
```

What happens:
Python recursively duplicates:
- outer list
- inner list 1
- inner list 2

Nothing shared.

Memory:

original
   |
   v
+------------------+
| outer A          |
+------------------+
    |         |
    v         v
 [1,2,99]   [3,4]


deep
   |
   v
+------------------+
| outer B          |
+------------------+
    |         |
    v         v
 [1,2,99]   [3,4]

Separate objects.

---

# Modify Deep Copy

Code:
```python
deep[0].append(500)
```

What happens:
Only deep nested object changes.

Result:
```python
original = [[1, 2, 99], [3, 4]]

deep = [[1, 2, 99, 500], [3, 4]]
```

Why?
No shared references.

---

# Flat List Case

Code:
```python
nums = [10, 20, 30]
copy1 = nums.copy()
```

What happens:
New outer list created.

Since integers are immutable:
safe behavior.

Result:
```python
nums = [10, 20, 30]
copy1 = [10, 20, 30]
```

Now:

```python
copy1.append(40)
```

Result:
```python
nums = [10, 20, 30]
copy1 = [10, 20, 30, 40]
```

Why?
Separate outer lists.

---

# Interview Trap

Code:
```python
matrix = [[0]] * 3
```

Looks like:
3 different lists.

Reality:
ONE inner list repeated.

Memory:

matrix
   |
   v
+---+---+---+
| * | * | * |
+---+---+---+
  \   |   /
      v
    [0]

All rows same object.

Now:

```python
matrix[0].append(99)
```

Result:
```python
[[0, 99], [0, 99], [0, 99]]
```

Why?
Shared reference.

---

# Complexity

Shallow Copy
```python
O(n)
```

Why?
Copies only outer references.

---

Deep Copy
```python
O(total object graph)
```

Why?
Recursively duplicates everything.

---

# When to Use

## Shallow Copy
Use when:
- flat lists
- immutable elements
- simple collections

Example:
```python
users = original_users.copy()
```

---

## Deep Copy
Use when:
- nested mutable objects
- JSON payload templates
- automation configs
- test data mutation

Example:
```python
payload = copy.deepcopy(base_payload)
```

---

# Principal SDET Use Case

Bad:
```python
payload = base_payload
payload["user"]["role"] = "admin"
```

Result:
base payload corrupted.

Good:
```python
payload = copy.deepcopy(base_payload)
```

Safe isolated mutation.

---

# Interview Answer

Shallow copy creates a new outer container while preserving references to nested objects.

Deep copy recursively duplicates the entire object graph, eliminating shared references.

---

# Memory Trick

SHALLOW

S → Shared nested objects  
H → Half copy  
A → Aliased references  

---

DEEP

D → Duplicate everything  
E → Entire object graph copied