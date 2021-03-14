# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:29:41 2021

@author: 11911627 Tan Sixu
"""

a="China"

b="jp"

print("私は{0}がすきです".format(a))# format, with {} content as index

c=10
print(f"I'm {c} years old")   #print(f)  with var into string output

print(a*5)                      #string operation: multiple output by "*"

d="your's name?"
e='your\'s name?'
print(len(d),len(e))         #placeholder "\" do not contribute to lenth

print(e[4:-1]) #not reversed, means at(4) to at(1from last)  ,"-1" only means count from last, not function
print(e[::3])  #second":"means print every 3 chars   [start:end:间隔]
#attention !!!!!! [start:end:间隔], here [start,end)  end is open range

date=["119","116","27"]
print(" ".join(date))       #useage of str.join(list): join all elements in list with str
f="hiimmars"

print("123".join(f))     #str.join(str2),will insert str between all chars in str2
# test=[1,2,3]
# print(":".join(test))    # only when strs in lists


g="hi i m mars how are you"
print(g.split())

