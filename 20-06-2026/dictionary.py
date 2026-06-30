# student = {
#     "name":"Harsh",
#     "age":22,
#     "city":"surat"
# }
# print(student)

# ---------------------------------------------?

# 2. Access Value

# student = {
#     "name":"Harsh",
#     "age":22,
# }

# print(student["name"])

# ---------------------------------------------?

# 3. Add New Key

# student = {
#     "name":"Harsh",
# }

# student["city"] = "surat"
# print(student)


# ---------------------------------------------?

# 4. Update Value


# student = {
#     "age":22
# }

# student["age"] = 25
# print(student)



# ---------------------------------------------?

# 5. Delete Key

# student = {
#     "name":"Harsh",
#     "city":"surat"
# }

# del student["city"]
# print(student)


# ---------------------------------------------?


# 6. Loop Through Dictionary


# student = {
#     "name":"Harsh",
#     "city":"surat"
# }
# for key in student:
#     print(key,student[key])


# ---------------------------------------------?

# Print Only Keys


# student = {
#     "name":"Harsh",
#     "city":"surat"
# }

# for i in student:
#     print(i)


# ---------------------------------------------?

# Count Frequency of Elements

# nums = [1,2,1,2,3,3,3,3]
# new = {}

# for i in nums:
#     if i in new:
#         new[i] += 1
#     else:
#         new[i] = 1
# print(new)


# ---------------------------------------------?

# find duplicated characters to repeat in ?

# word = "programming"
# new={}

# for i in word:
#     if i in new:
#         new[i] +=1
#     else:
#         new[i] = 1

# for key in new:
#     if new[key] > 1:
#         print(key)


# ---------------------------------------------?

# Find Employee with Maximum Salary

# employees = {
#     "Harsh": 25000,
#     "Raj": 40000,
#     "Amit": 35000,
#     "Neha": 45000
# }

# max_salary = 0
# employees_name = ""

# for key in employees:
#     if employees[key] > max_salary:
#         max_salary = employees[key]
#         employees_name = key

# print(employees_name,max_salary)


