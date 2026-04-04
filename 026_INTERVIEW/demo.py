

############# PATTERNS ###########

# rows = int(input("Enter the number: "))

# for i in range(rows):
#     for j in range(rows -i - 1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i - 1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# rows = int(input("Enter the number: "))

# # Upper part
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()

# # Lower part
# for i in range(rows - 2, -1, -1):
#     for j in range(rows - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()



# rows = int(input("Enter number: "))

# for i in range(rows,0,-1):
#     for j in range(rows - i):
#         print(" ",end=" ")
#     for k in range(2* i -1):
#         print("*",end=" ")
#     print()


# for i in range(2,rows +1):
#     for j in range(rows - i ):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()



# for i in range(1,6+1):
#     for j in range(i):
#         print("*",end=" ")
#     for k in range(2*(6-i)):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     for k in range(2*(6-i)):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()



########### LOGIC QUESTION ##########



# num = int(input("Enter the number: "))
# temp = num
# sum = 0

# while temp > 0 :
#     digit = temp %10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10

# if sum == num:
#     print("Armstornge number")
# else:
#     print("not")

# while temp > 0 :
#     digit = temp % 10
#     sum = sum * 10 + digit
#     temp //= 10

# if sum == num:
#     print("PALIDROM NUMBER")

# else:
#     print("NOT PALIDROM")


# num = int(input("Enter the number: "))
# flag = 0

# for i in range(2,num):
#     if num % i ==0:
#         flag =1
#         break
# if flag == 0:
#     print("PRIME NUMBER")
# else:
#     print("NOT PRIME")


# s = "pyhton"
# print(s[::-1])


# p  = "list"
# print(p[::-1])

# n = 0 

# def fibbnocie(n):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibbnocie(n-1) + fibbnocie(n-2)
# a = 10
# for i in range(a):
#     print(fibbnocie(i),end=" ")

# n = 5 
# fact = 1

# for i in range(1,n+1):
#     fact = fact*i
# print(fact)


# a = 10
# b = 20

# a,b = b,a
# print(a,b)



# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("ODD")


# name = "Patel"
# vowel = "aeiou"

# for i in name:
#     if i in vowel:
#         print(i)

# name = [10,20,30,40,50,10,20,30]
# a = (list(set(name)))
# print(a)


# a = [1,2,3]
# b = [4,5,6]
# c = []

# c = a
# a = b
# b = c
# print(a)
# print(b)

# s1 = "listen"
# s2 = "silent"

# print("Anagram" if sorted(s1) == sorted(s2) else "Not")

# Find Intersection of Two Lists

# a = [1,2,3]
# b = [2,3,4]

# print(list(set(a) & set(b)))

# nums = [10,20,5,30]
# num = list(set(nums))
# nums.sort()

# print(nums[-2])


####################### TUPLE ###############

# t = (1,2,3)
# print(list(t))

# nums = [1,2,2,3]
# print(set(nums))

# a = {1,2}
# b = {2,3}

# print(a | b)

# d = {"a":1, "b":2}
# print(d)
# print(d["a"])

# d1 = {"a":1}
# d2 = {"b":2}

# d1.update(d2)
# print(d1)

# d = {
#     "student": {
#         "name": "Harsh",
#         "marks": 90
#     }
# }

# print(d["student"]["name"])

# product = {
#     "laptop" :{
#         "price":30000,
#         "qty":10
#     },
#     "Mouse" :{
#        "price":300,
#        "qty":15
#     },
#     "keyboard" :{
#         "price":3000,
#         "qty":11
#     },
# }

# for i,j in product.items():
#     print(i)
#     for x,y in j.items():
#         print(x,y)


# student = {
#     "name":"Meet",
#     "email":"meet@gamil.com",
#     "sub" : ["java","python","php"]
# }

# print(student)
# print(student.get('name1'))

# print(student.keys())
# print(student.values())
# print(student.items())

# for i in student.keys():
#     print(i)

# for i in student.values():
#     print(i)

# for i,j in student.items():
#     print(i,j)