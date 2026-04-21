# loops in python 
# 1. the for loop in python
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. It is used to execute a block of code repeatedly for a fixed number of times.
for i in range(5):
    print("The value of i is :",i);

# 2. the while loop in python
# while loop is used to execute a block of code repeatedly as long as a given condition is true. It is used when the number of iterations is not known beforehand.
count = 0;
while count < 5:
    print("The value of count is :",count);
    count += 1;


# 3. the nested loops in python
# nested loops are used to execute a block of code inside another block of code. It is used when we want to perform a task that requires multiple levels of iteration.
for i in range(3):
    for j in range(2):
        print("The value of i is :",i," and the value of j is :",j);


# 4. the break statement in python
# break statement is used to exit the loop when a certain condition is met. It is used
# when we want to stop the loop before it has iterated through all the items in the sequence.
for i in range(5):
    if i == 3:
        break;
    print("The value of i is :",i); 

# 5. the continue statement in python
# continue statement is used to skip the current iteration of the loop and move to the next iteration. It is used when we want to skip a certain condition in the loop.
for i in range(5):
    if i == 3:
        continue;
    print("The value of i is :",i);


# functions inpython 
# 1. the def keyword in python
# def keyword is used to define a function in python. It is used to create a reusable block of code that can be called multiple times in the program.
def greet(name):
    print("Hello, " + name + "! Welcome to Python programming.");
greet("Alice");
greet("Bob");

# 🛠️ PART 2 — MINI PROJECT (REAL SYSTEM)
# 💡 Project: “ATM Machine System” with diffrent function and loops used in it 
# 1. the ATM machine system in python
# the ATM machine system is a simple program that simulates the functionality of an ATM machine. It allows the user to perform various operations such as checking balance, withdrawing money, depositing money, and exiting the program. The program uses functions and loops to implement the functionality of the ATM machine system.

# initial balance of the user
balance = 1000;
def check_balance():
    print("Your current balance is :",balance);
def withdraw_money(amount):
    # using global variable to access the balance variable inside the function. means that we can modify the balance variable inside the function and it will reflect in the global scope as well.
    global balance;
    if amount > balance:
        print("Insufficient balance. Please try again.");
    else:
        balance -= amount;
        print("You have withdrawn :",amount,". Your current balance is :",balance);
def deposit_money(amount):
    global balance;
    balance += amount;
    print("You have deposited :",amount,". Your current balance is :",balance);
def atm_machine():
    while True:
        print("Welcome to the ATM Machine System");
        print("1. Check Balance");
        print("2. Withdraw Money");
        print("3. Deposit Money");
        print("4. Exit");
        choice = int(input("Please enter your choice: "));
        if choice == 1:
            check_balance();
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "));
            withdraw_money(amount);
        elif choice == 3:
            amount = int(input("Enter the amount to deposit: "));
            deposit_money(amount);
        elif choice == 4:
            print("Thank you for using the ATM Machine System. Goodbye!");
            break;
        else:
            print("Invalid choice. Please try again.");
atm_machine();


