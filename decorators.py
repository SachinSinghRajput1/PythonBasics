import math
import functools

# Define a decorating function
"""
In the following example, the function outer_addition that is some voluminous is decorated.
"""
def addition(a, b):
 print(a+b)
def outer_addition(func):
 def inner(a, b):
  if a < b:
   a, b = b, a
  return func(a, b)
 return inner
result = outer_addition(addition)
result(math.pi, math.e)

"""
Rather than above function, Python ensures to employ decorator in easy way with the symbol @ called 'pie' syntax, as
"""
def outer_addition(function):
 def inner(a, b):
  if a < b:
   a, b = b, a
  return function(a, b)
 return inner
@outer_addition # Syntax of decorator
def addition(a, b):
 print(a+b)
result = outer_addition(addition)
result(math.pi, math.e)

#Reprocessing decorator
def do_twice(function):
 def wrapper_do_twice():
  function()
 function()
 return wrapper_do_twice
@do_twice
def text():
 print('Python is a programming language.')
text()




#decorators with Arguments
"""
The function wrapper_function() can admit any number of argument and pass them on the function.
 """
def do_twice(function):
 def wrapper_function(*args, **kwargs):
   function(*args, **kwargs)
   function(*args, **kwargs)
 return wrapper_function
@do_twice
def text(programming_language):
 print(f'{programming_language} is a programming language.')
text('Python')

# Fancy decorators
class Microorganism:
 def __init__(self, name, product,display):
  self.name = name
  self.product = product
  self.display = display


  def display(cls):
   return cls('Aspergillus niger', 'inulinase')

 @property
 def show(self):
  return self.name + ' produces ' + self.product + ' enzyme'
organism = Microorganism('Aspergillus niger', 'inulinase','display')
print(f'Microorganism name: {organism.name}')
print(f'Microorganism product: {organism.product}')
print(f'Message: {organism.show}.')
#organism = Microorganism.display()
#print(f'The fungus {organism.name} produces {organism.product} enzyme.')

@staticmethod
def name():
 print('Aspergillus niger is a fungus that produces inulinase enzyme.')
 organims = Microorganism()
 organims.name()
 Microorganism.name()






"""
In the following example, @iterate refers to a function object that can be called in another function.
The @iterate(numbers=4) will return a function which behaves as a decorator.
"""
def iterate(numbers):
 def decorator_iterate(function):
  @functools.wraps(function)
  def wrapper(*args, **kwargs):
   for _ in range(numbers):
    worth = function(*args, **kwargs)
    return worth
   return wrapper
  return decorator_iterate
#@iterate(numbers=4)

def function_one(name):
 print(f'{name}')
x = function_one('Python')

