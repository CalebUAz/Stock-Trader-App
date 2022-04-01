from datetime import date, datetime
from random import gauss
import pandas as pd
import sqlite3

def create_stocks(ticker, company_name, conn, c):
    df = pd.DataFrame(columns=['Date','Open','Close','High','Low','AdjClose','Volume'])
    df.Date = pd.date_range(start='03-25-2022', end=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), freq="1min")

    for i in range(len(df)):
        value = gauss(50, 100)
        
        if value < 0:
            value = value * -1

        df.Open[i] = value
        df.Close[i] = value + gauss(5, 10)
        df.High[i] = value + gauss(5, 10)
        df.Low[i]  = value + gauss(5, 10)
        df.AdjClose[i]  = value + gauss(5, 10)	
    
    cnx = sqlite3.connect('data.db')
    df.to_sql(name = '{}'.format(ticker), con = cnx)

    c.execute('CREATE TABLE IF NOT EXISTS lookuptable(TickerName TEXT, CompanyName TEXT)')
    c.execute('INSERT INTO lookuptable (TickerName, CompanyName) VALUES (?,?)',(ticker, company_name))
    conn.commit()
        #df.Volume[i]  = value + gauss(5, 10)
    #st.dataframe(df)
    return df   
