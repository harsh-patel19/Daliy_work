# num = int(input("Enter the number: "))
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp %10
#     cube = digit **3
#     sum = sum+ cube
#     temp //= 10

# if sum == num:
#     print("armstorng number")
# else:
# #     print("not")

# while temp > 0 :
#     digit = temp %10
#     sum  = sum*10 +digit
#     temp //= 10
# if sum == num:
#     print("palidrom")
# else:
#     print("not")


# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i

# print(fact)

# num = 10
# falge = 1

# for i in range(2,num):
#     if num % i ==0:
#         falge = 1
#         break
# if num == 0:
#     print("prime")
# else:
#     print("not")


# list1 = [10,20,10,20,30,40,50]
# list1 = list(set(list1))
# print(list1)


# name = "Patel"
# vowel = "aeiou"
# # count = 0

# for i in name:
#     if i in vowel:
#         # count += 1
#         print(i)

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

rows = int(input("Enter the number : "))

# for i in range(rows ,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i +1):
#         print("*",end=" ")
#     print()

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         if j == 0 or j ==2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         if j == 0 or j ==2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         print("*",end=" ")

#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         print("*",end=" ")

#     print()


