import math
#import decorator
#from decorator import *
import functools



#arbitrary arguments
def arbitrary_argument(func):
 def wrapper(*args,**kwargs):
  print(f'These are positional arguments {args}.')
  print(f'These are keyword arguments {kwargs}.')
  func(*args)
 return wrapper

"""1. Without arguments decorator"""
print(__doc__)
@arbitrary_argument
def without_argument():
 print("There is no argument in this decorator.")
without_argument()

"""2. With positional arguments decorator"""
print(__doc__)
@arbitrary_argument
def with_positional_argument(x1, x2, x3, x4, x5, x6):
 print(x1, x2, x3, x4, x5, x6)
with_positional_argument(math.inf, math.tau, math.pi, math.e, math.nan, -math.inf)

"""3. With keyword arguments decorator"""
print(__doc__)
@arbitrary_argument
def with_keyword_argument():
 print("Python and R are my favorite programming languages and keyword arguments.")
with_keyword_argument(language_1="Python", language_2="R")




#Debugging decorators
def capitalize_dec(function):
 @functools.wraps(function)
 def wrapper():
   return function().capitalize()
 return wrapper
@capitalize_dec
def message():
 "Python is the most popular programming language."
 return 'PYTHON IS THE MOST POPULAR PROGRAMMING LANGUAGE. '
print(message())
print()
print(message.__name__)
print(message.__doc__)



#Preserving decorators
def preserved_decorator(function):
 def wrapper():
   print('Before calling the function, this is printed.')
   function()
   print('After calling the function, this is printed.')
 return wrapper
@preserved_decorator
def message():
 """This function prints the message when it is called."""
 print('Python is the most popular programming language.')
message()
print(message.__name__)
print(message.__doc__)
print(message.__class__)
print(message.__module__)
print(message.__code__)
print(message.__closure__)
print(message.__annotations__)
print(message.__dir__)
print(message.__format__)