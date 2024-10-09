# Conditionals in Python

**Branching** refers to the decision-making process within a program that determines which code block to execute based on specific conditions. It is essential for creating programs that can adapt to different inputs and situations.

**Conditional statements** are a primary tool for branching in programming and enables programs to make decisions based on logical expressions created with different [operators](/4-Python-operators.md).

- [IF statements](#if-statements)
- [ELIF statements](#elif-statements)
- [ELSE statements](#else-statements)
- [Shorthand](#shorthand)
- [Nested IF statements](#nested-if-statements)

Additional code with examples of conditional statements can be found [here](/code/conditional-statements.py).

---

## IF statements

IF statements will execute a block of code if a condition is true. The basic syntax is:

```python
if condition:
   # indented block of code to execute if condition is true
```

For example, an IF statement can be used as follows:

```python
num1 = 6
num2 = 50
if num2 > num1:
# condition checks if variable num2 is larger than variable num1
  print("num2 is larger than num1")
  # if the condition is true, this code block will execute
```

---

## ELIF statements

When the output of the IF statement is false, Python can evaluate another condition and execute a block of code if that condition is true. The basic syntax is:

```python
if condition-1:
    # indented code block to execute if condition-1 is true
elif condition-2:
    # indented code block to execute if condition-2 is true
```

For example, an ELIF statement can be used as follows:

```python
num1 = 50
num2 = 50
if num2 > num1:
# condition checks if variable num2 is larger than variable num1
    print("num2 is larger than num1")
    # if the condition is true, this code block will execute
    # as condition is false, Python will now check elif
elif num2 == num1:
# conditions checks if variable num2 is equal to num1
    print("num2 is equal to num1")
    # if the condition is true, this code block will execute
```

---

## ELSE statements

When the output of the IF statement or all following ELIF statements are false, Python can execute a block of code. ELSE must always be last and is optional. The basic syntax is:

```python
if condition-1:
    # indented code block to execute if condition-1 is true
elif condition-2:
    # indented code block to execute if condition-2 is true
else:
    # indented code block to execute if all conditions are false
```

For example, an ELSE statement can be used as follows:

```python
num1 = 50
num2 = 6
if num2 > num1:
# condition checks if variable num2 is larger than variable num1
    print("num2 is larger than num1")
    # if the condition is true, this code block will execute
    # as condition is false, Python will now check elif
elif num2 == num1:
# conditions checks if variable num2 is equal to num1
    print("num2 is equal to num1")
    # if the condition is true, this code block will execute
    # as this condition is also false, Python will proceed to else
else:
    print("num2 is smaller than num1")
```

---

## Shorthand

A shorthand can be used for IF and ELSE statements that are not complicated with only one or two code lines to execute. The entire statement can be put on the same line, for example:

```python
num1 = 15
num2 = 6

# one line if statement
if num2 > num1: print("num2 is larger than num1")
# no output

# one line if-else statement
print (num2) if num2 > num1 else print(num1)
# output num1

# one line if-else statement with 3 conditions
print (num2) if num2 > num1 else print ("num2 = num1") if num2 == num1 else print (num1)
# output num1
```

---

## Nested IF statements

Nested IF statements are IF statements that are placed inside other IF statements, which allows for more complex decision-making processes.

```python
# Nested IF statements to check if a voter is eligible to vote
age = 25
country = "USA"
voter_status = "Unregistered"

if country == "USA":   # true - continue to nested if
    if age >= 18:   # true - continue to nested if
        if voter_status == "Registered":   # false - ignore and continue to else
            print("You are eligible to vote in the USA and registered for the upcoming elections.")
        else:   # code block executed as condition was false
            print("You are eligible to vote in the USA - please register to vote in the upcoming elections.")
    else:   # ignored as condition was true
        years_to_go = 18 - age
        print("You will be eligible to vote in the USA in", years_to_go, "years.")
else:   # ignored as condition was true
    print("Only USA citizens are eligible to vote in the upcoming elections.")
```

---
