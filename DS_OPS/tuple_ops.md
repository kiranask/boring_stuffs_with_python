# Python Tuple Cheat Sheet

## Definition
Tuple = ordered, immutable collection.

Example:
```python
t = (1, 2, 3)
```

---

## Properties
- Ordered ✅
- Immutable ✅
- Allows duplicates ✅
- Heterogeneous data ✅
- Hashable (if immutable elements) ✅

---

## Create Tuple
```python
t = (1, 2, 3)
t = 1, 2, 3
```

Single element:
```python
t = (5,)
```

Without comma:
```python
t = (5)
```

This is int, NOT tuple.

---

## Access
```python
t[0]
t[-1]
```

---

## Slicing
```python
t[1:3]
t[::-1]
```

---

## Packing
```python
person = ("Kiran", 35, "Principal SDET")
```

---

## Unpacking
```python
name, age, role = person
```

Extended:
```python
a, *mid, z = (1,2,3,4,5)
```

---

## Methods
Count:
```python
t.count(20)
```

Index:
```python
t.index(30)
```

---

## Membership
```python
20 in t
```

---

## Concatenation
```python
a + b
```

---

## Repetition
```python
("A",) * 3
```

---

## Conversion
Tuple → List:
```python
list(t)
```

List → Tuple:
```python
tuple(lst)
```

---

## Nested Tuple
```python
matrix = ((1,2),(3,4))
matrix[1][0]
```

---

## Tuple vs List

| Feature | Tuple | List |
|--------|------|------|
| Mutable | No | Yes |
| Memory | Lower | Higher |
| Speed | Faster | Slower |
| Methods | Few | Many |
| Hashable | Yes | No |

---

## Tuple Use Cases
- Fixed config
- API response records
- Coordinates
- DB keys
- Cache keys
- Safer framework constants

Example:
```python
("tenant", "environment")
```

---

## Principal SDET Interview Answers

### Why tuple?
- immutable
- memory efficient
- hashable
- protects accidental mutation
- ideal for config/state

---

### Tuple as dict key?
Because tuple is hashable.

Example:
```python
cache[(user, env)] = token
```

---

### Mutable object inside tuple?
Tuple immutable, internal mutable object can change.

Example:
```python
t = ([1,2], "python")
t[0].append(3)
```

---

## Memory Trick
Remember:

TUPLE

T → Tiny memory  
U → Unchangeable  
P → Pack/unpack  
L → Lightweight  
E → Efficient