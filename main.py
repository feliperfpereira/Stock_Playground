import pandas as pd
import pandas_ta 
from pandas_datareader import data as pdr
from datetime import date
import datetime
import yfinance as yf
yf.pdr_override()

stock_list = pd.read_csv("list.csv")
x = 1
number_of_stocks = 200
while x != number_of_stocks:
    ticker = stock_list.iloc[x]["Symbols"]
    today = date.today()
    start_date = today - datetime.timedelta(days = 365)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    openrate = data["Open"]
    close = data["Adj Close"]
    high = data["High"]
    low = data["Low"]
    data["RSI"] = pandas_ta.momentum.rsi(close, length=None, scalar=None, drift=None, offset=None)
    stoch = pandas_ta.momentum.stoch(high, low, close, k=None, d=None, smooth_k=None, offset=None)
    data["K"] = stoch.STOCHk_14_3_3
    data["D"] = stoch.STOCHd_14_3_3

    data['Up'] = data.RSI>60
    data['StochUp'] = (data.K>60) & (data.D>60)
    df = data.iloc[-3:]

    df.to_csv('df.csv')
    df = pd.read_csv('df.csv')

    cu = df.at[2,'Up']
    cy = df.at[1,'Up']
    cd = df.at[0,'Up']
    su = df.at[2,'StochUp']
    sy = df.at[1,'StochUp']
    sd = df.at[0,'StochUp']

    if cu == True & su == True:
        print("FPT "+ticker)
        x = x+1
        if cy == False & cd == False:
            print("SPT "+ticker)
            Buy = True
            print("Buy "+ticker)
        else:
            print("SPNT "+ticker)
    else:
        print("NT "+ticker)
        x = x+1


    #df = pd.DataFrame()
    #help(df.ta)
    #df.ta.indicators()
    #help(pandas_ta.atr)

