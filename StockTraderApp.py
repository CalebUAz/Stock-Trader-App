import pandas as pd
import streamlit as st
import sqlite3 


from Stocks import create_stocks

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

if __name__ == '__main__':
    main()