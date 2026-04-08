# 1. Set Definition

# 👉 Set is an unordered, mutable collection of unique elements.

# s = {1, 2, 3, 3}
# print(s)   # {1, 2, 3}


############## METHODS ###########

# s ={1,2}
# s.add(3)
# print(s)

# Adds multiple elements
# # s = {1,2}
# # s.update([3,4,5])
# # print(s)

# discard() Method
# 👉 Removes element, no error if not found
# s = {1,2,3}
# s.discard(10)  

# Removes random element
# s = {1,2,3}
# s.pop()
# print(s)

# All unique elements from both sets
# a = {1,2}
# b = {2,3}
# print(a | b)   # {1,2,3}


# Intersection
# 👉 Common elements
# print(a & b)   # {2}


# Differenc
# 👉 Elements in first set only
# print(a - b)   # {1}


# Symmetric Difference
# 👉 Elements not common
# print(a ^ b)   # {1,3}


# Frozen Set
# 👉 Immutable set
# fs = frozenset([1,2,3])
# # fs.add(4) ❌ Error