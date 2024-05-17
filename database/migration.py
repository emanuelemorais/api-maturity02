import sqlite3
con = sqlite3.connect("sqlite.db")
cur = con.cursor()

cur.execute("CREATE TABLE pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, description TEXT)")

con.commit()
con.close()