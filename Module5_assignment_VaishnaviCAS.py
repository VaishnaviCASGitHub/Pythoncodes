# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:00:29 2023

@author: C Adinarayana
"""

                                                 '''MODULE – 5 ASSIGNMENT
                                                 BY- VAISHNAVI C A S
File Handling & Exception Handling'''

#1) Write the code in Python to open a file named “try.txt”
f = open(r"C:\Users\C Adinarayana\Desktop\Vaish files\try.txt","w")
f.write("Hi I am Vaishnavi C A S")
f.close()
#2) What is the purpose of ‘r’ as a prefix in the given statement? 
     #f = open(r, “d:\color\flower.txt”)
'''The purpose of r as a prefix in the above statement shows that the string inside the open() is a raw string, such that 
   the codes inside it will be executed as such'''
#3) Write a note on the following
#A.	Purpose of Exception Handling
'''Exception handling helps the user to deal with variety of exceptions ie.)unexpected output errors like FileNotFoundError, 
   ValueError, ZeroDivisonError, etc.'''
#B.	Try block
'''When the user creates codes for a particular program, they can add them in try block, so that the codes inside it will be 
   executed'''
#C.	Except block
'''If there are any exceptions in try block, except block provides exceptions to deal with to let know the user about the 
   errors precisely '''
#D.	Else block
'''Once the try block is executed successfully without any errors, it enters into else block which has some set of statements 
   given by the user'''
#E.	Finally block
'''After executing try, except or else block, finally block will be executed irrespective of other blocks'''
#F.	Bulit-in exceptions
'''1. TypeError
   2. NameError
   3. SyntaxError'''
#4) Write 2 Custom exceptions
'''1. _init_
   2. _str_'''





