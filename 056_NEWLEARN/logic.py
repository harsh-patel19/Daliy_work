
# 1. write the fibbanoic seriros in using the function ?

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




# 2 . write the program print armstornge number ?


# num = int(input("Enter the Number: "))
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     cube = digit **3
#     sum = sum + cube
#     temp //=10

# if sum == num:
#     print("armstoneg number")
# else:
#     print("not")




# 3. print the prime and  not prime number ?



# for i in range(2,num):
#     if num % i == 0:
#         flage = 1
#         break

# if num == 0 :
#     print("prime")
# else:
#     print("not")


# 4.  print te prime and not prime number ?

# num = 17
# flag = 0

# for i in range(2,num):
#     if num % i == 0:
#         flag =1
#         break
# if flag == 0:
#     print('PRIME NUMBER')
# else:
#     print("NOT PRIME NUMBER")


# 5. write the palindorm number?

# num = int(input("Enter the number: "))
# temp  = num
# sum = 0 

# while temp > 0:
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //=10
# if sum == num:
#     print("PALIDROM")
# else:
#     print("NOT")


# 6. Print the element same as a a old element ya not ?
# a = "oops"
# b = "spoo"

# print(sorted(a) == sorted(b))


# 7. print the and count the vowles?

# name =  "Patel"
# vowels = "aeiou"
# count = 0 

# for i in name:
#     if i in vowels:
#         print(i)
#         count += 1
# print(count)


# 8. print the leap years ?

# year = int(input("Enter the number: "))

# if(year%400==0):
#     print("leap year")
# elif(year%100==0):
#     print("not leap year")
# elif(year%4==0):
#     print("leap year")
# else:
#     print("not leap year")

# 9. number even and odd print ?

# num = int(input("Enter the number: "))

# if num % 2 ==0:
#     print("Even")
# else:
#     print("odd")


# 10. print the negative,postive,zero ?

# num = int(input("Enter the number: "))

# if(num>0):
#     print("postive")
# elif(num<0):
#     print("negitive")
# else:
#     print("zero")


# 11 . find largest amog three number ?

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))

# if(num1>num2 and num1>num3):
#     print("number is 1 largest")
# elif(num2>num1 and num2>num3):
#     print("number 2 is largest")
# elif(num3>num1 and num3>num2):
#     print("number 3 is largest")
# else:
#     print("same number all")


# 12 swap two number chnage without third variable ?

# a = 10 
# b = 20 

# a,b = b,a
# print(a,b)

# a = 10 
# b = 20 

# a = a + b
# b = a- b
# a = a-b

# print(a,b)



# 13.find the factorial number?

# number = 5
# fact = 1

# for i in range(1,number+1):
#     fact = fact*i
# print(fact)


# 14 . table maltifications ?


# num= int(input("Enter the number: "))

# for i in range(1,11):
    # print(num,"x",i,"=",num*i)
    # print(num*i)


# 15. find sum of first a natural number ?


# num= int(input("Enter the number: "))

# sum = 0

# for i in range(1,num+1):
#     sum+=i
# print(sum)




#16 . reevers a number ?



# num= int(input("Enter the number: "))

# rev = 0 

# while num > 0 :
#     digit = num % 10 
#     rev = rev*10 + digit
#     num=num//10

# print(rev)



# 17. count the digit in a number ?

# num= (input("Enter the number: "))

# digit = 0

# for i in num:
#     digit += 1

# print(digit)



# 18. check weather a string ia palindrome or not ?

# string = input("rnter the string: ")
# rev = string[::-1]

# if string == rev:
#     print("string is palindrom")
# else:
#     print("string is not palindrom")



    
# 19 . find power of eny number without using the ** ?

