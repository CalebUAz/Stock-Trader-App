import streamlit as st
import sqlite3

def user_functionality(username, new_cash, c, conn):
    #deposit cash for specific user name
    c.execute('UPDATE usertable SET cash = ? WHERE username=?',(new_cash,username,))
    conn.commit()