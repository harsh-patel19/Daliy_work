# rows = int(input("Enter the Number: "))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1 ):
#         print("*",end=" ")
#     print()



# for i in range(rows):
#     print("*"*i)

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1 ):
#         if j == 0 or j == 2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()    


# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1 ):
#         if j == 0 or j == 2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()  


# FIND THE ARMSTORNGE NUMBER :

# num = int(input("Enter the number: "))
# temp = num
# sum = 0

# while temp>0:
#     digit=temp%10
#     cube = digit**3
#     sum = sum+cube
#     temp //=10


# while temp > 0:
#     digit = temp %10
#     cube = digit**3
#     sum = sum + cube
#     temp //=10

# while temp > 0:
#     digit = temp % 10
#     sum = sum * 10 + digit
#     temp //= 10

# for i in range(2,num):
#     if num % i == 0:
#         sum =1
#         break
# if sum == 0:
#     print("prime")
# else:
#     print("not prime")

# if sum == num:
#     print("Armstong")
# else:
#     print("Not")


# num = [10,20,30,40,50,60]
# num.sort()
# print(num[-1])

# text = "Dhruvika"
# vowel ="aeiou"
# count = 0

# for i in text:
#     if i in vowel:
#         count += 1
# print(count)


# a = "harsh"
# rev =""
# for i in a:
#     rev = i + rev
# print(rev)

# number = "harsh"
# print(number[::-1])

# list1 = [1,2,3,4,5,6]
# list2 = [1,2,4,5,6]

# result = list(set(list1)& set(list2))
# print(result)

# number = 4
# fact = 1
# for i in range(1,number+1):
#     fact =fact*i
# print(fact)

# list1 = [1,20,30,40,50,40]

# list1=list(set(list1))
# print(list1)



# a = 20
# b = 10

# a,b = b,a
# print(a,b)

