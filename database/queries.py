import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'TodoDatabase.db')


def QueryDB(sqlQuery):
    DB_Connection = sqlite3.connect(DB_PATH)
    cursor = DB_Connection.cursor()
    result = cursor.execute(sqlQuery).fetchall()
    cursor.close()
    DB_Connection.close()
    return result


def EditDB(sqlEdit, params=()):
    DB_Connection = sqlite3.connect(DB_PATH)
    cursor = DB_Connection.cursor()
    result = cursor.execute(sqlEdit, params)
    cursor.close()
    DB_Connection.commit()
    DB_Connection.close()
    return result


def GetAllEntries():
    result = QueryDB('''SELECT * FROM TodoEntries''')
    return result


def InsertNewEntry(Todo, Done):
    NextID = GetNextRowId()
    sqlTodoInsert = '''INSERT INTO TodoEntries (ID, Todo, Done) VALUES (?, ?, ?)'''
    EditDB(sqlTodoInsert, (NextID, Todo, Done))


def MarkTodoEntry(ID, code):
    # limit codes to [0, 1, 2]
    if code < 0 or code > 2:
        return
    sqlUpdate = '''UPDATE TodoEntries SET Done = ? WHERE ID = ?'''
    EditDB(sqlUpdate, (code, ID))


def DeleteTodoEntry(ID):
    sqlTodoDelete = f'''DELETE FROM TodoEntries WHERE ID = ?'''
    EditDB(sqlTodoDelete, (ID,))


def GetNextRowId():
    result = QueryDB('''SELECT * FROM TodoEntries''')
    if not result:
        return 0
    else:
        return result[-1][0] + 1
