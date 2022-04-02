from datetime import datetime, date
import time
import streamlit as st

def market_hours_schedule(c):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  start = c.execute('select OpenTime from "marketschedule"')
  start = start.fetchone()[0]
  end = c.execute('select CloseTime from "marketschedule"')
  end = end.fetchone()[0]
  #start = '09:30:00'
  #end = '16:00:00'
  if (0 <= time.localtime().tm_wday <= 4) and current_time > start and current_time < end:
    st.subheader('Market is open')
    return True
  else:
    st.subheader('Sorry, Market is closed')
    return False