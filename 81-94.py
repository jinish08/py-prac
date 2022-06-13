import pandas as pd
import numpy as np

# # 81
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = arr1*1.8 + 32
# print(arr2)
# arr3 = (arr2-32)*5/9
# print(arr3)

# # 82
# arr1 = np.array([4,3,2,1])
# arr2 = np.array([6,5,4,3])

# arr3 = np.setdiff1d(arr1,arr2)

# print(arr3)

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

newdf = pd.DataFrame(exam_data,index=labels)

# 83
# print(newdf)

# 84
# print(newdf.head(3))

# 85
# print(newdf.loc[:,['name','score']])
#  print(newdf[['name','score']])

# 86
# print(newdf.iloc[[1, 3, 5, 6], [1, 3]])

# 87
# print(newdf[newdf['attempts'] > 2])

# 88
# rows = len(newdf)
# col = len(newdf.axes[1])
# print("rows:", rows)
# print("col:", col)

# 89
# print(newdf[newdf['score'].between(15, 20)])

# 90
# print(newdf[(newdf['attempts'] < 2) & (newdf['score'] > 15)])

# 91
# newdf.loc['k'] = [ 'Suresh', 15.5,1, 'yes']
# print(newdf)
# newdf = newdf.drop('k')
# print(newdf)

# 92
# df = newdf.sort_values(by=['name', 'score'], ascending=[False, True])
# print(df)

# 93
# newdf['qualify'] = newdf['qualify'].map({'yes': True, 'no': False})
# print(newdf)

# 94
# newdf._set_value('h', 'score', 20)
# print(newdf)
