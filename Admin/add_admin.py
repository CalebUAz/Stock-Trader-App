from email.utils import parseaddr
import streamlit as st

def add_admin(fullname, email, username, password, c, conn):

    if any(char.isnumeric() for char in username) or any(char.isnumeric() for char in fullname):
        st.error(f"The username {username} is unavailable, please don't use numbers.")

    elif "@" not in parseaddr(email)[1]:
        st.error("Enter Valid email")    

    else:
        c.execute('INSERT INTO adminstable(fullname, email, username, password) VALUES (?,?, ?, ?)',(fullname, email, username, password))
        conn.commit()         