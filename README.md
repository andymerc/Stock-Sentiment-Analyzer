# Stock Sentiment Analysis Tool

This tool leverages the Twitter API and advanced natural language processing techniques to assess public sentiment regarding specific stocks. It uses the RoBERTa model from Hugging Face's transformers library for sentiment analysis and presents the results through a simple Tkinter GUI.

## Features

- Real-time sentiment analysis of tweets related to specified stock tickers.
- Clean and straightforward graphical user interface for easy interaction.
- Analysis based on a sophisticated NLP model, providing insights into public sentiment on financial markets.

## Prerequisites

Before you can run this tool, you need to have the following installed:
- Python 3.6 or higher
- `tweepy` for interacting with the Twitter API
- `transformers` for utilizing the pre-trained RoBERTa model
- `tkinter` for the GUI

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stock-sentiment-analysis.git
   cd stock-sentiment-analysis

2. **Install Required Python Packages**
   ```bash
   pip install tweepy transformers
   
3. **Twitter API Keys**
   * You will need to create a Twitter Developer account and create an app to obtain your API keys.
   * Place your keys in a config.json file

## Usage
1. **Run the application**
   ```bash
   python sentiment_analysis_app.py
   
2. **Enter a stock ticker in the GUI**
   * The interface will prompt you to enter a stock ticker symbol. Input the symbol and press "Analyze Sentiment".
    
3. **View the results**
   * The application will display the overall sentiment (Positive, Neutral, Negative) based on the latest tweets related to the entered stock ticker.

## Components
1. **Front End**
   * A simple GUI built with Tkinter where users can enter the stock ticker they are interested in.
    
2. **Sentiment Analysis**
   * Uses Hugging Face's RoBERTa model through the transformers library to analyze tweet sentiments.
  
3. **Twitter API Integration**
   * Fetches tweets in real-time using Tweepy based on user input.

  

## Made by
* Andres Mercado for CPSC 481 Final
