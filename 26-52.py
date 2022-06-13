from itertools import count
import numpy as np
import os.path

# # 26
# arr = np.ones(5)
# print(arr)

# #27
# arr = np.array([[1, 2, 3, 4, 5],
#                    [6, 7, 8, 9, 10],
#                    [11, 12, 13, 14, 15],
#                    [16, 17, 18, 19, 20]
#                    ])
# print(arr)
# print([1, 2, 3, 4, 5] in arr.tolist())
# print([16, 17, 20, 19, 18] in arr.tolist())

# # 28
# mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
# mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])

# res = np.dot(mat1,mat2)
# print(res)
# res = np.add(mat1,mat2)
# print(res)

# # 29
# arr = np.array([1,1,1,2,3,])
# print(np.bincount(arr).argmax())

# # 30
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# arr = arr.flatten()
# print(arr)

# # 31
# num = np.arange(36)
# arr1 = np.reshape(num, [4, 9])
# print("Original array:")
# print(arr1)
# result  = arr1.sum(axis=0)
# print("\nSum of all columns:")
# print(result)

# # 32
# arr = np.array([1,2,3,4,5])
# print(arr.mean())
# print(arr.std())
# print(arr.var())

# # 33
# x = np.array(["Python","is","not","easy"])
# print(x)
# r = np.char.join(" ",x)
# print(r)

# #35
# num = 1345
# revnum = 0
# while num>0:
#     temp = num%10
#     revnum = revnum*10 + temp
#     num //= 10
# print(revnum)

# # 36
# number = int(input("Enter the Natural Number: "))
# for j in range(1, number+1):
#     num = 0
#     for i in range(1, j+1):
#         print(i, sep=" ", end=" ")
#         if(i < j):
#             print("+", sep=" ", end=" ")
#         num += i
#     print("=", num)

# # 37
# limit = 30
# c = 0
# m = 2
# while c<limit:
#     for n in range(1,m):
#         a = m*m - n*n
#         b = 2*m*n
#         c = m*m + n*n
#         if(c>limit):
#             break
#         print(a,b,c)
#     m = m+1

# # 38
# num = 101
# str = str(num)
# zeros = 0
# ones = 0
# for i in range (len(str)):
#     if(str[i] == '0'):
#         zeros += 1
#     else:
#         ones += 1
# if(zeros == 1 or ones == 1):
#     print("YES")
# else:
#     print("NO")

# # 39
# l=list(map(int,input().split(" ")))
# print(l)
# c=0
# y=0
# while y < len(l)-1:
#     min=l[y]
#     val=l[y]
#     for x in range(y+1, len(l)):
#         val=l[x]
#         if val < min:
#             break
#     if val < min:
#         l.remove(min) 
#         l.append(min)
#         c=c+1
#     else:
#         y=y+1
# print(c)

# # 40
# for i in range (1,7):
#     for j in range(1,i+1):
#         print(i,end = "")
#     print("")

# #  41
# key = [1,2,3,4,5]
# val = ['a','b','c','d','e']
# dict = {}
# for i in range(0,len(key)):
#     dict[key[i]] = val[i]
# print(dict)
# res = dict(zip(key, val))
# print(res)

# # 42
# inp = int(input("Enter a number: "))
# c= 0
# while inp>=10:
#     inp //= 6
#     c+=1
# print(c)

# # 43
# with open("temp.txt",'r') as f:
#     for line in f:
#         print(line.title())
# f.close

# # 44
# with open("temp.txt",'r') as f:
#     dict = {}
#     for line in f:
#         for letter in line:
#             dict[letter] = dict.get(letter,0) +1
#     print(dict)
# f.close() 

# # 45
# part 1
# with open("temp.txt",'w') as f:
#     f.write("HELLO WORLD")
#     f.close()
# with open("temp.txt",'r') as f:
#     print(f.read())

# part 2
# with open("temp.txt",'a') as f:
#     f.write("HELLO WORLD")
#     f.close()
# with open("temp.txt",'r') as f:
#     print(f.read())

# # 47
# f2 = open("temp2.txt",'a')
# f = open("temp.txt",'r')
# cont  = f.read()
# f2.write(cont)

# # 48
# f = open("temp2.txt",'a')
# n = int(input("Enter the number of students: "))
# for i in range(0,n):
#     name = input("Enter the name of the student: ")
#     roll = input("Enter the roll number of the student: ")
#     str = name+":"+roll
#     f.write(str)
#     f.write("\n")
# f.close()
# path = "temp2.txt"
# isExist = os.path.exists(path)
# print(isExist)

# # 49
# file1 = input("Enter the first file :")
# file2 = input("Enter the second file :")
# f2 = open(file2,'a')
# with open(file1,'r') as f:
#     for line in f:
#         f2.write(line)

# # 50
# f = open("temp.txt",'r')
# for line in f:
#     list = line.split(" ")
#     for i in list:
#         print(i)

# # 51
# f = open("temp.txt",'r')
# for line in f:
#     for char in line:
#         print(char)

# # 52
# char = 0
# word = 0
# lines = 0
# f = open("temp.txt",'r')
# for line in f:
#     lines  = lines + 1
#     list = line.split(" ")
#     word = word + len(list)
#     for chars in line:
#         char = char + 1
# print(char)
# print(word)
# print(lines)














