##################### Removing all the punctuation from the string ########################################

# import string

# fruit = "banana!!! , grapes"
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



#################### FIBBNACCIO FUNCTION #################

# def fibbnaccio(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibbnaccio(n-1) + fibbnaccio(n-2)
    
# a = 10
# for i in range(a):
#     print(fibbnaccio(i),end=" ")




####################  PATTERNS    #########################

# rows = int(input("Enter number: "))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


####################  PATTERNS    #########################

# rows = int(input("Enter number: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2 *i +1):
#         print("*",end=" ")
    
#     print()


# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ",end=" ")
#     for k in range(2* i +1):
#         print("*",end=" ")
    
#     print()
    

##################### Remove Duplicates from List ########################################

# list1 = [1,2,2,3,4,4,5]

# unique = list(set(list1))

# print(unique)


#####################    Find Largest Number in List  #####################

# num = [10,5,5,63,80,100]
# largest = num[0]

# for i in num:
#     if i > largest:
#         largest = i

# print(largest)

#####################   Revers string   #####################


# s = input("Enter string: ")
# rev = s[::-1]
# print("Reverse:", rev)


##################### ODD EVEN NUMBER #####################

# number = 12

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


##################### PRIME NUMBER #####################

# number = 12
# flag = 0

# for i in range(2,number):
#     if number % i == 0:
#         flag = 1
#         break
#     if flag == 0 :
#         print("prime")  

#     else: 
#         print("not prime")

##################### FACTORIAL NUMBER #####################

# number = 5
# fact = 1

# for i in range(1,number +1):
#     fact = fact*i



# print(fact)

##################### DIMAND HOLO PATTERNS #####################

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

# # Lower half
# for i in range(n - 2, -1, -1):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


########## vowels number ###########

# text = "pyhton programming"
# vowels = "aeiou"

# for ch in text:
#     if ch in vowels:
#         print(ch)


########## Using count() method ##########



# text = "python programming"
# vowels = "aeiou"
# count = 0

# for v in vowels:
#     count += text.count(v)

# print("Total vowels:", count)


########  Using list comprehension ################


# text = "pyhton programming "
# vowels = [ch for ch in text if ch in "aeiou"]

# print(vowels)


######## ACTIVE USER CHECK TO FIND MAXMIMUM AND NAME ################

# users = [

#     {"name": "Harsh", "marks": 80, "active": True},
#     {"name": "Rahul", "marks": 90, "active": False},
#     {"name": "Amit", "marks": 95, "active": True},
#     {"name": "Neha", "marks": 70, "active": True}
# ]
# max_marks = 0
# top_user = ""
# for user in users:
#     if user["active"] and user["marks"] > max_marks:
#         max_marks = user["marks"]
#         top_user = user["name"]

# print("Top Activate USER :",top_user)
# print("MARKS: ",max_marks)


######## ACTIVE USER CHECK TO  ################


# users = [
#     {"name": "Harsh", "active": True},
#     {"name": "Rahul", "active": False},
#     {"name": "Amit", "active": True}
# ]

# for user in users:
#     if user["active"]:
#         print(user)
   



# number = 121
# temp = number
# sum = 0

# while number!=0:
#     rem = number%10
#     sum = sum*10 + rem
#     number //=10


#     if temp == sum:
#         print("pelindrom")
#     else:
#         print("Not pelidrom")