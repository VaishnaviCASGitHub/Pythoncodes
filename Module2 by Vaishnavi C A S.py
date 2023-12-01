# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:25:44 2023

@author: C Adinarayana
"""

                         '''Module – 2 ASSIGNMENT 
                            BY VAISHNAVI C A S
A. Data Types'''

#1.	Construct 2 lists containing all the available data types (integer, float, string, complex and Boolean) and do the following.
l1 = [1, 3.35, "Vaishnavi", 10+7j, False]
l2 = [3, 20.0, "Chandu", 3-2j, True]
#a.	Create another list by concatenating the above 2 lists.
l3 = l1 + l2
print(l3)
#b.	Find the frequency of each element in the concatenated list.
l3 = [1, 3.35, 'Vaishnavi', (10+7j), False, 3, 20.0, 'Chandu', (3-2j), True]
l3.count(1)
l3.count(3.35)
l3.count("Vaishnavi")
l3.count(10+7j)
l3.count(False)
l3.count(3)
l3.count(20.0)
l3.count("Chandu")
l3.count(3-2j)
l3.count(True)
    '''for i in l3:
        l4= l3.count(i)
        print (l4)'''
   
#c.	Print the list in reverse order.
l3 = [1, 3.35, 'Vaishnavi', (10+7j), False, 3, 20.0, 'Chandu', (3-2j), True]
print(l3[::-1])




#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in another set)
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {5,6,7,8,9,10,11,12,13,14,15}
#a.	Find the common elements in the above 2 Sets.
s3 = s1.intersection(s2)
print(s3)
#b.	Find the elements that are not common.
s4 = s1.difference(s2)
print(s4)
s5 = s2.difference(s1)
print(s5)
print(s4.union(s5))
#c.	Remove element 7 from both Sets.
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {5,6,7,8,9,10,11,12,13,14,15}
s1.remove(7)
s2.remove(7)
print(s1)
print(s2)



#3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
d1_India = {"Telangana":200,"Tamilnadu":150,"Kerala":300,"Karnataka":250,"Delhi":400}
#a.	Print only state names from the dictionary.
d1_India.keys()
#b.	Update another country and its covid-19 cases in the dictionary.
d2_US = {"California":1000,"Florida":1200,"Texas":2000}
d3={}
d3.update(d1_India)
print(d3)
d3.update(d2_US)
print(d3)
   




'''Operators'''

#1.	
#A. Write an equation that relates   399, 543, and 12345.
a = 399
b= 543
c = 12345
d = c % b
print(d)
print("When {} is divided by {}, it yields a remainder {}".format(c,b,a))
#B.  “When I divide 5 by 3, I got 1. But when I divide -5 by 3, I got -2”—How would you justify it?
a = 5
b = 3
c = -5
print(a//b)
print(c//b)
#2.  a=5, b=3, c=10. What will be the output of the following:
a=5
b=3
c=10
#A. a/=b
a=a/b
print(a)
#B. c*=5 
c=c * 5 
print(c)
#3. 
#A. How to check the presence of an alphabet ‘s’ in the word “Data Science”.
word = "Data Science"
"s" in word
#B. How can you obtain 64 by using numbers 4 and 3.
a = 4
b= 3
c = a ** b
print(c)



'''Variables'''

#1.	What will be the output of the following (can/cannot):
#a.	Age1=5: True
Age1=5
#b.	5age=55: False
5age=55
#2.	What will be the output of the following (can/cannot):
#a.	Age_1=100: True
Age_1=100
#b.	age@1=100: False
age@1=100

#3.	How can you delete variables in Python?

Name = "Vaishnavi"
del(Name)
print(Name)
