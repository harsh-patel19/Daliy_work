
##  LIST ###


# NUMBER = [1,2,3,4,5,6]
# for i in NUMBER:
#     print(i)


# NUMBER = [1,2,3,4,5,6]
# NUMBER.append(7)
# print(NUMBER)


# NUMBER = [1,2,3,4,5,6]
# NUMBER.insert(1,5)
# print(NUMBER)

#specifice number vise remove
# NUMBER = [1,2,3,4,5,6]
# NUMBER.remove(2) 

#specifice number vise remove
# NUMBER = [1,2,3,4,5,6]
# NUMBER.pop()  

# NUMBER = [1,2,3,4,5,6]
# new= len(NUMBER)
 
# print(new)

# NUMBER = [1,2,3,4,5,6]
# print(NUMBER[0])
# print(NUMBER[-1])

# NUMBER = [1,2,3,4,5,6]
# rev = NUMBER[::-1]
# print(rev)

# NUMBER = [1, 2, 3, 4, 5, 6]

# rev = []

# for i in NUMBER:
#     rev= [i] + rev 

# print(rev)

# number = [4551,1,2,4,5,3]
# number.sort()          
# number.sort(reverse=True)   # desc order ma kare 
# print(number)


# number = [15,2,5,3,55,2] 

# new = max(number)
# print(new)


# number = [15,2,3,5,6]

# news = min(number)
# print(news)


# lst = [1,4,5,6,1,23,78]

# min_num = lst[0]
# max_num = lst[0]

# for num in lst:
#     if num < min_num:
#         min_num=num
#     if num > max_num:
#         max_num= num

# print(min_num)
# print(max_num)


# Count how many times an element appears.
# number =  [15,1,2,3,4,5,6,1]
# count = 0

# for i in number:
#     if i == 2:
#         count +=1
# print(count)


# count how many time repeat in element in list?

# number =  [15,1,2,3,4,5,6,1]
# count = {}

# for i in number:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i]  = 1
# print(count)




#Take 10 numbers from user and store in list.

# new = []

# for i in range(10):
#     user = int(input("Enter number: "))
#     new.append(user)

# print(new)


# Find sum of all elements in list.

# number = [1,2,3,4,6,6]
# sum = 0 

# for i in number:
#     sum += i
# print(sum)


# Find even and odd numbers separately.?

# number = [1,2,3,4,5,6,7,8]
# even = []
# odd = []

# for i in number:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even: ",even)
# print("Odd: ",odd)


# Create a new list containing squares of numbers

# lst = [1,2,3,4,5,6,7,8,9]
# squares = []

# for i in lst:
#     squares.append(i * i)
# print(squares)


#Remove duplicate elements from list.??

# lst = [1,2,3,4,1,2,3]

# result = []


# for i in lst:
#     if i not in result:
#         result.append(i)
# print(result)



# Merge two lists. ??

# lst1 = [1,2,3,4,5,6,7,8]
# lst2 = [8,7,6,5,4,3,2,1,99]

# lst3 = lst1 +lst2
# print(lst3)



# Find second largest number. ?

# number = [1,2,3,50,90]

# largest = 0
# second = 0

# for i in number:
#     if i > largest:
#         second = largest
#         largest = i

# print(second)


# Check whether list is palindrome or not.


# lst = "aaa"

# if lst == lst[::-1]:
#     print("palindrom")
# else:
#     print("not palindrom")


# Rotate list left by 1 position.?

# lst = [1,2,3,4,5]

# result = lst[1:] + [lst[0]]

# print(result)


# Find common elements between two lists. ?

# lst = [1,2,3,4,5]
# lst1 = [2,3,45,6]

# list2 =(set(lst) & set(lst1))
# print(list2)


#Find missing number in list from 1–100. ??


# lst = [1,2,3,4,5,6,7,8,10]

# for i in range(1,11):
#     if i  not in lst:
#         print(i)


# Find missing number in list from 1–100.
# Move all zeros to end.


# lst = [10,0,0,0,0,0,2,3,4,5,6,7,8,10]

# result = []

# for i in lst:
#     if i != 0:
#         result.append(i)
# for i in lst:
#     if i == 0:
#         result.append(i)

# print(result)

# lst =[10,0,0,0,0,0,2,3,4,5,6,7,8,10]
# number =[]
# zero = []

# for i in lst:
#     if i != 0:
#         number.append(i)
#     else:
#         zero.append(i)


# new = number +zero
# print(new)
# print(zero)


# To flatten a nested list: ?

# lst = [[1,2],[3,4],[5,6]]
# result = []

# for i in lst:
#     for j in i:
#         result.append(j)

# print(result)


# Find pairs whose sum equals target.?


# print the vowles ?

# a = "python"
# vowels = "aeiou"

# for i in a:
#    if i in vowels:
#     print(i)



