import pandas as pd
import streamlit as st
import sqlite3 


from Stocks import (create_stocks, fetch_stocks, display_stock)
from Admin import (create_admin_table, add_admin, login_admin,
                    create_market_schedule, insert_market_schedule,
                    market_hours_schedule)
from User import (create_user_table, add_user, login_user, 
                    deposit_cash, create_transaction_table, 
                    update_transcation_table, fetch_bought_stocks, 
                    display_transcation_table, stock_portfolio)
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
        create_market_schedule(c)

        st.subheader("Admin Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            hashed_pswd = make_hashes(password)
            result = login_admin(username,check_hashes(password, hashed_pswd), c)

            if result:
                #If login was successful 
                st.success("Admin Logged In as {}".format(username))
                task = st.selectbox("Task",["AddStocks","Market Hours"])

                if task == "AddStocks":
                    new_ticker_name = st.text_input("Enter Ticker name")
                    new_company_name = st.text_input("Enter Company name")

                    if st.button('Add'):
                        create_stocks(new_ticker_name, new_company_name, conn, c)
                        st.info('Please wait while the stock is being generated')
                
                if task == "Market Hours":
                    open_time = st.time_input('Set market open time')
                    close_time = st.time_input('Set market close time')
                    if st.button('Add'):
                        insert_market_schedule(open_time, close_time, conn, c)
                        

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
                task = st.selectbox("Task",["Deposit Cash", "Buy Stocks", "Sell Stocks","Portfolio", "Cash Withdraw" ,"Transcation history"])

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

                    if market_hours_schedule(c) == True:
                    
                        ViewStk = st.selectbox("Select Stock",pd.DataFrame(fetch_stocks(c)))
                        display_stock(ViewStk)
                        buy = st.radio('Choose type of operation:',('Buy', 'Limit order buy'))
                        #if st.checkbox('Buy'):
                        if buy == 'buy':
                            new_cash = 0
                            update_transcation_table(username, new_cash , task, c, conn, ticker = ViewStk)
                        else:
                            new_cash = 0
                            limit_order = st.number_input("")
                            update_transcation_table(username, new_cash , task, c, conn, limorder = limit_order, ticker = ViewStk)

                if task == "Sell Stocks":
                    st.subheader('Sell Stocks')

                    if market_hours_schedule(c) == True:

                        ViewStk = st.selectbox("Select Stock",pd.DataFrame(fetch_bought_stocks(username, c)))
                        display_stock(ViewStk)
                        if st.checkbox('Sell'):
                            new_cash = 0
                            limit_order = st.number_input("")
                            update_transcation_table(username, new_cash , task, c, conn, ticker = ViewStk)

                if task == "Transcation history":
                    st.subheader("Transcation history")
                    display_transcation_table(username, conn)

                if task == "Portfolio":
                    st.subheader("Portfolio")
                    stock_portfolio(username, conn, c)
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