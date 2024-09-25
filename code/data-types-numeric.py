# DATA TYPES | NUMERIC
# Examples of how the different numeric data types function

print("Example | Adding two integers will return an integer")
num = 7 + 8
print("The sum of 7 and 8 is:")
print(num)
print(type(num))
print()

print("Example | Adding two floats will return a float")
num = 10.3 + 2.5
print("The sum of 10.3 and 2.5 is:")
print(num)
print(type(num))
print()

print("Example | Explicit conversion - Convert numeric value to a string using a function")
base = 5
height = 3
area = (base*height)/2
print("The area of the triangle with a base of 5 and height of 3 is:")
print(area)
print(type(area))
string = str(area)
print(string, "is the area of the triangle")
print(type(string))
print()

print("Example | Implicit conversion - Result of subtracting an integer and float automatically assigned type float")
num_int = 10
num_flt = 4.3
result = num_int - num_flt
print("If we take:")
print(num_int)
print(type(num_int))
print("and subtract:")
print(num_flt)
print(type(num_flt))
print("the result will be:")
print(result)
print(type(result))
print()