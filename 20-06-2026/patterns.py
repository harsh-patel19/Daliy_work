row = int(input("Enter the number: "))

#      * 
#     * * 
#   * * * 
# * * * * 

# for i in range(row,0,-1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(row -i -1):
#         print("*",end=" ")

#     print()

 
#  print("--------------------------------------------------------------")


# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


#  print("--------------------------------------------------------------")


# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# for i in range(row):
#     for j in range(row):
#         if i == 0 or j == 0 or i==row-1 or j==row-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()


#  print("--------------------------------------------------------------")

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# for i in range(row):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")

#     print()


#  print("--------------------------------------------------------------")


#   * * * * * * * 
#     * * * * * 
#       * * * 
#         *   

# for i in range(row-2,-1,-1):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")

#     print()


#  print("--------------------------------------------------------------")

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
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")

#     print()


# for i in range(row-2,-1,-1):
#     for j in range(row -i -1):
#         print(" ",end=" ")
#     for k in range(2 * i + 1):
#         print("*",end=" ")

#     print()



#  print("--------------------------------------------------------------")


#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 


# for i in range(row):
#     for j in range(row - i -1):
#         print(" ",end= " ")
#     for j in range(2 * i + 1):
#         if j == 0 or j ==2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()



#  print("--------------------------------------------------------------")

#   *           * 
#     *       * 
#       *   * 
#         * 

# for i in range(row -2,-1,-1):
#     for j in range(row - i -1):
#         print(" ",end= " ")
#     for j in range(2 * i + 1):
#         if j == 0 or j ==2*i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()
