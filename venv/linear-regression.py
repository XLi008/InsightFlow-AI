import pandas as pd
import matplotlib.pyplot as plt
import yfinance
import xgboost as xgb
import yfinance as yt

user = input("Choose a Stock Symbol: ")

stock = yfinance.download(user, start='2000-01-01', end='2024-01-01')



def plot(user):
    plt.figure()
    plt.plot(stock)
    plt.title(f"{user} Stock over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


plot(stock)
