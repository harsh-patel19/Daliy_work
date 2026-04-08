
# A FUNCTION IS A BLOCK OF RESUABLE CODE THAT PERFORMS A SPECIFIC TASK.


# def function_name(parameters):
#     return Value
# Arguments(like to defifne here 1,2,3,)

# ################ Why use Functions ?################

# Code reuse (DRY – Don’t Repeat Yourself)
# Easy to read and maintain
# Break big problems into small parts
# Used in real projects (like Django views, APIs)


################ TYPES OF FUNCTION ################

# BUILT-IN function
# PRINT()LEN()type()

# USER DEFINE function
# def greet():
#     print("Hello Harsh")


# Lambda (Anonymous) Function

# square = lambda x: x * x
# print(square(5))

################# Types of Arguments in Functions ################


# Positional Arguments
# POSITINAL ARGUMENT MENAS ODER BASED WORKING .
# def add(a,b):
#     print(a+b)
# add(2,3)


# Keyword Arguments
# KEYWORD ARGUMENT MEAS WORKING LIKE KEY BASED PASS USING THE NAME.
# add(a=2,b=3)

# Default Arguments

# variable-length argument

# *args (multiple values)
# ***kwargs (key-value)

# def check_even_odd(num):
#     if num % 2 ==0:
#         return "Even"
#     print(check_even_odd(10))


# def find(a,b,c):
#     return max(a,b,c)

# print(find(10,20,15))


# sum using the *args

# def total(*numbers):
#     return sum(numbers)
# print(total(1,2,3,45,6,))


# n = 0

# def fibonaccie(n):
#     if n == 0:
#         return 0 
    
#     elif n ==1:
#         return 1
#     else:
#         return fibonaccie(n-1) + fibonaccie(n-2)
# a = 5
# for i in range(a):
#     print(fibonaccie(i),end="   ")




# def revers(s):
#     return s[::-1]
# print(revers("oops"))
