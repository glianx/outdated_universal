import os
from icecream import ic
dirname = os.path.dirname(__file__)
DATASET_PATH = os.path.join(dirname, "file.csv")
ic(dirname,DATASET_PATH)

import sys
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import keras

#Using MatPlotLib.pyplot to show some data
DATASET = pd.read_csv(DATASET_PATH)

ic(DATASET.shape)
ic(DATASET.loc[1])
print(DATASET)

print(DATASET.loc[-20:])

data = DATASET[~DATASET.isin(['?'])]
print(data.loc[280:])

# drop rows with NaN values from DataFrame
data = data.dropna(axis=0)
print(data.loc[280:])

# print the shape and data type of the dataframe
ic(data.shape)
print(data.dtypes)

# transform data to numeric to enable further analysis
data = data.apply(pd.to_numeric)
data.dtypes

# print data characteristics, usings pandas built-in describe() function
print(data.describe())

import matplotlib.pyplot as plt
# plot histograms for each variable
data.hist(figsize = (9,9))
plt.show()

pd.crosstab(data.Age,data.Outcome).plot(kind="bar",figsize=(20,6))
plt.title('Diabetes Frequency for age')
plt.xlabel('age')
plt.ylabel('Frequency')
plt.show()

import seaborn as sns

plt.figure(figsize=(8,8))
sns.heatmap(data.corr(),annot=True,fmt='.1f')
plt.show()#