"""
PYTHON BASICS - CORE CONCEPTS
==============================
This file covers fundamental Python concepts from scratch.
"""

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

print("=" * 60)
print("1. VARIABLES AND DATA TYPES")
print("=" * 60)

# Variables (no declaration needed, dynamically typed)
name = "Python"
age = 32
height = 5.9
is_awesome = True

print(f"String: {name} (type: {type(name)})")
print(f"Integer: {age} (type: {type(age)})")
print(f"Float: {height} (type: {type(height)})")
print(f"Boolean: {is_awesome} (type: {type(is_awesome)})")

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 10

print(f"\nMultiple assignment: x={x}, y={y}, z={z}")
print(f"Same value assignment: a={a}, b={b}, c={c}")

# ============================================================================
# 2. STRINGS
# ============================================================================

print("\n" + "=" * 60)
print("2. STRINGS")
print("=" * 60)

# String creation
single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi
line
string"""

# String operations
text = "Python Programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('Python', 'Java')}")

# String slicing
print(f"\nSlicing [0:6]: {text[0:6]}")
print(f"Slicing [7:]: {text[7:]}")
print(f"Slicing [:6]: {text[:6]}")
print(f"Reverse: {text[::-1]}")

# String formatting
name = "Alice"
age = 25
print(f"\nf-string: My name is {name} and I'm {age} years old")
print("format(): My name is {} and I'm {} years old".format(name, age))
print("%-formatting: My name is %s and I'm %d years old" % (name, age))

# ============================================================================
# 3. NUMBERS AND OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("3. NUMBERS AND OPERATORS")
print("=" * 60)

# Arithmetic operators
a, b = 10, 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"\n{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical operators
x, y = True, False
print(f"\nTrue and False: {x and y}")
print(f"True or False: {x or y}")
print(f"not True: {not x}")

# ============================================================================
# 4. LISTS
# ============================================================================

print("\n" + "=" * 60)
print("4. LISTS (Ordered, Mutable)")
print("=" * 60)

# List creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# List methods
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "mango")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"Popped: {popped}, List: {fruits}")

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"\nConcatenation: {list1 + list2}")
print(f"Repetition: {list1 * 2}")
print(f"Length: {len(list1)}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# ============================================================================
# 5. TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("5. TUPLES (Ordered, Immutable)")
print("=" * 60)

# Tuple creation
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
single_item = (42,)  # Note the comma

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Access: {person[0]}, {person[1]}")

# Tuple unpacking
name, age, job = person
print(f"Unpacked: {name}, {age}, {job}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# ============================================================================
# 6. SETS
# ============================================================================

print("\n" + "=" * 60)
print("6. SETS (Unordered, Unique, Mutable)")
print("=" * 60)

# Set creation
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
print(f"Fruits set: {fruits}")

# Set operations
fruits.add("orange")
print(f"After add: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nUnion: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# ============================================================================
# 7. DICTIONARIES
# ============================================================================

print("\n" + "=" * 60)
print("7. DICTIONARIES (Key-Value Pairs, Unordered, Mutable)")
print("=" * 60)

# Dictionary creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript"]
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")

# Dictionary methods
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

person.update({"age": 26, "country": "USA"})
print(f"After update: {person}")

print(f"\nKeys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# ============================================================================
# 8. CONTROL FLOW - IF/ELIF/ELSE
# ============================================================================

print("\n" + "=" * 60)
print("8. CONTROL FLOW - IF/ELIF/ELSE")
print("=" * 60)

age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# ============================================================================
# 9. LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("9. LOOPS")
print("=" * 60)

# For loop
print("For loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

print("\nFor loop with range:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

print("\nFor loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

# Break and continue
print("\nBreak example:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end=" ")
print()

print("\nContinue example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}", end=" ")
print()

# ============================================================================
# 10. INPUT/OUTPUT
# ============================================================================

print("\n" + "=" * 60)
print("10. INPUT/OUTPUT")
print("=" * 60)

# Output
print("Simple print")
print("Multiple", "arguments", "separated", "by", "space")
print("No newline", end=" ")
print("continues here")

# Input (commented out for automated testing)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old")

print("\n" + "=" * 60)
print("BASICS COMPLETED!")
print("=" * 60)
