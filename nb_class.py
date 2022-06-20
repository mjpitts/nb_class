import numpy as np 
import pandas as pd


class NB_classifier:
    # First goal is to import the data and create a dictionary of frequencies
    def load(file, encoding):
        #read file into dataframe 
        df = pd.read_csv(file, encoding=encoding)

        # extract x and y component
        y  = df['v1']
        x = df['v2']

        return x,y

    def fit(x,y):
        # Count of negative case for spam 
        ham_count = y.value_counts().ham
        # Count of positive case for spam 
        spam_count = y.value_counts().spam

        # Calculate ham prior
        ham_prior = ham_count / (ham_count + spam_count)

        # Calculate spam prior
        spam_prior = spam_count / (ham_count + spam_count)

        print(ham_prior)
        print(spam_prior)

    def evaluate():
        pass