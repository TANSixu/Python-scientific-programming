# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:07:20 2021

@author: 11911627 Tan Sixu
"""

a=1,2,3,4          #()not needed, default to create a tuple
b=(1,2,3,4)
one_ele_tuple_false = ("hello")
one_ele_tuple_true = ("hello", )      #single element need a comma!!!
print (type(one_ele_tuple_false))
print(type(one_ele_tuple_true))        
# <class 'str'>
# <class 'tuple'>
#%% operations
a=(1,2,3)
b=(4,5,6)
print(a+b)   #a+b not change the original value

c=a+b
print(c)       #tuple does not have append funct

print(3*a)

print(a>b)   #element by element, pair1, pair2...

# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (1, 2, 3, 1, 2, 3, 1, 2, 3)
# False

str_to_tuple='helloworld'
d=tuple(str_to_tuple)
print (d)                   #same as list, when on string type, change to char element
# ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')

s="second World"
print(tuple(s)+d)

#%% functs
years=[2000,1998,2010,2020,2021,1996]
print(len(years))
print(sum(years))
print(sorted(years,reverse=True))
print(type(sorted(years)))   #sorted funct return a list!!!
# 6
# 12045
# [1996, 1998, 2000, 2010, 2020, 2021]
# <class 'list'>

list_in=[1,2,3]
ctuple=('t1','t2',list_in)

#elements in tuple are address, the fixed address cannot be changed, while the content can.
# ctuple
# Out[56]: ('t1', 't2', [1, 2, 3])

# ctuple[2].append(4)

# ctuple
# Out[58]: ('t1', 't2', [1, 2, 3, 4])

# list_in
# Out[59]: [1, 2, 3, 4]

# list_in.append(5)

# list_in
# Out[61]: [1, 2, 3, 4, 5]

# ctuple
# Out[62]: ('t1', 't2', [1, 2, 3, 4, 5])


tuple_to_dic=(('hi',1),("nohi",2)) #change to couple in list [()] also works
tuple_to_dic2=[['hi',1],["nohi",2]]  #also works
d=dict(tuple_to_dic)
print(d)


#!!!for i, j in .items()   here i,j will be regarded as tuple.

founding_year = {"Google":1996, "Apple":1976, 
"Sony":1946, "ebay":1995, "IBM":1911}
founding_year.items()


# for company, year in founding_year.items():
#      print(f"{company} was found in the year {year}")
for it in founding_year.items():
      print(f"{it[0]} was found in the year {it[1]}")
      
#%% methods
test=(1,1,2,3,4,4,5,6)
print(test.count(1))
print(test.count(7))

print(test.index(1))   #index get the index of the item

#%% exchanging values in a simple way
a=4
b=3
a,b=b,a

#%%  zip funct
# =============================================================================
# Returns a sequence of tuples, where the i-th tuple contains 
# the i-th element from each of the iterables. The aggregation of 
# elements stops when the shortest input iterable is exhausted:
# =============================================================================
x = [1, 2, 3]
y = [4, 5, 6, 7]
z=zip(x,y)
print(z)
# <zip object at 0x0000020CEA45B040>  need to transfer to list, default zip
z_l=list(z)
print(dict(z_l))

#%%exercise
# =============================================================================
# Accept n inputs from your keyboard and form a tuple using 
# for loop:
# =============================================================================
n=int(input("n:"))
t=()
for i in range(n):
    tmp=int(input())
    t=t+(tmp,)
print(t)

