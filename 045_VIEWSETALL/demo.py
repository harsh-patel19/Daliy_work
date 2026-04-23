# import random

# FIRSTNAME = input("ENTER NAME: ")
# LASTNAME = input("ENTER NAME: ")

# if len(FIRSTNAME) < 2 or len(LASTNAME) < 2 :
#     print("please add the both two number is same")
# else:
#     part_1 = FIRSTNAME[:2]
#     part_2 = LASTNAME[-2:]

#     randomnumber = random.randint(1000,9999)
#     passsword = part_1 + part_2 + str(randomnumber)

#     print("password:", passsword)


# num = int(input("enter the number: "))
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     cube = digit**3
#     sum = sum + cube
#     temp //=10

# if sum == num:
#     print("armstornge number")
# else:
#     print("not")

# while temp > 0 :
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //=10 

# if sum == num:
#     print("palidrom")
# else:
#     print("not")


# num = 10
# flage = 0

# for i in range(2,num):
#     if num % i == 0:
#         flage = 1
#         break
# if flage == 0:
#     print("prime")
# else:
#     print("not")

# number = 5
# fact = 1

# for i in range(1,number+1):
#     fact = fact*i
# print(fact)

# n = 0 

# def fibbanoice(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibbanoice(n-1) + fibbanoice(n-2)
    
# a = 10
# for i in range(a):
#     print(fibbanoice(i),end="  ")

# name = "Patel"
# vowel ="aeiou"
# count = 0

# for i in name:
#     if i in vowel:
#         count += 1
# print(count)

# list1 = [10,10,20,20,30,40,50]
# list1 = list(set(list1))
# print(list1)

# name = "Patel"
# print(name[::-1])

# a = 20 
# b = 10 

# a,b = b,a
# print(a,b)



# rows = int(input("Enter the number: "))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2* i +1):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2* i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2* i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2* i +1):
#         print("*",end=" ")
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     print()


# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2* i +1):
#         print("*",end=" ")
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# for i in range(rows - 1):
#     for j in range(rows - i - 1):
#         print("*", end=" ")
#     print()



# for i in range(rows):
#     for j in range(i + 1):
#         print((i + j) % 2, end=" ")
#     print()


