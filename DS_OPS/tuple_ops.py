"""
PYTHON TUPLE CHEAT SHEET
Interview + Practical Reference
"""

# ----------------------------
# 1. Create Tuple
# ----------------------------
t1 = (1, 2, 3)
t2 = 1, 2, 3
single = (5,)   # IMPORTANT

print(type(t1))
print(type(single))

# ----------------------------
# 2. Access Elements
# ----------------------------
t = ("python", "java", "go")

print(t[0])
print(t[-1])

# ----------------------------
# 3. Slicing
# ----------------------------
print(t[0:2])
print(t[::-1])

# ----------------------------
# 4. Tuple Packing
# ----------------------------
person = ("Kiran", 35, "SDET")

# ----------------------------
# 5. Tuple Unpacking
# ----------------------------
name, age, role = person
print(name, age, role)

# Extended unpacking
print("extended unpacking..")
a, *middle, z = (1, 2, 3, 4, 5)
print(a, middle, z)

# ----------------------------
# 6. Immutability
# ----------------------------
t = (1, 2, 3)

# t[0] = 100   # ERROR

# ----------------------------
# 7. Mutable object inside tuple
# ----------------------------
print("Mutable object inside tuple")
t = ([1, 2], "python")
t[0].append(3)

print(t)

# ----------------------------
# 8. Tuple Methods
# ----------------------------
nums = (10, 20, 30, 20)

print(nums.count(20))
print(nums.index(30))

# ----------------------------
# 9. Membership
# ----------------------------
print(20 in nums)

# ----------------------------
# 10. Looping
# ----------------------------
for item in nums:
    print(item)

# ----------------------------
# 11. Concatenation
# ----------------------------
a = (1, 2)
b = (3, 4)

print(a + b)

# ----------------------------
# 12. Repetition
# ----------------------------
print(("test",) * 3)

# ----------------------------
# 13. Length
# ----------------------------
print(len(nums))

# ----------------------------
# 14. Min / Max / Sum
# ----------------------------
scores = (50, 70, 90)

print(min(scores))
print(max(scores))
print(sum(scores))

# ----------------------------
# 15. Tuple to List
# ----------------------------
t = (1, 2, 3)
lst = list(t)

# ----------------------------
# 16. List to Tuple
# ----------------------------
lst = [4, 5, 6]
t = tuple(lst)

# ----------------------------
# 17. Nested Tuple
# ----------------------------
print("Nested Tuple")
matrix = ((1, 2), (3, 4))
print(matrix[1][0])

# ----------------------------
# 18. Tuple as Dictionary Key
# ----------------------------
cache = {
    ("user1", "prod"): "token123"
}

print(cache[("user1", "prod")])

# ----------------------------
# 19. Memory Efficient
# ----------------------------
# Tuple uses less memory than list

# ----------------------------
# 20. Faster Iteration
# ----------------------------
# Slightly faster than list

# ----------------------------
# Interview Question
# Why tuple over list?
# ----------------------------
"""
1. Immutable
2. Safer config/state handling
3. Hashable
4. Better performance
5. Lower memory
6. Good for fixed records
"""