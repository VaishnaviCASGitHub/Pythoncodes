# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:15:08 2023

@author: C Adinarayana
"""

                                                  '''MODULE – 4 ASSIGNMENT
                                                  BY- VAISHNAVI C A S
Functions'''

#1.	 Write a Python function to find the Max of three numbers.
def maximum(a,b,c):
    if a>b:
        print("{} is maximum".format(a))
        if a>c:
            print("{} is maximum".format(a))
    elif b>c:
        print("{} is maximum".format(b))
    else:
        print("{} is maximum".format(c))
maximum(2,6,4)
    
#2.	 Write a Python function to sum all the numbers in a list.
l1 = [1,2,3,4]
def addition(l1):
    x = 0
    for i in l1:
        x = x + i
        print(x)
        i = i + 1
addition(l1)
#3.	 Write a Python function to multiply all the numbers in a list.
l1 = [1,2,3,4]
def mul(l1):
    x = 1
    for i in l1:
        x = x * i
        print(x)
        i = i + 1
mul(l1)
