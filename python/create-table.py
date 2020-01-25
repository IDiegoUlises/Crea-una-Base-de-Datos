import sqlite3


connect = sqlite3.connect("database.db")

connect.execute("""CREATE TABLE product
                  (name text, business text, price int, 
                   quantity int, comment text)""")
