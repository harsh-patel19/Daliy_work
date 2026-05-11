# rows = int(input("Enter the number: "))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")



# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print(" ")




# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print(" ")

# for i in range(rows-2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print(" ")



# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# for i in range(rows-2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")



# **************************************************************************

# number = int(input("Enter the number: "))
# temp = number
# sum = 0

# while temp > 0 :
#     digit = temp % 10
#     cube = digit**3
#     sum = sum + cube
#     temp //=10
# if sum == number:
#     print("Aemstorne")
# else:
#     print("Not")

# while temp > 0 :
#     digit = temp % 10 
#     sum = sum*10 + digit
#     temp //= 10 
# if sum == number:
#     print("palindrom")
# else:
#     print("not")

# number = 5
# fact = 1

# for i in range(1,number+1):
#     fact = fact*i

# print(fact)


# name = "Patel"
# vowel = "aeiou"
# count = 0 

# for i in name:
#     if i in vowel:
#         print([i])
#         count +=1
# print(count)
  
# num = 11
# flage = 0 

# for i in range(2,num):
#     if num % i == 0 :
#         flage = 1
#         break
# if flage == 0 :
#     print("prime")
# else:
#     print("not")


# list1 = [10,20,30,40,50,60,10,20,30,40]
# list1 = list(set(list1))
# print(list1)


# list1 = [1,2,3,4,5,6,7,8]
# list2 = [8,7,9,6,4,5,2,3,1,2]


# new = list(set(list1) &set(list2))
# print(new)