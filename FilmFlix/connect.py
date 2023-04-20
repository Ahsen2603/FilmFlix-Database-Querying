import sqlite3 as sql # we have imported the extension sqlite

# To use the module, start by creating a database Connection object:
# import sqlite3 cx = sqlite3.connect("test.db") # test.db will be created or opened

#~ Database Connection object

conn = sql.connect("Python_and _SQL\FilmFlix\FilmFlix.db")

# Once a connection has been estabilished, create a cursor object 
# and call its execute() method to perform SQL queries:
cursor = conn.cursor()  # used to query db by calling its execute method 
row = cursor.fetchall()

cursor.execute("SELECT * FROM tblfilms")
for record in row:     # Loops through all records and then prints.
    print(record)
        