#  Create a tuple with 5 elements.??

# t = (1,2,3,4,5)
# print(t)


#  Access tuple elements using indexing. ??

# t = (1,2,3,4,5)
# print(t[1:])


# Find length of tuple.?

# t = (1,2,3,4,5)
# print(len(t))


# Count occurrence of element.?

# t = (1,2,3,1)
# print(t.count(1))


# Find index of element. ???

# t = (1,0,20,30,40,50)
# print(t[0])
# print(t[-1])



# Convert tuple to list.?

# t = (1,0,20,30,40,50)

# lst = list(t)
# print(type(lst))



# Convert list to tuple. ??

# t = [10,20,30,40,50]

# tup = tuple(t)
# print(tup)


# Unpack tuple values. ???

# a,b,c  = (1,2,3)

# print(a)
# print(b)
# print(c)


# Concatenate two tuples ???

# t1 = (1,2,3)
# t2 = (4,5,6)

# result = t1 + t2
# print(result)


# Check whether an element exists in tuple ??

# tup = (10,20,30,40)

# if 30 in tup:
#     print("Found")

# else:
#     print("Not Found")



# Find repeated elements in tuple ???


# tup = (1,2,3,2,4,1,5)

# for i in tup:
#     if tup.count(i) > 1:
#         print(i)


# Swap values using tuple unpacking ??
# a = 10
# b = 20

# a,b = b,a
# print(a,b)



# Find maximum and minimum in tuple ???
# tup = (1,20,30,40,50)

# largest = tup[0]
# samllest = tup[0]

# for i in tup:
#     if i > largest:
#         largest = i

#     if i < samllest:
#         samllest = i 

# print(largest)
# print(samllest)


# sort tuple elements ??

# tup = (5,2,9,1,4)
# new = tuple(sorted(tup))
# print(new)



# def hello(func):
#     def h():
#         print("hello")
#         func()
#     return h


# @hello
# def new():
#     print("all")
# new()



