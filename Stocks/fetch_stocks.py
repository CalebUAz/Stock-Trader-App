def fetch_stocks(c):
    all_stcks = c.execute('SELECT TickerName FROM lookuptable').fetchall()
    return all_stcks