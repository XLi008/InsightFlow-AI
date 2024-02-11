import pandas as pd
import matplotlib.pyplot as plt
import yfinance
import xgboost as xgb
import yfinance as yf
import csv as cs


stock = input("Choose a Stock Symbol: ")

user =  yfinance.download(stock, start='2000-01-01', end='2024-01-01')





def training(user):
    X_training  = user[['Open', 'High', 'Low', 'Volume']]  
    Y_training =  user['Close']
    return X_training, Y_training


def plot(user):
    plt.figure()
    plt.plot(user)
    plt.title(f"{user} Stock over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()




def linear_regression_model(stock):
    x_model, y_model = xgb.XGBRegressor(stock)


    



data = training(user)
plot_data = plot(data)

plot_data(data)


#Psuedocode:
# We need to create a csv file and save it to a user sql database to ensure that a user can
# access their past history and we'll export the history through userentry.sql so for
#csv_yfinance: we need to create a CSV file and save it to a user sql database


