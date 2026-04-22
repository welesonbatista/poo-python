#@classmethod
#@staticmethod

class MyClass:

    value = 10  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute (requires an object)

    # requires an object to be instantiated
    def instance_method(self):
        return f"Instance method called for {self.name}"
    
    @classmethod
    def class_method(cls):
        return f"class method called for value = {cls.value}"
    
    @staticmethod
    def static_method():
        return "Static method called"


obj = MyClass(name="Example Class")
print(obj.instance_method())
print(MyClass.value)
print(MyClass.class_method())
print(MyClass.static_method())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year =  year

    @classmethod
    def car_create(cls, config):
        brand, model, year = config.split(",")
        return cls(brand, model, int(year))

config1= "Honda, Civic, 2009"
car1 = Car.car_create(config1)
print(f"Brand: {car1.brand}, Model: {car1.model}, Year: {car1.year}")