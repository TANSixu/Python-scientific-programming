# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:34:44 2021

@author: 11911627 Tan Sixu
Assignment 4

Notice: "input" here replece raw_input in Python2, which means, input
 can read a whole line. 
mind "strip","rstrip", "lstrip"
"""
#%% Problem 1
# =============================================================================
# 1. Write a program to input information from keyboard for n (≥2) number of students’
# as given below; then check the presence of a given student (from keyboard input) in 
# the dictionary, and if yes, print the ID and marks:
# name, ID, marks
# =============================================================================

students_info={}
n=int(input("How many students: "))
for i in range(n):
    info=input(f"Student{i+1}' s info:")
    info=info.split(", ")
    students_info[info[0]]=tuple(info[1:])
    
name=input("Query student:")
if name in students_info:
    print(f"ID: {students_info[name][0]}")
    print(f"Marks: {students_info[name][1]}")
else:
    print("Student not found")
    
#%% Problem 2
# =============================================================================
# 2. Write a program to count the number of times each word appears in the following 
# sentence; store the word:times information in a dictionary and print the result:
# can you can a can as a canner can can a can
# =============================================================================
s="can you can a can as a canner can can a can"
s=s.split()
dic={}
for word in s:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
        
for word, times in dic.items():
    print(f"{word}: {times}")