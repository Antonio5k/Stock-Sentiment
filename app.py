# Importing Libraries
import streamlit as st
from textblob import TextBlob
import PyPDF2
import io
import pandas as pd
import yfinance as yf

#Logo
logo_path = "C:\\Users\\bmsto\\OneDrive\\Desktop\\trading_projects\\Sentiment_classifier\\app_files\photos\\5klabs.jpg"
st.image(logo_path, width=100) 


# Creating sentiment analyzer for stocks
st.title('Stock Sentiment Analysis')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # To convert to a string based IO:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)


# Creating sentiment analyzer for body of text
user_input = st.text_area("Or paste your text here")

if st.button("Analyze"):
    if uploaded_file is not None:
        blob = TextBlob(string_data)
    else:
        blob = TextBlob(user_input)
    result = blob.sentiment.polarity
    if result < 0:
      st.success('This text is negative')
    elif result == 0:
      st.success('This text is neutral')
    else:
      st.success('This text is positive')


#Stock info

st.title('Get Financial Data')

ticker_symbol = st.text_input("Enter the ticker symbol of the stock (e.g., AAPL for Apple Inc.)", "AAPL")
if st.button("Fetch Financial Data"):
    ticker_data = yf.Ticker(ticker_symbol)
    financial_data = ticker_data.info
    st.write(financial_data)
