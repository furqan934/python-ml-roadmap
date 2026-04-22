# polymarpisam in the puthon oop 
# the 2nd pillar of the oop in python the polymorphism :
# polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass. Polymorphism is achieved through method overriding and method overloading.
# method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The implementation in the subclass overrides the implementation in the superclass.
# method overloading is a feature that allows a class to have more than one method with the same name, but with different parameters. The correct method to call is determined at runtime based on the number and type of arguments passed to the method.
# example of method overriding :
class Animal:
    def sound(self):
        print("Animal makes a sound")   
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animal1 = Animal()
animal2 = Dog()
animal3 = Cat()
animal1.sound()  # Output: Animal makes a sound
animal2.sound()  # Output: Dog barks
animal3.sound()  # Output: Cat meows

# example of method overloading :
class Math:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
math = Math()
# print(math.add(1, 2))  # This will raise a TypeError because the add method with two parameters is overridden by the add method with three parameters.
print(math.add(1, 2, 3))  # Output: 6

