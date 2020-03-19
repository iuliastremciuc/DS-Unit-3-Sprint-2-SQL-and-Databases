import sqlite3
import pandas
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

conn = sqlite3.connect("rpg_db.sqlite3")
print(conn)
df = pandas.read_sql("select * from armory_item;", conn)
print(df)
#df.reset_index(inplace =True)
print(df)
data = df.to_dict(orient = "records")
print(data)

# print(data)
print("----------------")
print("URI:", connection_uri)
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
db = client.test_database_2 # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)
collection = db.rpg # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
print("----------------")
collection.insert_many(data)
print("DOCS:", collection.count_documents({}))
print("COLLECTIONS:")
print(db.list_collection_names())
print("DOCS:", collection.count_documents({})) # select *
# print(collection.findOne())