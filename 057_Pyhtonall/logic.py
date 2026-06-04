# number = int(input("Enter the number: "))
# temp = number
# sum = 0

# while temp > 0 :
#     digit = temp % 10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10

# if sum == number:
#     print("ARMSTORNG NUMBER")
# else:
#     print("Not Number")



# while temp > 0 :
#     digit = temp % 10
#     sum = sum*10 + digit
#     temp //= 10

# if sum == number:
#     print("Palindrom")
# else:
#     print("Not")


row = int(input("Enter the number: "))

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
    
#     print()


#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# for i in range(row-2,-1,-1):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
    
#     print()


#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


# for i in range(row-2,-1,-1):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


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
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(row -2,-1,-1):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for j in range(2 * i +1):
#         if j == 0 or j ==2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# for i in range(row):
#     for j in range(row):
#         if i ==0  or j == 0 or i==row-1 or j==row-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# for i in range(row,0,-1):

#     for j in range(i -1):
#         print(" ",end=" ")
#     for k in range(row -i +1):
#         print("*",end=" ")

#     print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


