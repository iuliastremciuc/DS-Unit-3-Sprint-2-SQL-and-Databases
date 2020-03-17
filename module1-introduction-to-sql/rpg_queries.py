import sqlite3
rpg_filepath = 'rpg_db.sqlite3'
connection = sqlite3.connect(rpg_filepath)
#connection.row_factory = sqlite3.Row
print( "Connection:", connection)

cursor = connection.cursor()
print("Cursor: ", cursor)


#query = 'SELECT * FROM charactercreator_character;'
## How many total Characters are there?
query = """ 
SELECT 	
   count(character_id) as CharacterID

FROM charactercreator_character
"""
result = cursor.execute(query)
print("Result: ", result)

result2 = cursor.execute(query).fetchall()
print("TOTAL CHARACTERS: ", result2[0][0])

##How many total Items?
query2 = """
SELECT 	
   count(item_id) as ItemID

FROM armory_item
"""
result3 = cursor.execute(query2)
print("Result: ", result3)

result4 = cursor.execute(query2).fetchall()
print("TOTAL ITEMS: ", result4[0][0])

##How many of the Items are weapons? How many are not?
query3 = """
SELECT
   armory_weapon.item_ptr_id,
   armory_item.item_id,
   armory_item.name
   
FROM  armory_item
JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
""" 
result5 = cursor.execute(query3)
print("Result: ", result5)

result6 = cursor.execute(query3).fetchall()
print("ITEMS ARE WEAPONS: ", result6)
for row in result6:
    print(type(row))
    print(row)
    print("-------")

#How many Items does each character have? (Return first 20 rows)
query4 = """
SELECT
   charactercreator_character_inventory.character_id,
   count(DISTINCT charactercreator_character_inventory.item_id) as Items_per_Character
FROM charactercreator_character_inventory
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20
"""
result7 = cursor.execute(query4)
print("Result: ", result7)

result8 = cursor.execute(query4).fetchall()
print("ITEMS PER CHARACTER: ", result7)
for row in result8:
    print(type(row))
    print(row)
    print("-------")

# How many Weapons does each character have? (Return first 20 rows)
query5 = """
SELECT
   charactercreator_character_inventory.character_id,
   count(DISTINCT charactercreator_character_inventory.item_id) as Weapons_per_Character
FROM charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20
"""
result9 = cursor.execute(query5)
print("Result: ", result9)

result10 = cursor.execute(query5).fetchall()
print("WEAPONS PER CHARACTER: ", result9)
for row in result10:
    print(type(row))
    print(row)
    print("-------")
