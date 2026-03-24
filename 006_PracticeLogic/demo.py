
####### Q1  Write program to reverse string #######..
   
# text = "python"
# rev = ""

# for i in text:
#     rev = i + rev
# print(rev)


# text = "Dhruvika"
# rev =""

# for i in text:
#     rev = i +rev
# print(rev)


############# Q2  Write program to Count Vowels #######.

# text = "pyhton django"

# vowels = "aeiou"
# count = 0

# for i in text:
#     if i in vowels:
#         count += 1
# print(count)



# a = "shiva"
# b = "aeiou"
# count = 0

# for i in a:
#     if i in b:
#         count += 1
# print(count)


############# Q3  Write program to Second Largest Number #######.


# nums = [10,20,30,40,50,60,71,82,100,500]

# nums.sort()
# print(nums[-2])



############# Q4  Patterns  #################

# *                     
# * *               
# * * *
# * * * *


# * * * * * 
# * * * *
# * * *
# * *
# *


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# for i in range(1,5):
#     print("*"*i)


# rows = int(input("enter number :"))

# for i in range(rows ,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")
#     print()


############# Q5 Nested Dictionary  #######.

# users = {
# "u1":{"age":25,"active":True},
# "u2":{"age":30,"active":False},
# "u3":{"age":22,"active":True}
# }

# Find:

# Total Users
# Active Users
# Maximum Age

# total = len(users)

# active = 0

# for  i in users.values():
#     if i["active"]:
#         active += 1

# max_age = max(i["age"] for i in users.values())

# print(total)
# print(active)
# print(max_age)


######################## Swap Two Numbers (Without Third Variable) ###############

# a = 10
# b = 20

# a,b = b,a

# print(a,b)

############### Find largest Number in list ###############

# nums = [10,20,30,40,50,60]

# largest = nums[0]

# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)


############# RRMOVE DUPILCATES #################

# nums = [10,20,30,40,50,60,10,20]

# nums = list(set(nums))
# print(nums)

###########################################   VERSION CHNAGE ##############################################################

# def version(v):
#     major, minor , patch = map(int,v.split("."))

#     patch += 1 
#     if patch == 100:
#         patch = 0
#         minor += 1
#     if minor == 100:
#         minor = 0
#         major += 1

#     return f"{major}.{minor}.{patch}"

# print(version("1.99.99"))


############################ Patterns Dimond ##################################


# n = 5 

# # Upper half
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # # # Lower half
# for i in range(n - 2, -1, -1):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# _______________________________________________
# _______________________________________________
# n = int(input("number: "))
# for i in range(n):
#     for j in range(n -i -1):
#         print(" ",end="")
#     for j in range(2 *i +1):
#         if j == 0 or j == 2 * i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# for i in range(n -2, -1, -1):
#     for j in range(n -i -1):
#         print(" ",end="")
#     for j in range(2 *i +1):
#         if j == 0 or j == 2 * i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# rows = int(input("Enter the Number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i +1):
#         print("*",end=" ")
#     print("")


# for i in range(rows ,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()




# num = int(input("Enter the Number: "))
# flag = 0

# for i in range(2,num):
#     if num % i == 0:
#         flag =1
#         break

# if flag == 0:
#     print("PRIME")
# else:
#     print("NOT PRIME")



# num = int(input("Enter the number: "))
# temp = num
# sum = 0

# while num !=0 :
#     rem = num % 10
#     sum = sum*10 +rem
#     num //=10
# if temp == sum:
#     print("palidrom")
# else:
#     print("not palindrom")



# while temp>0:
#     digit= temp %10
#     cube = digit**3
#     sum = sum+cube
#     temp //=10

# if sum == num:
#     print("Armstrong..")
# else:
#     print("Not Armstrong...")

