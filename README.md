## Link
https://5k-classifier.streamlit.app/

## Introduction
This application will aid traders and investors that are seeking a competitive edge agaigst financial market. You can use this tool to gauge if a stock's news is positive or negative, and then trade in accordance with the sentiment. 

### Source
We have intergrated pre-trained models that NLTK uses, and also the TextBlob library. These are widely used in the python community for naturual language proccessing applications. Then I download the 'punkt' corpora.

### How it works
Using streamlit's comprehensive hosting service, a user can input text from a given body of text about stocks, and get an instant classification in regards to the sentiment. It'll also display visualizations as an added feature to the user.

### Preprocessing
Once the user enters the text, everything will be converted to lowercase, the punctuation and stop words will be removed. Next the words will be stemmend and laemmatized for sentiment analysis.

Using the TextBlob API, we can get an instant classification for the stock.

### Approach

Finally we used a Langchain OpenAI and Question and Answer models to analyze the stock sentiment. Provide analysis based on user input. 


## Conclusion
The app is initial step towards building a larger Sentiment Classifier and make it more interactive and effective so users can use this application as a confluence to their investment decisions.
