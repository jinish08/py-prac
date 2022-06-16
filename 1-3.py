import matplotlib.pyplot as plt 
import numpy as np 
import math

# # Q1
# x = np.random.randn(50) 
# y = np.random.randn(50)
# plt.scatter(x, y, s=70, facecolors='none', edgecolors='g') # s is the size of circles 
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Q2 
# x = np.random.randn(50)
# y = np.random.randn(50)
# z = math.pi * np.random.randn(50)**2
# plt.scatter(x,y,s=z,edgecolors='r')
# plt.show()

# # Q3
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# plt.scatter(marks_range, math_marks, label='Math marks', color='r')
# plt.scatter(marks_range, science_marks, label='Science marks', color='g')
# plt.title('Scatter Plot')
# plt.xlabel('Marks Range')
# plt.ylabel('Marks Scored')
# plt.legend()
# plt.show()