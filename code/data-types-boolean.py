# DATA TYPES | BOOLEAN
# Examples of how the boolean data type functions

print("EXAMPLE | Compare two integers and create a new variable")
x = 4
y = 23
compare = x == y
print("Comparing x(4) and y(23) gives the result:")
print(compare)
print("This is of the type:")
print(type(compare))
print()

print("EXAMPLE | Compare an integer with a string and create a new variable")
x = 123
y = "123"
compare = x == y
print("Comparing integer x(123) and string y(123) gives the result:")
print(compare)
print("This is of the type:")
print(type(compare))
print()

print("EXAMPLE | Conditional if-else statement")
x = 5
if x > 10:
    print("x is:", x)
    print("x is greater than 0")
else:
    print("x is:", x)
    print("x is not greater than 0")
print()

print("EXAMPLE | Converting values to boolean with the bool() function")
print("A value that is positive such as 10 will be:")
print(bool(10))
print("A negative value such as -13 will also be:")
print(bool(-13))
print("However, a 0 will be:")
print(bool(0))
print()
name = "'Anne'"
empty_name = ""
print("A string of any kind such as", name, "will be:", bool(name))
print("However, an empty string will be:", bool(empty_name))
print()
list = ["Apple","Banana","Cherry"]
empty_list = []
print("A list with any number of items will be:", bool(list))
print("However, a list that does not contain any items will be:", bool(empty_list))