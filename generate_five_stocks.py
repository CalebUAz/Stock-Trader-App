from Stocks import create_stocks
import pandas as pd
import sqlite3 

conn = sqlite3.connect('data.db')
c = conn.cursor()

def main():
    ticker_list = ['AMD', 'AAPL', 'T', 'MU', 'VZ']
    company_name = ['Advanced Micro Devices, Inc.', 'Apple Inc.', 'AT&T Inc.', 'Micron Technology, Inc.', 'Verizon Communications Inc.']

    for ticker, company_name in zip(ticker_list,company_name):
        df = create_stocks(ticker, company_name, conn, c)

if __name__ == '__main__':
    main()