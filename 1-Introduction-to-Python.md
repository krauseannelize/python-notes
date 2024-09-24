# 1. Introduction to Python

Python is a programming language with a syntax that is very readable feeling similar to human language. This makes it easier to learn and understand, even for beginners. Python allows you to express programming concepts in a clear and concise way - see below compared to Bash and Powershell:

![Code snippet printing "Hello World" in Python, Bash and Powershell](images/hello-world-comparison.png 'Code snippet printing "Hello World" in Python, Bash and Powershell')

---

## Programming Concepts

| TERM | DEFINITION |
| --- | --- |
| **Branching** | The ability of a program to alter its execution sequence |
| **Conditional statements** | Sections of code that direct program execution based on specified conditions |
| **Control statements** | Programming constructs that direct the flow of execution of a program by allowing you to make decisions, repeat actions, or choose between different code paths based on specific conditions |
| **Conversion - Explicit** | Convert between one data type and another by calling a function with the name of the type we're converting to, e.g. `num = 13, print(”Number is: “ + str(num))` converts an integer to a string |
| **Conversion - Implicit** | The interpreter automatically converts one data type into another, e.g. `print(7+8.5)` adds an integer and a float - Python implicitly converts the integer to a float |
| **Expressions** | A combination of numbers, symbols, and variables to compute and return a result upon evaluation |
| **Functions** | A group of related statements to perform a task and return a value |
| **Iterators** | Variables that allow you to loop through a collection one item at a time |
| **Keywords** | Special words that are reserved for specific purposes and that can only be used for those purposes |
| **List** | A sequences of elements of any type that is *mutable* |
| **List comprehension** | Create new lists based on sequences or ranges |
| **Loops - For** | Iterates, or repeats over a sequence of values like numbers, letters, etc |
| **Loops - Infinite** | A loop that keeps executing and never stops |
| **Loops - While** | Instruct your computer to continuously execute your code based on the value of a condition |
| **Operators** | Symbols that perform operations on objects and values |
| **Pass** | A placeholder statement which is used when the syntax requires a statement, but you don't want to execute any code or command |
| **Range** | A sequence of values defined by a starting and end point, alternatively a continuous set of numbers or characters within a specific interval, that is *immutable* |
| **Recursion** | Repeated application of the same procedure to a smaller problem. Recursion lets us tackle complex problems by reducing the problem to a simpler one. Recursion is a way of doing a repetitive task by having a function call itself |
| **Refactoring** | Process of rewriting code to be more self-documenting |
| **Strings** | A sequences of characters and are immutable |
| **Tuple** | A sequences of elements of any type that are immutable. The position of the elements inside the tuple have meaning so it is useful when when we want to make sure an element in a certain position or index refers to one specific thing and won't change. We write tuples in parentheses instead of square brackets |
| **Variables** | Represent data stored as strings, tuples, dictionaries, lists, and objects |

---

## Naming Rules and Conventions

When assigning names to objects, programmers adhere to a set of rules and conventions which help to standardize code and make it more accessible to everyone. Some common naming rules and conventions are:

- Names cannot contain spaces.
- Names may be a mixture of upper and lower case characters.
- Names can’t start with a number but may contain numbers after the first character.
- Variable names and function names should be written in **snake_case**, which means that *all letters are lowercase and words are separated using an underscore*.
- Use **descriptive names** (e.g. 'student_name') and **not cryptic abbreviations** (e.g. 'sn') as it will make your code easier to read and interpret - your future self with thank you!

---

## Resources

### Online interpreters and code-pads

- <https://www.python.org/shell/>
- <https://www.onlinegdb.com/online_python_interpreter>
- <https://repl.it/languages/python3>
- <https://www.tutorialspoint.com/execute_python3_online.php>
- <https://rextester.com/l/python3_online_compiler>
- <https://trinket.io/python3>

### Additional resources

- Read the [official Python documentation](https://docs.python.org/3/).
- [Built-in Functions](https://docs.python.org/3/library/functions.html) - Lists and summarizes Python’s built-in functions.
- [Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp) - Lists Python’s reserved keywords and a brief description of what each keyword does.
- [Different Arithmetic operators in Python](https://flexiple.com/python/arithmetic-operators-in-python/) - Provides more examples of the proper syntax for using arithmetic operators in Python.
- Search for answers or ask a question on [Stack Overflow](https://stackoverflow.com/).
- Subscribe to the Python [tutor](https://mail.python.org/mailman/listinfo/tutor) mailing list, where you can ask questions and collaborate with other Python learners.
- Subscribe to the [Python-announce](https://mail.python.org/mailman/listinfo/python-announce-list) mailing list to read about the latest updates in the language.

---

## Resolving Problems

### Common syntax errors

- Misspellings
- Incorrect indentations
- Missing or incorrect key characters:
  - Bracket types - ( curved ), \[ square ], { curly }
  - Quote types - "straight-double" or 'straight-single', “curly-double” or ‘curly-single’
  - Block introduction characters, like colons - :
- Data type mismatches
- Missing, incorrectly used, or misplaced Python reserved words
- Using the wrong case (uppercase/lowercase) - Python is a case-sensitive language

If your syntax is correct, but the script has unexpected behavior or output, this may be due to a semantic problem. Syntax is like the vocabulary, grammar, spelling, and punctuation of code. Semantics are the meaning and logic of coded statements. It is possible to have syntactically correct code that runs successfully, but doesn't do what we want it to do.

### Common semantic errors

- Creating functional code, but getting unintentional output
- Poor logic structures in the design of the code

When working with the code blocks in exercises for this course, be mindful of syntax and semantic (logic) errors, along with the overall result of your code. Just because you fixed an error doesn't mean that the code will have the desired effect when it runs! Once you’ve fixed an error in your code, don't forget to click Run to check your work.
