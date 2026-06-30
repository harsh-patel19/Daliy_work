#  -----  PRINT THE SIMPLE USING FOR LOOP FRINT ONE BY ONE ------ ?

# number = [1,2,3,4,5]
# for i in number:
#     print(i)


#  -----  print the revser the loop without any bulit function  ------ ?

# number = [1,2,3,4,5]
# rev =[]

# for i in number:
#     rev = [i] + rev
# print(rev)


#  -----  COUNT HOW MANY TIME FOR REPET IN ELEMENTS IN spicfeic elemets repeat LIST  ------ ?

# number = [5,1,2,3,4,2,3]
# count = 0

# for i in number:
#     if i == 2:
#         count += 1
# print(count)


#  -----  COUNT HOW MANY TIME FOR REPET IN ELEMENTS list ------ ?

# number = [5,1,2,3,1,2,4]
# count = {}

# for i in number:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)



#  ----- TAKE 10 number in user store it in list  ------ ?

# new  = []

# for i in range(10):
#     user = int(input("number"))
#     new.append(user)
# print(new)



#  ----- FIND THE EVEN AND ODD NUMBER USING THE LIST ------ ?

# number = [1,2,3,4,5,6,7,8]
# even = []
# odd = []

# for i in number:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


#  ----- FIND THE maxmuim number in list ------ ?


# number = [1,2,4,5,6]
# max_num = 0

# for i in number:
#     if i > max_num:
#         max_num = i
# print(max_num)


#  ----- FIND THE seocund mamium number in list ------ ?

# number = [1,2,4,5,6]
# max_num = 0
# sec_num = 0

# for i in number:
#     if i > max_num:
#         sec_num = max_num
#         max_num = i
# print(sec_num)
    


#  ----- CHECK LSIT IN PALINDORM YA NOT ------ ?

# lst = 10,10,10

# if lst == lst[::-1]:
#     print("palindrom")
# else:
#     print("not")


#  ----- FIND THE COOMAN LEMENTS BETWEEN TWI LISTS ------ ?

# lst = [1,2,4,5,6]
# lst1 = [2,4,5,7,8,9]

# lstnew = (set(lst) & set(lst1))
# print(lstnew)



# lst = [1,2,4,5,6]
# lst1 = [2,4,5,7,8,9]

# comman = []

# for i in lst:
#     if i in lst1:
#         comman.append(i)
# print(comman)


#  ----- MOVE ALL ZERO IN THE LAST OF LIST ------ ?


# lst = [1,2,3,4,0,0,0,9,8,7,6,5,1]
# result = []

# for i in lst:
#     if i != 0 :
#         result.append(i)
# for i in lst:
#     if i == 0:
#         result.append(i)
# print(result)


#  ----- PRINT THE VOWLES IN STING INTO LIST ------ ?

# name = "dhruvika"
# vowels = "aeiou"

# count = 0

# for i in name:
#     if i in vowels:
#         count += 1
# print(count)


#  ----- PRINT THE VOWLES IN STING INTO LIST ------ ?
