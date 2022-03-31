def login_admin(username,password,c):
    c.execute('SELECT * FROM adminstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data