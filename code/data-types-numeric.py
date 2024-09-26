# DATA TYPES | NUMERIC
# Examples of how the different numeric data types function

print("EXAMPLE | Adding two integers")
sum = 7 + 8
print("The sum of 7 and 8 is:")
print(sum)
print(type(sum))
print()
# sum = 7 + "8" will result in an error due to type mismatch as 8 will be treated as a string

print("EXAMPLE | Multiplying two floats")
sum = 10.3 * 2.5
print("The sum of 10.3 multiplied by 2.5 is:")
print(sum)
print(type(sum))
print()

print("EXAMPLE | Subtracting two complex numbers")
sum = 150j - 70j
print("70j subtracted from 150j is:")
print(sum)
print(type(sum))
print()

print("EXAMPLE | Explicit conversion - Convert integer to a float using a function")
num = 23
new_num = float(num)
print("The number before conversion:")
print(num)
print(type(num))
print("The number after conversion with the float() function:")
print(new_num)
print(type(new_num))
print()

print("EXAMPLE | Explicit conversion - Convert numeric value to a string using a function")
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

print("EXAMPLE | Implicit conversion - Calculation with an integer and a float")
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

print("EXAMPLE | Implicit conversion - Calculation with an integer and a complex number")
num_int = 10
num_clx = 4j
result = num_int * num_clx
print("If we take:")
print(num_int)
print(type(num_int))
print("and multiply it with:")
print(num_clx)
print(type(num_clx))
print("the result will be:")
print(result)
print(type(result))
print()

print("EXAMPLE | Implicit conversion - Calculation with a float and a complex number")
num_flt = 13.3
num_clx = 6j
result = num_int / num_clx
print("If we take:")
print(num_flt)
print(type(num_flt))
print("and divide it with:")
print(num_clx)
print(type(num_clx))
print("the result will be:")
print(result)
print(type(result))
print()