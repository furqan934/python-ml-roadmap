# the basics of the python and the syntax of the python is very easy to learn and understand
name = "Muhammad Furqan";
age = 21;
print("My name is :",name , "and my age is :",age);

# now we will learn about the data types in python
# there are several data types in python such as int, float, str, list, tuple, dict, set, etc.
# int is used to store the whole numbers
x = 10;
print("The value of x is :",x);
# float is used to store the decimal numbers
pi = 3.14;
print("The value of pi is :",pi);

# str is used to store the string values
greeting = "Hello, World!";
print(greeting);


# 2. the input and output in python
# input is used to take the input from the user
# name = input("Enter your name: ")
# print("Hello, " + name + "! Welcome to Python programming.");


# 3. the conditional statements in python
# if statement is used to execute a block of code if a condition is true
# age = int(input("Enter your Date of Birth: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# elif statement is used to check multiple conditions
# marks = int(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("Grade: A")
# elif marks >= 80 and marks < 90:
#     print("Grade: B")
# elif marks >= 70 and marks < 80:
#     print("Grade: C")
# elif marks >= 60 and marks < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")



# nested if statement is used to check multiple conditions within another condition conceptually the main complexity `of nested if statements is that it can lead to a large number of conditions and can make the code difficult to read and understand. It can also lead to a lot of indentation which can make the code look cluttered and hard to follow. Additionally, if not used carefully, nested if statements can lead to logical errors and bugs in the code. Therefore, it is important to use nested if statements judiciously and to consider alternative approaches such as using functions or switch statements when appropriate.`

# giveing an exmple of the routes startign fro  inital position and used nested elif rto check that the user ig go and back to its inital position and check all the cities once and then print the final position of the user
# use nested if statement to check the routes of the user
# initial position of the user
# make it like that the user can go to different cities and then come back to the initial position and check the final position of the user
initial_position = "City A"
print("Initial position:", initial_position)
# user goes to City B
current_position = "City B"
if current_position == "City B":
    print("User is in City B")
    # user goes to City C
    current_position = "City C"
    if current_position == "City C":
        print("User is in City C")
        # user goes back to City A
        current_position = "City A"
        if current_position == "City A":
            print("User is back to City A")
            final_position = current_position
            print("Final position:", final_position)

# TASKS 
# Task 1:Largest of 3 Numbers , take 3 numbers as input from the user and find the largest number among them using if-else statements.
# Task 2: Check if a number is even or odd, take a number as input from the user and check if it is even or odd using if-else statements.
# Task 3: Check if a number is positive, negative or zero, take a number as input from the user and check if it is positive, negative or zero using if-else statements.

# solution of the tasks
# Task 1: Largest of 3 Numbers
# num_1 = float(input("Enter the first number: "))
# num_2 = float(input("Enter the 2nd number: "))
# num_3 = float(input("Enter the 3rd number: "))


# if num_1 >= num_2 and num_1 >= num_3:
#     largest = num_1
# elif num_2 >= num_1 and num_2 >= num_3:
#     largest = num_2
# else:
#     largest = num_3
# print("The largest number is:", largest)    

# # Task 2: Check if a number is even or odd
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# Task 3: Check if a number is positive, negative or zero
# number = float(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")    
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


# PART 3 — Mini Challenge (IMPORTANT)
# Build:

# 👉 “User Info Checker”

# Program should:

# Take name, age, marks
# Print:
# Name
# If user is adult or not
# Grade based on marks

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
print("Name:", name)
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
else:
    print("Grade: F")
