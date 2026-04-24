# abstraction in puthon:
# the 3rd pillar of the oop in python is the abstraction :
# abstraction is the process of hiding the implementation details and only exposing the functionality. It is achieved through the use of abstract classes and interfaces. Abstract classes are classes that cannot be instantiated and are meant to be subclassed. Interfaces are a collection of abstract methods that can be implemented by any class.
# importing the ABC module to create an abstract class and the abstractmethod decorator to define abstract methods.
from abc import ABC, abstractmethod 
# example of abstract class :

class Shape(ABC):
    # area is an abstract method that is defined in the abstract class and must be implemented by any subclass that inherits from the abstract class.
    @abstractmethod # the @abstractmethod decorator is used to indicate that the method is an abstract method and must be implemented by any subclass that inherits from the abstract class.
    def area(self):
        pass # the pass statement is used as a placeholder for the body of the method, which will be implemented in the subclass.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
circle1 = Circle(5)
print(circle1.area())  # Output: 78.5

# example of interface :
# in python we can create an interface using an abstract class with only abstract methods.

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass
class Document(Printable):
    def __init__(self, content):
        self.content = content
    def print(self):
        print(self.content)
document1 = Document("Hello, World!")
document1.print()  # Output: Hello, World!

# diffrence between abstract class and interface :
# 1. An abstract class can have both abstract and concrete methods, while an interface can only have abstract methods.
# 2. A class can inherit from only one abstract class, but it can implement multiple interfaces.
