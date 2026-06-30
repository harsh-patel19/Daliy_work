


# What is a String in Python?

# Answer:
# A string is a sequence of characters enclosed in 
# single quotes (' '),double quotes (" "), or 
# triple quotes (''' ''').


# print("----------How to find the length of a string?-------")

# name = "Harsh"
# print(len(name))


# ----------- methods all -------

# name = "harsh"
# print(name.upper())
# print(name.lower())


#  --- using the remove the space to use in strip ---- ?

# text = "  Hello  "
# print(text.strip())


# ------ How to replace a word ------- ?

# text = "I love pyhton"
# print(text.replace("pyhton","java"))



#------- How to split a string? ------ ?

# text = "apple, banana,mango"
# print(text.split(","))


#  ----- How to join strings? ----- ?

# fruite = ["apple","banaana","mango"]
# print(",".join(fruite))



#  ---- Difference Between find() and index() ----- ?

# text = "banana"
# print(text.find("z")) retern the -1 
# print(text.index("z")) return the valueerror





#  ---- REVERSE THE STRING WITHOUT USIN THE BULIT FUNCTION ----- ?

# name  = "youvan"
# rev = ""

# for i in name:
#     rev = i +rev
# print(rev)



#  ---- FIND THE LEN WITHOUN USING LEN function ----- ?

# name = "youvan"
# count = 0

# for i in name:
#     count += 1

# print(count)



#  ---- REMOVE THE DUPLICATE  CHARACHTER IN STRING ----- ?

# name = "harsh"
# result = ""

# for i in name:
#     if i not in result:
#         result += i
# print(result)



#  ----- FREQUENCY OF SPICIFIC CHARCHTER ----- ?

# name = "banana"
# count = 0

# for i in name:
#     if i == "a":
#         count += 1
# print(count)