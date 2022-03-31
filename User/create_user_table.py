def create_user_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS usertable(fullname TEXT, email TEXT, username TEXT,password TEXT)')
    