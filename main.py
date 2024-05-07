import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import tweepy
import requests
import pandas as pd
import matplotlib.pyplot as plt


# Function to authenticate and fetch tweets
def get_tweets(stock_name, num_tweets):
    # Authenticate to Twitter (fill in with your credentials)
    auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET_KEY')
    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
    api = tweepy.API(auth)

    # Fetch tweets
    tweets = api.search_tweets(q=stock_name, count=num_tweets, lang='en')
    return tweets


# Function to perform sentiment analysis
def analyze_sentiment(tweets):
    sentiment_scores = []
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        sentiment_scores.append(analysis.sentiment.polarity)
    return sentiment_scores


# Function to fetch historical stock prices
def get_stock_data(stock_symbol, start_date, end_date):
    # Example with Yahoo Finance API
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{stock_symbol}?period1={start_date}&period2={end_date}'
    response = requests.get(url)
    data = response.json()
    # Process JSON into a DataFrame
    timestamps = data['chart']['result'][0]['timestamp']
    prices = data['chart']['result'][0]['indicators']['quote'][0]['close']
    df = pd.DataFrame({'Time': timestamps, 'Price': prices})
    return df


# Main analysis function
def analyze():
    stock_symbol = symbol_entry.get()
    stock_name = name_entry.get()
    num_tweets = int(num_tweets_entry.get())
    start_date = int(pd.Timestamp(start_entry.get()).timestamp())
    end_date = int(pd.Timestamp(end_entry.get()).timestamp())

    try:
        # Get data
        tweets = get_tweets(stock_name, num_tweets)
        stock_data = get_stock_data(stock_symbol, start_date, end_date)

        # Perform sentiment analysis
        sentiments = analyze_sentiment(tweets)

        # Aggregate and compare data (implement your own logic)
        # Example comparison visualization
        plt.plot(stock_data['Time'], stock_data['Price'], label='Stock Price')
        plt.plot(range(len(sentiments)), sentiments, label='Tweet Sentiment')
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Tkinter UI Setup
root = tk.Tk()
root.title("Stock Sentiment Analysis")

# Stock Symbol
tk.Label(root, text="Stock Symbol (Ticker):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1, padx=5, pady=5)

# Stock Name for Tweets
tk.Label(root, text="Stock Name/Hashtags:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Number of Tweets
tk.Label(root, text="Number of Tweets:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
num_tweets_entry = tk.Entry(root)
num_tweets_entry.grid(row=2, column=1, padx=5, pady=5)

# Date Range (Start)
tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
start_entry = tk.Entry(root)
start_entry.grid(row=3, column=1, padx=5, pady=5)

# Date Range (End)
tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
end_entry = tk.Entry(root)
end_entry.grid(row=4, column=1, padx=5, pady=5)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze", command=analyze)
analyze_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
