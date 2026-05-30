# 1.


# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

rows = int(input("enter the number: "))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 


# 2...



#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# for i in range(rows):
#     for j in range(rows - i -1):
#         print(" ",end=" ")
#     for k in range(2*i +1):
#         print("*",end=" ")

#     print()


# 3 

#       *
#     * *
#   * * *
# * * * *

# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end=" ")
    
#     print()


# 4 

# * * * * *
# *       *
# *       *
# * * * * *

# for i in range(rows):
#     for j in range(rows):
#         if i ==0  or j == 0 or i==rows-1 or j==rows-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# 5

# *
# * *
# *   *
# *     *
# * * * * *

# for i in range(rows):
#     for j in range(i + 1):
#         if j == 0 or j ==i or i ==rows -1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# 6 
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 
# for i in range(rows):
#     for j in range(rows - i -1):
#         print(" ",end=" ")
#     for k in range(2*i +1):
#         print("*",end=" ")

#     print()

# for i in range(rows -2,-1,-1):
#     for j in range(rows - i -1):
#         print(" ",end=" ")
#     for k in range(2*i +1):
#         print("*",end=" ")

#     print()


# 7 . 

# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *

# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end="")

#     for j in range(2*(rows-i)):
#         print(" ",end="")

#     for j in range(i):
#         print("*",end="")

#     print()



# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end="")

#     for j in range(2*(rows-i)):
#         print(" ",end="")

#     for j in range(i):
#         print("*",end="")

#     print()


# 8..

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# for i in range(1,rows +1):
#     for j in range(1,i +1):
#         print(j,end=" ")
#     print()


# 9 .

# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print()


# 10 ..

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

# num = 1

# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end=" ")
#         num += 1

#     print()


# 11. 

