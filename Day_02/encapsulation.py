# the 1st pillar of the oop in python the encapsulation :
# encapsulation is the process of hiding the internal details of an object and only exposing a public interface. It is achieved through the use of access modifiers such as private, protected, and public.
# in python we can use the following access modifiers :
# 1. public : attributes and methods with no leading underscore are public and can be accessed from anywhere.
# 2. protected : attributes and methods with a single leading underscore are protected and should only be accessed from within the class or its subclasses.
# 3. private : attributes and methods with a double leading underscore are private and should only be accessed from within the class itself.

class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self._age = age   # protected attribute
        self.__ssn = "123-45-6789"  # private attribute is not accessible outside the class

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")


# now we can create an object of the person class and access the public and protected attributes, but we cannot access the private attribute directly.
person_01 = Person("Ali", 30)
person_01.display_info()  # Output: Name: Ali, Age: 30
print(person_01.name)     # Output: Ali
print(person_01._age)     # Output: 30
# print(person_01.__ssn)   # This will raise an AttributeError

# task : create a class called BankAccount with the following attributes and methods:
# attributes : account_number (public), balance (protected), __pin (private)
# methods : deposit (public), withdraw (public), display_balance (public)

class BankAccount:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number 
        self._balance = balance
        self.__pin = pin

    # method deposit is a public method that allows the user to deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")
    # method withdraw is a public method that allows the user to withdraw money from the account.
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    # method display_balance is a public method that allows the user to display the current balance of the account.
    def display_balance(self):
        print(f"Current balance: {self._balance}")
# now we can create an object of the BankAccount class and access the public methods, but we cannot access the protected and private attributes directly.
account_01 = BankAccount("123456789", 1000, "1234")
account_01.display_balance()  # Output: Current balance: 1000
account_01.deposit(500)      # Output: Deposited 500. New balance: 1500
account_01.withdraw(200)      # Output: Withdrew 200. New balance: 1300


