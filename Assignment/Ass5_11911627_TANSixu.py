# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:44:00 2021

@author: 11911627 Tan Sixu
Assignment 5
"""
# =============================================================================
# 1. Write a program to sort the following names according to their alphabetical order 
# without using sort() function. Hint: use tuple-like multiple assignment to swap 
# items.
# yashmith ava noah isabella emma
# 
# =============================================================================
#dictionary order
names='yashmith ava noah isabella emma'
names=names.split()
for i in range(len(names)):
    for j in range(len(names)-i-1):
        if(names[j]>names[j+1]):
            names[j], names[j+1]=names[j+1], names[j]
print(f"after sorting: {names}")



#%%
# =============================================================================
# 2. Find the unique characters in each of the following word and print the sorted unique 
# characters for each of them:
# "egg", "immune", "feed", "vacuum", "goddessship"
# =============================================================================
words=["egg", "immune", "feed", "vacuum", "goddessship"]
result=[]
for word in words:
    tmps=set(word)
    tmpr=[]              #record unique chr in each word
    for c in tmps:
        if word.count(c)==1:
            tmpr.append(c)
    result.append(tmpr)

for w, u in zip(words,result):
    print(f"unique in {w}: {u}")
    
    