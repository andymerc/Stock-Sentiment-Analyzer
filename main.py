import tkinter as tk
from tkinter import messagebox
import tweepy
import json
from collections import Counter
import re
from transformers import pipeline

# Function to authenticate Twitter using Tweepy
def authenticate_twitter():
    with open("bearer_token.json") as infile:
        creds = json.load(infile)
        token = creds["bearer_token"]
        client = tweepy.Client(bearer_token=token)
    return client

# Function to fetch tweets
def get_tweets(client, stock_name, num_tweets=100):
    query = f"{stock_name} -is:retweet"
    tweets = client.search_recent_tweets(query=query, max_results=num_tweets, tweet_fields=['text'])
    return [tweet.text for tweet in tweets.data] if tweets.data else []

# Function to clean tweets using regex
def clean_tweet(tweet):
    tweet = re.sub(r'https?://\S+', '', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet = re.sub(r'\s+', ' ', tweet).strip()
    return tweet

# Function to analyze sentiment
def analyze_sentiment(tweets):
    sentiment_analyzer = pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment')
    results = sentiment_analyzer(tweets)
    label_mapping = {'LABEL_0': 'Negative', 'LABEL_1': 'Neutral', 'LABEL_2': 'Positive'}
    readable_labels = [label_mapping[result['label']] for result in results]
    sentiment_counts = Counter(readable_labels)
    overall_sentiment = max(sentiment_counts, key=sentiment_counts.get) if sentiment_counts else "No clear sentiment"
    return overall_sentiment

# Function to perform all tasks when button is clicked
def on_button_click():
    stock_query = entry.get()
    client = authenticate_twitter()
    tweets = get_tweets(client, stock_query)
    cleaned_tweets = [clean_tweet(tweet) for tweet in tweets]
    sentiment_result = analyze_sentiment(cleaned_tweets)

    # Determine suggested moves based on sentiment
    if sentiment_result == "Positive":
        advice = ("Consider a Covered Call if you own the stock, or a Bull Call Spread to capitalize on expected gains."
                  " These strategies can provide profit from a rising market while managing risk.")
    elif sentiment_result == "Neutral":
        advice = ("Consider an Iron Condor or a Butterfly Spread. These strategies profit from low market volatility"
                  " and are best used when little change in the stock price is expected.")
    elif sentiment_result == "Negative":
        advice = ("Consider a Bear Put Spread to gain from downward movements or a Protective Put to safeguard your holdings."
                  " These can be effective during anticipated declines.")
    else:
        advice = "Unable to determine a clear move."

    # Display the sentiment and suggested move
    result_label.config(text=f"Overall Sentiment: {sentiment_result}\nSuggested Move: {advice}")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Stock Sentiment Analyzer")

tk.Label(root, text="Enter stock query:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
tk.Button(root, text="Analyze Sentiment", command=on_button_click).pack(pady=10)
result_label = tk.Label(root, text="Overall Sentiment: None")
result_label.pack(pady=20)

root.mainloop()