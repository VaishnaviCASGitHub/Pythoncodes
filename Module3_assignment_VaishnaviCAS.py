# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 20:28:33 2023

@author: C Adinarayana
"""

                            '''MODULE – 3 ASSIGNMENT
                               BY- VAISHNAVI C A S
Conditional Statements'''

#1.	 Take a variable ‘age’ which is of positive value and check the following:
#a.	If the age is less than 10, print “Children”.
age = 5
if age < 10: #indentataion
    print("Children")
#b.	If the age is more than 60, print ‘senior citizens’.
age = 65
if age > 60:
    print("senior citizens")
#c.	 If it is between 10 and 60, print ‘normal citizen’.
age = 100
if 10 < age < 60:
    print("normal citizen")

#2.	Find the final train ticket price with the following conditions. 
#a.	If male and ‘sr.citizen’, 70% of the fare is applicable
#b.	If female and ‘sr.citizen’, 50% of the fare is applicable.
#c.	If a female and a normal citizen, 70% of the fare is applicable.
#d.	If a male and a normal citizen, 100% of the fare is applicable.
#[Hint: First check for the gender, then calculate the fare based on the age factor. For both ‘Male’ and ‘Female’, consider them as sr.citizens if their age >=60]
gender = str(input("Type your gender:"))
age = int(input("Enter your age:"))
if gender == "male":
    if age>=60:
        print("70% of the fare is applicable")
    else:
        print("100% of te fare is applicable")
else:
    if age>=60:
        print("50% of the fare is applicable")
    else:
        print("70% of te fare is applicable")
#3.	Check whether the given number is positive and divisible by 5 or not.  
n = int(input("Enter any number:"))
if n>0:
    print("{} is positive".format(n))
    if n%5==0:
        print("{} is divisible by 5".format(n))
    else:
        print("{} is not divisble by 5".format(n))
else:
    print("{} is not positive".format(n))
        
#Conditional Statements
#1.	
#A) list1 = [1, 5.5, (10+20j), ’data science’]. Print default functions and parameters exist in list1.
dir(list)
help(list.append)
#B) How do we create a sequence of numbers in Python?

n = range(10)
for i in n:
    print(i)
   
#C) Read the input from the keyboard and print a sequence of numbers up to that number
user1 = int(input("Enter any number:"))
user2 = list(range(user1))
print(user2)
   
#2.	Create 2 lists: One list contains 10 numbers (list1 = [0, 1, 2, 3....9]) and another 
#list contains words of those 10 numbers (list2 = ['zero', 'one', 'two', ...., 'nine']).
list1= list(range(10))
print(list1)
list2 = []
for num in list1:
    if num==0: 
        list2.append("zero") 
    if num==1:
        list2.append("one")
    if num==2:
        list2.append("two") 
    if num==3:
        list2.append("three")  
    if num==4:
        list2.append("four")   
    if num==5:
        list2.append("five")   
    if num==6:
        list2.append("six")   
    if num==7:
        list2.append("seven")    
    if num==8:
        list2.append("eight")   
    if num==9:
        list2.append("nine")
print(list2)
#a.	Create a dictionary such that list2 are keys and list1 are values.

dict1= {'Vaish': 22, 'Chandu': 20, 'Adi': 55, 'Bhagya': 46}
list2= dict1.keys()
list1= dict1.values()
print("List2 keys are:",list2)
print("List1 values are:",list1)

#3.	Consider list1 [3, 4, 5, 6, 7, 8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is an odd number in the list1.
list1 = [3, 4, 5, 6, 7, 8]
list2 = []
for i in list1:
    if i%2==0:
        k= i + 10
        list2.append(k)
    else:
        t = i * 5
        list2.append(t)
list2      

#4.  Write a simple user-defined function that greets a person in such a way that:
#i) It should accept both the name of a person and the message you want to deliver.
#ii) If no message is provided, it should greet a default message ‘How are you’.
          	#Ex: Hello ---xxxx---, How are you - default message.
           	#Ex: Hello ---xxxx---, --xx your message xx---
              
def greeting():
    name = str(input("Enter your good name:"))
    msg = str(input("Enter any message you want to convey!"))
    if msg:
        #print("Hello {},How are you?".format(name))
        print("Hello {}, your message is {}".format(name,msg))
    else:
        print("Hello {},How are you?".format(name))
greeting()
