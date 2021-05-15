import requests
import json
import sqlite3

# names = []
# key = '4096477517076531'
#
# for each in range(1,10):
#     url = f"https://superheroapi.com/api/4096477517076531/{each}/powerstats"
#     req = requests.get(url)
#     checker = req.headers
#
#     if req.status_code == 200 and checker["Content-Type"] == 'application/json':
#
#         context = req.text
#         toDict = json.loads(context)
#         ind = json.dumps(toDict, indent=4)
#
#         names.append(toDict["name"])
#     else: print('error')
#
#
# print(names)

# task 2
from typing import Dict

# key = '4096477517076531'
# url = f"https://superheroapi.com/api/4096477517076531/106/powerstats"
# req = requests.get(url)
# with open("superheroes.json", "w") as file:
#     dictForFile = json.loads(req.text)
#     file.write(json.dumps(dictForFile, indent=4))

# task 4
# ეს კოდი ქმნის ცხრილს და შეჰყავს მასში API სგან მიღებულ სუპერგმირთა მონაცემები, გმირთა რაოდენობა განისაზღვრება იმით თუ რა ციფრს შეიყვანს მომხმარებელი heroAmount ცვლადში.
dataBaseFile = open("database.sqlite", "w")

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

# cursor.execute("""
#         CREATE TABLE heroes
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(50),
#         intelligence INTEGER,
#         strength INTEGER,
#         speed INTEGER,
#         durability INTEGER,
#         power INTEGER,
#         combat INTEGER)
#
#     """)

# რაც უფრო დიდია heroAmount რიცხვი მით ნელია პროგრამა !!!
heroAmount = int(input("რამდენი გმირის ინფორმაცია ამოვიღო? : "))
for each in range(1, heroAmount):

    key = '4096477517076531'
    heroStats = []
    urlForInsert = f"https://superheroapi.com/api/{key}/{each}/powerstats"

    reqForInsert = requests.get(urlForInsert)
    context = reqForInsert.text
    toDict = json.loads(context)

    cursor.execute(f'''

        INSERT INTO heroes (name, intelligence, strength, speed, durability, power, combat)
        VALUES ('{toDict["name"]}', {toDict["intelligence"]}, {toDict["strength"]},
                {toDict["speed"]}, {toDict["durability"]}, {toDict["power"]}, {toDict["combat"]})

    ''')
    conn.commit()
conn.close()

# print(req.headers)
# print(req.status_code)
# print(toDict)
