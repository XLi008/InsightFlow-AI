
# Alternative solution 
# s1 import the libiraries 
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# s2 Fetch stock data 
stock_data = yf.download('AAPL', start='2020-01-01', end='2021-01-01', progress=False)

# s3 Prepare your X and y
X = stock_data['Close'].values.reshape(-1, 1)
y = stock_data['Close'].shift(-1).dropna().values

# s4 Train the data with suitable model
model = LinearRegression()
model.fit(X, y)

# Analyse the results 
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Linear Regression - AAPL Stock')
plt.show()
