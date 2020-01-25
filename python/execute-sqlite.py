import sqlite3


db = sqlite3.connect("database.db")

consulta = db.cursor()
consulta.execute("select * from tabla")
