# Built-in Python Functions

Python has certain functions that exist within it and that you can call directly. Some of commonly used functions are described below.

| Function | Description | Input | Output |
|--- | --- | --- | --- |
| `abs()` | Return the absolute value of a number | `print(abs(-9.25))` | `9.25` |
| `all()` | Returns True if all items in an iterable object are true | `print(all(list((0, 1, 5))))` | `False` |
| `any()` | Returns True if any item in an iterable object are true | `print(any(list((0, 1, 5))))` | `True` |
| `bool()` | Returns the boolean value of the specified object | `print(bool(0))` | `False` |
| `complex()` | Returns a complex number | `print(complex(4,7))` | `(4+7j)` |
| `float()` | Returns a floating point number | `print(float(2))` | `2.0` |
| `int()` | Returns an integer number | `print(int(8.4))` | `8` |
| `len()` | Returns the length of a string or number of items in an object | `print(len("blue bells"))` | `10` |
| `list()` | Returns a list | `print(list((0, 1, 5)))` | `[0, 1, 5]` |
| `max()` | Returns the largest item in an iterable | `print(max(0, 1, 5))` | `5` |
| `min()` | Returns the smallest item in an iterable | `print(min(0, 1, 5))` | `0` |
| `pow(x, y)` | Returns the value of x to the power of y | `print(pow(2, 5))` | `32` |
| `print()` | Prints to the standard output device | `print("Python is fun!")` | `Python is fun!` |
| `range()` | Returns a sequence of numbers or characters | `print([x**4 for x in range(5)])` | `[0, 1, 16, 81, 256]` |
| `round(x, y)` | Rounds numbers x to indicated digits y | `print(round(6.29784, 1))` | `6.3` |
| `sorted()` | Returns a sorted list | `print(sorted(list(("c", "b", "a"))))` | `['a', 'b', 'c']` |
| `str()` | Returns a string object | `print(type(str(-9.25)))` | `<class 'str'>` |
| `sum()` | Sums the items of an iterator | `print(sum([0, 1, 5]))` | `6` |
| `tuple()` | Returns a tuple | `print(tuple((0, 1, 5)))` | `(0, 1, 5)` |
| `type()` | Returns the type of an object | `print(type(32))` | `<class 'int'>` |
