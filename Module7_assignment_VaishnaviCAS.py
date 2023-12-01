# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:55:53 2023

@author: C Adinarayana
"""
                                                     '''MODULE – 7 ASSIGNMENT
                                                     BY- VAISHNAVI C A S
Python for data analytics'''
    
'''1)	Please take care of missing data present in the “Data.csv” file using the Python module 
“sklearn.impute” and its methods, also collect all the data that has “Salary” less than “70,000”.'''
#importing libraries
import pandas as pd
import numpy as np
import matpltlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("C:/Users/C Adinarayana/Downloads/Data.csv")
data
a = data.isnull().sum()
a
data["Salaries"]
data["Salaries"].mean() #finding mean in salaries column

#dealing with missing values using sklearn.impute module
import sklearn
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan,strategy="mean") 
data.iloc[:,7:9]=imp.fit_transform(data.iloc[:,7:9])
data["Salaries"].isnull().sum()
data["age"].isnull().sum()
imp_race= SimpleImputer(missing_values=np.nan,strategy="most_frequent")
data.iloc[:,-1:]=imp_race.fit_transform(data.iloc[:,-1:])
data["Race"].isnull().sum()
impu=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
data.iloc[:,0:7]=impu.fit_transform(data.iloc[:,0:7])
data.isnull().sum()
data

# salaries less than 70,000
newdata = data.loc[data["Salaries"]<70000] 
newdata

'''3)	Representing dates in different ways
Date objects in Python have a great number of ways they can be printed out as strings. 
In some cases, you want to know the date in a clear, language-agnostic format. In other cases, 
you want something which can fit into a paragraph and flow naturally.
Print out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), 
in a number of different ways, by using the “ .strftime() ” method. Store it in a variable called “Andrew”. 
Instructions: 	
Print it in the format 'YYYY-MM', 'YYYY-DDD', and 'MONTH (YYYY)''''
import date from datetime
import time
a = "August 26, 1992"
a = time.strftime("%Y-%m")
a
b = time.strftime("%Y-%d")
b
c = time.strftime("%B(%Y)")
c
#4)	For the dataset “Indian_cities”, 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
city = pd.read_csv("C:/Users/C Adinarayana/Downloads/Indian_cities.csv")
city
np.shape(city)
d = city.describe()
d

#a)	Find out the top 10 states in female-male sex ratio.
top10 = city.nlargest(10, columns=["sex_ratio"],keep="first")
top10states = top10["state_name"]
top10states

#b)	Find out the top 10 cities in the total number of graduates.
top10grad = city.nlargest(10, columns=["total_graduates"],keep="first")
top10cities = top10grad["name_of_city"]
top10cities

#c)	Find out the top 10 cities and their locations in respect of total ‘effective_literacy_rate’.
top10elr = city.nlargest(10, columns=["effective_literacy_rate_total"],keep="first")
top10city = top10elr["name_of_city"]
top10city
top10loc = top10elr["location"]
top10loc
merged = pd.concat([top10city,top10loc],axis = 1)
merged
#5)	 For the data set “Indian_cities”
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
city = pd.read_csv("C:/Users/C Adinarayana/Downloads/Indian_cities.csv")
#a)	Construct a histogram on ‘literates_total’ and comment on the inferences.
plt.title("histttt")
plt.hist(city["literates_total"],edgecolor="black",label="total literates")
plt.show()

#INFERENCE
#Bihar has the low literacy_total with value 56998

#b)	Construct a scatter plot between male graduates and female graduates.
plt.scatter()
male = city["male_graduates"]
male
female = city["female_graduates"]
female
plt.scatter(male,female,c="red")
#6)	 For the data set “Indian_cities”
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
city = pd.read_csv("C:/Users/C Adinarayana/Downloads/Indian_cities.csv")
#a)	Construct Boxplot on the total effective literacy rate and draw inferences.
box = city.boxplot(column="effective_literacy_rate_total",by="state_name")

#INFERENCE
#Uttar Pradesh has the low effective_literacy_rate_total with value 49

#b)	Find out the number of null values in each column of the dataset and delete them.
city.isnull().sum()









