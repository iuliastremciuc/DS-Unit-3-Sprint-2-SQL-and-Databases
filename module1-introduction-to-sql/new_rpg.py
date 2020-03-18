import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import sqlite3
load_dotenv() ## looking in .env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()                        
print("Connection:", conn)
print("Cursor: ", cur)

rpg_filepath = 'rpg_db.sqlite3'

rpg_conn = sqlite3.connect(rpg_filepath)
rpg_cur = rpg_conn.cursor()
query = """ 
SELECT 	
   *
FROM armory_weapon
"""
result = rpg_cur.execute(query).fetchall()

query = """
CREATE TABLE IF NOT EXISTS armory_weapon(
    id serial primary key,
    item_ptr_id int,
    power int
);
"""
cur.execute(query)
cur.execute("SELECT * FROM armory_weapon;")
result = cur.fetchall()
print("result: ", len(result))

insert_query = "INSERT INTO armory_weapon(item_ptr_id, power) VALUES %s"
execute_values(cur, insert_query, [
    (138, 0),
    (139, 0), 
    (140, 0)
])
cur.execute("SELECT * FROM armory_weapon;")
result = cur.fetchall()
print("result:", len(result))
conn.commit()
