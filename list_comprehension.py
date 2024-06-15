import math

# Using for loop
cubic_nums = []
for i in range(5):
    i**=3
    cubic_nums.append(i)
print(cubic_nums)
# Using list comprehension
cubic_nums = [i**3 for i in range(5)]
print(cubic_nums)
# Using list comprehension
cubic_nums = [math.pow(i, 3) for i in range(5)]
print(cubic_nums)

# Using for loop
even_numbers = []
for i in range(21):
     if i%2 == 0:
      even_numbers.append(i)
print(even_numbers)
# Using list comprehension
even_numbers = [i for i in range(21) if i%2==0]
print(even_numbers)

# Create a list of multiplies of three from 0 to 30
# Using for loop
nlis =[]
for i in range(30):
 if i%3 == 0:
    nlis.append(i)
    print(nlis)
# Using list comprehension
nlis = [i for i in range(30) if i%3==0]
print(nlis)

 #Using for loop
text = []
for i in 'Python is a programming language':
 text.append(i)
print(text)
# Using list comprehension
text = [i for i in 'Python is a programming language']
print(text)


# Using for loop
languages = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'PHP']
python = []
for i in 'Python':
 python.append(i)
print(python)
# Using list comprehension
python = [i for i in 'Python']
print(python)
# Using lambda function
python = list(map(lambda i: i, 'Python'))
print(python)

lang_lis = []
for i in languages:
    if i != 'C':
        lang_lis.append(i)
print(lang_lis)
#Using list comprehension
lang_lis = [i for i in languages if i != 'C']
print(lang_lis)

special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
# Using for loop
new_lis = []
for i in special_nums:
 if i < 5:
    new_lis.append(i)
    print(new_lis)
# Using list comprehension
new_lis = [i for i in special_nums if i < 5]
print(new_lis)

# Using for loop
numbers = []
for i in range(11):
 if i%2 == 0:
    numbers.append('Even')
else:
 numbers.append('Odd')
print(f'For loop: {numbers}')
# Using list comprehension
numbers = ['Even' if i%2==0 else 'Odd' for i in range(11)]
print(f'List comprehension: {numbers}')
# Using lambda function
numbers = list(map(lambda i: i, ['Even' if i%2==0 else 'Odd' for i in range(11)]))
print(f'Lambda: {numbers}')

 #Using nested for loop
empty_list = []
matrix_list = [[0.577, 1.618, 2.718, 3.14], [6, 28, 37, 1729]]
for i in range(len(matrix_list[0])):
 T_row = []
 for row in matrix_list:
    T_row.append(row[i])
 empty_list.append(T_row)
print(empty_list)
# Using list comprehension
empty_list = [[row[i] for row in matrix_list] for i in range(4)]
print(empty_list)

 #Using nested for loop
empty_matrix = []
for i in range(5):
 empty_matrix.append([])
 for j in range(5):
    empty_matrix[i].append(j)
print(empty_matrix)
# Using list comprehension
empty_matrix = [[j for j in range(5)] for i in range(5)]
print(empty_matrix)

 #Transpose of 2D matrix
matrix = [[0.577, 1.618, 0],
 [2.718, 3.14, 1],
 [6, 28, 28]]
transpose_matrix = [[i[j] for i in matrix] for j in range(len(matrix))]
print(transpose_matrix)
