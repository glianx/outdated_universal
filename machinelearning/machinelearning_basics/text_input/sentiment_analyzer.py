import tensorflow as tf
import numpy as np
import os
from icecream import ic
import keras
from keras.models import Sequential
from keras.layers import Dense

dirname = os.path.dirname(__file__)

#show path to files
import pandas as pd

filepath_dict = {'yelp':   os.path.join(dirname,'sentiment_analysis/yelp_labelled.txt'),
                 'amazon': os.path.join(dirname,'sentiment_analysis/amazon_cells_labelled.txt'),
                 'imdb':   os.path.join(dirname,'sentiment_analysis/imdb_labelled.txt')}

#create list of data
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

#create pandas dataframe
df = pd.concat(df_list)

ic(df[:5],type(df),df.shape)
ic(len(df_list),type(df_list))



#create a vectorizer word processor
from sklearn.feature_extraction.text import CountVectorizer

#stopwords to remove
STOPWORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", \
"itself","they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", \
"having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",\
"during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", \
"all","any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#demo sentence
sentences = ['hello world', 'learning machine learning','researcher at MIT']

#define vectorizer
vectorizer = CountVectorizer(min_df=0, lowercase=True, stop_words=STOPWORDS)

#fit vectorizer and demo vectorizer
vectorizer.fit(sentences)

ic(vectorizer.vocabulary_)
ic(vectorizer.transform(sentences).toarray())

#split yelp data into train and test dataset
from sklearn.model_selection import train_test_split

df_yelp = df[df['source'] == 'yelp']

sentences = df_yelp['sentence'].values
y = df_yelp['label'].values


sentences_train, sentences_test, y_train, y_test = train_test_split(
   sentences, y, test_size=0.25, random_state=1000)

#fit vectorizer on training data
vectorizer.fit(sentences_train)

#vectorize the data
X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
ic(X_train)

#show wordlist (bag_of_words)
import random
words_list = list(vectorizer.vocabulary_.items()) 
random.shuffle(words_list)
ic(words_list[:15])

#built-in LogisticRegression model
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

print("Accuracy:", score)

#train LogisticRegression model on each dataset
for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = df_source['sentence'].values
    y = df_source['label'].values

    sentences_train, sentences_test, y_train, y_test = train_test_split(
        sentences, y, test_size=0.25, random_state=1000)

    vectorizer.fit(sentences_train)
    X_train = vectorizer.transform(sentences_train)
    X_test  = vectorizer.transform(sentences_test)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    score = classifier.score(X_test, y_test)
    print('Accuracy for {} data: {:.4f}'.format(source, score))

#tokenize data
from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(sentences_train)

X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index

ic(sentences_train[2])
ic(X_train[2])

#pad sequences
from keras.preprocessing.sequence import pad_sequences

maxlen = 100

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

ic(X_train[0, 0])

from keras.models import Sequential
from keras import layers

import matplotlib.pyplot as plt

embedding_dim = 50

#==================================================================

#Sequential model
model = Sequential()
model.add(layers.Embedding(input_dim=vocab_size, 
                           output_dim=embedding_dim, 
                           input_length=maxlen))
model.add(layers.Flatten())
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train,
                    epochs=20,
                    verbose=0,
                    validation_data=(X_test, y_test),
                    batch_size=32)

loss, accuracy = model.evaluate(X_train, y_train, verbose=0)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Testing Accuracy:  {:.4f}".format(accuracy))

ic(X_test[0],y_test[0])