# Conditionals in Python

**Branching** refers to the decision-making process within a program that determines which code block to execute based on specific conditions. It is essential for creating programs that can adapt to different inputs and situations.

**Conditional statements** are a primary tool for branching in programming and enables programs to make decisions based on logical expressions created with different [operators](/4-Python-operators.md).

## IF statements

IF statements will execute a statement if a condition is true. The basic syntax is:

```python
if condition:
   # indented statement to execute if condition is true
```

For example, an IF statement can be used as follows:

```python
num1 = 6
num2 = 50
if num2 > num1:
# condition checks if variable num2 is larger than variable num1
  print("num2 is larger than num1")
  # if the condition is true, this statement will execute
```

## ELIF statements

When the output of the IF statement is false, Python can evaluate another condition and execute a statement if that condition is true. The basic syntax is:

```python
if condition-1:
    # indented statement to execute if condition-1 is true
elif condition-2:
    # indented statement to execute if condition-2 is true
```

For example, an ELIF statement can be used as follows:

```python
num1 = 50
num2 = 50
if num2 > num1:
# condition checks if variable num2 is larger than variable num1
    print("num2 is larger than num1")
    # if the condition is true, this statement will execute
    # as statement is false, Python will now check elif
elif num2 == num1:
    print("num2 is equal to num1")
```
