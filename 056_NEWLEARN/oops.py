# class Student:

#     def dem0(self):    #self represents current object.
#         print("Hello student")

# s1 = Student()
# s1.dem0()



# 2 . Constructor __init__??

# class student:

#     def __init__(self):
#         print("done")

# s1 = student()


# 3. Parameterized Constructor ??

# class student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

    
#     def display(self):
#         print(self.name)
#         print(self.age)


# s1 = student("Harsh",22)
# s1.display()
        

 
#  4. class method ? 

# class employee:

#     company = "google"

#     @classmethod
#     def show(cls):
#         print(cls.company)

# employee.show()



# 5. inheritance some example in oops ?

#  single inheritance ??

# class Father:

#     def bike(self):
#         print("bike")

# class son(Father):

#     def mobile(self):
#         print("iphone")
 

# s1 = son()
# s1.bike()
# s1.mobile()



# 6 . multiple inheritance ??


# class father:
#     def mony(self):
#         print("nice")


# class Mother:
#     def gold(self):
#         print("Good")


# class child(father,Mother):
#     pass

# c = child()
# c.mony()
# c.gold()


# 7 . multilevel inheritance ???

# class A:
#     def show(self):
#         print("hello")

# class b(A):
#     def show1(self):
#         print("hey")

# class c(b):
#     def show2(self):
#         print("nice")


# s1 = c()
# s1.show()
# s1.show1()
# s1.show2()


# 8 . Polymorphisum in pyhton 
# same function name ,differnt behaviour but 

# class animanl:
#     def sound(self):
#         print("yeahhh")

# class dog(animanl):
#     def sound(self):
#         print("owwww")

# d = dog()
# d.sound()


#  9 . Encapsulation in pyhton ??

# encapsulation means hididng and protecting data inside a class:
    
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
# p1 = Person("tobias",24)
# print(p1.get_age())


# 10 . employee management system ?


# class Employee:
#     company = "infosys"

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

    
#     def display(Self):
#         print(Self.name)
#         print(Self.salary)

# e1 = Employee("Harsh",50000)
# e1.display()


# 11 . 

# Bank system : -

# class student:

#     def __init__(self,name,age,email,course):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.course = course


#     def display(self):

#             print("--- student details---") 
#             print("name: ",self.name)
#             print("age: ",self.age)
#             print("email:",self.email)
#             print("course :",self.course)


# name = input("Enter name: ")
# age = int(input("Enter age:"))
# email = input("Enter email:")
# course = input("Enter course: ")

# s1 = student(name,age,email,course)
 
# s1.display()



