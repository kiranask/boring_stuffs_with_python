"""
set_ops.py
Author: Kiran SK
Purpose: Memory Palace for Python Sets - Learn, recall, and master set operations
for automation, SDET interviews, and real-world Python usage.

Features included:
- Set creation
- Mutable vs Immutable sets
- Add / Update / Remove operations
- Set algebra: union, intersection, difference, symmetric difference
- Subset / Superset / Disjoint checks
- Membership & fast lookup
- Mnemonics & memory aids
"""

# ======================================================
# 1️⃣ Basic Set Creation
# ======================================================

# Sets automatically remove duplicates
numbers = {1, 2, 3, 3, 4}
print("Unique numbers:", numbers)  # Output: {1, 2, 3, 4}

fruits = set(["apple", "banana", "apple"])
print("Unique fruits:", fruits)    # Output: {'apple', 'banana'}

# Empty set ({} creates a dict, not set)
empty_set = set()
print("Empty set:", empty_set)      # Output: set()

# Immutable set (cannot change after creation)
immutable_set = frozenset([1, 2, 3])
print("Immutable set:", immutable_set)  # Output: frozenset({1, 2, 3})

# ======================================================
# 2️⃣ Add / Update / Remove Operations
# ======================================================

s = {1, 2, 3}

# Add single element
s.add(4)
print("After add:", s)              # {1, 2, 3, 4}

# Add multiple elements
s.update([5, 6, 7])
print("After update:", s)           # {1, 2, 3, 4, 5, 6, 7}

# Remove element (throws KeyError if missing)
s.remove(2)

# Remove element safely (no error if missing)
s.discard(10)

print("After remove/discard:", s)

# Remove and return arbitrary element
popped_item = s.pop()
print("Popped item:", popped_item)
print("Set now:", s)

# Clear all elements
s.clear()
print("Cleared set:", s)

# ======================================================
# 3️⃣ Set Algebra Operations
# ======================================================

a = {1, 2, 3}
b = {3, 4, 5}

# Union: all elements from both sets
union_set = a | b
print("Union:", union_set)                  # {1, 2, 3, 4, 5}

# Intersection: common elements
intersection_set = a & b
print("Intersection:", intersection_set)    # {3}

# Difference: elements in a not in b
diff_set = a - b
print("Difference (a-b):", diff_set)       # {1, 2}

# Symmetric Difference: elements in either a or b but not both
sym_diff_set = a ^ b
print("Symmetric Difference:", sym_diff_set)  # {1, 2, 4, 5}

# ======================================================
# 4️⃣ Subset / Superset / Disjoint
# ======================================================

print("Is a subset of b?", a <= b)          # False
print("Is a superset of b?", a >= b)        # False
print("Are a and b disjoint?", a.isdisjoint(b))  # False

# ======================================================
# 5️⃣ Membership & Fast Lookup
# ======================================================

users = {"alice", "bob", "charlie"}
print("Is 'bob' in users?", "bob" in users)   # True (fast O(1) lookup)

# Remove duplicates from a list using set
emails = ["a", "b", "a", "c"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)        # {'a', 'b', 'c'}

# ======================================================
# 6️⃣ Mutable vs Immutable Sets
# ======================================================

# Mutable set - can add/remove elements
mutable_set = {1, 2, 3}
mutable_set.add(4)
print("Mutable set after add:", mutable_set)  # {1,2,3,4}

# Immutable set (frozenset) - cannot modify
immutable_set = frozenset([1, 2, 3])
# immutable_set.add(4)  # Would throw AttributeError

# frozenset can be used as dictionary key
cache = {frozenset([1, 2]): "cached_value"}
print("Immutable set as dict key:", cache)

# ======================================================
# 7️⃣ Mnemonics for Memory Retention
# ======================================================

"""
Mnemonic for Set Operations: ARDU-CUIDSS
----------------------------------------
A = Add
R = Remove
D = Discard
U = Update
C = Clear
U = Union
I = Intersection
D = Difference
S = Symmetric difference
S = Subset/Superset checks
"""

# ======================================================
# 8️⃣ Real SDET Examples
# ======================================================

# 8.1 Remove duplicates in test data
test_data = ["login", "api", "login", "dashboard"]
unique_test_data = set(test_data)
print("Unique test steps:", unique_test_data)

# 8.2 Fast lookup for allowed users
allowed_users = set(["alice", "bob", "charlie"])
if "eve" in allowed_users:
    print("User allowed")
else:
    print("User NOT allowed")  # Eve not allowed

# 8.3 Compare test environments
qa_features = {"login", "api", "dashboard"}
prod_features = {"login", "dashboard"}

missing_features = qa_features - prod_features
print("Missing in production:", missing_features)  # {'api'}

# ======================================================
# 9️⃣ Memory Anchors / Interview Notes
# ======================================================

"""
Analogies:
- Set = Security guard 🚫 (no duplicates)
- Add / Update = Throw items in bag 👜
- Remove / Discard = Take out items / discard safely
- Union = Marriage 💍 (all friends together)
- Intersection = Common friends 🤝
- Difference = What remains after breakup 😅
- Symmetric Difference = Exclusive friends ✌️
- Mutable = Living object (bag)
- Immutable = Locked locker 🔒
- Membership = Fast O(1) check
"""