# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display_details(self):
#         details = "Name: "+str(self.name)+" Age: "+str(self.age)
#         return details
#
# name = "Ajay"
# age = 12
# student_class = Student(name,age)
# student_details = student_class.display_details()
# print(student_details)


# 1. Write a Python program to create a person class. Include attributes  like name, country and date of birth. Implement a method to  determine the person’s age.

# import datetime
# class Person:
#     def __init__(self,name,country,dob):
#         self.name = name
#         self.country = country
#         self.dob = dob
#
#     def calculate_age(self):
#         today = datetime.datetime.now()
#         today_year = today.year
#         birthday = datetime.datetime.strptime(self.dob,'%d-%m-%Y')
#         birthday_year = birthday.year
#         age = today_year - birthday_year - ((today.month, today.day) < (birthday.month, birthday.day))
#         return age
#
#
# cal_person = Person(name="Ajay",country="USA",dob="30-03-1998")
# print(cal_person.name)
# print(cal_person.country)
# print(cal_person.dob)
# print("Age: "+str(cal_person.calculate_age()))

# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.