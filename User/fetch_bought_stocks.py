def fetch_bought_stocks( username, c):
    tickers = c.execute('SELECT ticker FROM transactiontable WHERE username= ?',(username,)).fetchall()
    return tickers