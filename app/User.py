import sqlite3

banco = sqlite3.connect("app.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, email TEXT)")
banco.commit()