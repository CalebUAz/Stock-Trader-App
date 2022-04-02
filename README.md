# Stock-Trader-App
Stock trader app built with streamlit and SQLite3
Install the necessary packages using `pip`
```bash
pip install -r requirements.txt
```
**or** using `conda`
```bash
conda install --file requirements.txt
```
## Start Stock Trader application

The `generate_five_stocks.py` application must run **before** launching `StockTraderApp.py` application. 
Follow these steps:

1. Launch the generate five stocks file with:
 ```bash
python3 generate_five_stocks.py
```
  This would take a minute or two to generate random stocks. 

2. Launch the Stock Trader Application with:
```bash
streamlit run StockTraderApp.py
```
3. Once the application launches successfully on the browser, navigate to `Create Admin Account`, enter details and sign up. 

4. After logging in as the administrator, under task navigate to `Market Hours` and set the `Open time` and `Close time` and submit it.

  **Important**: 
  
  A. If this step isn't completed then it might throw errors when you go to buy/sell stocks.  
  B. Right now market schedule is hard coded to work only during working days i.e. Monday to Friday, if you run this application       during a weekend, then you may want to change some parameters under `Stock-Trader-App/Admin/market_hours_schedule.py` change                                    `(0 <= time.localtime().tm_wday <= 4)` to `(0 <= time.localtime().tm_wday <= 6)`
 
5. Now you may now proceed to register as a user from sidebar. 

6. After registering as user you may now login as user and proceed to perform deposit/buy/sell/withdraw operations. 

  **Important**: Perform this in a sequential order deposite -> Buy -> Sell/Withdraw/ViewPorfolio operation else it might throw errors.

7.  View Porfolio might throw an error but all you have to do is select another stock from the drop down menu. 
  
## Architecture diagram of the system:
![image](https://user-images.githubusercontent.com/90938130/161369549-09383103-33b5-4a1c-80fd-baa4a3cef467.png)

## Key components of the system:
## 1. User:
> A. The user can add create an account with their credentials, the system check if username exists or not, if it does it won't allow the same user to be used for registration. The system also checks if the email is entered correctly. 
> B. The user can buy or sell stocks during the market time window and schedule. 
> C. When it come to buying stocks, it check if the user has sufficient funds to purchase those stocks. When the user buys a stock it deducts amount from users cash account. 
> D. When the user sells the stock, the cash goes back to the users cash account. 

## 2. Admin:
> A. The Admin can Add stocks. 
> B. The Admin assigns the market schedule and market time window. 
