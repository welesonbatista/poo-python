from typing import Any

def my_decorator(func):
  def wrapper():
    print("Before my function was called")
    func()
    print("After my function was called")
  return wrapper

@my_decorator
def my_function():
  print("My function was called")

my_function()

class MyClassDecorator:
  def __init__(self, func)->None:
    self.func = func
  
  def __call__(self)->Any:
    print("Before my function was called(Class Decorator)")
    self.func()
    print("After my function was called(Class Decorator) ")
  
@MyClassDecorator
def second_function():
  print("Second function was called")

second_function()