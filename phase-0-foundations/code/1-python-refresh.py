### PYTHON VERSION
import dataclasses
import sys

print(sys.version)
# 3.14.3 (main, Feb  3 2026, 15:32:20) [Clang 17.0.0 (clang-1700.6.3.2)]

################################
### DATA TYPES
################################

print(type(1))  # int
print(type(1.0))  # float
print(type("hello"))  # str
print(type(True))  # bool
print(type([1, 2, 3]))  # list
print(type((1, 2)))  # tuple
print(type({1: 'one', 2: 'two'}))  # dict
print(set([1, 2, 3]))  # set
print(frozenset([1, 2, 3]))  # frozenset
print(type(None))  # NoneType

'''
Mutable can be changed:
- list
- dict
- set
Immutable cannot be changed:
- int
- float
- string
- bool
- tuple
- frozenset
- NoneType

Important: In Python only immutable keys can be used for dictionary and immutable items can be put inside a set. 
This is because Python uses the hashing of these keys and values for instant lookups. 
If a value could be changed the hashing would break.

Some of the new data types:
- Tuple is an immutable list which cannot be changed.
- Set is a mutable collection of unique items. It can automatically remove duplicates and checks if an item 
  already exists in O(1) time.
- Frozenset is an immutable set which cannot be changed after the creation. 
  This way frozenset can be a key for dictionary, unlike the normal set.
- NoneType is a Python version of null, representing missing or no value.
'''

################################
### STRINGS *
################################
user_name = " John "
age = 25

# Clean name
clean_name = user_name.strip()

# Print greeting
print(f"Hello {clean_name}, you are {age} years old.")
# Hello John, you are 25 years old.

# Print debug - GOOD FOR DEBUGGING
print(f"{clean_name=}, {age=}")
# clean_name='John', age=25

# Split and join
csv_data = "1,2,3,4,5"
items = csv_data.split(",")
print(items)
# ['1', '2', '3', '4', '5']

print(f"Items string: {', '.join(items)}")
# Items string: 1, 2, 3, 4, 5

# Formatting
print("#" * 80)
###############################################################################
print(f"{age:>10}")  # Right align
#         25
print(f"{age:<10}")  # Left align
# 25
print(f"{age:^10}")  # Center align
#     25
print(f"{age:=^10}")  # Center align with padding
# ====25====
print(f"{age:0>10}")  # Zero padding
# 0000000025

print(f"{3.3255:.2f}")  # 2 decimal places
# 3.33
print(f"{3_325_500:,}")  # Thousands separator
# 3,325,500

# Operations
print(clean_name.replace("h", ""))  # replace
# Jon
print(clean_name.upper())  # convert to uppercase
# JOHN
print(clean_name.lower())  # convert to lowercase
# john
print(clean_name.title())  # capitalize first letter of each word
# John
print(clean_name.swapcase())  # swap case
# jOHN
print(clean_name.capitalize())  # capitalize first letter
# John
print(clean_name.isalpha())  # check if string contains only letters
# True
print("file.txt".endswith(".txt"))  # check if string ends with a specific substring
# True
print(clean_name[::-1])  # reverse string
# nhoJ

################################
### LISTS & COMPREHENSIONS *
################################

numbers = [10, 20, 30, 40, 50]

# Methods
numbers.append(60)
print(numbers)  # append
# [10, 20, 30, 40, 50, 60]
print(numbers.pop())  # pop
# 60
numbers.remove(30)
print(numbers)  # remove
# [10, 20, 40, 50]
print(numbers.index(40))  # index
# 2
print(numbers.count(20))  # count
# 1
numbers[1:3]  # slicing
# [20, 40]
numbers[::-1]  # reverse
# [50, 40, 20, 10]
numbers[::2]  # step
# [10, 40]
sorted(numbers, reverse=True)  # sorting NEW LIST
# [50, 40, 20, 10]
numbers.sort()  # sorting IN PLACE
print(numbers)
# [10, 20, 40, 50]
numbers.reverse()  # reverse
print(numbers)
# [50, 40, 20, 10]

# List comprehension
numbers = [10, 20, 30, 40, 50]
halved = [x / 2 for x in numbers]
print(halved)
# [5.0, 10.0, 15.0, 20.0, 25.0]
print([x for x in numbers if x > 35])
# [40, 50]
print([f"Item {i}: {x}" for i, x in enumerate(numbers)])
# ['Item 0: 10', 'Item 1: 20', 'Item 2: 30', 'Item 3: 40', 'Item 4: 50']

# Builtins
print(f"Sum: {sum(numbers)}, Max: {max(numbers)}, Min: {min(numbers)}")
# Sum: 150, Max: 50, Min: 10
print(list(map(str, numbers)))
# ['10', '20', '30', '40', '50']
labels = [f"Item {i + 1}" for i, _ in enumerate(numbers)]
print(list(zip(numbers, labels)))
# [(10, 'Item 1'), (20, 'Item 2'), (30, 'Item 3'), (40, 'Item 4'), (50, 'Item 5')]
print(any([x > 35 for x in numbers]))
# True
print(all([x > 35 for x in numbers]))
# False

'''
SLICING
For extracting parts of sequences e.g., strings, lists, or tuples.
Analogy: Cutting a loaf of bread.

[start : stop : step]
start: inclusive, default 0
stop: exclusive, default len(sequence)
step: default 1

Negative indices:
-1: last item
-2: second last item

step can be negative:
-1: reverse
'''

################################
### DICTIONARIES *
################################
'''
Represents structured data. Used to map JSON in Python.

- Keys are unique, immutable (str, int, etc.)
- Can't retrieve a value if the key doesn't exist
- Use .get() to avoid KeyError
- Merge dictionaries with pipe operator (|) (3.9+) -> duplicated keys righthand wins
'''

user = {
    "id": 1,
    "username": "alex_ai",
    "role": "dev"
}

# Accessing values
print(user['email'])  # KeyError
# KeyError: 'email'
email = user.get("email", "No email found")
print(f"User email: {email}")
# User email: No email found
print("name" in user)
# False

# Add or updating values
user["last_login"] = "2026-05-11"  # For adding or updating one value
print(user)
# {'id': 1, 'username': 'alex_ai', 'role': 'dev', 'last_login': '2026-05-11'}
user.update({"city": "Colombo"})  # For adding or updating multiple values
print(user)
# {'id': 1, 'username': 'alex_ai', 'role': 'dev', 'last_login': '2026-05-11', 'city': 'Colombo'}

# Merge dictionaries
defaults = {"theme": "light", "role": "guest"}
merged_user = defaults | user  # 3.9+, right hand wins
print(f"Merged user: {merged_user}")
# Merged user: {'theme': 'light', 'role': 'dev', 'id': 1, 'username': 'alex_ai', 'last_login': '2026-05-11', 'city': 'Colombo'}
merged_user = {**defaults, **user} # Dictionary merge
print(f"Merged user: {merged_user}")
# Merged user: {'theme': 'light', 'role': 'dev', 'id': 1, 'username': 'alex_ai', 'last_login': '2026-05-11', 'city': 'Colombo'}
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
combined_list = [*list_1, *list_2] # List merge
print(combined_list)
# [1, 2, 3, 4, 5, 6]


# Iteration
for key, value in merged_user.items():
    print(f"{key.capitalize()}: {value}")
# Theme: light
# Role: dev
# Id: 1
# Username: alex_ai
# Last_login: 2026-05-11
# City: Colombo

# Dictionary comprehension
user_uppercased = {k.upper(): v for k, v in merged_user.items()}
print(user_uppercased)
# {'THEME': 'light', 'ROLE': 'dev', 'ID': 1, 'USERNAME': 'alex_ai', 'LAST_LOGIN': '2026-05-11', 'CITY': 'Colombo'}

################################
### Sets
################################
'''
- Unique items
- No order
- Immutable

Purpose:
- Remove duplicates
- Check if an item exists in O(1) time faster than a list
    - if ID in list -> O(n) (reading books)
    - if ID in set -> O(1) (looking at books index)
    - Converting a list to set is faster for multiple lookups, but not beneficial for single lookups.
- Find the intersection (|), union (&), and difference (-) of two sets
'''
raw_tags = ["python", "python", "javascript", "javascript", "java"]

# Deduplication
unique_tags = set(raw_tags)
print(f"Unique tags: {unique_tags}")
# Unique tags: {'javascript', 'java', 'python'}
unique_tags_same_order = list(dict.fromkeys(raw_tags))  # 3.7+ dicts preserve order
print(f"Unique tags (same order): {unique_tags_same_order}")
# Unique tags (same order): ['python', 'javascript', 'java']

# Membership Testing
print(f"Is 'python' in tags? {'python' in unique_tags}")
# Is 'python' in tags? True

# Set operations
backend_skills = {"python", "django", "sql"}
cloud_skills = {"aws", "docker", "python"}

print(f"All skills: {backend_skills | cloud_skills}")  # | union
# All skills: {'aws', 'docker', 'sql', 'python', 'django'}
print(f"Common skills: {backend_skills & cloud_skills}")  # & intersection
# Common skills: {'python'}
print(f"Skills to learn: {backend_skills - cloud_skills}")  # - difference
# Skills to learn: {'sql', 'django'}
print(f"New skills: {backend_skills ^ cloud_skills}")  # ^ symmetric difference
# New skills: {'aws', 'docker', 'sql', 'django'}


################################
### Tuples
################################
'''
- Immutable

Purpose:
- Immutable data structure e.g., coordinates in a map (x, y).
- Unpacking - clean variable assignments.
'''


def get_location() -> tuple[float, float]:
    return 6.93, 79.86  # Returns a tuple of floats


lat, lon = get_location()
print(f"Latitude: {lat}, Longitude: {lon}")
# Latitude: 6.93, Longitude: 79.86
first, *rest = [10, 20, 30, 40, 50]  # Star unpacking
print(f"First: {first}, Rest: {rest}")
# First: 10, Rest: [20, 30, 40, 50]


################################
### Control flows *
################################
# Ternary operator
score = 85
status = "Pass" if score > 50 else "Fail"
print(status)
# Pass

# Enumerate and zip
users = ["Alex", "Dane", "Jane"]
roles = ["Admin", "User", "Guest"]

for i, user in enumerate(users):
    print(f"User {i + 1}: {user}")
# User 1: Alex
# User 2: Dane
# User 3: Jane

for user, role in zip(users, roles):
    print(f"{user} is a {role}")
# Alex is a Admin
# Dane is a User
# Jane is a Guest

# Match-case (3.10+) - pattern matching - to parse LLM tool call outputs
events = [
    {"type": "message", "content": "Hello there!"},
    {"type": "tool_call", "function": "get_weather", "location": "Paris"},
    {"type": "error", "code": 500},
    {"type": "unknown", "data": "???"}
]

for event in events:
    match event:
        case {"type": "message", "content": content}:  # Capture the content
            print(f"User said: {content}")
        case {"type": "tool_call", "function": func_name, "location": loc}:
            print(f"System calling {func_name}() for {loc}")
        case {"type": "error", "code": code} if code >= 500:  # guard clause
            print(f"CRITICAL Server Error: {code}")
        case _:  # Default case
            print(f"Ignored unhandled event: {event}")
# User said: Hello there!
# System calling get_weather() for Paris
# CRITICAL Server Error: 500
# Ignored unhandled event: {'type': 'unknown', 'data': '???'}

'''
Compared to if/else:
- Matches the first pattern and extracts variables in 1 statement
'''


################################
### Functions *
################################
'''Catch-alls - wrappers, decorators, API clients, etc.
*args and **kwargs (args and kwargs naming conventions, only * and ** are reserved)
*args: arguments into a tuple
**kwargs: keyword arguments into a dictionary'''
def flexible_logger(level, *args, **kwargs):
    print(f"[{level.upper()}]")
    print(f"   Positional args: {args} (Type: {type(args).__name__})")
    print(f"   Keyword args: {kwargs} (Type: {type(kwargs).__name__})")


flexible_logger("info", "User logged in", "IP: 127.0.0.1", user_id=34, status="success")
# [INFO]
#    Positional args: ('User logged in', 'IP: 127.0.0.1') (Type: tuple)
#    Keyword args: {'user_id': 34, 'status': 'success'} (Type: dict)

# Mutable default
def bad_add(item, bucket=[]):
    bucket.append(item)
    return bucket


print(bad_add('apple'))
# ['apple']
print(bad_add('banana')) # DEFAULT ARGUMENTS ARE CREATED ONCE AT FUNCTION DEFINITION TIME
# ['apple', 'banana']

# FOR SAFETY: USE NONE
def safe_add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(safe_add('apple'))
# ['apple']
print(safe_add('banana'))
# ['banana']

# Lambda functions
double = lambda x: x * 2
print(double(5))
# 10
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sorted_users = sorted(users, key=lambda user: user['age'])
print(sorted_users)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


################################
### Type hints **
################################
'''
Type hints are real-code.
Purpose (FastAPI & Pydantic):
- FastAPI validates incoming JSON and generates OpenAPI docs

- No need to import from typing module in latest Python versions
- Can use standard built-ins and pipe operator
    - Lists and dicts: list[str], dict[str, int]
    - Optional: str | None (no need for Optional[str])
    - Union: str | int (no need for Union[str, int])
'''

def process_payment(amount: int | float, currency: str = "USD") -> str:
    return f"Processed {amount:.2f} {currency.upper()}"

print(process_payment(100))
# Processed 100.00 USD
print(process_payment(100.50, "EUR"))
# Processed 100.50 EUR

def find_admin(users_list: list[str]) -> dict[str, str] | None:
    for user_item in users_list:
        if user_item == "admin":
            return {"name": "admin", "status": "active"}
    return None

print(find_admin(["admin", "guest"]))
# {'name': 'admin', 'status': 'active'}
print(find_admin(["tester", "guest"]))
# None

# Type alias (reusable and readable)
coordinate = tuple[float, float]

def get_distance(p1: coordinate, p2: coordinate) -> float:
    return 43.3 # After some calculations

print(get_distance((1.2, 3.4), (5.6, 7.8)))
# 43.3

# GENERICS
'''
Any - we lose auto-completion
[T] - 3.12+, we don't know the exact type yet, but will be the same type once given. E.g.,
    list[int] -> int & list[str] -> str.
'''
from typing import Callable, Iterable

def get_first_item[T](items: list[T]) -> T | None:
    return items[0] if items else None

names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3]

first_name = get_first_item(names)
print(f"First name: {first_name} (Type: {type(first_name).__name__})")
# First name: Alice (Type: str)
first_number = get_first_item(numbers)
print(f"First number: {first_number} (Type: {type(first_number).__name__})")
# First number: 1 (Type: int)

# Higher-order types (Callable, Iterable)
'''
Functions can be passed as arguments and returned as results.
Callable: function
    - Callable[[InputType], ReturnType]] - e.g., Callable[[int], str] takes an int and returns a str.
Iterable: object that can be iterated over. e.g., list, tuple, set, or generator.
    - Iterable[int] - iterable of ints.
    
IMPORTANT:
- BE GENEROUS ON INPUT TYPES e.g., Iterable or Sequence
- BE STRICT ON RETURN TYPES e.g., list or tuple
'''
def double(x: int) -> int:
    return x * 2

def apply_math_operations(values: Iterable[int], operation: Callable[[int], int]) -> list[int]:
    """Applies the given operation to each value in the iterable."""
    return [operation(v) for v in values]

print(apply_math_operations([1, 2, 3, 4], double))
# [2, 4, 6, 8]
print(apply_math_operations([1, 2, 3, 4], lambda x: x ** 2)) # Lambda functions can be used as Callable
# [1, 4, 9, 16]


################################
### Classes (OOP)
################################
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    @property # can call like a variable user.is_adult than a function call user.is_adult()
    def is_adult(self) -> bool:
        return self.age >= 18

    @staticmethod # Standalone function, doesn't need `self` and logically belongs to the class
    def create_anonymous() -> "User": # "User" is the return type - forward reference (class hasn't loaded into memory yet)
        return User("Anonymous", 0)

    @classmethod # Factory methods, alternative constructors (used for creating from JSON dictionary or database row)
    def from_dict(cls, data: dict) -> "User": # Doesn't need `self` but needs class reference `cls`
        # `cls` not User(), for subclasses (e.g., Admin) to construct full Admin object, not just User
        # return cls(data["name"], data["age"])

        # IMPORTANT; To avoid the need of overriding in subclasses due to additional attributes,
        # can use `**data` to unpack the dictionary. But keys should match the class attributes.
        return cls(**data)

    def __repr__(self) -> str: # used for debugging and printing
        return f"User(name={self.name}, age={self.age})"

# Inheritance
class Admin(User):
    def __init__(self, name: str, age: int, level: int):
        super().__init__(name, age) # Call the parent class's constructor
        self.level = level

    def __repr__(self) -> str:
        return f"Admin(name={self.name}, age={self.age}, level={self.level})"

alex = Admin("Alex", 28, 10)
print(alex.greet())
# Hello, my name is Alex and I am 28 years old.
print(alex.is_adult)
# True
print(alex)
# Admin(name=Alex, age=28, level=10)

someone = Admin.create_anonymous()
print(someone)
# User(name=Anonymous, age=0)

john = Admin.from_dict({"name": "John", "age": 30, "level": 5})
print(john)
# Admin(name=John, age=30, level=5)


################################
### Data classes *
################################
'''
From Python 3.7. Removes the boilerplate code i.e., __init__ (self), __repr__, etc. for simple data objects.
Just define the class attributes and type hints.

- Exact mental model for Pydantic (BaseModel): data validation in FastAPI and LangChain.
- Makes it easier to understand Pydantic.

Two rules:
- Mutable default safety: forces to use `field(default_factory=...)` and will not allow `tags: list = []`.
    - Factory issues a new list every time the class is instantiated.
- Frozen dataclasses: immutable by default by adding `@dataclass(frozen=True)`. Act like a tuple.
    - Prevents accidental mutation.
    - Can be used as a key in a dictionary or put in a set (hashable).
'''
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    tags: list[str] = field(default_factory=list) # Factory function to create a new list every time

u1 = User(name="Alex", age=28)
u1.tags.append("developer")
print(u1) # Prints with a clean representation
# User(name='Alex', age=28, tags=['developer'])

# Frozen dataclasses
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p1 = Point(x=14.2, y=43.0)
print(p1)
# Point(x=14.2, y=43.0)

try:
    p1.x = 10.0
except AttributeError as e: # dataclasses.FrozenInstanceError inherits from AttributeError
    print(f"Cannot modify frozen dataclass: {e}")
except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")
# Cannot modify frozen dataclass: cannot assign to field 'x'


################################
### Decorators *
################################
'''
A function that wraps another function to change its behavior.
Will not modify the original function's code.

Purpose:
- To avoid code duplication of the same functionality.
    e.g., measuring execution time of functions, logging, etc.
- Used by FastAPI (@app.get, @app.post, etc.) and LangChain (@tool).
    
@wraps(original_func) - Preserves the original function's name, docstring, etc during the wrapping.

Decorators can be chained. E.g., @repeat @timed.
IMPORTANT: Chaining order matters - Bottom -> up. And changes the behavior.
'''
import time
from functools import wraps

def timed(func):
    @wraps(func) # Preserves the original function's name and docstring.
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        start_time = time.perf_counter()

        # Execute the original function
        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        print(f"Finished {func.__name__} in {end_time - start_time:.4f} seconds")
        return result

    return wrapper

@timed
def slow_greeting(name: str) -> str:
    """Returns a greeting after a delay."""
    time.sleep(2)
    return f"Hello, {name}!"

print(slow_greeting("Alex"))
# Starting slow_greeting...
# Finished slow_greeting in 2.0053 seconds
# Hello, Alex!
print(f"Function_name: {slow_greeting.__name__}, \nDocstring: {slow_greeting.__doc__}")
# Function_name: slow_greeting,
# Docstring: Returns a greeting after a delay.

# Parameterized decorators
def repeat(times: int): # gets the `times` parameter from the decorator
    def decorator(func): # gets the target function
        @wraps(func)
        def wrapper(*args, **kwargs): # executes the target function
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator

@repeat(3)
def slow_greeting(name: str) -> str:
    """Returns a greeting after a delay."""
    time.sleep(1)
    return f"Hello, {name}!"

print(slow_greeting("Alex"))
# ['Hello, Alex!', 'Hello, Alex!', 'Hello, Alex!']

# Decorator chaining
@repeat(3)
@timed
def slow_greeting(name: str) -> str:
    """Returns a greeting after a delay."""
    time.sleep(1)
    return f"Hello, {name}!"

print(slow_greeting("Alex"))
# Starting slow_greeting...
# Finished slow_greeting in 1.0023 seconds
# Starting slow_greeting...
# Finished slow_greeting in 1.0051 seconds
# Starting slow_greeting...
# Finished slow_greeting in 1.0001 seconds
# ['Hello, Alex!', 'Hello, Alex!', 'Hello, Alex!']

# Change chaining order
@timed
@repeat(3)
def slow_greeting(name: str) -> str:
    """Returns a greeting after a delay."""
    time.sleep(1)
    return f"Hello, {name}!"

print(slow_greeting("Alex"))
# Starting slow_greeting...
# Finished slow_greeting in 3.0091 seconds
# ['Hello, Alex!', 'Hello, Alex!', 'Hello, Alex!']


