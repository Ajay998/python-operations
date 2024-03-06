# 1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
# a = [1,2,3,4]
# result1 = map(lambda x:x+x+x,a)
# print(list(result1))

# Write a Python program to add three given lists using Python map and lambda.
# a = [1,2,3,4]
# b = [2,4,6,8]
# c = [3,6,9,12]
#
# result = map(lambda x,y,z:x+y+z,a,b,c)
# print(list(result))

# 3. Write a Python program to listify the list of given strings individually using Python map.
# color = ['Red', 'Blue', 'Black', 'White', 'Pink']
# reults = map(list,color)
# print(list(reults))

# Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
# b = [10,20,30,40]
# a = [1,2,3,4]
# # result = map(lambda x:x**x,a)
# # print(list(result))
# result2 = list(map(pow,b,a))
# print(result2)

# 5. Write a Python program to square the elements of a list using the map() function.
# b = [10,20,30,40]
# results = map(lambda x:x*x,b)
# print(list(results))

# 6. Write a Python program to convert all the characters into uppercase and lowercase
# and eliminate duplicate letters from a given sequence. Use the map() function.

# b = ['a','b','c','d','c']
# a = set(b)
#
# results = map(lambda x:(x.upper(),x.lower()),list(a))
# print(list(results))

# Write a Python program to add two given lists and find the difference between them. Use the map() function.

# a = [1,2,3,4]
# b = [2,4,6,8]
# result = map(lambda x,y:(x+y,x-y),a,b)
# print(list(result))

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.