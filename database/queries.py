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


def EditDB(sqlEdit):
    DB_Connection = sqlite3.connect(DB_PATH)
    cursor = DB_Connection.cursor()
    result = cursor.execute(sqlEdit)
    cursor.close()
    DB_Connection.commit()
    DB_Connection.close()
    return result


def GetAllEntries():
    result = QueryDB('''SELECT * FROM TodoEntries''')
    return result


def InsertNewEntry(Todo, Done):
    NextID = GetNextRowId()
    sqlTodoInsert = f'''INSERT INTO TodoEntries (ID, Todo, Done) VALUES ('{NextID}', '{Todo}', '{Done}')'''
    EditDB(sqlTodoInsert)


def MarkTodoEntry(ID, code):
    # limit codes to [0, 1, 2]
    if code < 0 or code > 2:
        return
    sqlTodoMark = f'''UPDATE TodoEntries SET Done = '{code}' WHERE ID = '{ID}' '''
    EditDB(sqlTodoMark)


def DeleteTodoEntry(ID):
    sqlTodoDelete = f'''DELETE FROM TodoEntries WHERE ID = '{ID}' '''
    EditDB(sqlTodoDelete)


def GetNextRowId():
    result = QueryDB('''SELECT * FROM TodoEntries''')
    if not result:
        return 0
    else:
        return result[-1][0] + 1
