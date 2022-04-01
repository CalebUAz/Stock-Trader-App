import pandas as pd
import streamlit as st
import sqlite3 


from Stocks import create_stocks, fetch_stocks, display_stock
from Admin import create_admin_table, add_admin, login_admin
from User import (create_user_table, add_user, login_user, 
                    deposit_cash, create_transaction_table, 
                    update_transcation_table, fetch_bought_stocks)
from Encryption import check_hashes, make_hashes

conn = sqlite3.connect('data.db')
c = conn.cursor()

def main():
    
    st.title("Stock trading application")

    menu = ["Home","User Login","SignUp", "Admin Login"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
         st.subheader("Home")
         ViewStk = st.selectbox("Select Stock",pd.DataFrame(fetch_stocks(c)))
         display_stock(ViewStk)
    
    elif choice == "Admin Login":
        st.subheader("Admin Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            hashed_pswd = make_hashes(password)
            result = login_admin(username,check_hashes(password, hashed_pswd), c)

            if result:
                #If login was successful 
                st.success("Admin Logged In as {}".format(username))
                task = st.selectbox("Task",["AddStocks","ViewStocks","DeleteStocks","Profiles"])

                if task == "AddStocks":
                    print("")

            else:
                st.error("[Error] Login Failed")    

    elif choice == "User Login":
        st.subheader("Login Section")           
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password, hashed_pswd), c)

            if result:
                #If login was successful 
                st.success("Admin Logged In as {}".format(username))
                task = st.selectbox("Task",["Deposit Cash", "Buy Stocks", "Sell Stocks","Portfolio", "Cash Withdraw"])

                if task == "Deposit Cash":
                    st.subheader('Deposit Cash')
                    new_cash = st.number_input("") 
                    if st.checkbox('Deposit'):
                        deposit_cash(username, new_cash, c, conn)
                        update_transcation_table(username, new_cash, task, c, conn)
                        
                if task == "Cash Withdraw":
                    st.subheader('Cash Withdraw')
                    new_cash = st.number_input("")
                    if st.checkbox('Withdraw'):
                        update_transcation_table(username, new_cash, task, c, conn)
                
                if task == "Buy Stocks":
                    st.subheader('Buy Stocks')
                    ViewStk = st.selectbox("Select Stock",pd.DataFrame(fetch_stocks(c)))
                    if st.checkbox('Buy'):
                        new_cash = 0
                        update_transcation_table(username, new_cash , task, c, conn, ticker = ViewStk)

                if task == "Sell Stocks":
                    st.subheader('Sell Stocks')
                    ViewStk = st.selectbox("Select Stock",pd.DataFrame(fetch_bought_stocks(username, c)))
                    if st.checkbox('Sell'):
                        new_cash = 0
                        update_transcation_table(username, new_cash , task, c, conn, ticker = ViewStk)

            else:
                st.error("[Error] Login Failed")   

    elif choice == "SignUp":
        create_admin_table(c)
        create_user_table(c)
        create_transaction_table(c)        
        st.subheader("Create New Account")
        task = st.selectbox("Choose",["Create Admin Account","Create User Account"])

        if task == "Create Admin Account":
            #first create an admin and user table if not created already
            new_full_name = st.text_input("Full Name")
            new_email = st.text_input("Email")      
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                #add entered details to the DB
                add_admin(new_full_name, new_email, new_user, make_hashes(new_password), c, conn)
                #clear 
                #st.experimental_singleton.clear()

        elif task == "Create User Account":
            new_full_name = st.text_input("Full Name")
            new_email = st.text_input("Email")      
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                #add entered details to the DB
                add_user(new_full_name, new_email, new_user, make_hashes(new_password), c, conn)
                #clear 
                st.experimental_singleton.clear()

if __name__ == '__main__':
    main()