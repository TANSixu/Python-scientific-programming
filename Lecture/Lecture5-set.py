# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:25:09 2021

@author: 11911627 Tan Sixu
"""

#Set unordered, no duplicate

# =============================================================================
# a={}
# 
# a.add(1)
# Traceback (most recent call last):
# 
#   File "<ipython-input-3-46e96c9c7506>", line 1, in <module>
#     a.add(1)
# 
# AttributeError: 'dict' object has no attribute 'add'
# cannot create set through {}, which will result in creating a dict.
# set is mutable
# no indexing, clicing
# =============================================================================

#set operation
a=set("hello world")
b=set("hello")
print(a&b)
print(a|b)
print(a^b)
print(a-b)

b.update(a) #renew, changing original set
print(b.issubset(a))
print(a.pop())   #randomly pop elements
# =============================================================================
# 1、如果集合的元素都是数字, 删除时, 删掉的是最小的数字, 其余数字升序排列
# 
# 2、如果集合的元素是非数字, 删除时, 删掉的是随机的元素, 其余元素随机排列
# 
# 3、如果集合里既有数字又有非数字元素, 删除时:
# 
# 若删掉的是数字, 则一定是删掉了最小的, 其他数字升序排列, 非数字元素随机排列;
# 若删掉的非数字, 则一定是随机删掉了一个, 其他数字升序排列, 非数字则随机排列.
# =============================================================================


# =============================================================================
# a.difference(b)
# Out[46]: set()
# 
# b.difference(a)
# Out[47]: set()
# 
# b
# Out[48]: {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}
# not change the original set, return a new set
# =============================================================================

#%% frozenset
s="helloworld"
fs=frozenset(s)


#%%exercise
n=int(input("n:"))
test=set()
for i in range(n):
    #test.add(int(input(f"{i+1}th element:")))

print(test)


#%%exercise
# =============================================================================
# Swap two numbers (obtained from keyboard input) without 
# using intermediate/temporary variables:
# =============================================================================
a=int(input("a:"))
b=int(input("b:"))
a,b=b,a
print(a,b)


#%%exercize
# =============================================================================
#  Sort words in the following sentence in decreasing order of 
# their length, and store each word and the corresponding 
# length in tuples. Display the sorted words along with their 
# length:
# Everything you can imagine is real
# 
# =============================================================================
s="Everything you can imagine is real"
s=s.split()
record={}
for word in s:
    record[len(word)]=word
    
record=sorted(record.items(),reverse=True)   #sorted return list!
for i,j in record:
    print(f"{j}:{i}")

#%%way 2
s="Everything you can imagine is real"
s=s.split()
record=[]
for word in s:
    record.append((word, len(word)))
    
def sbylen(a):
    return a[1]
    
# record=sorted(record,key=sbylen,reverse=True)   #set keys
record=sorted(record,key=lambda r: r[1],reverse=True)   #lambda function
for i,j in record:
    print(f"{j}:{i}")
    
    
#%%exercise
s=input("your string:")
uni=set(s)
print(len(uni)==len(s))
 
s1="".join(uni)        #join funct
for c in s1:
    if s.count(c)>1:
        print(c)


#%%exercise
# =============================================================================
#  Find unique words in the following sentence and print the 
# sorted unique words:
# The man we saw saw a saw
# =============================================================================

s="The man we saw saw a saw"
ls=s.split()
uni=set(ls)
unil=list(uni)
for word in unil:
    if ls.count(word)>1:
        print (word)
