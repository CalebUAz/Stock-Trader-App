import streamlit as st
import sqlite3
from datetime import datetime

def deposit_cash(username, new_cash, c, conn):
    #deposit cash for specific user name
    c.execute('UPDATE usertable SET cash = ? WHERE username=?',(new_cash,username,))
    conn.commit()
    st.success("Successfully deposited {}".format(new_cash))

def update_transcation_table(username, new_cash, operation, c, conn, ticker = ""):
    dateTim = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    c.execute('INSERT INTO transactiontable(username, operation, amount, date, ticker) VALUES (?,?, ?, ?, ?)',(username, operation, new_cash, dateTim, ticker))
    conn.commit()