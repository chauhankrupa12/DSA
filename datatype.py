# Demonstrate int, float, str, bool, and complex
a = 10
b = 10.5
name = "Atmiya"
is_student = True
c = 2 + 3j

print(a, type(a))
print(b, type(b))
print(name, type(name))
print(is_student, type(is_student))
print(c, type(c))

#Accept two numbers and display their data types
a = input("Enter first number: ")
b = input("Enter second number: ")

print("First number:", a)
print("Data type:", type(a))

print("Second number:", b)
print("Data type:", type(b))

#Convert a string number into integer and float
num = "25"

integer_num = int(num)
float_num = float(num)

print("Integer:", integer_num)
print("Float:", float_num)

#Find the length of a string
name = "Atmiya"

length = len(name)

print("Length:", length)

#Create list, tuple, set, and dictionary
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dictionary = {"name": "Atmiya", "age": 20}

print(my_list)
print(type(my_list))

print(my_tuple)
print(type(my_tuple))

print(my_set)
print(type(my_set))

print(my_dictionary)
print(type(my_dictionary))

