import pandas as pd
import matplotlib.pyplot as plt
import yfinance
import xgboost as xgb
from xgboost import XGBRegressor
import yfinance as yf
import csv as cs


user = input("Choose a Stock Symbol: ")



def plot(user):
    plt.figure()
    plt.plot(user)
    plt.title(f"{user} Stock over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()



def csv_yfinance(user):
    X_training  = user[['Open', 'High', 'Low', 'Volume']]  
    Y_training =  user[[]]





def linear_regression_model(stock):
    x_model, y_model = xgb.XGBRegressor(stock)


    



plot(stock)


csv_yfinance(stock)
#Psuedocode:
# We need to create a csv file and save it to a user sql database to ensure that a user can
# access their past history and we'll export the history through userentry.sql so for
#csv_yfinance: we need to create a CSV file and save it to a user sql database

