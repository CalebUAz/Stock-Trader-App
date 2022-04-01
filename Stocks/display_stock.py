import pandas as pd
import streamlit as st
import sqlite3 

def display_stock(ViewStk):
    #stk = c.execute('SELECT * FROM {}'.format(ViewStk))
    #st.subheader(type(stk))
    cnx = sqlite3.connect('data.db')
    df = pd.read_sql('SELECT * FROM {}'.format(ViewStk), cnx)
    df = df.set_index('Date')
    #df = df.drop('Date',axis=1)
    df = df.drop('index',axis=1)
    #df = df.rename(columns={'Date':'index'}).set_index('index')
    st.line_chart(df[['Open','AdjClose']].iloc[-20:])
    st.dataframe(df)