# 4. Python Operators

Operators are used to perform different types of operations on variables and values.

- [Arithmetic operators](#arithmetic-operators)
- [Assignment operators](#assignment-operators)
- [Comparison operators](#comparison-operators)
- [Logical operators](#logical-operators)
- [Identity operators](#identity-operators)
- [Membership operators](#membership-operators)

## Arithmetic operators

Arithmetic operators are used with the numeric data types to mathematical operations.

| Operator | Name | Input | Output |
| --- | --- | --- | --- |
| + | Addition | 10 + 4 | 14 |
| - | Subtraction | 10 - 4 | 6 |
| * | Multiplication | 10 * 4 | 40 |
| / | Division | 10 / 4 | 2.5 |
| % | Modulus | 10 % 4 | 5 |
| // | Floor division | 10 // 4 | 2 |
| ** | Exponential | 10 ** 4 | 10000 |

Some arithmetic operators take precedence over others and will affect the order in which calculations are performed. The precedence is as follows:

1. Parentheses ()
1. Exponential
1. Multiplication and division (also modulus and floor division)
1. Addition and subtraction.

---

## Assignment operators

Assignment operators are used to assign values to variables.

| Operator | Function | Equivalent to |
| --- | --- | --- |
| = | Assigns value on right-side of operand to variable on left-side | `x = 5` |
| += | Adds value on right-side of operand to variable on left-side and assigns new value to variable on left-side | `x = x + 5` |
| -= | Subtract value on right-side of operand from variable on left-side and assigns new value to variable on left-side | `x = x - 5` |
| *= | Multiplies value on right-side of operand with variable on left-side and assigns new value to variable on left-side | `x = x * 5` |
| /= | Divides variable to left-side of operand with value on right-side and assigns new value to variable on left-side | `x = x / 5` |
| %= | Divides variable to left-side of operand with value on right-side and assigns remainder to variable on left-side | `x = x % 5` |
| //= | Divides variable to left-side of operand with value on right-side and assigns whole integer without remainder to variable on left-side | `x = x // 5` |
| **= | Calculates variable on left-side to power of value on right-side and assigns new value to variable on left-side | `x = x ** 5` |

---

## Comparison operators

Comparison operators are used to compare two values and can only return the boolean data type, so the result will always be either `True` or `False`.

| Operator | Is variable | Input | Output |
| --- | --- | --- | --- |
| == | equal to | `10 == 5` | False |
| != | not equal to | `10 != 5` | True |
| > | greater than | `10 > 10` | False |
| >= | greater than or equal to | `10 >= 10` | True |
| < | less than | `10 < 10` | False |
| <= | less than or equal to | `10 <= 10` | True |

---

## Logical operators

Logical operators are used to combine conditional statements and enable operations to be performed on multiple conditions. The result will always be either a `True` or `False`, thus of the boolean data type. Note that the operators are case sensitive and must be lowercase.

| Operator | Function | Input | Output |
| --- | --- | --- | --- |
| and | Both statements must be true to return a true | `10 > 6 and 11 < 7` | False |
| or | Either statement must be true to return a true | `10 > 6 or 11 < 7` | True |
| not | Statement must be false to return a true | `not 11 < 7` | True |

---

## Identity operators

Identity operators are used to see if two objects are the same object with the same memory location, and not just simply equal.

| Operator | Function | Input | Output |
| --- | --- | --- | --- |
| is | Variables must be the same object | `x is y` | False |
| is not | Variables must not be the same object | `x is not y` | True |

---

## Membership operators

Membership operators are used to check if an element is present within a sequence such as strings, ranges, lists, and tuples.

| Operator | Function | Input | Output |
| --- | --- | --- | --- |
| in | Element must be present in the sequence | `print(3 in range(10))` | True |
| not in | Element must not be present in the sequence | `print(7 not in range(10))` | False |

---
