# Defining Python Functions

Functions enables us to define blocks of code that can be reused multiple times throughout a program. This can avoid code duplication, reduce complexity and make your code easier to read, understand, maintain, debug and reuse.

A function is a reusable block of code that performs a specific task. It takes input, processes it, and returns an output. The keyword `def` is used to define a function in Python and the basic syntax is:

```python
# Define function
def FunctionName(parameter):
    # Body of code that will execute when function is called
    return # optional return value to exit a function

# Call function
FunctionName(argument)
```

The **function name** is a unique identifier used to call the function. **Parameters** can be defined within the parentheses of a function declaration to act as placeholders for the actual values that will be passed to the function when called. The actual values will be passed to the function when the function is called and **arguments** are added within the parentheses after the function name. For example:

```python
# Define function

def calculate_days(years, months, days):
# calculate_days is the function name
# years, months, days are parameters acting as placeholders

    total_days = (years*365) + (months*30) + days
    # code that executes when function is called and
    # calculates total number of days

    return total_days
    # return value of total_days to the function call
 
# Call function

print(calculate_days(3,6,9))
# calls the function and returns the value received to standard output

# OUTPUT: 1284
```

Here is an example to illustrate how you can clean up your code using a function to make it easier to read, understand, and reuse:

```python
# Code before clean up - without a function
name = "Mark"
number = len(name) * 7

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Bethany"
number = len(name) * 7

print("Hello " + name + ". Your lucky number is " + str(number))

# Code after clean up - with a function
def lucky_number(name):
    number = len(name) * 7
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Mark")
lucky_number("Bethany")
```

Code with more examples of defining functions can be found [here](/code/functions-defining.py).
