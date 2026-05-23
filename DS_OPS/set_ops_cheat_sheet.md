Python Set Operations Cheat Sheet
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
1. Union (combine unique values)
a | b
a.union(b)

Output:

{1, 2, 3, 4, 5, 6}
2. Intersection (common values)
a & b
a.intersection(b)

Output:

{3, 4}
3. Difference (values in a but not b)
a - b
a.difference(b)

Output:

{1, 2}

Reverse:

b - a

Output:

{5, 6}
4. Symmetric Difference (not common)
a ^ b
a.symmetric_difference(b)

Output:

{1, 2, 5, 6}
5. Add single item
a.add(10)
6. Add multiple items
a.update([7, 8, 9])
7. Remove item (error if missing)
a.remove(2)
8. Remove safely (no error)
a.discard(100)
9. Remove random item
a.pop()
10. Clear all
a.clear()
11. Copy
c = a.copy()
12. Subset
{1, 2}.issubset(a)
13. Superset
a.issuperset({1, 2})
14. Disjoint (no common items)
a.isdisjoint({100, 200})
Fast Memory Trick

Remember:
UIDS ARP CSCD

U → Union |
I → Intersection &
D → Difference -
S → Symmetric Difference ^

Modification:

A → Add
R → Remove
P → Pop

Checks:

S → Subset
S → Superset
D → Disjoint
Interview one-liner

Set = unordered collection of unique mutable elements.