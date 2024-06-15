import sys

def function():
    for i in range(10):
        if i % 2 == 0:
            yield i


nlis = []
for i in function():
    nlis.append(i)
print(nlis)


"""In the following example, the list comprehension will return the list of cube of elements.
Whereas the generator expression will return the reference of the calculated value.
Rather than this application, the ^function 'next()' can be used on the generator object. """

special_nums = [0.577, 1.618, 2.718, 3.14, 6, 37, 1729]
list_comp = [i*3 for i in special_nums] # This is a list comprehension.
generator_exp = (i*3 for i in special_nums) # This is a generator expression.
print(list_comp)
print(generator_exp)

special_nums = [0.577, 1.618, 2.718, 3.14, 6, 37, 1729]
generator_exp = (i*3 for i in special_nums) # This is a generator expression.
nums_list = []
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
nums_list.append(next(generator_exp))
print(nums_list)

def mult_table(n):
 for i in range(0, 11):
    yield n*i
    i+=1
mult_table_list = []
for i in mult_table(20):
 mult_table_list.append(i)
print(mult_table_list)

# List comprehension
cubic_nums_lc = [i**3 for i in range(1500)]
print(f'Memory in bytes with list comprehension is {sys.getsizeof(cubic_nums_lc)}.')
# Generator expression of the same conditions
cubic_nums_gc = (i**3 for i in range(1500))
print(f'Memory in bytes with generator expression is {sys.getsizeof(cubic_nums_gc)}.')

def infinite():
 count = 0
 while True:
    yield count
    count = count + 1
for i in infinite():
 print(i)

def square_number(num):
 for i in range(num):
     yield i**i
generator = square_number(6)
# Using 'while' loop
while True:
 try:
    print(f'The number using while loop is {next(generator)}.')
 except StopIteration:
    break
# Using 'for' loop
nlis = []
for square in square_number(6):
 nlis.append(square)
print(f'The numbers using for loop are {nlis}.')
# Using generator comprehension
square = (i**i for i in range(6))
square_list = []
square_list.append(next(square))
square_list.append(next(square))
square_list.append(next(square))
square_list.append(next(square))
square_list.append(next(square))
square_list.append(next(square))
print(f'The numbers using generator comprehension are {square_list}.')



def fibonacci(numbers):
 a, b = 0, 1
 for _ in range(numbers):
    a, b = b, a+b
    yield a
def square(numbers):
 for i in numbers:
    yield i**2
print(sum(square(fibonacci(25))))

