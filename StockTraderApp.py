import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import streamlit as st
from PIL import Image
import requests
import pandas_datareader as web
import sqlite3 
import hashlib
from datetime import date, datetime
import random
from random import gauss

conn = sqlite3.connect('data.db')
c = conn.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_stocks():
    #Idea behind 
    df = pd.DataFrame(columns=['Date','Open','Close','High','Low','AdjClose','Volume'])
    df.Date = pd.date_range(start='03-01-2022', end=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), freq="1min")

    for i in range(len(df)):
        value = gauss(50, 100)
        
        if value < 0:
            value = value * -1

        df.Open[i] = value
        df.Close[i] = value + gauss(5, 10)
        df.High[i] = value + gauss(5, 10)
        df.Low[i]  = value + gauss(5, 10)
        df.AdjClose[i]  = value + gauss(5, 10)	
        #df.Volume[i]  = value + gauss(5, 10)
    st.dataframe(df)
    return df    

def main():

    st.title("Stock trading application")

    menu = ["Home","Login","SignUp", "Admin"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
         st.subheader("Admin Login Section")
    
    elif choice == "Admin":
        st.subheader("Admin Login Section")

    elif choice == "Login":
        st.subheader("Login Section")           

    elif choice == "SignUp":
        st.subheader("Create New Account")

if __name__ == '__main__':
    main()