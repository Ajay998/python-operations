# Basically we need def keyword with a name to create a function but we can use lambda keyword to define an unnamed function.
# Syntax: lambda arguments: expression


# add = lambda num: num + 4
# print( add(6) )

# a = lambda x, y : (x * y)
# print(a(4, 5))

# a = lambda x, y, z : (x + y + z)
# print(a(4, 5, 5))

# ****************************************
# The filter() method accepts two arguments in Python: a function and an iterable such as a list. (Avishyam ulath kitiyal mathi)
# filter(function, iterable)

# list_ = [35, 12, 69, 55, 75, 14, 73]
# odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))
# print('The list of odd number is:',odd_list)

# Syntax: map(fun, iter)
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.) (Every element check cheyth and give answer)

# list_ = [35, 12, 69, 55, 75, 14, 73]
# check_odd_list = list(map(lambda num:(num % 2 != 0) , list_ ))
# print(check_odd_list)
#
# list_ = [35, 12, 69, 55, 75, 14, 73]
# square_number = list(map(lambda num:num*num, list_ ))
# print(square_number)

# ******************************************
# from functools import reduce
# def add(a,b):
#     return a+b
# list1 = [1,2,3,4]
# print(reduce(add,list1))
#
# a = map(lambda a,b:a+b,list1)
# print(a)





# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.

# add = lambda x : x+15
# print(add(12))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an most_used given number.

# double_number = lambda a:a+a
# print(double_number(15))

# Write a Python program to sort a list of tuples using Lambda.
# a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# a.sort(key=lambda a:a[1])
# print(a)

# Write a Python program to sort a list of dictionaries using Lambda.
# b =[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# c = sorted(b,key=lambda x:x['color'])
# print(c)

# Write a Python program to filter a list of integers using Lambda.
# num_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_list = list(filter(lambda num:(num%2==0),num_))
# print(odd_list)

# Write a Python program to square and cube every number in a given list of integers using Lambda.
# num_ =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = list(map(lambda num:num*num,num_))
# print(square)

# Write a Python program to find if a given string starts with a given character using Lambda.
# words = ['There','is','a','tape']
# starting_word = "t"
# check_string = list(map(lambda word:word.lower().startswith(starting_word.lower()),words))
# print(check_string)

# string = str(input("Enter the string: "))
# starting_word = "P"
# check_string = lambda word:True if word.startswith(starting_word) else False
# print(check_string(string))

# Write a Python program to check whether a given string is a number or not using Lambda.
# string = str(input("Enter the string: "))
# check_no = lambda word:True if word.isnumeric() else False
# print(check_no(string))

# Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]

# Program to display the Fibonacci sequence up to n-th term
# a, b = 0, 1
# n = 5
# for i in range(n):
#     # print("a: ", a)
#     # print("b: ", b)
#     # print("=================")
#     print(a)
#     # a, b = b, a + b
#     c = a+b
#     a = b
#     b = c




# Write a Python program to find the intersection of two given arrays using Lambda.
# a = [1, 2, 3, 5, 7, 8, 9, 10]
# b = [1, 2, 4, 8, 9, 14]
# # print(set(a).intersection(set(b)))
#
# find_intersection = list(filter(lambda x:x in a,b))
# print(find_intersection)

# a = [-1, 2, -3, 5, 7, 8, 9, -10]
# a.sort()
# print(a)

# Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
# a = [1, 2, 3, 5, 7, 8, 9, 10]
# even_ctr = len(list(filter(lambda x:(x%2==0),a)))
# print(even_ctr)

# 14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
# list1 = ['Monday','Sunday','Tuesday']
# check_count = list(filter(lambda x:(len(x)==6),list1))
# print(check_count)

# days = filter(lambda day: day if len(day) == 6 else '', list1)

# Write a Python program to add two given lists using map and lambda.
a = [1, 2, 3]
b = [4, 5, 6]
add = map(lambda x, y: x + y, a, b)
print(list(add))
