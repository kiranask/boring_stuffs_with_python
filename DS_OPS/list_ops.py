"""
list_ops.py
Principal SDET Python Interview Prep

Goal:
Understand Python list operations WITHOUT executing code.
Learn internal behavior, complexity, and interview reasoning.
"""

import copy

# ==========================================================
# LIST CREATION
# ==========================================================

# BEFORE:
# Nothing exists.

# WHAT PYTHON DOES:
# Creates a resizable array (dynamic array).
# Stores REFERENCES to Python objects, not raw integer values.

# CONCEPTUAL MEMORY:
#
# lst
# +----+----+----+
# | *  | *  | *  |
# +----+----+----+
#   |    |    |
#  10   20   30

lst = [10, 20, 30]

# AFTER:
# lst = [10, 20, 30]


# ==========================================================
# ACCESS
# ==========================================================

# BEFORE:
# lst = [10, 20, 30]

# WHAT PYTHON DOES:
# Directly jumps to index 0.
# No looping.
# Formula concept:
# base memory address + offset

first = lst[0]

# AFTER:
# first = 10

# Complexity:
# O(1)


# Negative indexing

# BEFORE:
# lst = [10, 20, 30]

# WHAT PYTHON DOES:
# Converts:
# -1 → len(lst)-1 → 2
# Then normal indexing

last = lst[-1]

# AFTER:
# last = 30

# Complexity:
# O(1)


# ==========================================================
# APPEND
# ==========================================================

# BEFORE:
# lst = [10, 20, 30]

# POSSIBLE MEMORY:
#
# +----+----+----+----+
# | *  | *  | *  |    |
# +----+----+----+----+

# WHAT PYTHON DOES:
# 1. Checks if spare capacity exists
# 2. Finds free slot
# 3. Places reference to new object

lst.append(40)

# AFTER:
# lst = [10, 20, 30, 40]

# MEMORY:
#
# +----+----+----+----+
# | *  | *  | *  | *  |
# +----+----+----+----+

# Complexity:
# O(1) amortized


# ==========================================================
# EXTEND
# ==========================================================

# BEFORE:
# lst = [10, 20, 30, 40]

# WHAT PYTHON DOES:
# Iterates through incoming iterable:
# 50
# 60
#
# Appends one by one internally

lst.extend([50, 60])

# AFTER:
# lst = [10, 20, 30, 40, 50, 60]

# Complexity:
# O(k)


# ==========================================================
# INSERT
# ==========================================================

# BEFORE:
# lst = [10, 20, 30]

demo = [10, 20, 30]

# WHAT PYTHON DOES:
#
# Step 1:
# Find index = 1
#
# Step 2:
# Shift elements right
#
# 30 moves right
# 20 moves right
#
# Intermediate:
# [10, _, 20, 30]
#
# Step 3:
# Insert new item

demo.insert(1, 999)

# AFTER:
# demo = [10, 999, 20, 30]

# Complexity:
# O(n)


# ==========================================================
# REMOVE
# ==========================================================

demo = [10, 999, 20, 30]

# WHAT PYTHON DOES:
#
# Scan:
# 10 != 999
# 999 == 999
#
# Remove matched element
#
# Shift remaining left

demo.remove(999)

# AFTER:
# demo = [10, 20, 30]

# Complexity:
# O(n)


# ==========================================================
# POP LAST
# ==========================================================

demo = [10, 20, 30]

# WHAT PYTHON DOES:
# Remove last reference only
# No shifting

item = demo.pop()

# AFTER:
# item = 30
# demo = [10, 20]

# Complexity:
# O(1)


# ==========================================================
# POP FIRST
# ==========================================================

demo = [10, 20, 30]

# WHAT PYTHON DOES:
#
# Remove first element
#
# Shift:
# 20 → left
# 30 → left

item = demo.pop(0)

# AFTER:
# item = 10
# demo = [20, 30]

# Complexity:
# O(n)


# ==========================================================
# DELETE
# ==========================================================

demo = [10, 20, 30]

# WHAT PYTHON DOES:
# Remove index 1
# Shift remaining left

del demo[1]

# AFTER:
# demo = [10, 30]

# Complexity:
# O(n)


# ==========================================================
# CLEAR
# ==========================================================

demo = [10, 20, 30]

# WHAT PYTHON DOES:
# Removes all references
# If no other references exist:
# garbage collector can reclaim objects

demo.clear()

# AFTER:
# demo = []

# Complexity:
# O(n)


# ==========================================================
# SEARCH
# ==========================================================

nums = [10, 20, 30, 40]

# WHAT PYTHON DOES:
#
# Compare sequentially:
# 10 ?= 30
# 20 ?= 30
# 30 == 30

exists = 30 in nums

# AFTER:
# exists = True

# Complexity:
# O(n)


# ==========================================================
# SORT
# ==========================================================

scores = [90, 20, 70, 10]

# WHAT PYTHON DOES:
# Uses Timsort
#
# Rearranges in-place

scores.sort()

# AFTER:
# [10, 20, 70, 90]

# Complexity:
# O(n log n)


# ==========================================================
# REVERSE
# ==========================================================

scores = [10, 20, 30, 40]

# WHAT PYTHON DOES:
#
# swap:
# 10 ↔ 40
# 20 ↔ 30

scores.reverse()

# AFTER:
# [40, 30, 20, 10]

# Complexity:
# O(n)


# ==========================================================
# SHALLOW COPY
# ==========================================================

nested = [[1, 2], [3, 4]]

# WHAT PYTHON DOES:
# New outer list
# Same inner references

shallow = nested.copy()

# MEMORY:
#
# nested ----+
#           +--> [1,2]
# shallow ---+
#
# nested ----+
#           +--> [3,4]
# shallow ---+


# ==========================================================
# DEEP COPY
# ==========================================================

deep = copy.deepcopy(nested)

# WHAT PYTHON DOES:
# Duplicates entire object tree


# ==========================================================
# LIST COMPREHENSION
# ==========================================================

# WHAT PYTHON DOES:
# Loop internally:
#
# x=0 -> 0
# x=1 -> 1
# x=2 -> 4
# x=3 -> 9
# x=4 -> 16

squares = [x * x for x in range(5)]

# AFTER:
# [0, 1, 4, 9, 16]


# ==========================================================
# CONCATENATION
# ==========================================================

a = [1, 2]
b = [3, 4]

# WHAT PYTHON DOES:
# Create brand new list
# Copy references from a
# Copy references from b

combined = a + b

# AFTER:
# [1, 2, 3, 4]


# ==========================================================
# REPETITION
# ==========================================================

# WHAT PYTHON DOES:
# Repeats references, NOT deep copies

repeated = ["A"] * 3

# AFTER:
# ["A", "A", "A"]


# ==========================================================
# NESTED ACCESS
# ==========================================================

matrix = [[1, 2], [3, 4]]

# WHAT PYTHON DOES:
# matrix[1] -> [3,4]
# [3,4][0] -> 3

value = matrix[1][0]

# AFTER:
# value = 3

# Complexity:
# O(1)