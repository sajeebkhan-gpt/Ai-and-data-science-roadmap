"""
PYTHON INTERMEDIATE CONCEPTS
=============================
This file covers intermediate Python concepts including functions, OOP, and more.
"""

# ============================================================================
# 1. FUNCTIONS
# ============================================================================

print("=" * 60)
print("1. FUNCTIONS")
print("=" * 60)

# Basic function
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default parameters
def power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")

# Function with *args (variable positional arguments)
def sum_all(*args):
    """Sum all arguments"""
    return sum(args)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs (variable keyword arguments)
def print_info(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Person info:")
print_info(name="Alice", age=25, city="New York")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"\nLambda square(5): {square(5)}")
print(f"Lambda add(3, 4): {add(3, 4)}")

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print(f"\nMap (squared): {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter (evens): {evens}")

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Reduce (product): {product}")

# ============================================================================
# 2. OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================================

print("\n" + "=" * 60)
print("2. OBJECT-ORIENTED PROGRAMMING")
print("=" * 60)

# Basic class
class Person:
    """A simple Person class"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Constructor (initializer)"""
        self.name = name  # Instance variable
        self.age = age
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def birthday(self):
        """Increment age"""
        self.age += 1
        return f"Happy birthday! Now {self.age} years old"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Class method - alternative constructor"""
        age = 2025 - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        """Static method - doesn't access instance or class"""
        return age >= 18

# Create instances
person1 = Person("Alice", 25)
person2 = Person.from_birth_year("Bob", 2000)

print(person1.introduce())
print(person2.introduce())
print(person1.birthday())
print(f"Is Alice an adult? {Person.is_adult(person1.age)}")

# Inheritance
class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade"""
        self.grades.append(grade)
    
    def average_grade(self):
        """Calculate average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def introduce(self):
        """Override parent method"""
        return f"{super().introduce()} and my student ID is {self.student_id}"

student = Student("Charlie", 20, "S12345")
print(f"\n{student.introduce()}")
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)
print(f"Average grade: {student.average_grade():.2f}")

# Encapsulation (private attributes)
class BankAccount:
    """Bank account with private balance"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return self.__balance

account = BankAccount("Alice", 1000)
print(f"\n{account.deposit(500)}")
print(f"{account.withdraw(200)}")
print(f"Current balance: ${account.get_balance()}")

# Property decorators
class Temperature:
    """Temperature class with property"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"\n{temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 100
print(f"{temp.celsius:.2f}°C = {temp.fahrenheit}°F")

# ============================================================================
# 3. EXCEPTION HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("3. EXCEPTION HANDLING")
print("=" * 60)

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Value error!")

# Catch all exceptions
try:
    x = int("abc")
except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")

# Try-except-else-finally
try:
    file_content = "Sample content"
    print(f"Processing: {file_content}")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors occurred!")
finally:
    print("Cleanup code (always runs)")

# Custom exceptions
class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    pass

def withdraw_money(balance, amount):
    """Withdraw money with custom exception"""
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount}. Balance: ${balance}")
    return balance - amount

try:
    new_balance = withdraw_money(100, 150)
except InsufficientFundsError as e:
    print(f"\nCustom exception: {e}")

# ============================================================================
# 4. FILE HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("4. FILE HANDLING")
print("=" * 60)

# Writing to a file
with open("/vercel/sandbox/sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is easy!\n")
print("File written successfully")

# Reading from a file
with open("/vercel/sandbox/sample.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Reading line by line
print("Reading line by line:")
with open("/vercel/sandbox/sample.txt", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# Appending to a file
with open("/vercel/sandbox/sample.txt", "a") as file:
    file.write("Appended line\n")

# Reading all lines into a list
with open("/vercel/sandbox/sample.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")

# ============================================================================
# 5. MODULES AND IMPORTS
# ============================================================================

print("\n" + "=" * 60)
print("5. MODULES AND IMPORTS")
print("=" * 60)

# Standard library imports
import math
import random
import datetime
from collections import Counter, defaultdict

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 100)}")
print(f"Current date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Counter example
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"\nWord count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# defaultdict example
scores = defaultdict(list)
scores["Alice"].append(85)
scores["Bob"].append(90)
scores["Alice"].append(88)
print(f"Scores: {dict(scores)}")

# ============================================================================
# 6. LIST/DICT/SET COMPREHENSIONS (Advanced)
# ============================================================================

print("\n" + "=" * 60)
print("6. COMPREHENSIONS (Advanced)")
print("=" * 60)

# List comprehension with condition
numbers = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by 2 and 3: {numbers}")

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table:\n{matrix}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "date"]}
print(f"Unique word lengths: {unique_lengths}")

# ============================================================================
# 7. ITERATORS AND ITERABLES
# ============================================================================

print("\n" + "=" * 60)
print("7. ITERATORS AND ITERABLES")
print("=" * 60)

# Creating an iterator
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print("Using iterator:")
print(f"  {next(my_iter)}")
print(f"  {next(my_iter)}")
print(f"  {next(my_iter)}")

# Custom iterator
class CountDown:
    """Custom iterator for counting down"""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print("\nCustom iterator (countdown from 5):")
for num in CountDown(5):
    print(f"  {num}", end=" ")
print()

print("\n" + "=" * 60)
print("INTERMEDIATE CONCEPTS COMPLETED!")
print("=" * 60)
