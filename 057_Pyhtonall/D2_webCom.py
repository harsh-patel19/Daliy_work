# remove duplicated in without any method and buit without ...?

# lst = [1,2,3,4,1,2,3]
# result = []


# for i in lst:
#     if i not in result:
#         result.append(i)
# print(result)


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")
# revers the string without any method..?


# name = "Harsh"
# rev = ""

# for i in name:
#     rev = i  +rev
# print(rev)



# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")
# find the list off the secound largest number to print..?

# lst = [1,2,3,4,1,2]
# large = 0
# second = 0 

# for i in lst:
#     if i > large:
#         second = large
#         large = i
# print(second)

# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# row = int(input("Enter the number: "))
# for i in range(row,0,-1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(row - i +1):
#         print("*",end=" ")

#     print()


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")
# count the sting len ..?


# str = "Hello World"
# count = 0 

# for i in str:
#     count +=1
# print(count)


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


# row = int(input("Enter the number: "))


# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")


# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 
# row = int(input("Enter the number: "))

# for i in range(row):
#     for j in range(row):
#         if i == 0 or j ==0 or i==row -1 or j ==row -1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()



# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
# row = int(input("Enter the number: "))

# for i in range(row):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 *i +1):
#         print("*",end=" ")
#     print()



# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")

#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# for i in range(row -2,-1,-1):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 *i +1):
#         print("*",end=" ")
#     print()


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")
#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 
#   *           * 
#     *       * 
#       *   * 
#         * 


# for i in range(row):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for j in range(2*i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(row -2,-1,-1):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for j in range(2*i +1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# print("_ __ _ _ _ _ _  _  _ _ __ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _")


# ****************** ARRAY **********************


# Arrays = [5,8,7,6,3,2,1,4]
# result = 6 


# for i in Arrays:
#     for j in Arrays:
#         if i + j == result and i != j :
#             print(i,j)





# num = 5
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i

# print(fact)

# row = int(input("ENTER THE NUMBER: "))

# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


# for i in range(row,0,-1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(row - i +1):
#         print("*",end=" ")
    
#     print()


# for i in arr:
#     for j in arr:
#         if i +j == total and i != j:
#             print(i,j)


# for i in range(row,0,-1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(row -i +1):
#         print("*",end=" ")

#     print()


# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()