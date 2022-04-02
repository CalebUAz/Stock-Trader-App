from datetime import datetime
import streamlit as st 
from datetime import datetime
def create_market_schedule(c):
    c.execute('CREATE TABLE IF NOT EXISTS marketschedule (OpenTime timestamp, CloseTime timestamp)')
    
def insert_market_schedule(otime, ctime, conn, c):
     c.execute('INSERT INTO marketschedule VALUES (?, ?)',(otime, ctime, ))
     conn.commit()
     num_entries = c.execute('select max(RowId) from marketschedule').fetchone()[0]

     if num_entries > 1:
         #if the admin enters time multiple time, then you want to keep the latest time in DB
         c.execute('DELETE FROM marketschedule WHERE (OpenTime) not in(?)',(otime,))
         conn.commit()
     st.success("Successfully set Open time as {} and close time as {}".format(otime, ctime))