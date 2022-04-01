import streamlit as st
import sqlite3

def deposit_cash(username, new_cash, c, conn):
    #deposit cash for specific user name
    c.execute('UPDATE usertable SET cash = ? WHERE username=?',(new_cash,username,))
    conn.commit()
    st.success("Successfully deposited {}".format(new_cash))