import pandas as pd
import streamlit as st
import sqlite3 

from Stocks import create_stocks
from Admin import create_admin_table, add_admin

conn = sqlite3.connect('data.db')
c = conn.cursor()


def main():

    st.title("Stock trading application")

    menu = ["Home","Login","SignUp", "Admin"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
         st.subheader("Home")
    
    elif choice == "Admin":
        st.subheader("Admin Login Section")

    elif choice == "Login":
        st.subheader("Login Section")           

    elif choice == "SignUp":
        st.subheader("Create New Account")
        task = st.selectbox("Choose",["Create Admin Account","Create User Account"])
        if task == "Create Admin Account":
            #first create an admin table if not created already
            create_admin_table(c)

            new_full_name = st.text_input("Full Name")
            new_email = st.text_input("Email")      
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')
            if st.button("Signup"):
                add_admin(new_full_name, new_email, new_user, new_password, c, conn)


if __name__ == '__main__':
    main()