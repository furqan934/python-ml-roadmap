# oops in python :
# 1. class
# 2. object
# 3. inheritance
# 4. polymorphism
# 5. encapsulation
# 6. abstraction
# class : class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# object : object is an instance of a class. It is created from a class and has the attributes and methods defined in the class.
# inheritance : inheritance is a mechanism in which a new class is derived from an existing class. The new class is called the child class or subclass, and the existing class is called the parent class or superclass. The child class inherits the attributes and methods of the parent class and can also have its own attributes and methods.
# polymorphism : polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass. Polymorphism is achieved through method overriding and method overloading.
# encapsulation : encapsulation is the process of hiding the internal details of an object and only exposing a public interface. It is achieved through the use of access modifiers such as private, protected, and public.
# abstraction : abstraction is the process of hiding the implementation details and only exposing the functionality. It is achieved through the use of abstract classes and interfaces. Abstract classes are classes that cannot be instantiated and are meant to be subclassed. Interfaces are a collection of abstract methods that can be implemented by any class.
# example of class and object :
class Car:
    # __init__ is a special method that is called when an object is created from the class. It is used to initialize the attributes of the object.
    # self is a reference to the current instance of the class. It is used to access the attributes and methods of the class.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Camry", 2020)
car1.display_info()  # Output: 2020 Toyota Camry