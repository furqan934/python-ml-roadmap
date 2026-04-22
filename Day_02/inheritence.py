# inheritence in python 
# inheritance is a mechanism in which a new class is derived from an existing class. The new class is called the child class or subclass, and the existing class is called the parent class or superclass. The child class inherits the attributes and methods of the parent class and can also have its own attributes and methods.
# types of inheritance in python :
# 1. single inheritance : a child class inherits from a single parent class.
# 2. multiple inheritance : a child class inherits from multiple parent classes.
# 3. multilevel inheritance : a child class inherits from a parent class, which in turn inherits from another parent class.
# 4. hierarchical inheritance : multiple child classes inherit from a single parent class.
# example of single inheritance :
# superclass or parent class
class Animal:
    # method eat is a method that is defined in the parent class and can be inherited by the child class.
    def eat(self):
        print("Eating...")  
    
# subclass or child class that inherits from the parent class Animal
class Dog(Animal):
    # method bark is a method that is defined in the child class and is not inherited from the parent class.
    def bark(self):
        print("Barking...")
dog1 = Dog()
dog1.eat()  # Output: Eating...
dog1.bark()  # Output: Barking...

# example of multiple inheritance :
class Father:
    def skills(self):
        print("Programming, Cooking")
class Mother:
    def skills(self):
        print("Dancing, Singing")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)  # calling the skills method of the Father class
        Mother.skills(self)  # calling the skills method of the Mother class
        print("Drawing, Writing")
child1 = Child()
child1.skills()


# example of multilevel inheritance :
class Grandfather:
    def skills(self):
        print("Gardening, Fishing")
class Father(Grandfather):
    def skills(self):
        Grandfather.skills(self)  # calling the skills method of the Grandfather class
        print("Programming, Cooking")
class Child(Father):
    def skills(self):
        Father.skills(self)  # calling the skills method of the Father class
        print("Drawing, Writing")
child1 = Child()
child1.skills()


# example of hierarchical inheritance :
class Parent:
    def skills(self):
        print("Programming, Cooking")
class Child1(Parent):
    def skills(self):
        Parent.skills(self)  # calling the skills method of the Parent class
        print("Drawing, Writing")
class Child2(Parent):
    def skills(self):
        Parent.skills(self)  # calling the skills method of the Parent class
        print("Dancing, Singing")

child1 = Child1()
child2 = Child2()

child1.skills()  # Output: Programming, Cooking, Drawing, Writing
child2.skills()  # Output: Programming, Cooking, Dancing, Singing


# now there is other term in the inheritence which is the aggregation and composition :
# aggregation is a relationship between two classes where one class is a part of another class. The part class can exist independently of the whole class. For example, a car has an engine, but the engine can exist without the car.
class Engine:
    def start(self):
        print("Engine started.")    
class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine (aggregation)
    def start(self):
        self.engine.start()  # Car uses the Engine to start
car1 = Car()
car1.start()  # Output: Engine started.

# composition is a relationship between two classes where one class is a part of another class. The part class cannot exist independently of the whole class. For example, a house has a room, but the room cannot exist without the house.
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Bedroom")]  # House has Rooms (composition)
house1 = House()
for room in house1.rooms:
    print(room.name)  # Output: Living Room, Bedroom
    