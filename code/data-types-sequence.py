# DATA TYPES | SEQUENCE
# Examples of how the sequence data types function

print("EXAMPLE | Range")
print("Using the print() function:")
print(range(5))
print()

new_range = range(5)
print("Assigning range to a variable to print the variable and type:")
print(new_range)
print(type(new_range))
print()

print("Using the list() function:")
print(list(new_range))
print()

new_list = list(new_range)
print("When assigned to a new variable, it is evident that the list function created a list type:")
print(new_list)
print(type(new_list))
print()

print("Using a for loop to iterate over the range:")
for num in range(5):
    print(num)
print()

print("EXAMPLE | Lists")   # lists can be changed
fruits = ["Apple", "Orange", "Litchi", "Cherry"]
numbers = [13, 34, 67, 22, 99]
duplicates = ["Bear", "Donkey", "Monkey", "Cat", "Donkey"]
mix_list = ["Peter", 34, True, "London"]
print("List with different string values:")
print(fruits)
print(type(fruits))
print()

print("List with different integer values:")
print(numbers)
print(type(numbers))
print()

print("Lists can contain duplicates:")
print(duplicates)
print(type(duplicates))
print()

print("Lists can contain different data types:")
print(mix_list)
print(type(mix_list))
print()

print("Lists can be sorted:")
print("Fruits:", sorted(fruits))
print("Numbers:", sorted(numbers))
print("Duplicates:", sorted(duplicates))
print("However, because of a type mismatch, the mixed list cannot be sorted.")
print()

print("You can use index to display only certain items in a list:")
print(fruits[2])
print(numbers[-1])   # using negative indexing
print(duplicates[2:5])   # using range of indices (start inclusive, stop exclusive)
print(mix_list[2])
print()

print("EXAMPLE | Tuples")   # tuples cannot be changed
veggies = ("Spinach", "Beetroot", "Cabbage")
num_tuple = (34, 56, 20, 6)
dupli_tuple = ("Anne", "Mervin", "Ben", "Anne")
mix_tuple = ("Ben", 23, False)
print("A tuple with different string values:")
print(veggies)
print(type(veggies))
print()

print("A tuple with different integer values:")
print(num_tuple)
print(type(num_tuple))
print()

print("Tuples can contain duplicates:")
print(dupli_tuple)
print(type(dupli_tuple))
print()

print("A tuple can contain different data types:")
print(mix_tuple)
print(type(mix_tuple))
print()

print("You can use index to display only certain items in a tuple:")
print(veggies[0])
print(num_tuple[-1])   # using negative indexing
print(dupli_tuple[1:4])   # using range of indices (start inclusive, stop exclusive)
print(mix_tuple[0])
print()