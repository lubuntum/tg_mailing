import sqlite3

def getUserByUsername(username):
    db = getDB()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username =?", (username, ))
    user = cursor.fetchone()
    db.close()
    return user

def getDB():
    return sqlite3.connect('./database/database.db')