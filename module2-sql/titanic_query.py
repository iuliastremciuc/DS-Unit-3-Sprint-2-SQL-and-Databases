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

cur.execute("SELECT * FROM titanic;")
result = cur.fetchall()
#print(result)
#How many passengers survived, and how many died?
cur.execute("SELECT count (*) From titanic  WHERE SURVIVED = 1")
result = cur.fetchall()
print(result[0][0])
#How many passengers were in each class?
cur.execute("Select Pclass, COUNT(*) from titanic group by Pclass;")
result = cur.fetchall()
print(result)
#How many passengers survived/died within each class?
cur.execute("select count(*), pclass from titanic where survived = 1 group by pclass order by pclass;")
result = cur.fetchall()
print("Survived: ", result)
cur.execute("select count(*), pclass from titanic where survived = 0 group by pclass order by pclass;")
result = cur.fetchall()
print("Died: " , result)
#What was the average age of survivors vs nonsurvivors?
cur.execute("select avg(age), survived from titanic group by survived")
result = cur.fetchall()
print("Average age for survivors/nonsurvivors: ", result)
#What was the average age of each passenger class?
cur.execute("select avg(age), pclass from titanic group by pclass order by pclass")
result = cur.fetchall()
print("Average age for classes: ", result)
#What was the average fare by passenger class? By survival?
cur.execute("select avg(fare), pclass from titanic group by pclass order by pclass")
result = cur.fetchall()
print("Average fare for classes: ", result)
cur.execute("select avg(fare), survived from titanic group by survived")
result = cur.fetchall()
print("Average fare for survival: ", result)
#How many siblings/spouses aboard on average, by passenger class? By survival?
cur.execute("select avg(siblings_spouses_aboard), pclass from titanic group by pclass")
result = cur.fetchall()
print("Average sibling/spouse for classes: ", result)
cur.execute("select avg(siblings_spouses_aboard), survived from titanic group by survived")
result = cur.fetchall()
print("Average sibling/spouse for survivals: ", result)
#How many parents/children aboard on average, by passenger class? By survival?
cur.execute("select avg(parents_children_aboard), pclass from titanic group by pclass")
result = cur.fetchall()
print("Average parents/children for classes: ", result)
cur.execute("select avg(parents_children_aboard), survived from titanic group by survived")
result = cur.fetchall()
print("Average parents/children for survivals: ", result)
#Do any passengers have the same name?
cur.execute("select name from titanic group by name having count(*) > 1")
result = cur.fetchall()
print("Passengers with the same names: ", len(result))
