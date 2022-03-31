import pandas as pd
from datetime import date, datetime
import streamlit as st
from random import gauss

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