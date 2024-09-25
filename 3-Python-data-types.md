# 3. Python data types

 Data type specifies the kind of value a variable can hold and the operations that can be performed on the variable. Understanding data types in Python is essential for writing correct, efficient, and readable code. Return the data type of any object with the `type()` function.

## Text

**String** is a collection of one or more characters put in single quotes `'Hello'` or double-quotes `"Hello"`. Python does not have a character data type and a character will be a string of length one.

```python
x = "Hello World!"
print(type(x))
```

*Output:* `<class 'str'>` informs you that variable x is of the string data type.

---

## Numeric

Code with examples of how the different numeric data types function can be found [here](/code/data-types-numeric.py).

### *Integers*

**Integer** is a positive or negative whole number that does not have a fraction or decimal. There is no length limitation in Python for integers. You can convert a value to an integer data type with the function `int()`.

```python
x = 5
print(type(x))
```

*Output:* `<class 'int'>` informs you that variable x is of the integer data type.

### *Floats*

**Float** is a positive or negative number that also has a fraction or decimal (a floating-point representation). It can also be used for scientific numbers with an "E" that indicates the power of 10. You can convert a value to a float data type with the function `float()`.

```python
x = 10.5
y = 12E4
print(type(x))
print(type(y))
```

*Output:* `<class 'float'>` informs you that variables x and y are of the float data type.

### *Complex numbers*

**Complex number** is numbers that have both a real and an imaginary part (represented by j) that are used in various mathematical and scientific calculations. You can convert a value to an complex number data type with the function `complex()`.

```python
x = 5j
y = 3 - 6j
print(type(x))
print(type(y))
```

*Output:* `<class 'complex'>` informs you that variables x and y are of the float data type.

---

## Boolean

**Boolean** can only have 1 of 2 values: `True` or `False`. This is used to represent logical conditions or decisions. Note that you will need to capitalize the first letter of true or false, otherwise it will return an error.

```python
x = 10 > 5   # Returns True as 10 is larger than 5
y = 6 == 7   # Returns False as 6 is not equal to 7
print(type(x))
print(type(y))
```

*Output:* `<class 'bool'>` informs you that variables x and y are of the boolean data type.

---

## Sequence

### *Range*

**Range** is a sequence of values defined by a starting and end point, alternatively a continuous set of numbers or characters within a specific interval, that is *immutable*. The basic syntax is `range(start, stop, step)` and the parameters mean:

- *start* is optional to indicate the start of the sequence, being 0 by default
- *stop* indicates the end of the sequence and the value being exclusive
- *step* is optional to indicate the interval or increment size, being 1 by default

```python
x = range(6)   # sequence of numbers: 0, 1, 2, 3, 4, 5
y = range(10, 0, -2)   # sequence of number: 10, 8, 6, 4, 2
print(type(x))
print(type(y))
```

*Output:* `<class 'range'>` informs you that variables x and y are of the range data type.

### *List*

**List** is a sequence of elements of any type into a single variable that is *mutable*. You can combine multiple data types in one list. Lists have a defined order that will not change, but you can change, add, and remove elements in a list after it has been created. To create a list add the list elements in square brackets ( [ ] ) separating each element with a comma.

```python
x = ["Ants", "Bees", "Crickets"]   # List of 3 strings
y = ["Tom","Parker", 20, True]   # List combining 2 strings, an integer and a boolean
print(type(x))
print(type(y))
```

*Output:* `<class 'list'>` informs you that variables x and y are of the list data type.

### *Tuple*

**Tuple** is a sequences of elements of any type into a single variable that is *immutable*. You can combine multiple data types in one tuple. Tuples have a defined order that will not change and you cannot change, add or remove elements in a tuple after it has been created. To create a tuple add the tuple elements in round brackets ( () ) separating each element with a comma.

```python
x = ("Avocado", "Beet", "Cucumber")   # Tuple of 3 strings
y = ("Anne","Nelson", 38, False)   # Tuple combining 2 strings, an integer and a boolean
print(type(x))
print(type(y))
```

*Output:* `<class 'list'>` informs you that variables x and y are of the list data type.

---
