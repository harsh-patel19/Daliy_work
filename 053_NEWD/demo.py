# num = int(input("ENTER THE NUMBER: "))
# temp = num
# sum = 0

# while temp > 0 :
#     digit = temp % 10 
#     cube = digit**3
#     sum = sum + cube
#     temp //=10

# if sum == num:
#     print("ARMSTORNGE NUMBER")
# else:
#     print("Not")


# while temp > 0 :
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //=10 

# if sum == num:
#     print("ARMSTORNGE")
# else:
#     print("not")


# num = 5
# fact =1 
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

# n = 0

# def fibbanoic(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibbanoic(n-1) + fibbanoic(n-2)
    
# a = 10
# for i in range(a):
#     print(fibbanoic(i),end=" ")


# name = "Patel"
# vowel = "aeiou"

# for i in name:
#     if i in vowel:
#         print(i)

# lis1 = "silent"
# list2 = "silent"

# if sorted(lis1) == sorted(list2):
#     print("is anagram")
# else:
#     print("not")


# a = 20 
# b = 10 

# a,b = b,a
# print(a,b)

# rows = int(input("Enter the number: "))


# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
    
#     print()

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2* i +1 ):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2* i +1 ):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
    
#     print("")

# for i in range(rows-2,-1,-1):
#     for j in range(rows - i - 1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
    
#     print("")

# rows = int(input("enter the number: "))
# for i in range(rows,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


