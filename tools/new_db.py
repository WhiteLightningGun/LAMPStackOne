import sqlite3

DB_Connection = sqlite3.connect('TodoDatabase.db')

DB_Connection.execute('''
    CREATE TABLE TodoEntries
        (ID INT PRIMARY KEY NOT NULL,
        Todo TEXT NOT NULL  CHECK(length(Todo) <= 200), 
        Done INT NOT NULL
);
    ''')

DB_Connection.close()
