# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:08:44 2021

@author: 11911627 Tan Sixu
"""

dic1={2:1,1:2}
dic2={1:2, 2:1}

print(dic1==dic2)  #orders not matter in dics

a=dic1.keys()
print(type(a))    #new data type: dickeys

b=list(dic1.keys())  #transform to list
print(b)

c=dic1.values()    #same as keys()

d=dic1.items()   
print(d)          #datatype: dict_items

e=list(d)
print(e)         #tranform to tuple in list
# =============================================================================
# True
# <class 'dict_keys'>
# [2, 1]
# dict_items([(2, 1), (1, 2)])
# [(2, 1), (1, 2)]
# =============================================================================

#%%
dic=dict(one=1, two=2, three=3)   #another way to creat a dict
print(dic)

l=len(dic)
print (l)             #count items

dic3=sorted(dic)      #sorted return a list of keys, not change the original one
print(dic3)         #sort based on dictionary order of keys

dic3=sorted(dic, reverse=True)      #reverse=True, get a reverse sort
print(dic3)         

print(sorted(dic.items()))       #sort based on keys, display with values

print ('one' in dic)              #"in" method of dic
print('one' in dic.keys())
print('one' in dic.items())

# =============================================================================
# {'one': 1, 'two': 2, 'three': 3}
# 3
# ['one', 'three', 'two']
# ['two', 'three', 'one']
# [('one', 1), ('three', 3), ('two', 2)]
# True
# True
# False
# =============================================================================


#%%
numbers={'one':1, 'two':2, 'three':3}
nf=numbers.fromkeys(numbers)          #fromkeys, create a new dict with same keys
print(nf)

nf=numbers.fromkeys(numbers, "num")   #can assign a value to every key(same as numebrs) in nf  
print(nf)

print(numbers.get('one'))    #get function is safe to get values, even key not exist
print(numbers.get('four'))

#add and remove
numbers.update({'four':4})
numbers['five']=5
print(numbers)

numbers.pop('five')
print(numbers)

numbers.popitem()      #remove the last one and return the tuple
print(numbers)

# numbers.clear()       #clear all, keep name
# print(numbers)

del numbers['three']
print (numbers)          #del one element

del numbers
# print(numbers)        #del space

# =============================================================================
# {'one': None, 'two': None, 'three': None}
# {'one': 'num', 'two': 'num', 'three': 'num'}
# 1
# None
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# {'one': 1, 'two': 2, 'three': 3}
# {'one': 1, 'two': 2}
# =============================================================================

#%% excercise
chance=int(input("counts?:"))
info={}
for i in range(chance):
    name=input("name:")
    height=int(input("height:"))
    info[name]=height
# print(info)

for i, j in info.items():
    print(f"name: {i}, height:{j}")
    
    
#%% exercise
n=int(input("your n:"))
d1={}
for i in range(1,n):
    d1[i]=i**2

print(d1)


#%%excercise
Dynasties = {"tang": 618, "song": 960, "yuan": 
1279, "ming": 1368, "qing": 1644}
    
indy=input("your input:")
print(indy in Dynasties)
s=sum(list(Dynasties.values()))
print(f"The sum of values is {s}")


#%%excercise
# =============================================================================
# Write a program to count the number of characters in a word 
# using dictionary. Display the character and their appeared 
# times in alphabetical order:
# pneumonoultramicroscopicsilicovolcanoconiosis
# 
# =============================================================================

s='pneumonoultramicroscopicsilicovolcanoconiosis'
dic={}
# for c in s:
#     if c in dic:
#         dic[c]+=1
#     else:
#         dic[c]=1

#O(n) method, common manipulation of counting letters
letter=[chr(i) for i in range(97,126)]
zero=[0 for i in range(26)]
dic=dict(zip(letter,zero))
for c in s:
    dic[c]+=1
            
ss=sorted(dic.items())
for i in ss:
    if i[1]:
        print(f"{i[0]}:{i[1]}")
# =============================================================================
# 
# note here chr() not chr[]!
# and sorted function return a new dict, not changing the original one.
# zip()funt can generate a tuple used in dict
# =============================================================================

#%%exercise
# =============================================================================
# Write a program to calculate the number of digits, uppercase 
# and lowercase letters of the following sentence:
# I am Time, the great destroyer of the world -
# Bhagavad Gita 11.32
# =============================================================================
s1='I am Time, the great destroyer of the world -Bhagavad Gita 11.32'
dic={"upper":0, "lower":0, "digits":0}
for c in s1:
    if c.isdigit():
        dic["digits"]+=1
    elif c.isupper():
        dic["upper"]+=1
    elif c.islower():
        dic["lower"]+=1

for i,j in dic.items():
    print(f"{i}:{j}")
    

#%%exercise
# =============================================================================
# Write a program to print the following student's name, ID, and 
# average score:
# student_details = {"name": "John", "ID": "100101", 
# "marks": {"python": 95, "java": 90, "C": 85}}
# dict in a dict
# =============================================================================
student_details = {"name": "John", "ID": "100101", 
"marks": {"python": 95, "java": 90, "C": 85}}
for attribution, info in student_details.items():
    if type(info)==dict:
        print(f"{attribution}:")
        for i, j in info.items():
            print(f"{i}:{j}")
    else:print(f"{attribution}:{info}")
