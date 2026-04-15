# num = int(input("ENTER THE NUMBER: "))
# temp = num
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     cube = digit**3
#     sum = sum+cube
#     temp //=10

# if sum == num:
#     print("Armstronge")
# else:
#     print("not")


# while temp > 0:
#     digit = temp %10
#     sum = sum*10 + digit
#     temp //=10

# if sum == num:
#     print("palidndrom")
# else:
#     print("not")

# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i
# print(fact)


# num = 2
# falge = 1

# for i in range(2,num):
#     if num % i == 0:
#         falge = 1
#         break
# if num == 0:
#     print("prime number")

# else:
#     print("Not prime")

# list1 = [10,20,10,30,40,50]
# list1 = list(set(list1))
# print(list1)


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


# rows = int(input("Enter the number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#             print("*",end=" ")
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     print()


# for i in range(rows -2,-1,-1):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i + 1):
#             print("*",end=" ")
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     print()


# for i in range(rows,0 ,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(rows,0,-1):
#     for j in range(rows - i):
#         print(" ",end=" ")
#     for k in range(2* i -1):
#         print("*",end=" ")
#     print()


# for i in range(2,rows +1):
#     for j in range(rows - i ):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2* i +1):
#         print("*",end=" ")
    
#     print()
    


# text = "pyhton programming"
# vowels = "aeiou"

# for ch in text:
#     if ch in vowels:
#         print(ch)


##################### Removing all the punctuation from the string ########################################

# import string

# fruit = "banana!!! , grapes"
# result = fruit.translate(str.maketrans('','',string.punctuation))
# print(result)

# fruit = "banana!!! , grapes"
# result = fruit.translate(str.maketrans('','',string.punctuation))
# print(result)

# fruit = "sneha!!@@@!!# , nayska"
# result = fruit.translate(str.maketrans('','',string.punctuation))
# print(result)


##################### Check two string in the same rotation ########################################

# strA = "abcd"
# strB = "cdab"

# print(len(strA) == len(strB) and strB in strA + strA)


##################### Check the string Anagram  = for example { listen | silent } every character of first string present is same as second string ##########################################

# lis = "csawdw"
# lis1 = "silent"

# if sorted(lis) == sorted(lis1):
#     print("is Anagram")
# else:
#     print("not Anagram")
