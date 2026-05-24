import copy

# =====================================================
# SHALLOW COPY
# =====================================================

# BEFORE:
original = [[1, 2], [3, 4]]

# RESULT:
# original = [[1, 2], [3, 4]]

shallow = original.copy()

# WHAT HAPPENS:
# New outer list created
# Inner lists are shared

# RESULT:
# original = [[1, 2], [3, 4]]
# shallow  = [[1, 2], [3, 4]]


# =====================================================
# MODIFY SHALLOW INNER OBJECT
# =====================================================

shallow[0].append(99)

# WHAT HAPPENS:
# shallow[0] and original[0] point to SAME inner list
# append modifies shared object

# RESULT:
# original = [[1, 2, 99], [3, 4]]
# shallow  = [[1, 2, 99], [3, 4]]


# =====================================================
# MODIFY SHALLOW OUTER OBJECT
# =====================================================

shallow.append(["NEW"])

# WHAT HAPPENS:
# Only shallow outer container changes

# RESULT:
# original = [[1, 2, 99], [3, 4]]
# shallow  = [[1, 2, 99], [3, 4], ['NEW']]


# =====================================================
# DEEP COPY
# =====================================================

deep = copy.deepcopy(original)

# WHAT HAPPENS:
# New outer list
# New inner lists
# No shared references

# RESULT:
# original = [[1, 2, 99], [3, 4]]
# deep     = [[1, 2, 99], [3, 4]]


# =====================================================
# MODIFY DEEP INNER OBJECT
# =====================================================

deep[0].append(500)

# WHAT HAPPENS:
# Only deep copy changes

# RESULT:
# original = [[1, 2, 99], [3, 4]]
# deep     = [[1, 2, 99, 500], [3, 4]]


# =====================================================
# ASSIGNMENT (NOT COPY)
# =====================================================

a = [10, 20]
b = a

# RESULT:
# a = [10, 20]
# b = [10, 20]

b.append(30)

# WHAT HAPPENS:
# Same object reference

# RESULT:
# a = [10, 20, 30]
# b = [10, 20, 30]


# =====================================================
# INTERVIEW TRAP
# =====================================================

matrix = [[0]] * 3

# RESULT:
# [[0], [0], [0]]

matrix[0].append(99)

# WHAT HAPPENS:
# Same inner list repeated

# RESULT:
# [[0, 99], [0, 99], [0, 99]]