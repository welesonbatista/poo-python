#Inheritance Exemple
print ("\nExemple to Inheritance")
class Animal:
  def __init__(self, name)->None:
    self.name = name

  def walk (self):
    print(f"The animal is walking")
    return

  def make_sound(self):
    pass

class Dog (Animal):
  def make_sound(self):
    return "woof woof"
  
class Cat(Animal):
  def make_sound(self):
    return "Meow meow"
    
dog = Dog(name = "Rex")
cat = Cat(name= "black panther")

animals = [dog, cat]

for animal in animals:
  print(f"{animal.name} make: {animal.make_sound()}")

print("\nExemple for encapsulation")

class BankAccount:
  def __init__(self, balance)->None:
    self.__balance = balance # private atribute

  def deposit (self, value):
    if value > 0:
      self.__balance += value
  
  def withdraw(self, value):
    if value > 0 and value <= self.__balance:
      self.__balance -= value

  def get_balance(self):
    return self.__balance
  
account = BankAccount(balance=8000)
print(f"The balance of your account is: ", {account.get_balance()})

account.deposit(122)
print(f"The balance of your account is: ", {account.get_balance()})

account.withdraw(888)
print(f"The balance of your account is: ", {account.get_balance()})
