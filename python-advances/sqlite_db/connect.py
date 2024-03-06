import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()

# c.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, priority INTEGER NOT NULL)")
# print("Table created successfully")
# c.close()

# c.execute("INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1)")
# print("Inserted data in table")


# conn.commit()
# conn.close()

