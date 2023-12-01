# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:23:56 2023

@author: C Adinarayana
"""

                                                   '''MODULE – 6 ASSIGNMENT
                                                    BY- VAISHNAVI C A S
Regular Expression'''
#1)	Write a Python program to check that a string contains only a certain set of characters.
#(In this case a-z, A-Z, and 0-9). 
import re
s1 = "Hi Vaishnavi C A S, Welcome to 360DigiTMG!, Chennai" 
s2 = re.split(r"\W+",s1)
print(s2)
#2)	Write a Python program to replace all occurrences of space, commas, or dots with a colon.
import re
s1 = "Hi Vaishnavi C A S, Welcome to 360DigiTMG!, Chennai" 
s2 = re.sub(r"\s*\W",":",s1)
print(s2)
