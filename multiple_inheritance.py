class Animal:
  def __init__(self, name):
    self.name = name
  
  def make_sound(self):
    pass

class Mammal (Animal):
  def breastfeed(self):
    return f"{self.name} are breastfeeding"

class Bird (Animal):
  def fly(self):
    return f"{self.name} are flying"
  
class Bat (Mammal, Bird):
  def make_sound(self):
    return "Bats make ultrasonic sounds."
  
bat = Bat(name="Batman")

print("Bat's name is:", bat.name)
print("Bat sound: ", bat.make_sound())

print ("Bat breastfeeding: ", bat.breastfeed())
print ("Bat flying: ", bat.fly())