#code not complete
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
from icecream import ic

dirname = os.path.dirname(__file__)
ic(dirname)

dataset = pd.read_csv(os.path.join(dirname,'iris_dataset.csv'),delimiter=',')
ic(dataset.shape)
ic(dataset.dtypes)

ic(dataset.head())

dataset = dataset.apply(pd.to_numeric)

ic(dataset.head())