
# 
#   list  
# 


# (1) FIND THE MAX AND MIN IN THIS LIST ?
# lst = [1,2,4,5,6,8,2]
# user_min = lst[0]
# user_max = lst[0]

# for num in lst:
#     if num >user_max:
#         user_max = num
#     if num < user_min:
#         user_min = num


# print("user_min: ",user_max)
# print("user_max:",user_min)




# (2) cou t how many time repeat the elements ?
# number = [15,2,3,4,5,2,3]
# count = {}

# for i in number:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1

# print(count)


# (3) take in 10 number form user and store in list ?

# new = []

# for i in range(10):
#     user = int(input("Entert the number: "))
#     new.append(user)

# print(new)


# (4) find the sum all menets in list ?


# number = [10,5,456,40]
# sum = 0

# for i in number:
#     sum += i
# print(sum)


# (5) fins the evene and odd number in list ??

# number = [1,2,3,4,5,6]
# even = []
# odd = []
# for i in number:
#     if i % 2 == 0 :
#         even.append(i)
#     else:
#         odd.append(i)


# print("even: ",even)
# print("odd: ",odd)



# (6)remove duplicated in list ?

# lst = [1,2,3,4,5,1,2]
# new = []

# for i in lst:
#     if i not in new:
#         new.append(i)

# print(new)


# (7) create a new list in containing in quares of list old ?

# lst  = [10,20,30,40,50]
# square = []

# for i in lst:
#     square.append(i * i)
# print(square)



# (8) FIND THE second largest number in list ?

# lst  = [10,20,30,40,50]
# largest = 0
# secound = 0


# for i in lst:
#     if i >largest:
#         secound = largest
#         largest = i
# print(secound)


# (9) check waterr in list in palindom ya not?

# name = "aaa"

# if name == name[::-1]:
#     print("palidrom")
# else:
#     print("not")


# (10) fins the comman elemnt in list ?

# lst = [10,20,30]
# lst1 = [40,50,10]

# new = (set(lst) & set(lst1))
# print(new)


# (11) fins the missning element in list ?

# lst = [1,2,3,4,5,6,8,10]

# for i in range(1,11):
#     if i not in lst:
#         print(i)


# (12) move all zero in the in last of in the list ?

# lst = [1,2,3,4,0,0,0,0,5,6,7,8]

# result = []

# for i in lst:
#     if i != 0:
#         result.append(i)
# for i in lst:
#     if i == 0:
#         result.append(i)

# print(result)

# (13) print the vomels in lsit and count how many ?

# name = "harsh"
# vowels = "aeiou"
# count = 0

# for i in name:
#     if i in vowels:
#         print(i)
#         count += 1

# print(count)



# 
#   set
# 

# (1) find the union of to (AUB) ?
#  thats is the removing the duplicated used..

# A = {1,2,3}
# B = {3,4,5}

# print(A | B)


# (2) find intersection ?
#  thats is the using same element to print..

# A = {1,2,3,4}
# B = {3,4,5}

# print(A & B)


# (3) remove duplicate in list ?

# lst = [1,2,3,4,1,2]

# result = list(set(lst))
# print(result)


# (4) check subset and superset ?

# A = {1,2}
# B={4,5,6,1,2}

# print(A.issubset(B))
# print(B.issuperset(A))


# (5) Check whether one set is subset of another?

# A = {1,2}
# b = {1,2,3,4}

# if A.issubset(b):
#     print("subset")
# else:
#     print("not")



# (6)  take user input ?


# a = set(map(int,input("Enter first set: ").split()))
# b = set(map(int,input("Enter seound set: ").split()))


# print("subset: ", a.issubset(b))
# print("superset:",b.issuperset(a))


# (7) find the multiple elements in this set ??
# a = {1,2,3,4}
# b ={2,3,4}
# c= {2,3,6}

# print(a & b & c)


# (8) 
# name = "Patel Harsh pyhton"
# words = name.split()

# unique = set(words)
# print(len(unique))



# 
#   dictiory
# 

# 1. Create and Access Dictionary ?
# student = {
#     "name":"Harsh",
#     "age":22,
#     "city":"surat"
# }

# print(student["name"])
# print(student["city"])
# print(student["age"])
# print(student.items())


# 2 . add and new key in old dic ?

# student = {
#     "name":"harsh",
#     "age":22
# }
# student["course"] = "pyhton"
# print(student)


# 3 .updateing the value in dic ?

# student = {
#     "name":"harsh",
#     "age":22
# }
# student["age"] = 25
# print(student)


# 4 .delet the key  ?

# student = {
#     "name":"harsh",
#     "age":22
# }


# del student["age"]
# print(student)


# 5 . print all keys ?

# student ={
#     "name":"Harsh",
#     "age":22,
#     "city":"surat"
# }

# print(student.keys())
# for key in student.keys():
#     print(key)


# 6 . print all values ?

# student = {
#     "name":"harsh",
#     "age":22,
#     "city":"surat"
# }

# for key,value in student.items():
#     print(key,":",value)


# 7 . count charachter Frequency ??

# name = "programming"
# new = {}

# for i in name:
#     if i in new:
#         new[i] += 1
#     else:
#         new[i] = 1
# print(new)


# 8. student result system ??
# student = {
#     "Harsh":75,
#     "rahul":45,
#     "amit":90,
#     "jay":30
# }

# for name,marks in student.items():
#     if marks >= 50:
#         print("pass: ",name)
#     else:
#         print("fail:",name)


# 9. shopping cart system

# cart = {
#     "mobile":15000,
#     "laptop":50000,
#     "mouse":500
# }
# total = 0

# for i in cart.values():
#     total += i
# print(total)


# 10 . login system

# userss = {
#     "username":"sneha",
#     "password":"1234"
# }

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username in userss["username"] == username and userss["password"] == password:
#     print("Login successful")

# else:
#     print("Invalid username or password")


# 11 . invenstoy system ?

# product = {
#     "apple":20,
#     "banana":0,
#     "orange":15
# }

# for product,quantity in product.items():
#     if quantity > 0 :
#         print("in stock: ",product)
#     else:
#         print("out stock: ",product)




# 
#   function
# 


# q1. print user name using fuction ?

# def show(name):
#     print(name)

# show("Harsh")


# 2. find square of number ?


# def square(num):
#     return num*num

# print(square(5))

# 3. Check even or odd ?

# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "ODD"
    
# print(check(5))


# 4 .function with *args ?

# def total (*number):
#     print(number)

# total(10,20,30,40,50)


# 5 . function with **kwarge ?

# def user(**data):
#     print(data)

# user (name="harsh",age=22)


# 6. lamda function ?

# square = lambda x:x*x
# print(square(5))



# 7. recersion function ?

# n = 0
# def fibbno(n):
#     if n == 0 :
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibbno(n-1) + fibbno(n-2)
    
# a = 10 

# for i in range(a):
#     print(fibbno(i),end=" ")


# 8. decorate function ?

# def hello(func):
#     def h():
#         print("hello")
#         func()
#     return h


# @hello
# def new():
#     print("all")
# new()


# 9.
# def star(n):
#     for i in range(1,n+1):
#         print("*"*i)
# star(5)

# 10 . 
    # local variables scope

# def demo():
#     x = 10
#     print(x)

# demo()


# 11 . global variable ?

# x = 100
# def demo():
#     print(x)

# demo()

# 12. find maximum number using function ..?

# def maximum(a,b):
#     if a> b:
#         return a
#     return b
# print(maximum(10,20))


# 
# 
# 