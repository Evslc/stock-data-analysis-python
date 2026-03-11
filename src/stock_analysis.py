import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download Tesla stock data
tesla = yf.Ticker("TSLA")
data = tesla.history(period="max")

# Reset index
data.reset_index(inplace=True)

# Save dataset
data.to_csv("tesla_stock.csv", index=False)

# Plot closing price
plt.figure(figsize=(10,5))
plt.plot(data["Date"], data["Close"])
plt.title("Tesla Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Price USD")
plt.show()
