import sqlite3

banco = sqlite3.connect("app.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id AUTO INTEGER PRIMARY KEY, name TEXT, idade INT, email TEXT)")
banco.commit()