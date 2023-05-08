import sqlite3

db = sqlite3.connect('book_store_my.sqlite')
curr = db.cursor()

table_users = ("CREATE TABLE IF NOT EXISTS users ("
               "id integer primary key autoincrement,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL)")


table_publishing_house = ("CREATE TABLE IF NOT EXISTS publishing_house ("
                          "id integer primary key autoincrement,"
                          "name TEXT,"
                          "rating INTEGER DEFAULT 5)")


table_books = ("CREATE TABLE IF NOT EXISTS books ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER,"
               "price INTEGER,"
               "publishing_house_id INTEGER NOT NULL,"
               "FOREIGN KEY (publishing_house_id) references publising_house(id))"
               )

table_purchases = ("CREATE TABLE IF NOT EXISTS purchases ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "user_id INTEGER NOT NULL,"
                   "book_id INTEGER NOT NULL,"
                   "date TEXT DEFAULT CURRENT_TIMESTAMP,"
                   "FOREIGN KEY (user_id) references users(id),"
                   "FOREIGN KEY (book_id) references books(id))")

curr.execute(table_users)
curr.execute(table_publishing_house)
curr.execute(table_books)
curr.execute(table_purchases)
