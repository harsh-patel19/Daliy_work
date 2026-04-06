# student = {
#     "name": "Harsh",
#     "age": 22,
#     "city": "Surat"
# }

# print(student["name"])
# print(student["age"])
# print(student["city"])


# Empty
# d = {}

# d = {"name": "Harsh", "age": 22}
# print(d["name"])
# print(d.get("age"))

# [] → error if key not found
# get() → returns None

# Add & Update Values

# d = {"name":"harsh"}

# d["age"] =20
# print(d)



# d = {"name":"Harsh","age":22}

#keys
# for i in d:
#     print(i)


# values
# for i in d.items():
#     print(i)

#key-values

# for k,v in d.items():
#     print(k,v)

# d = {"a":1}
# d.setdefault("b",2)
# print(d)

# Merge two dictionaries

# d1 = {"a":1}
# d2 = {"b":2}

# d1.update(d2)
# print(d1)

# Sort dictionary by key

# d = {"b":2, "a":1}
# print(dict(sorted(d.items())))

# Get max value key

# d = {"a":10,"b":20}
# print(max(d,key=d.get))

# Remove duplicates from list using dict

# a = [1,2,3,1,3]
# a = list(dict.fromkeys(a))
# print(a)



