import numpy as np 

#This is a multinomial naive bayes classifier
class NB_classifier:
    
    def fit(self, x, y):
        print("Start fitting data...")
        # Count number of catagories then count instance of each class to get priors.
        cat_count = y.value_counts()
        total = len(y)

        priors = []
        likelyhoods = {}
        cat_map = {}

        # All x will be 200 in length
        for cat in y:
            cat_map[cat] = [[1] for i in range(len(x[0]))]
            if(len(cat_map) == len(y.value_counts())):
                break

        for cat in cat_count:
            priors.append(cat/total)

        for prior in priors:
            print(prior)

        # Calculate likelyhoods 
        # Likelyhood = P(x1|yi) * P(x2|yi) * … P(xn|yi) 
        for i, instance in enumerate(x):
            for i, element in enumerate(instance):
                cat_map[y[i]][element[i]] += 1



    def predict():
        pass

    def evaluate():
        pass