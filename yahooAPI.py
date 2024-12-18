import yfinance as yf

data = yf.download("TD", period="1d", interval="1m")
print(data)
