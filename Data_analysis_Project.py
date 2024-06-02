import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def process_data(stock_data):
    stock_data["Daily Return"] = stock_data["Adj Close"].pct_change()
    stock_data["50-Day MA"] = stock_data["Adj Close"].rolling(window=50).mean()
    stock_data["200-Day MA"] = stock_data["Adj Close"].rolling(window=200).mean()
    return stock_data

def visualize_data(stock_data, ticker):
    sns.set(style="whitegrid")

    plt.figure(figsize=(14, 7))
    plt.plot(stock_data["Adj Close"], label="Adjusted Close Price")
    plt.plot(stock_data["50-Day MA"], label="50-Day Moving Average")
    plt.plot(stock_data["200-Day MA"], label="200-Day Moving Average")
    plt.title(f'{ticker} Stock Price and Moving Averages')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 7))
    sns.histplot(stock_data["Daily Return"].dropna(), kde=True, bins=100, color="purple")
    plt.title(f'{ticker} Daily Returns Distribution')
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.show()

def main():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    stock_data = fetch_data(ticker, start_date, end_date)
    stock_data = process_data(stock_data)
    visualize_data(stock_data, ticker)

if __name__ == "__main__":
    main()
