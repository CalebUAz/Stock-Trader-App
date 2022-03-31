def create_admin_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS adminstable(fullname TEXT, email TEXT, username TEXT,password TEXT)')
    