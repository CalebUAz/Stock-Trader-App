import sqlite3

def login_user(username,password,c):
    try:   
        c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
        data = c.fetchall()
        return data

    except sqlite3.OperationalError:
        print("[Error] User Table not created")            