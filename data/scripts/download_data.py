import yfinance as yf
import pandas_datareader as pdr
import pandas as pd

def dataDownlaoder(ticker:str):
    data = yf.Ticker(ticker)
    data_df = data.history(period="max")
    data_df.reset_index(inplace=True)
    return data_df

print(dataDownlaoder("TCS"))