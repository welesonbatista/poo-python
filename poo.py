#OOP

#Example Class
class Person:
  def __init__(self, name, age)->None:
    self.name = name
    self.age = age
  
  def greet(self):
    return f"Hello, my name is {self.name} and i'm {self.age} years old" 
  
#Object
person1 = Person ("Weleson",29)
print("Name: ", person1.name)
print("Age: ", person1.age)
message = person1.greet()
print(message)

person2 = Person("Wilson", 45)
message= person2.greet()
print(message)