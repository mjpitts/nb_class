import pandas as pd
from nb_class import NB_classifier

def main():
    
    file = 'spam.csv'
    encoding = 'cp1252'

    print("Start loading data...")
    #read file into dataframe 
    df = pd.read_csv(file, encoding=encoding)

    # extract x and y component
    y  = df['v1']
    x = df['v2']

    print("Done loading data...")

    # First do analysis so we can see the most used words an pick some of the best out of them for our vocabulary.
    vocab = {}
    for instance in x:
        row = instance.split()
        for word in row:
            if(word[-2:] == "ing"):
                vocab[word[:len(word)-3]] = 1 + vocab.get(word[:len(word)-3], 1)
            elif(word[-1] == 's'):
                vocab[word[:len(word)-1]] = 1 + vocab.get(word[:len(word)-1], 1)
            elif(word[-1:] == 'er' or word[-1:] == 'ed'):
                vocab[word[:len(word)-2]] = 1 + vocab.get(word[:len(word)-2], 1)
            else:
                vocab[word] = 1 + vocab.get(word, 1)

    
    sorted_dict = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=False))
    words = list(sorted_dict.keys())
    top_words = words[-200:]


    data = [[0 for j in range(200)] for i in range(len(x))]
    # Next, transform each email in x into an 200 length vector where each index represents one of the top 200 words, the min value will be zero to prevent calculation errors later
    for i, instance in enumerate(x):
        row = instance.split()
        for j, word in enumerate(top_words):
            data[i][j] = (row.count(word)+1)

    model = NB_classifier()
   # model.fit(data,y)



if __name__ == "__main__":
    main()
