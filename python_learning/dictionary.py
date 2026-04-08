# 1. Dictionary Definition

# 👉 Dictionary is an unordered, mutable collection of key-value pairs.
# Key is a unique identifier used to access value.


# Empty
# d = {}

# # With data
# d = {"name": "Harsh", "age": 21}

# # Using dict()
# d = dict(name="Harsh", age=21)


# d = {"name": "Harsh", "age": 21}

# print(d["name"])      # Harsh
# print(d.get("age"))   # 21

# 👉 get() → no error if key not found
# 👉 [] → gives error


# d.pop("age")      # remove key
# d.popitem()       # remove last item
# del d["name"]     # delete key
# d.clear()         # empty dict

# keys()Returns all keys
# values()Returns all values
# items() Returns key-value pairs
# update() Merge dictionaries
