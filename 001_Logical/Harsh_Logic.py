# 1. PRINT THE PALINDORM NUMBER 


# num = int(input("Enter the Number: "))
# a = num 
# b = 0

# while num > 0 :
#     digit = num % 10
#     b = b*10 + digit
#     num = num // 10

# if a == b:
#     print("Palidrom number")
# else:
#     print("Not Palindorm Number")


# 2. Find the fibbonaci number 

# n = 0

# def fibbonaci(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibbonaci(n-1) + fibbonaci(n-2)
    
# a = 10
# for i in range(a):
#     print(fibbonaci(i),end=" ")


# 3. PRINT THE PRIME OR NOT PRIME NUMBER 


# num = 2
# flag = 0

# for i in range(2,num):
#     if num % i == 0:
#         flag =1
#         break
# if flag == 0:
#     print('PRIME NUMBER')
# else:
#     print("NOT PRIME NUMBER")


# 4. FACTORIAL NUMBER 

# number = 4
# fact =1

# for i in range(1,number+1):
#     fact = fact*i

# print(fact)



# 5. FIND LARGEST NUMBER IN LIST

# num =  [10,5,63,45,6,85,55343]

# larget = num[0]

# for i in num:
#     if i > larget:
#         larget = i
# print(larget)





# 7 . ODD EVEN NUMBER 


# NUMBER = int(input("ENTER THE NUMBER: "))


# if NUMBER % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")



# 8 . count the vowels number 


# a = "pyhton"
# b = "aeiou"
# count = 0

# for i in a:
#     if i in b:
#         count += 1
# print(count)



# a = "pyhton"
# b = [ch for ch in a if ch in "aeiou"]
# print(b)



# 9 . remove duplications 

# nums = [10,20,30,40,5,60,10,20,40,50,60]
# nums = list(set(nums))
# print(nums)


             #    -: PATTERNS :-   #

# rows = int(input("Enter the Number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1 ):
#         print("*",end=" ")

#     print(" ")


# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")


# for i in range(rows):
#     print("*"*i)


# for i in range(rows):
#     for j in range(rows -i -1):
#         print("",end=" ")
#     for j in range(2 * i + 1 ):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print("")


# for i in range(rows -2 ,-1,-1):
#     for j in range(rows -i -1):
#         print("",end=" ")
#     for j in range(2 * i + 1 ):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print("")





# users = {
#     "user1":"active",
#     "user2":"inactive",
#     "user3":"active",
# }

# count = 0

# for key in users:
#     if users[key] == "active":
#         count += 1
    
# print(count)


# marks = {

#     "ram":40,
#     "harsh":50,
#     "patel":30,
# }

# count = 0

# for i in marks:
#     if marks[i] >= 35:
#         count += 1
    
# print(count)




# n = int(input("Enter numbers: "))

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
    
#     for j in range(2 * (n - i - 1)):
#         print(" ", end="")
    
#     for j in range(i + 1):
#         print("*", end="")
    
#     print()
    
# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
    
#     for j in range(2 * i):
#         print(" ", end="")
    
#     for j in range(n - i):
#         print("*", end="")
    
#     print()


