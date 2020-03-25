# name = input("What is your name?  ")
# Age = input("how old are you?")
# DOB = input("what is your DOB? ")
# Door_Number = input("what is your door number ")
# First_Line_Address = input("what is your address? ")
# Postcode = input("what is your postcode? ")
# print(name, Age, DOB, Door_Number, First_Line_Address, Postcode)

# Palindrome
# word = "Noon"
# print(word[::-1])
# print(word.lower() == word[::-1].lower())

# a = input("Enter your first number ")
# b = input("Enter your second number ")
# if (a>b):
#     print("{} is bigger {} ".format(a, b))
# else:
#     print("{} is bigger than {}".format(b, a))

# a = input("Enter your first number ")
# b = input("Enter your second number ")
# c = input("Enter your 3rd number ")
# if(a > b) and (a > c):
#     print("{} is the largest number".format(a))
# elif(b > a) and (b > c):
#     print("{} is the largest number".format(b))
# else:
#     print("{} is the largest number".format(c))
#
# a = input("Your number pls ")
# if (int(a) % 2) == 0:
#     print("your number is even")
# else:
#     print("your number is odd")

# a = [1, 2, 5, 7, 8, 3, 19, 27]
# NewList = []
#
# for num in a:
#     if (num > 15):
#         NewList.append(num)
#     else:
#         continue
# print(NewList)

# List = [1, 3, 6, 25, 42, 64, 79]
# OddList = []
# EvenList = []
# for num in List:
#     if (int(num) % 2) == 0:
#         EvenList.append(num)
#     else:
#         OddList.append(num)
# print(List)
# print(OddList)
# print(EvenList)

# number = int(input("Your number pls  "))
# if (number % 3) == 0 and (number % 5) == 0:
#     print("FizzBuzz")
# elif (number % 3) == 0:
#     print("Fizz")
# elif (number % 5) == 0:
#     print("Buzz")
# else:
#     print("Not a valid number")

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# NewList = []
#
# for num in a:
#     if (num % 3 == 0 and num % 5 == 0):
#         NewList.append("FizzBuzz")
#     elif (num % 3 == 0):
#         NewList.append("Fizz")
#     elif (num % 5 == 0):
#         NewList.append("Buzz")
#     else:
#         NewList.append(num)
# print(NewList)

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         # self.email = first_name + "." + last_name + "@university.com"
#
#     def fullname(self):
#          return f"{self.first_name} {self.last_name}"
#
# student_1 = Student
# student_1.first_name = input("Your first name?  ")
# student_1.last_name = input("Your second name?  ")
#
# class Person(Student):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#
#     def enjoy(self):
#         hobby = input("Give me one hobby  ")
#         return f"{self.first_name} enjoys {hobby}"
#     def chill(self):
#         return f"{self.first_name} likes to chill"
#
# print("Your full name is", Student.fullname(student_1))





