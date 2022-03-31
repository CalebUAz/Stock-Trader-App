def add_admin(fullname, email, username,password, c, conn):
    c.execute('INSERT INTO adminstable(fullname, email, username, password) VALUES (?,?, ?, ?)',(fullname, email, username, password))
    conn.commit()