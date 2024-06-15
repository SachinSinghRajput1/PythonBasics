import functools
import itertools


#Multiplication table
def mult_table(n):
    return lambda x:x*n
n = int(input('Enter a number: '))
y = mult_table(n)
print(f'The entered number is {n}.')
for i in range(11):
# print(('%d x %d = %d' %(n, i, y(i))))


#map() function
 # This program will multiplicate each element of the list with 5 and followed by power of 2.
 special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
 print(f'Non special numbers are {list(map(lambda x: x * 5, special_nums))}')
 print(f'Non special numbers list is {list(map(lambda x: pow(x, 2), special_nums))}')

#lambda function with if/else
age = int(input('Enter an age: '))
print(f'The entered age is {age}.')
(lambda age: print('Therefore, you can use a vote.') if (age>=18) else print('Therefore, you do not use a vote.'))(age)

#lambda function usage with multiple statements
special_nums = [[0.577, 1.618, 2.718, 3.14], [6, 28, 37, 1729]]
special_nums_sorted = lambda a: (sorted(i) for i in a)
# Get the maximum of special numbers in the list
special_nums_max = lambda a, f: [y[len(y) - 1] for y in f(a)]
print(f'The maximum of special numbers in each list is {special_nums_max(special_nums, special_nums_sorted)}.')
# Get the minimum of special numbers in the list
special_nums_min = lambda a, f: [y[len(y) - len(y)] for y in f(a)]
print(f'The minimum of special numbers in each list is {special_nums_min(special_nums, special_nums_sorted)}.')
# Get the second maximum of special numbers in the list
special_nums_second_max = lambda a, f: [y[len(y) - 2] for y in f(a)]
print(f'The second maximum of special numbers in each list is {special_nums_second_max(special_nums, special_nums_sorted)}')


lambda_list = []
# Multiplication of pi number and 12 in one line using lambda function
lambda_list.append((lambda x:x*3.14) (12))
# Division of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x/3.14) (12))
# Addition of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x+3.14) (12))
# Subtraction of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x-3.14) (12))
# Remainder of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x%3.14) (12))
# Floor division of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x//3.14) (12))
# Exponential of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x**3.14) (12))
# Printing the list
print(lambda_list)

help(functools)
help(itertools)
