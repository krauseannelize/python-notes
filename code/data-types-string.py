# DATA TYPES | STRING
# Examples of how the string data type functions

print("EXAMPLE | Display a string literal")
print("...using the print function.")
print()

print("EXAMPLE | Assigning string to a variable")
name = "George"
print("A curious fictional monkey:", name)
print()

print("EXAMPLE | Strings using different quotation marks")
phrase = 'Single quotation marks'
print(phrase)
print(type(phrase))
print()
phrase2 = "Double quotation marks"
print(phrase2)
print(type(phrase2))
print()

print("EXAMPLE | Combining quotations marks to quote")
phrase = 'Single quotation marks outside to "quote with double" inside'
print(phrase)
print(type(phrase))
print()
phrase2 = "Double quotation marks outside to 'quote with single' inside"
print(phrase2)
print(type(phrase2))
print()

print("EXAMPLE | Multiline strings")
sentence = '''Wrapping a sentence
in three single quotation marks
to create a multiline string'''
print(sentence)
print(type(sentence))
print()
sentence = """Wrapping a sentence
in three double quotation marks
to create a multiline string"""
print(sentence)
print(type(sentence))
print()

print("EXAMPLE | Joining strings with a + operator")
# Spaces needs to be added in every string
print("Joined " + "using " + "string " + "literal.")
print()
word1 = "Joined "
word2 = "using "
word3 = "variables."
print(word1 + word2 + word3)
print()

print("EXAMPLE | Create a variable by joining strings with a + operator")
sentence = "Variable " + "created " + "using " + "string " + "literal."
print(sentence)
print(type(sentence))
print()
word4 = "Variable "
word5 = "created "
word6 = "using "
word7 = "variables."
sentence2 = word4 + word5 + word6 + word7
print(sentence2)
print(type(sentence2))
print()

print("EXAMPLE | Joining strings with a comma delimiter")
# Using the comma delimiter automatically adds spaces
print("Joined", "using", "string", "literal.")
print()
word1 = "Joined"
word2 = "using"
word3 = "variables."
print(word1, word2, word3)
print()

print("EXAMPLE | Create a variable by joining strings with a comma delimiter")
# Using a comma delimiter creates a sequence and cannot be used to create a new string
sentence1 = "Variable", "created", "using", "string", "literal."
sentence2 = ("Variable", "created", "using", "string", "literal.")
sentence3 = ["Variable", "created", "using", "string", "literal."]
print("String literal - Not using parentheses or square brackets:")
print(sentence1)
print(type(sentence1))
print()
print("String literal - Using parentheses:")
print(sentence2)
print(type(sentence2))
print()
print("String literal - Using square brackets:")
print(sentence3)
print(type(sentence3))
print()
word1 = "Variable"
word2 = "created"
word3 = "using"
word4 = "variables."
sentence4 = word1, word2, word3, word4
sentence5 = (word1, word2, word3, word4)
sentence6 = [word1, word2, word3, word4]
print("Variables - Not using parentheses or square brackets:")
print(sentence4)
print(type(sentence4))
print()
print("Variables - Using parentheses:")
print(sentence5)
print(type(sentence5))
print()
print("Variables - Using square brackets:")
print(sentence6)
print(type(sentence6))
print()