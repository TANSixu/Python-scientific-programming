# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:06:46 2021

@author: 11911627 Tan Sixu
"""

# =============================================================================
# A3Q1
# =============================================================================
numbers=[-1,-2,-3,4,5]
nsum=0
psum=0
tsum=0
for i in numbers:
    if i>0:
      psum+=i
    elif i<0:
        nsum+=i
    tsum+=i

avg=tsum/len(numbers)
print(f"sum of negative numebrs:{nsum}\nsum of positive numebrs:{psum}")
print(f"average of numebrs:{avg}")
print("numbers above average:")
for i in numbers:
    if i >avg:
        print(f"\t{i}")
        
        
#%%
# =============================================================================
# A3Q2
# =============================================================================
matrix=[[10,20],[30,40],[50,60]]
row=len(matrix)
col=len(matrix[0])

trans=[[0 for i in range(row)] for j in range(col)]

for i in range(row):
    for j in range(col):
        trans[j][i]=matrix[i][j]
        
print(trans)    