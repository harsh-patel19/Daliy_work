# num = int(input("Enter the Number: "))
# temp = num
# sum = 0

# while temp > 0 :
#     digit = temp % 10
#     cube = digit **3
#     sum = sum + cube
#     temp //=10
# if sum == num:
#     print("armstornge")
# else:
#     print("Not")


# while temp > 0 :
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //=10
# if sum == num:
#     print("palindrom")
# else:
#     print("not")


# rows = int(input("Enter the Number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

# for i in range(rows , 0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 


# name = "pyhtoaen"
# vowel = "aeiou"

# for i in name:
#     if i in vowel:
#         print([i],end=" ")
#     else:
#         pass



############# list #############

# a = [10,20,30]
# b = list((4,5,6))

# print(b)

# a = [10,20,30]
# print(a[0])

# a = [10,20,30,40,50,60]
# print(a[1:4])

# a.append(4)               # add at end
# a.insert(1,10)            # insert at index
# a.remove(20)              # remove value
# a.pop()                   # remove last
# a.sort()                  # sort list
# a.reverse()               # revers list
# print(a)


# squre = [x*x for x in range(5)]
# print(squre)

# a =  [1,2,2,3,3,4]
# a = list(set(a))
# print(a)

# Reverse a list without using reverse()

# a = [1,2,3]
# print(a[::-1])

# Find common elements in two lists
# a = [1, 2, 3]
# b = [2, 3, 4]

# print(list(set(a) & set(b)))

# a = 20
# b  = 10
# a,b = b,a
# print(a,b)


############# TUPLE #############

# t = (1,[2,3])
# t[1].append(4)
# print(t)

# t = (5,)
# print(t)

# a,b,c = (1,2,3)
# print(a,b,c)

# t = (1, 2, 2, 3)

# t.count(2)
# # t.index(3)
# print(t)


############# FUNCTIONS #########

### TYPES OF FUNCTIONS ::

# 1.Built-in (print, len)
# 2.User-defined
# 3.Lambda (anonymous)

# def add(a, b):
#     return a + b

# add(2, 3)

# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res

# def palidrom(s):
#     return s == s[::-1]

# def largest(lst):
#     return max(lst)


# student = {
#     "name": "Harsh",
#     "age": 22,
#     "course": "Python"

# }

# for key,value in student.items():
#     print(key,value)

 
