# FUNCTIONS | Defining
# Examples of how to define functions

print("EXAMPLE | Greeting with one parameter")
# Defining a function named "greeting" that takes parameter "name"

def greeting(name):
    print("Welcome, " + name)
    # Code that executes when function is called to print
    # a personalized welcome message
    
# Calling greeting function
greeting("Bob")
greeting("Margaret")
print()

print("EXAMPLE | Greeting with two parameters")
# Defining a function named "greeting" that takes
# parameters "name" and "department"

def greeting(name, department):
    print("Welcome, " + name)
    print("You are in the " + department + " Department")
    # Code that executes when function is called to print
    # a personalized welcome message
    
greeting("Bob", "Marketing")
greeting("Margaret", "Accounts Receivable")
print()

print("EXAMPLE | Calculation with two parameters")
# Defining area_triangle function that
# use return to indicate return value

def area_triangle(base, height):
    return base*height/2

# Calling area_triangle function to:
#1. calculate two triangles areas separately
#2. add the two areas to find the sum
#3. print result converting returned floats to string

area_a = area_triangle(6,3)
area_b = area_triangle(9,6)
sum = area_a + area_b
print("The area of a triangle with a base of 6 and height of 3 is: " + str(area_a))
print("The area of a triangle with a base of 9 and height of 6 is: " + str(area_b))
print("The sum of the areas of both triangles is: " + str(sum))
print()

print("EXAMPLE | Calculation with one parameter returning three values")
# Defining covert_seconds function that
# use return to indicate return values

def convert_seconds(seconds):
    hours = seconds // 3600   # floor division - returns integer part only
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds   # returning 3 values

# Calling convert_seconds function
# and assign return values to variables
hours, minutes, seconds = convert_seconds(5000)
print("5000 second is " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
print()