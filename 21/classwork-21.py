import random
import sqlite3
from pprint import pprint

connection = sqlite3.connect('21-my_database.db')

print(connection)

cursor = connection.cursor()

# check if table already exists and create if not

query = ('CREATE TABLE IF NOT EXISTS books ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'author TEXT,'
         'year INTEGER NOT NULL ,'
         'price INTEGER NOT NULL,'
         'title TEXT)')

cursor.execute(query)

conn = sqlite3.connect('21-my_database.db')
cursor = conn.cursor()

# create data
titles = ['title - a', 'title - b', 'title - c', 'title - d', 'title - e', 'title - f', 'title - s', 'title - g']
authors = ['author - a', 'author - b', 'author - c']




# for i in range(100):
#     title = random.choice(titles)
#     author = random.choice(authors)
#     year = random.randint(1950, 2023)
#     price = random.randint(100,1000)
#     query1 = f"INSERT INTO books (author,year,price,title) VALUES ('{author}', '{year}', '{price}', '{title}')"
#     cursor.execute(query1)
#     conn.commit()

# will work faster if use executemany
# and insert many records in the table at once

records = [(lambda a, t: [a, random.randint(1950, 2023), random.randint(100, 1000), t])(random.choice(authors), random.choice(titles)) for _ in range(100)]

# pprint(records)
query1 = f"INSERT INTO books (author,year,price,title) VALUES (?, ?, ?, ?)"
cursor.executemany(query1, records)
conn.commit()

limit = 10
offset = 0
for _ in range(1):
    query = f'SELECT title, AVG(price) FROM books GROUP BY title LIMIT {limit} OFFSET {offset}'
    res = cursor.execute(query)
    pprint(res.fetchall())
    # print([item[0] for item in res.fetchall()])
    offset += limit
