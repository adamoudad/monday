import sys

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('vader_lexicon')

if __name__ == "__main__":
    text = """Today is a great day."""
    sia = SentimentIntensityAnalyzer()
    print("Sentiment Score:", sia.polarity_scores(passage)['compound'])

    
