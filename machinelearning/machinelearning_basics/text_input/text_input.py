import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from icecream import ic
import os

dirname = os.path.dirname(__file__)
DATA_FILE = os.path.join(dirname,'spam.csv')

EPOCHS = 3

# example text for model training (SMS messages)
simple_train = ['hello world', 'learning python3', 'machine learning']

# import and instantiate CountVectorizer (with the default parameters)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

# learn the 'vocabulary' of the training data (occurs in-place)
ic(vect.fit(simple_train))

# examine the fitted vocabulary
ic(vect.get_feature_names())

# transform training data into a 'document-term matrix'
simple_train_dtm = vect.transform(simple_train)
ic(simple_train_dtm)

# convert sparse matrix to a dense matrix
simple_train_dtm = simple_train_dtm.toarray()

ic(simple_train_dtm)
ic(type(simple_train_dtm),simple_train_dtm.shape)
# examine the vocabulary and document-term matrix together
dataframe = pd.DataFrame(np.array(simple_train_dtm), columns=vect.get_feature_names())
ic(dataframe)

# check the type of the document-term matrix
print(type(simple_train_dtm))

# examine the sparse matrix contents
print(simple_train_dtm)

# example text for model testing
simple_test = ["please don't call me"]

# transform testing data into a document-term matrix (using existing vocabulary)
simple_test_dtm = vect.transform(simple_test)
ic(simple_test_dtm.toarray())

# examine the vocabulary and document-term matrix together
dataframe2 = pd.DataFrame(simple_test_dtm.toarray(), columns=vect.get_feature_names())
ic(dataframe2)

# read file into pandas using a relative path
sms = pd.read_csv(DATA_FILE, encoding='latin-1')
sms.dropna(how="any", inplace=True, axis=1)
sms.columns = ['label', 'message']
ic(type(sms),sms.shape)
ic(sms.head())

sms.describe()

sms.groupby('label').describe()

# convert label to a numerical variable
sms['label_num'] = sms.label.map({'ham':0, 'spam':1})
ic(sms.head())

sms['message_len'] = sms.message.apply(len)
ic(sms.head())

plt.figure(figsize=(12, 8))

sms[sms.label=='ham'].message_len.plot(bins=35, kind='hist', color='blue', 
                                       label='Ham messages', alpha=0.6)
sms[sms.label=='spam'].message_len.plot(kind='hist', color='red', 
                                       label='Spam messages', alpha=0.6)
plt.legend()
plt.xlabel("Message Length")

# plt.show()

ic(sms[sms.label=='ham'].describe())
ic(sms[sms.label=='spam'].describe())

print(sms[sms.message_len == 910].message.iloc[0])

import string
from icecream import ic
"""
Takes in a string of text, then performs the following:
1. Remove all punctuation
2. Remove all stopwords
3. Returns a list of the cleaned text
"""

def text_process(mess):

    STOPWORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", \
    "itself","they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", \
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",\
    "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", \
    "all","any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    
    PUNCTUATION = '`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'

    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in PUNCTUATION]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS]).lower()

print(text_process("Hello! I'm a machine learning researcher at MIT university"))

ic(sms.head())

sms['clean_msg'] = sms.message.apply(text_process)

ic(sms.head())

from collections import Counter

words = sms[sms.label=='ham'].clean_msg.apply(lambda x: [word.lower() for word in x.split()])
ham_words = Counter()

for msg in words:
    ham_words.update(msg)
    
print(ham_words.most_common(50))

words = sms[sms.label=='spam'].clean_msg.apply(lambda x: [word.lower() for word in x.split()])
spam_words = Counter()

for msg in words:
    spam_words.update(msg)

print()    
print(spam_words.most_common(50))

# how to define X and y (from the SMS data) for use with COUNTVECTORIZER
X = sms.clean_msg
y = sms.label_num
ic(X.shape)
ic(y.shape)

# split X and y into training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
ic(X_train.shape)
ic(X_test.shape)
ic(y_train.shape)
ic(y_test.shape)

from sklearn.feature_extraction.text import CountVectorizer

# instantiate the vectorizer
vect = CountVectorizer()
vect.fit(X_train)

# learn training data vocabulary, then use it to create a document-term matrix
X_train_dtm = vect.transform(X_train)

# equivalently: combine fit and transform into a single step
X_train_dtm = vect.fit_transform(X_train)

# examine the document-term matrix
ic(X_train_dtm)

# transform testing data (using fitted vocabulary) into a document-term matrix
X_test_dtm = vect.transform(X_test)
ic(X_test_dtm)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X_train_dtm)
tfidf_transformer.transform(X_train_dtm)

ic(type(X),type(y))
ic(type(X_train_dtm),type(X_test_dtm))
ic(type(np.array(X_train_dtm)),type(np.array(X_test_dtm)))

X_train_dtm = np.array(X_train_dtm)
X_test_dtm = np.array(X_test_dtm)

ic(X_train_dtm, X_test_dtm)

import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(20, input_shape = (4179,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.compile(optimizer='rmsprop',loss = 'binary_crossentropy',metrics = ['accuracy'])

model.fit(X_train_dtm,y_train,batch_size = 50, epochs = EPOCHS, validation_data=(X_test_dtm,y_test), verbose = 2)



