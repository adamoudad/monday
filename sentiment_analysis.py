# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('vader_lexicon')


import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import re


if __name__ == "__main__":
    positive_text = """Today is a great day. I love my life. Everything works fine. It is so awesome. We are the world!"""
    negative_text = """I failed everything. Even my success are failure. I have nowhere to go. Everything is dark in my head. I hate you all."""
    
    # sia = SentimentIntensityAnalyzer()
    # print("Posistive text:", positive_text)
    # print("Sentiment Score:", sia.polarity_scores(positive_text)['compound'])
    # print("Negative text:", negative_text)
    # print("Sentiment Score:", sia.polarity_scores(negative_text)['compound'])
    

    
