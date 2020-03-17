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
 sum(w.item_ptr_id is null) as non_weapon_count,
 sum(w.item_ptr_id is not null) as weapon_count
 
FROM armory_item i 
LEFT JOIN armory_weapon w ON  i.item_id = w.item_ptr_id
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
  c.character_id,
  c.name as char_name,
  count(inv.item_id) as item_count,
  count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
GROUP BY c.character_id -- row per what?
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
