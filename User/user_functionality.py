import streamlit as st
import sqlite3
from datetime import datetime

def deposit_cash(username, new_cash, c, conn):
    #deposit cash for specific user name
    c.execute('UPDATE usertable SET cash = (cash + ?) WHERE username=?', (new_cash,username,)) 
    conn.commit()
    st.success("Successfully deposited {}".format(new_cash))

def update_transcation_table(username, new_cash, operation, c, conn, ticker = ""):
    if operation == "Cash Withdraw":
        #here we update usertable as well
        c.execute('UPDATE usertable SET cash = (cash - ?) WHERE username=?', (new_cash,username,)) 
        st.success("Successfully withdrew {}".format(new_cash))

    if operation == "Buy Stocks":
        UserCash = c.execute('SELECT cash FROM usertable where username=?', (username,)) 
        UserCash = UserCash.fetchone()[0]
        StockCash = c.execute('SELECT Open FROM {} ORDER BY Date DESC LIMIT 1'.format(ticker))
        StockCash = StockCash.fetchone()[0] 

        if UserCash > StockCash:
            c.execute('UPDATE usertable SET cash = (cash - ?) WHERE username=?', (StockCash,username,)) 
            st.success("Successfully bought {}".format(ticker))
            new_cash = StockCash
        else:
            st.warning("You don't have suffient cash to buy {}".format(ticker))

    if operation == "Sell Stocks":
        UserCash = c.execute('SELECT cash FROM usertable where username=?', (username,)) 
        UserCash = UserCash.fetchone()[0]
        StockCash = c.execute('SELECT Open FROM {} ORDER BY Date DESC LIMIT 1'.format(ticker))
        StockCash = StockCash.fetchone()[0] 

        c.execute('UPDATE usertable SET cash = (cash + ?) WHERE username=?', (StockCash,username,)) 
        st.success("Successfully Sold {}".format(ticker))
        new_cash = StockCash

        
    dateTim = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    c.execute('INSERT INTO transactiontable(username, operation, amount, date, ticker) VALUES (?,?, ?, ?, ?)',(username, operation, new_cash, dateTim, ticker))
    conn.commit()

