# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:59:23 2023

@author: C Adinarayana
"""

                                                  '''MODULE – 8 ASSIGNMENT
                                                  BY- VAISHNAVI C A S
Database connectivity using Python.'''
     
#1)	Connect to MySQL using Python, and push "Data.csv" into the database.

import pandas as pd
pip install sqlalchemy
pip install mysql 
import mysql #(google colab: import MySQLdb)
from sqlalchemy import create_engine
import pandas as pd
db = pd.read_csv(r"C:\Users\C Adinarayana\Downloads\Data.csv")
conn = create_engine("mysql://{user}:{pw}@localhost/{db}".format(user="root",pw="root",db="Data"))
db.to_sql("Data", con = conn, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None, method=None)

#2)	Connect to MySQL using Python, push "Indian Cities.csv" into the database.

pip install sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv(r"C:\Users\C Adinarayana\Downloads\Indian Cities.csv")
user = 'root'
pw = 'root'
db = 'Indian Cities'
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")
df.DataFrame.to_sql(Indian_Cities, con = engine, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None, method=None)
