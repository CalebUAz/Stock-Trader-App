from email.utils import parseaddr
import streamlit as st

def add_user(fullname, email, username, password, c, conn):

    #perform sanity check for entered username and emails
    if any(char.isnumeric() for char in username) or any(char.isnumeric() for char in fullname):
        st.error(f"The username {username} is unavailable, please don't use numbers.")

    elif "@" not in parseaddr(email)[1]:
        st.error("Enter Valid email")    

    else:
        #check to see if the username already exists in the table 
        if len(c.execute('SELECT username FROM usertable WHERE username=?', (username, )).fetchall()) > 0:
            st.error("Username already exsists") 
        else:
            c.execute('INSERT INTO usertable(fullname, email, username, password) VALUES (?,?, ?, ?)',(fullname, email, username, password))
            conn.commit() 
            st.success("You have successfully created a valid User Account")
            st.info("Go to User Login Menu to login")        
            