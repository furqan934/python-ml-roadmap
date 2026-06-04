# now cover the basic to advance function in python
# function is a block of code which only runs when it is called. you can pass data, known as parameters, into a function. a function can return data as a result.
# function is a reusable block of code that performs a specific task. it helps to break down a program into smaller, modular pieces, making it easier to read, maintain, and debug. functions can take input in the form of parameters and can return output as well.
# there are two types of functions in python: built-in functions and user-defined functions. built-in functions are pre-defined functions that are available in python, such as print(), len(), and input(). user-defined functions are created by the programmer to perform specific tasks.
# to define a function in python, you use the def keyword followed by the function name and parentheses. you can also specify parameters inside the parentheses if the function takes any input. the function body is indented below the function definition.
# here is an example of a simple function that adds two numbers:    
def add(a, b):
    return a + b
# you can call this function by passing two numbers as arguments, like this:
result = add(5, 3)
print(result)  # Output: 8
# you can also define a function that takes no parameters and simply prints a message:
def print_message():
    print("Hello, World!")
print_message()  # Output: Hello, World!
# functions can also return values. for example, you can define a function that calculates the area of a circle given its radius:
import math
def calculate_area(radius):
    return math.pi * radius ** 2
area = calculate_area(5)
print(area)  # Output: 78.53981633974483


# you can also define a function that takes multiple parameters and returns a value. for example, you can define a function that calculates the average of a list of numbers:
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)  

average = calculate_average([1, 2, 3, 4, 5])
print(average)  # Output: 3.0

# functions can also have default parameter values. for example, you can define a function that greets a person with a default greeting message:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"   
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
# functions can also take variable-length arguments. for example, you can define a function that takes any number of arguments and returns their sum:
def sum_numbers(*args):
    return sum(args)
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15
# **kwargs allows you to pass a variable number of keyword arguments to a function. for example, you can define a function that takes any number of keyword arguments and prints them:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Alice", age=30, city="New York"
            )


# python decoraters, lambda , recursive function, generator function, higher order function, closure, global and nonlocal variable, docstring, type hinting, anonymous function, lambda function, map(), filter(), reduce(), zip(), enumerate(), args and kwargs, *args and **kwargs, default parameter values, variable-length arguments, keyword-only arguments, positional-only arguments, function annotations, function overloading, function nesting, function scope, function recursion, function memoization, function decorators, function generators, function closures, function factories, function currying, function partial application.
# decoraters
# in simmple words, a decorator is a function that takes another function as input and extends its behavior without modifying the original function. it allows you to add functionality to an existing function in a clean and reusable way.
def change_case(func):
    def  myInner():
        return func().upper()
    return myInner
@change_case
def greet():
    return "hello"
print(greet())  # 


# next the important proprty of function 
# lambda function
# a lambda function is a small anonymous function that can take any number of arguments but can only have one expression. it is often used for short, simple functions that are not worth defining with a full function definition. the syntax for a lambda function is:
# lambda arguments: expression
# for example, you can define a lambda function that adds two numbers like this:
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8


# recursive function
# a recursive function is a function that calls itself in order to solve a problem. it typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems. for example, you can define a recursive function to calculate the factorial of a number:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)  # Output: 120

# generator function
# a generator function is a special type of function that returns an iterator. it allows you to iterate over a sequence of values without having to store the entire sequence in memory at once. you can define a generator function using the yield keyword. for example, you can define a generator function that generates the Fibonacci sequence:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# example usage of the fibonacci generator
for num in fibonacci(10):
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34