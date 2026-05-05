class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Animal Sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
    
class Ele(Animal):
    def speak(self):
        return f"{self.name} says Booo"
    
my_dog = Dog(name = "Buddy")
my_cat = Cat(name = "danddo")
my_ele = Ele(name = "ele")

print(my_dog.speak())
print(my_cat.speak())
print(my_ele.speak())