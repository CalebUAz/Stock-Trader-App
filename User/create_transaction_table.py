def create_transaction_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS transactiontable(username TEXT, operation TEXT, amount INTEGER, date TIMESTAMP, ticker TEXT)')
    