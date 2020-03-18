import pandas 
import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import sqlite3
load_dotenv() 
df = pandas.read_csv('titanic.csv')
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()                        
print("Connection:", conn)
print("Cursor: ", cur)
print(df.head(5))
print(df.columns)

print(df.loc[[0]])
query = """
CREATE TABLE IF NOT EXISTS titanic(
    id serial primary key,
    Survived int not null,
    Pclass int not null,
    Name text not null,
    Sex text not null,
    Age float not null,
    Siblings_Spouses_Aboard int not null,
    Parents_Children_Aboard int not null,
    Fare real not null
);
"""
cur.execute(query)
cur.execute("SELECT * FROM titanic;")
result = cur.fetchall()
print("Result: ", len(result))

data = list(df.itertuples(index = False))

insert_query = """INSERT INTO titanic(Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    
    """
for row in data:
    cur.execute(insert_query, row)

cur.execute("SELECT * FROM titanic;")
result = cur.fetchall()

print("Final result: ", len(result))

conn.commit()



