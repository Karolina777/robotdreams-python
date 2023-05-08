import random
import sqlite3
import string
import time
from pprint import pprint

db = sqlite3.connect('lesson22.sqlite')
curr = db.cursor()

table_users = ("CREATE TABLE IF NOT EXISTS users ("
               "id integer primary key autoincrement,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL)")


table_loans = ("CREATE TABLE IF NOT EXISTS loans ("
               "id integer primary key autoincrement,"
               "amount INTEGER NOT NULL,"
               "is_payed BOOLEAN DEFAULT FALSE,"
               "user_id INTEGER NOT NULL,"
               "FOREIGN KEY (user_id) references users(id))"
               )

table_payback = ("CREATE TABLE IF NOT EXISTS payback ("
               "id integer primary key autoincrement,"
               "loan_id INTEGER NOT NULL,"
               "user_id INTEGER NOT NULL ,"
               "amount INTEGER NOT NULL ,"
               "date TEXT DEFAULT CURRENT_TIMESTAMP,"
               "FOREIGN KEY (user_id) references users(id),"
               "FOREIGN KEY (loan_id) references loans(id))"
               )

curr.execute(table_users)
curr.execute(table_loans)
curr.execute(table_payback)

names = ['Oleksii', 'Serhii', 'Dmytro', 'Oksana', 'Nadiia', 'Sofiia', 'Ivan', 'Maksym']
last_names = ['Oleksiieno', 'Serhiienko', 'Dmytrenko', 'Mostovenko', 'Bovtruk', 'Bondarenko', 'Ivanenko', 'Maksymenko']
#
# # # generate users
users = []
for _ in range(100):
    users.append(
        (random.choice(names), random.choice(last_names), random.randint(18, 65))
    )

curr.executemany("INSERT INTO users(first_name, last_name, age) VALUES (?, ?, ?)", users)
db.commit()
#
# # # generate loans
# #
# #
loans = []
for _ in range(200):
    loans.append(
        (random.randint(100, 10000), random.randint(1, 80))
    )

curr.executemany("INSERT INTO loans(amount, user_id) VALUES (?, ?)", loans)
db.commit()

# # generate paybacks
#
paybacks = []
loans_records = curr.execute("SELECT id, user_id FROM loans where user_id > 20")
loads_data = loans_records.fetchall()
for _ in range(500):
    random_loan = random.choice(logit ads_data)
    paybacks.append(
        (random_loan[0], random_loan[1], random.randint(100, 700))
    )
#
curr.executemany("INSERT INTO payback (loan_id, user_id, amount) VALUES (?, ?, ?)", paybacks)
db.commit()


# get payback amounts for loans

# query = ("SELECT loans.id, payback.amount "
#          "FROM loans "
#          "JOIN payback ON loans.id = payback.loan_id ")
#
# res = curr.execute(query)
# pprint(res.fetchmany(10))

# get payback total sum for loans
#
# query = ("SELECT loans.id, loans.amount, SUM(payback.amount) as total_sum "
#          "FROM loans "
#          "JOIN payback ON loans.id = payback.loan_id "
#          "GROUP BY loans.id ")
#
# res = curr.execute(query)
# pprint(res.fetchmany(10))

# update payed loans

# -> get ids to update
# query = ("SELECT loans.id as total_sum "
#          "FROM loans "
#          "JOIN payback ON loans.id = payback.loan_id "
#          "GROUP BY loans.id "
#          "HAVING SUM(payback.amount) >= loans.amount")
#
# res = curr.execute(query)
# pprint(res.fetchall())

# -> transform ids to a string
# ids = ', '.join([str(item[0]) for item in res.fetchall()])

# -> update loans by id
# query = (f"UPDATE loans SET is_payed=1 WHERE id IN ({ids})")
# res = curr.execute(query)
# db.commit()

# -> use nested query for update
# query = ("UPDATE loans SET is_payed=1 WHERE id in (SELECT loans.id from loans join payback on loans.id = payback.loan_id group by loans.id having SUM(payback.amount) >= loans.amount)")
# curr.execute(query)
# db.commit()


# indexes

# names = ['Oleksii', 'Serhii', 'Dmytro', 'Oksana', 'Nadiia', 'Sofiia', 'Ivan', 'Maksym']
# last_names = ['Oleksiieno', 'Serhiienko', 'Dmytrenko', 'Mostovenko', 'Bovtruk', 'Bondarenko', 'Ivanenko', 'Maksymenko']

# # generate users
# users = []
# for _ in range(1000000):
#     users.append(
#         (random.choice(names), random.choice(last_names), random.randint(18, 65))
#     )
# curr.executemany("INSERT INTO users(first_name, last_name, age) VALUES (?, ?, ?)", users)
# db.commit()


# start = time.time()
# res = curr.execute("SELECT * FROM users where first_name='T2'")
# print(res.fetchall())
# print(time.time() - start)
