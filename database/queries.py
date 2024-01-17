import sqlite3
import os


def QueryDB(sqlQuery):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(script_dir, 'TodoDatabase.db')
    DB_Connection = sqlite3.connect(db_path)
    cursor = DB_Connection.cursor()
    result = cursor.execute(sqlQuery).fetchall()
    cursor.close()
    DB_Connection.close()
    return result


def GetAllEntries():
    result = QueryDB('''SELECT * FROM TodoEntries''')
    return result
