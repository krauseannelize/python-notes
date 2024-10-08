# Loops in Python

**Loops** are programming constructs that allow you to repeatedly execute a block of code until a certain condition is met. They are essential for automating repetitive tasks and making your code more efficient. There are two main types of loops in Python:

1. [WHILE loops](#while-loops)
    - [BREAK statement with a WHILE loop](#break-statement-with-a-while-loop)
    - [CONTINUE statement with a WHILE loop](#continue-statement-with-a-while-loop)
    - [ELSE statement with a WHILE loop](#else-statement-with-a-while-loop)
1. [FOR loops](#for-loops)

---

## WHILE loops

**WHILE loops** are used when you want to repeat a block of code as long as a certain condition is true, and the condition is checked at the beginning of each iteration. The basic syntax is:

```python
variable = ("initial value")
# Initialization | Set initial value that will be used in loop condition

while condition:
# Condition | Loop will continue as long as this condition is true,
# typically a statement about the variable that was initialized

    ("Do this if true")
    # Body | Indented block of code that executes if condition is true
    
    variable = ("updated value")
    # Update | Updated variable used in condition before it is
    # returned to the loop to eventually make the condition false
```

For example, a WHILE loop can be used as follows:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1

# output:
# 1
# 2
# 3
# 4
# 5
# loops stops as num = 6 and condition now false
```

---

### BREAK statement with a WHILE loop



---

### CONTINUE statement with a WHILE loop



---

### ELSE statement with a WHILE loop

An ELSE statement can be used to execute a block of code once the condition is no longer true and will only be executed if the loop wasn't terminated by a BREAK statement. For example:

```python
num = 1   # initialize variable to use in loop
while num < 6:   # condition evaluates if num is smaller than 6
    print(num)   # code that executes if num is smaller than 6
    num += 1   # update variable by incrementing it by 1
else:
    print("The end.")  # code executes once condition false

# output:
# 1
# 2
# 3
# 4
# 5
# The end.
```

---

## FOR loops

**FOR loops** are used when you know how many times you want to repeat a block of code and is often used to iterate over a sequence like lists, tuples, or ranges. The basic syntax is:

```python
iterable = [element1, element2, element3]
# Iterable | Any object that can be iterated over with a set number of
# values (list, tuple, range) or characters (string)

for element in iterable:
# Element | Temporary variable to hold current item from iterable
# during each iteration - choose any valid variable name

    ("Do this for each element")
    # Body | Indented block of code that executes for every iteration
```

For example, a FOR loop can be used as follows:

```python
for num in range(0, 10, 2):
# range sequence start 0, end 10 (exclusive), step 2
    print(num)

# output:
# 0
# 2
# 4
# 8
# loops stops as it has executed for every iteration in range
```

---
