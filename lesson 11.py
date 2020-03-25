# print("Hello world")
# create a variable
'''
name = "john"
print(name)
a = 1
b = 2
c = 3.5
hi = "hello world"
print(hi)
'''
# print("what is your name?")
# name = input()
# print("hi")
# print(name)

# a = 24
# b = 16
# print(a + b)
# print(a-b)
# print(4 * "me")
# print(8%3)

# FloatNum = 1.356
# IntNum = 4
# name = "xyz"
# print(FloatNum + IntNum)
# print(str(IntNum) + name)

# SingleQuotes = 'look! single quotes'
# DoubleQuotes = "Look! double quotes"
# print(SingleQuotes, DoubleQuotes)

# EscapeExample1 = 'I said \'wow\''
# EscapeExample2 = "I said 'wow'"

# Slicing strings
# Hw = "Hello world"
# print(Hw[7:])
# print(Hw[:5])
# print(len(Hw))

#String methods
# WhiteSpace = "lots of spaces at the end             "
# print(len(WhiteSpace))
# print(len(WhiteSpace.strip()))

# Count
# ExampleText = "here is some text with lots of text"
# print(ExampleText.count("text"))
# print(ExampleText.upper())
# print(ExampleText.lower())
# print(ExampleText.replace("lots", "plenty"))

# Concatenation
# a = "here "
# b = "more "
# c = "much more"
# d = 10
# print(a + b + c, d)
# print(a, b, c, d)

#Concatenation and casting

# x = 2
# y = 5.4
# z = "there's now a number 25.4 unless we put a space in"
# print((str(x)))
#
# IntString = "6"
# print(int(IntString))
# print(type(int(IntString)))
# print(float(IntString))

#Booleans
# Single equal to means i am assigning son=me value, where has when
#I use two, im comparing two things
# a = True
# # b = False
# # print(a == b)
# # print(a != b)
# # print(a >= b)
# # print(b <= a)

# hi = "Hello world!"
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("!"))
# print(hi.startswith("H"))

# Boolean values with numbers
# x = -1
# y = 2
# print(bool(x))
# print(bool(y))
# print(bool(None))

#Lists
# ShoppingList = ["eggs", "bread", "bananas", "biscuits", "milk"]
# print(type(ShoppingList))
# print(ShoppingList[0])
# print(ShoppingList[-1])
# ShoppingList[1] = "Roti"
# print(ShoppingList)
# ShoppingList.pop(-2)
# print(ShoppingList)
# print(len(ShoppingList))

#Mixed data type lists
# mixture = [1, 2, 3, "one", "two", "three"]
# print(mixture)
# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[-2::-1])

# ListData = [1, 2, 3, 4, 5]
# for m in ListData:
#     print(m*2)

# Tuple
# Tuple is a collection which is ordered and unchangable and allows duplicates.
# cannon be changed

# essentials = ("bread", "eggs", "milk")
# print(essentials)
# print(essentials.count("bread"))

# Dictionaries
#Dictionary is a collection ehich is unordered changeble...
#we use curly brackets
# Student1 = {
#     "name": "susan",
#     "stream": "tech",
#     "CompletedLessons": 4,
#     "CompletedLessonNames": ["variables", "data", "FilmStudies", "banter"]
# }
# print(Student1["stream"])
# print(Student1["CompletedLessonNames"][1])

#Changing a value
# Student1["CompletedLessons"] = 3
# print(Student1["CompletedLessons"])

# Removing an Item
# Student1["CompletedLessonNames"].remove("data")
# print(Student1["CompletedLessonNames"])

# Sets
# Set is a collection which is unordered and unindexed
# Sets are written with curly brackets

# car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)
# car_parts.add("windows")
# print(car_parts)
# car_parts.discard("doors")

# Frozen sets
# Frozen sets are immutable versions of the set similar to tuple
# x = frozenset([1, 2, 3, 4])
# print(type(x))

# control flow
# if statements, for statements and whike loops

# age = int(input("age pls "))
# if (age <= 19):
#     print("You are not eligible for the film")
# else:
#     print("you are good to go")
# film_rating = input("What is the film rating?  ")
# if film_rating is "universal":
#      print("all age groups can watch this film")
#   elif film_rating == "pg":
#      print("General viewing, but some scenes may be unsuitable for young children.")
#   elif film_rating == "12" or film_rating == "12a":
#      print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
#    elif film_rating.lower() == "15":
#      print("No one younger than 15 may see a 15 film in a cinema.")
#   elif film_rating.lower() == "18":
#      print("No one younger than 18 may see an 18 film in a cinema.")
#      else:
#     print("this is not a correct rating, please use unniversal, pg, 12, 12a, 15, 18")

# For loop

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
#
# for x in range(6)
#     print(x)
# else:
#     print("Finally finished")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruits:
#         print(x, y)

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3],[4, 5, 6]]
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# dict_data = {1: {"name": "Bronson", "money": "$0.05"},
#              2:{"name": "masha", "money":"$3.66"},
#              3: {"name": "Roscoe", "money": "$1.14"}}
# for z in dict_data:
#     print(z)
#
# for y in dict_data.values():
#     print(y)
# #
# for y in dict_data.values():
#     for x in z.values:
#         print(x)

# While loop
# Initialising the variable
# x = 0
# Condition
# while x < 10:
#     print("its working --> {}".format(x))
#     x = x +1
# Another way to format
# while x < 10:
#     print(f"its working --> {x}")
#     x = x +1

# while x < 10:
#     print(f"its working --> {x}")
#     if x == 4:
#         break
#     x = x+1

# Functions
# Each input has a single output

# def hello():
#     print("Hello")
# hello()

# Function with arguments
# def func(a, b):
#     return a + b
# print("The sum is", func(10, 21))

# Function with default arguments
# def func(a=10,b=30):
#     return a + b
# print("The sum is", func())

# Function with default and again passing the values
# def func(a=10, b=15):
#     return a+b
# print("The sum is", func(20, 40))

# def add(a, b):
#     return a + b
# print(add(2, 6))
#
# def multiply(a, b):
#     return a * b
# print(multiply(4, 5))
#
# def subtract(a, b):
#     return a - b
# print(subtract(10, 5))
#
# def divide(a, b):
#     return a / b
# print(divide(15, 3))

# Class
# Classes are a way of bringing both data and functionality together

# class Dog:
#     animal_kind = "canine" # Class variable
#
#     def bark():
#         return "woof"
#
# print(Dog.animal_kind)
# print(Dog.bark())
# x = Dog()
# print(x.bark())

# class Student:
#     student_type = "Trainee"
#     def enrol(self):
#         return "All Good"
#
# print(Student.student_type)
# print(type(Student))

# When a function is declared in a class it is called a method

# class Car:
#     car_make = "Volkswagen"
#
#     def drive():
#         return "Vroom"
#
# print(Car.car_make)
# print(Car.drive())

# class Car:
#     car_type = ['Hatch Back', 'Limo', 'Sports Car']
#
#     def speed(self):
#         return "Good Choice"
#
# print(Car.car_type[0])
# print(Car.speed(1))

# class Student:
#     student_type = "Trainee"
#     def enrol():
#         return "Completed"
#
# print(Student.student_type)
# print(Student.enrol())

# libraries and modules
# import random
# import math
#
# print(random.random())
#
# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))

# from animal import Animal
#
# Dog1 = Animal("Nyme", 100)
# Dog2 = Animal("Mone", 5)
# print(Dog1.name)

# import requests
#
# request_bbc = requests.get("https://www.bbc.co.uk/")
# print(request_bbc.status_code)
# print(request_bbc.content)

# Abstraction is displaying only essential information to the user

# class Employee:
#     def __init__(self, first_name, last_name, pay):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.email = first_name + "." + last_name + "@company.com"
#
#     def fullname(self):
#          return f"{self.first_name} {self.last_name}"
#
# emp_1 = Employee("Brian", "Smith", 90000)
#
# print(emp_1.email)
# print(Employee.fullname(emp_1))
# print(emp_1.fullname()) # Same thing

# Inheritance is a mechanism in which one class acquires
# the prperty of another class.
# It allows you to call methods of the superclass in your subclass
# The primary use case of this is to extend the functionality of the inherited method

# In an object orientated python program, you can restrict access to methods
# and variables. This can prevent the data from being modified by accident and is known as encapsulation

# Polymorphism in python defines methods in the child class that have the same
# name as the methods in the parent class
# In inheritance, the child class inherits the methods from the parent class
# Also, it is possible to modify a method in a child class
# that it has inherited from the parent class and this is called as method overriding.

# Lambda function
# Lambdas are essentially anonymous function that can take
# multiple parameters but return only one expression

# def add(num1, num2):
#     return num1 + num2
# addition = lambda num1, num2:num1 + num2
# print(add(23, 45))
# print(addition(23, 45))
#
# savings = [234, 567, 674, 78]
# bonus = list(map(lambda x: x * 1.1, savings))
# print(bonus)

# from simple_calc import SimpleCalc
# import unittest
#
# class Calctests(unittest.TestCase):
#
#     cal = SimpleCalc()
#
#     def test_add(self):
#         self.assertEqual(self.cal.add(2, 4), 6)
#
#     def test_subtract(self):
#         self.assertEqual(self.cal.subtract(4, 2), 2)
#
#     def test_multiply(self):
#         self.assertEqual(self.cal.multiply(2, 2), 4)
#
# if __name__ == '__main__':
#     unittest.main()

# This lesson includes
# introduction to the openxyl and xlswriter libraries
# using these libraries to write excel and read from the same files

# create a python folder and a file inside





