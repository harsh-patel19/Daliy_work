# number = int(input("Enter the Number: "))
# temp = number
# sum = 0

# while temp > 0 :
#     digit = temp % 10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10
# if sum == number:
#     print("ARMSTORNGE NUMBER")
# else:
#     print("NOT")


# while temp > 0 :
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //= 10
# if sum == number:
#     print("palidrom")
# else:
#     print("not")


# number = int(input("Enter the Number: "))
# falge = 0

# for i in range(2,number):
#     if number % i == 0:
#         falge = 1
#         break
# if falge == 0:
#     print("prime")
# else:
#     print("not prime")
  

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i
# print(fact)


# number = [10,20,30,40,50,10,20,30]
# number = list(set(number))
# print(number)

# s = "harsh"
# rev = s[::-1]
# print(rev)

rows = int(input("Enter the Number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2*i +1):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 *i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 *i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
    