import sqlite3

connection = sqlite3.connect('my_database.db')

print(connection)

cursor = connection.cursor()

# check if table already exists and create if not
try:
    query = ('CREATE TABLE users1 ('
             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
             'name TEXT,'
             'age INTEGER,'
             'city TEXT)')
    cursor.execute(query)
except sqlite3.OperationalError:
    pass
    # print('Table already exists')

# insert 1 record of data into the table
# query1 = ('INSERT INTO users (name) VALUES ("oLEXII")')
# cursor.execute(query1)

# insert many records in the table at once
# records = [
#     ('alesya', 6),
#     ('alisa', 7),
#     ('natalia', 8)
# ]
#
# query2 = 'INSERT INTO users (name, age) VALUES (?,?)'
#
# cursor.executemany(query2, records)

# needed to run a transaction to actually make changes in the table
# connection.commit()

# print(cursor)

# read data from the table

query_select = 'SELECT * FROM users'
# res - is a curson object
res = cursor.execute(query_select)

# retrieve data from the cursor object of results - res

# data = res.fetchall()
# print(data)

# make a nicier output of results

from pprint import pprint
# pprint(data)

# use fetchmany for retrieving a portion of data records.
# fetchmany remembers  how many records it has fetched previously
# and with the next run it retrieves the next records

data = res.fetchmany(2)
pprint(data)
data = res.fetchmany(3)
print(data)