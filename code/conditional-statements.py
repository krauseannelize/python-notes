# CONDITIONAL STATEMENTS
# Examples of how the conditional statements function

print("EXAMPLE | Use if-elif-else block with comparison operators")
number = -13

if number >= 1:   # false - evaluate next condition
   print("The number ", number, " is positive.")
elif number == 0:   # false - no conditions left to evaluate
   print("The number is null.")
else:   # all conditions false - execute else statement
   print("The number ", number, " is negative.")
print()

print("EXAMPLE | Use if-elif-else block with comparison and logical operators")
number = 31

if number <= 5:   # false - evaluate next condition
   print("The number is 5 or smaller.")
elif number == 33:   # false - evaluate next condition
   print("The number is 33.")
elif number < 32 and number >= 6:   # true - execute this statement
   print("The number is less than 32 and greater than 6.")
else:   # one condition true - else statement skipped
   print("The number is " + str(number))
print()

print("EXAMPLE | Define function and use if-else to round up value to nearest multiple of 10")
def round_up(number):
# calculate value of number rounded to nearest multiple of 10
  x = 10
  whole_number = number // x  # floor operator will return integer after division = 25
  remainder = number % x  # modulo operator will return the remainder after division = 6
  
  if remainder >= 5:
    return x*(whole_number+1) #remainder larger than 5 (10*(25+1)) and 260 returned to function round_up
  
  return x*whole_number   # second return used instead of else
 
print(round_up(256))
print()

print("EXAMPLE | Define function to take error number and use if-elif-else to return error message")
def translate_error_code(error_code):
    
    if error_code == "401 Unauthorized":   # false - evaluate next condition
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":   # true - execute statement
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":   # condition ignored as true found
        translation = "Server request to close unused connection"
    else:   # else ignored as true found
        translation = "Unknown error code"
    return translation   # translation variable returned to function translate_error_code

print(translate_error_code("404 Not Found"))
print()

print("EXAMPLE | Define function to take time input and use if-elif-else to return task message")
def task_reminder(time_as_string):
# assign value to variable task according to conditions
    
    if time_as_string == "8:00 a.m.":   # false - evaluate next condition
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":   # false - evaluate next condition
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":   # false - evaluate next condition
        task = "Reboot servers"
    else:
        task = "Provide IT Support to employees"   # all conditions false - execute else statement

    return task   # task variable returned to function task_reminder

print(task_reminder("10:00 a.m."))
print()

print("EXAMPLE | Return fractional remainder after division")
def get_remainder(x, y):
# calculate value to variable remainder according to conditions

    if x == 0 or y == 0 or x == y:   # cannot divide by 0 and number divided by itself is 1 without fractional remainder
       remainder = 0
    else:
       remainder = (x % y) / y
    return remainder

print(get_remainder(117, 17))