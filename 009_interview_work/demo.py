

# rows = int(input("Enter the number: "))

# (1)
# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")
#     print()


# (2)
# for i in range(rows ,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# (3)

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2*i




# num=int(input("Enter the number:"))
# sum=0 
# temp=num
# while temp>0:
#     digit=temp%10
#     cube=digit**3 
#     sum=sum+cube
#     temp//=10
# if sum==num:
#     print("Armstrong..")
# else:
#     print("Not Armstrong..")




# number = 12
# flag = 0

# for i in range(2,number):
#     if number % i ==0:
#         flag=1
#         break
#     if  flag == 0:
#         print("prime")
#     else:
#         print("not prime")

# number = 5
# fact = 1

# for i in range(1,number+1):
#     fact = fact*i

# print(fact)




# nums = [10,2030,50,20,30,30,40,10,20,30,50]
# nums = list(set(nums))
# print(nums)


# s = input("Enter string: ")

# rev = s[::-1]
# print(rev)


# num = int(input("enter the number: "))
# temp = num
# sum = 0

# while num !=0 :
#     rem = num % 10
#     sum = sum*10 +rem
#     num //=10
# if temp == sum:
#     print("palidrom")
# else:
#     print("no palidrom")





# num = int(input("Enter the number: "))
# flag = 0

# for i in range(2,num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 0 :
#     print("PRIME")
# else:
#     print("NOT PRIME")





# a = 20 
# b = 10

# a,b = b,a
# print(a,b)




# numbers = [10.0,10,10,10,20,30,40,50,60,70,80,90,100,100.0,222]

# # Largest number in the stirng
# print(max(numbers))

# # Print sortest number in the list
# print(min(numbers))

# # Find the sum of all number 
# print(sum(numbers))

# # Count the occurence of number 
# print(numbers.count(10))

# # REverse the string 
# print(numbers[::-1])

# # Remove the dupications from the list
# num = list(set(numbers))
# print(num)

# # Frind the second largest from the list
# numbers.sort()
# print(numbers[-2])

# check is list in sub list or not usiing set
# list1 = [1,2,3,4,5,2,2,2,6]
# list2 = [8,2,6,4,52,4,6]

# result = list(set(list1)& set(list2))
# print(result)

# # remove even number from the list 
# result = [n for n in list1 if n % 2 != 0]
# print(result)

# Find the second largest from the list 

# num = list(set(numbers))
# num.sort()
# print(num[1])


# check the list is sorted or not
# print(list1 == sorted(list1))

# res = [n for n in numbers if list1.count(n) == 1]
# print(res)

# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________



# rows = int(input("Enter the number: "))

# for i in range(rows):
#     for j in range(rows -i - 1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows - 2, -1, -1):
#     for j in range(rows -i - 1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1 ):
#         print(" ",end=" ")
#     for k in range(2 * i +1):
#         print("*",end=" ")
    
#     print()


# for i in range(rows , 0 , -1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(rows):
#     print("*"*i)





# num = int(input("enter the number: "))
# flage = 0

# for i in range(2,num):
#     if num % i == 0:
#         flage =1 
#         break

# if flage == 0:
#     print("prime")
# else:
#     print("not prime")


# num = 12321 
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     cube = digit **3
#     sum = sum +cube
#     temp //=10

# if sum == num:
#     print("Armstorng")
# else:
#     print("not")



# while temp > 0:
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //=10
# if num == sum:
#     print("palidrom")
# else:
#     print("not")


# text ="Harsh Patel"
# vowel = "aeiou"
# count = 0

# for i in text:
#     if i in vowel:
#         count += 1
# print(count)



# a  = "Harsh"
# rev = ""
# for i in a:
#     rev = i +rev
# print(rev)


# num = [10,20,30,40,50,60]
# num.sort()
# print(num[-1])


# users = {
# "u1":{"age":25,"active":True},
# "u2":{"age":30,"active":False},
# "u3":{"age":22,"active":True}
# }

# total = len(users)
# active = 0


# for i in users.values():
#     if i ["active"]:
#         active += 1
# print(total)