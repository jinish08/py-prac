import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# # 53
# class InvalidMarks(Exception):
#     pass
# while True:
#     try:
#         marks = int(input("Enter your marks"))
#         if marks > 100:
#             raise InvalidMarks
#         else:
#             print(marks)
#             break
#     except InvalidMarks:
#         print("Please enter marks below 100")

# # 54
# class ZeroDivisionError(Exception):
#     pass
# a = 1
# b= 2
# c = 3
# d = 0
# try:
#     if b*d == 0:
#         raise ZeroDivisionError
#     ans =  ((a+d) + (b*c))/ (b*d)
#     print(ans)
# except ZeroDivisionError:
#     print("b*d ie the denominator turns out to be 0")

# # 55
# class InvalidAge(Exception):
#     pass
# try:
#     age = int(input("Enter your age"))
#     if age<18:
#         raise InvalidAge
#     print("Age is valid")
# except InvalidAge:
#     print("Age is not valid")

# # 56
# try:
#     f = open("temp3.txt",'r')
# except FileNotFoundError:
#     print("File not found")

##57
# x = "ev"
# try:
#     if not (type(x)== str):
#         raise TypeError
# except TypeError:
#     print("Enter a string")

# # 58
# class Complex ():
#     def initComplex(self):
#         self.realPart = int(input("Enter the Real Part: "))
#         self.imgPart = int(input("Enter the Imaginary Part: "))            
#     def display(self):
#         print(self.realPart,"+",self.imgPart,"i", sep="")
#     def sum(self, c1, c2):
#         self.realPart = c1.realPart + c2.realPart
#         self.imgPart = c1.imgPart + c2.imgPart
# c1 = Complex()
# c2 = Complex()
# c3 = Complex()
# print("Enter first complex number")
# c1.initComplex()
# print("First Complex Number: ", end="")
# c1.display()
# print("Enter second complex number")
# c2.initComplex()
# print("Second Complex Number: ", end="")
# c2.display()
# print("Sum of two complex numbers is ", end="")
# c3.sum(c1,c2)
# c3.display()

# # 59
# class Triangle():
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def perimeter(self):
#         return self.a+self.b+self.c
# triobj = Triangle(1,2,3)
# print(triobj.perimeter())

# # 60
# class check():
#     def __init__(self):
#         self.n=[]
#     def add(self,a):
#         return self.n.append(a)
#     def remove(self,b):
#         self.n.remove(b)
#     def dis(self):
#         return (self.n)
# newlist = check()
# newlist.add(5)
# newlist.add(4)
# newlist.add(3)
# newlist.remove(4)
# print(newlist.dis())

# # 61
# class calculator():
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
#     def addNumbers(self):
#         return self.number1+self.number2
#     def mulNumbers(self):
#         return self.number1*self.number2
#     def divNumbers(self):
#         return self.number1/self.number2
#     def subNumbers(self):
#         return self.number1-self.number2

# # 62
# class Student:
#     name = 'Adam'
#     id = 1
# def display(self):
#     print(self.name)
#     print(self.id)
#     print(self.class_name)
    
# s = Student()
# setattr(s, 'class_name', 23)
# display(s)


# # 63
# def func(str):
#     list = str.split(" ")
#     str = ' '.join(reversed(list))
#     return str

# str = "Marry had a little lamb"
# print(func(str))

# # 64
# class string:
#     def get_String(self):
#         self.str=input("Enter a string : ")
#     def print_String(self):
#         print(self.str.upper())
# str1 = string()
# str1.get_String()
# str1.print_String()

# # 65
# class Circle():
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         return self.radius**2*3.14
    
#     def perimeter(self):
#         return 2*self.radius*math.pi
# NewCircle = Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())

# # 66
# class vehicle:
#     def __init__(self, speed , milege):
#         self.speed=speed
#         self.milege=milege        
#     def ride(self):
#         print("The speed of car is " +self.speed +"  kmph and milege is "+self.milege)
# p1=vehicle("120","20")
# p1.ride()
# print("---Child class---")
# class bus(vehicle):
#     pass
# x=bus("140","40")
# x.ride()

# # 67
# data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
#  'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
#  'age': [41, 28, 33, 34, 38, 31, 37],
#  'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
#  }

# f1=pd.DataFrame(data)

# print(f1)

# x=data["name"]
# y=data["age"]

# plt.plot(x,y)
# plt.show()

# # 68
# arr = [0,2,3,4,6,7,9,0]
# for i in arr:
#     if i == 0:
#         arr.remove(0)
#         arr.append(0)
# print(arr)

# # 69
# sen = input("Enter a comma sepreated sentence")
# lis = sen.split(",")
# lis.sort()
# sen = ",".join(lis)
# print(sen)

# # 70
# d = input("Enter a comma seperated sentence: ")
# list = d.split(",")
# ans = []
# for val in list:
#     valint = int(val)
#     f = math.sqrt((2*50*valint)/30)
#     ans.append(str(int(f)))
# print(','.join(ans))

# # 71
# ans = []
# list = [12,24,35,24,88,120,155,88,120,155]
# for i in list:
#     if not i in ans:
#         ans.append(i)
# print(ans)

# # 72
# n = int(input("Enter n"))
# def printDict():
#     dict = {}
#     for i in range(1,n+1):
#         dict[i] = i*i
#     print(dict)
# printDict()

# # 73
# n = int(input("Enter an integer"))
# ans = 0
# while n>0:
#     i = n%10
#     ans += i
#     n //= 10
# print(ans)

# # 74
# def print_prime(n):
#     for num in range(2, n + 1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
# print_prime(25)

# # 75
# def rec(n):
#     if n <= 0:
#         return
#     print(n)
#     n -= 1
#     rec(n)
# rec(8)

# 76
# def student_data(student_id, **kwargs):
#     print(f'\nStudent ID: {student_id}')
#     if 'student_name' and 'student_class' in kwargs:
#             print(f"Student Name: $ {kwargs['student_name']}")
#             print(f"Student Class: $ {kwargs['student_class']}")

#     elif 'student_name' in kwargs:
#         print(f"Student Name: $ {kwargs['student_name']}")
# student_data(student_id='SV12', student_name='Jean Garner')
# student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')

# # 77
# def roman_to_int(str):
#     rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     ans = 0
#     for i in range(len(str)):
#         ans += rom_val[str[i]]
#         if i>0 and rom_val[str[i]]>rom_val[str[i-1]]:
#             ans -= 2*rom_val[str[i-1]]
#     print(ans)
# roman_to_int("IIV")

# # 78
# import itertools
# def findSubsets(s,n):
#     return list(itertools.combinations(s,n))
# s={1,2,3,4}
# for n in range(1,len(s)):
#     print(findSubsets(s,n))

# # Q79
# class py_solution:
#   def twoSum(self, nums, target):
#        lookup = {}
#        for i, num in enumerate(nums):
#            print(i,num)
#            if target - num in lookup:
#                return (lookup[target - num], i )
#            lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

# # Q80 
# def pow(x,n):
#     return x**n
# print(pow(2,4))
            
