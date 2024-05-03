# 5K Classifier: A Sentiment Analysis Tool for Traders and Investors

## Overview
The 5K Classifier is a sentiment analysis tool designed to provide traders and investors with a competitive edge in the financial market. This application allows users to gauge whether the sentiment around a stock, based on news or other text sources, is positive or negative, enabling them to trade accordingly.

## Live Application
The application is hosted on Streamlit and can be accessed here.
https://5k-classifier.streamlit.app/

## How It Works
The application leverages the power of Natural Language Processing (NLP) to analyze and classify sentiment. Here's a step-by-step breakdown of how it works:

1. **User Input**: Users can input a body of text related to a stock.
2. **Preprocessing**: The input text is preprocessed by converting all text to lowercase, removing punctuation and stop words, and then stemming and lemmatizing the words for sentiment analysis.
3. **Sentiment Analysis**: The preprocessed text is analyzed using the TextBlob API, providing an instant sentiment classification for the stock.
4. **Visualization**: The application also displays visualizations as an added feature for the user.

## Technologies Used
The application integrates pre-trained models from NLTK and the TextBlob library, which are widely used in the Python community for natural language processing applications. The 'punkt' corpora is also downloaded for use in the application.

In the final step, we use a Langchain OpenAI and Question and Answer models to analyze the stock sentiment and provide analysis based on user input.

## Future Work
This application is an initial step towards building a larger Sentiment Classifier. Our goal is to make it more interactive and effective so that users can use this application as a key resource in their investment decision-making process.

## Conclusion
We believe that the 5K Classifier will serve as a valuable tool for traders and investors, providing them with insights that can help guide their trading strategies. We look forward to seeing how our users leverage this tool in their trading journey.
