import random
import math

# # 4
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# dic4 = {**dic1, **dic2, **dic3}
# print(dic4)


# # 5
# i = 4
# if i in dic4:
#     print(i," is present")
# else:
#     print(i," is not present")


# # 6
# dic5 = {}

# for i in range(1,6):
#     dic5[i] = i*i
# print(dic5)


# # 7
# dic5.pop(3)
# print(dic5)


# # 8
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# dic6 = dict(zip(l1,l2))
# print(dic6)


# #9
# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)

# s = set()
# for dic in L:
#     for val in dic.values():
#         s.add(val)
# print("Unique Values: ",s)


# #10
# str1 = 'pythonprac' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1  #get use karne ne default value daal sakte hai , warna error aata
# print(my_dict)


# # 11
# string = input("Enter a sentence: ") 
# newstr = string.replace(" ","-") 
# print(newstr)

# #12
# rno = min(random.sample(range(100, 200), 10))
# print(rno)

#13
# dict = {"Afghanistan":"Afghani","Luxembourg ":"Euro","Qatar":"Qatari Riyal","Vietnam":"Dong","India":"Rupee"}
# for i,j in dict.items():
#     print(i,":",j)

# #14
# comnum = 3+2j
# comnum2 = complex(3,2)
# print(type(comnum))
# print(comnum.real)
# print(comnum.imag)
# print(comnum.conjugate())
# def magnitude(comnum):
#     r = comnum.real
#     i = comnum.imag
#     ans = r*r + i*i
#     return math.sqrt(ans)
# print(magnitude(comnum))

# #15
# str = "   hello"
# str = str.lstrip()
# str = str.replace("llo","lp")
# print(str)

# #17
# str = "firstandlast"
# strnew = str[-1:] + str[1:-1] + str[:1]
# print(strnew)

# #18
# str = "ispresent"
# if "present" in str:
#     print("present is present")
# else:
#     print("present is not present")

# #20
# str = "biggib"
# revstr = reversed(str)
# if list(str) == list(revstr):
#     print(True)
# else:
#     print(False)

# # 21
# str = "hello world"
# str = str.title()
# print(str)

# #22
# str = "hello world"
# map = {}
# for i in str:
#     map[i] = map.get(i,0) +1 
# print(map)

# # 23
# dict = {
#     "state1":"cap1",
#     "state2":"cap2",
#     "state3":"cap3",
#     "state4":"cap4",
# }
# dict["state5"] = "cap5"
# print(dict)


# #24
# def countCharacterType(str):
#     vowels = 0
#     consonant = 0
#     specialChar = 0
#     digit = 0

#     for i in range(0, len(str)):
         
#         ch = str[i]
 
#         if ( (ch >= 'a' and ch <= 'z') or
#              (ch >= 'A' and ch <= 'Z') ):
 
#             ch = ch.lower()
 
#             if (ch == 'a' or ch == 'e' or ch == 'i'
#                         or ch == 'o' or ch == 'u'):
#                 vowels += 1
#             else:
#                 consonant += 1
         
#         elif (ch >= '0' and ch <= '9'):
#             digit += 1
#         else:
#             specialChar += 1
     
#     print("Vowels:", vowels)
#     print("Consonant:", consonant)
#     print("Digit:", digit)
#     print("Special Character:", specialChar)
# str = "Password23@#"
# countCharacterType(str)

# # 25
# str = input("Enter a string with less then 15 letter: ")
# if(len(str)>15):
#     print("Enter a string with less characters")
# else:
#     for i in range(len(str)):
#         print(i,":",str[i])



 

