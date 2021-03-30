# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:14:12 2021

@author: 11911627 Tan Sixu
"""

'''
nparray
'''
import numpy as np

a=[0,0,1,4]
b=np.array(a)
print(b.dtype)     #return the datatype in the adarray
'''
int 32
'''

#diffenrent datatype, change to most upper type

f=[1,4.,-2.8,7 ]       #int mix float
e=np.array(f)
print(e.dtype)      #float64      automatic casting

e1=np.array(f,dtype=np.int32)         #!!!!!!!!explicitly casting
print(e1)
print(e1.dtype)
'''
float64
[ 1  4 -2  7]          !!float不会四舍五入，会discard floating num
'''

s=["abc", 1., 2,4]               
g=np.array(s)
print(g.dtype)
print(g)

a2d = np.array([[1,2,3], [4,5,6]])
print(a2d.dtype)

#%% 

arr=np.array([[10,20,30],[14,12,16]])
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)       #num of bytes
'''
(2, 3)     shape returns tuple
6
int32
4
'''


#%%array creation
t1=np.zeros(6)
t2=np.ones(5)
print(t1.dtype)         #默认创建floar

t3=np.ones(5, dtype=np.int64)      #customize
t4=np.zeros((4,5), dtype=np.complex64)    #change length and height, through tuple or list
print(t4)

t5=np.ones([6,5,8,7])     #high dimention with tuple or list

t6=np.empty((2,5))        #not zeros, means totally empty, random in RAM

t7=np.full((5,6),10)   #filled with assigned number

t8=np.eye(5,6)
print(t8)
t81=np.eye(5,6,2)      #the third arg means shift,  identity matrix
print(t81)

t82=np.identity(8)
"""
[[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]]
[[0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0. 0.]]

"""

t9=np.random.random((2,2))
print(t9)


# =============================================================================
# The linspace function creates an array of N evenly spaced 
# points between a starting point and an ending point. The form 
# of the function is linspace(start, stop, N). If the third 
# argument N is omitted, then N=50:
# =============================================================================
"""
here (start, end, step)  range[start, end] contains end!!!!!! closed interval
step by default is 50
"""
test1=np.linspace(0,10,3)
print(test1)

test2=np.logspace(1,3,5)
"""
here, from 10**1 to 10**3, firstly slice 1-3 into 5 same pieces, then
calculate 10**i
"""
print(test2)



'''
here (start, end, step), range : [start, end) open interval!

'''
test3=np.arange(0,10,1)   
test5=np.arange(0.,10,1)    #any of args is float result will be float
test4=np.arange(0,10,1.5)   #when one argument is float
print(test3)
print(test4)
print(test5)
# =============================================================================
# In general arange produces an integer array if the arguments 
# are all integers; if any one of the arguments is a float, the 
# generated array would be a float
# =============================================================================


#%%array indexing
a=np.arange(1,13,1)      #[axis0, axis1, axis2]
a=a.reshape((3,4))
print(a)
print(a[1,2])
print(a[:2,1:3])
print(a.ndim)

""" slicing 时 dim变化问题
a[1][:]
Out[83]: array([5, 6, 7, 8])

c=a[1][:]

c.ndim
Out[85]: 1

c=a[1:2][:]

c
Out[87]: array([[5, 6, 7, 8]])

c.ndim
Out[88]: 2
"""

'''访问二维数组时
a[[0,1,2],[0,1,0]]
Out[102]: array([1, 6, 9])
'''

for e in a.flat:        #内存中顺序
    print(e)
    
#%%dim, shape
# =============================================================================
# 
# a=np.array([1,2,3])  dim：1
# 
# a.shape
# Out[2]: (3,)    表示1维向量size
# 
# a=np.array([[1,2,3],[4,5,6]])
# 
# a.shape
# Out[4]: (2, 3)
# 
# a=np.array([[1,2,3],])     dim：2
# 
# a.shape
# Out[6]: (1, 3)    变成二维

# a=np.array([[[1,2,3]]])
# a.ndim
# Out[9]: 3

# a.shape
# Out[10]: (1, 1, 3)
# =============================================================================

#%%fancy indexing
a=np.arange(0,10,1)

# =============================================================================
# a
# Out[24]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 
# a>5
# Out[25]: 
# array([False, False, False, False, False, False,  True,  True,  True,
#         True])
# 
# b=[a>5]
# 
# b
# Out[27]: 
# [array([False, False, False, False, False, False,  True,  True,  True,
#          True])]
# 
# b=a>5                    
# 
# b
# Out[29]: 
# array([False, False, False, False, False, False,  True,  True,  True,
#         True])
# 
# b*a
# Out[30]: array([0, 0, 0, 0, 0, 0, 6, 7, 8, 9])
# 
# a[a>5]                    条件筛选式   选出下标为true的, 返回地址索引
# Out[31]: array([6, 7, 8, 9])
# 
# a[a>5]=11                condion filter assignment  给下表true的赋值， 给地址索引赋值
# 
# a
# Out[33]: array([ 0,  1,  2,  3,  4,  5, 11, 11, 11, 11])
#
#
#  比较floating number： a=1.0, b=1.0,   a==b change to (a-b==1.0e-8)
# =============================================================================


#%%mathmatic operation
a=np.linspace(-1,5,5)
print(a**2)
print(sin(a**2))       #radian, not angle

# =============================================================================
# inf: infinite
# nan: not a number
# 
# =============================================================================

print(a+4)        #broad-casting


a=np.arange(10)
b=np.arange(10,20)
print(a/b)        #vectorized processing


c=np.array([[1,1],[6,1]])
d=np.array([[2,8],[3,4]])

print(c*d)              #elementary multi
print(np.dot(c,d))      #matrix multi


# =============================================================================
# argmax:默认平铺数组，填axis视为矩阵 
    
    
    
# np.max(c)
# Out[80]: 6
# 
# argmax(c)
# Out[81]: 2
# 
# argmin(c)
# Out[82]: 0
# 
# argmin(c,axis=1)
# Out[83]: array([0, 1], dtype=int64)
# 
# argmin(c,axis=0)
# Out[84]: array([0, 0], dtype=int64)
# 
# argmax(c,axis=0)
# Out[85]: array([1, 0], dtype=int64)


# np.max(c,axis=0)                  max 指定axis返回有最大值的行/列
# Out[89]: array([6, 1])

# np.max(c,axis=1)
# Out[90]: array([1, 6])
# =============================================================================


#%% stacking
a = np.array([[3, 1, 2], [8, 7, 9]])
b = np.array([[2, 4, 6], [5, 4, 8]])
print(np.vstack((a, b)))

print(np.hstack((a, b)))     #combine two array, vetical or horizontal

c=np.hstack((a,b))
print(np.hsplit(c,3))      #evenly divide into 3 parts, return list

#also, vsplit


# =============================================================================
# d,e=np.hsplit(c,2)        tuple and list can both be multi-assigned
# 
# d
# Out[106]: 
# array([[3, 1, 2],
#        [8, 7, 9]])
# 
# e
# Out[107]: 
# array([[2, 4, 6],
#        [5, 4, 8]])
# =============================================================================


#%%broad-casting

