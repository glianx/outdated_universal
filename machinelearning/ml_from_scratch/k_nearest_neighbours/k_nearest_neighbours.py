import os
import math
import csv
import random

def return_distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i]-b[i])**2
    return math.sqrt(sum)

def insert_distances(inputs,dataset):
    for row in dataset:
        distance = return_distance(inputs, row[:-1])
        row.insert(0,distance)

def k_nearest_neighbours(k,dataset):
    k_nearest = []
    for row in dataset[:k]:
        k_nearest.append(row[-1])
    unique_labels = set(k_nearest) 
    label_frequencies = [[k_nearest.count(label), label] for label in unique_labels]
    label_frequencies.sort()
    label_frequencies.reverse()
    print('label frequencies:', label_frequencies)
    return label_frequencies[0][1]

def accuracy(k, test, train):
    score = 0
    for row in test:
        print(row[-1])
        inputs = row[:-1]
        insert_distances(inputs, train)
        train.sort()
        prediction = k_nearest_neighbours(k,train)
        if prediction == row[-1]:
            score += 1
    return score/len(test)

# Load a CSV file raw
def load_csv_raw(filename):
	file = open(filename, 'r')
	return list(csv.reader(file))

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = list(dict.fromkeys(class_values))
    labels = {}
    for i,value in enumerate(unique):
        labels[value] = i
    print(labels)
    for row in dataset:
        row[column] = labels[row[column]]

filename = os.path.dirname(__file__) + '/heart.csv'
dataset = load_csv_raw(filename)

for i in range(len(dataset[0])):
	try: str_column_to_float(dataset, i)
	except: str_column_to_int(dataset, i)

# convert class column from str/float to int
str_column_to_int(dataset, len(dataset[0])-1)

random.shuffle(dataset)

train = dataset[:int(0.8 * len(dataset))]
test = dataset[int(0.8 * len(dataset)):]

# row = [11, 10, 13, 13, 11, 1]
row = [63,1,3,145,233,1,0,150,0,2.3,0,0,1,1]
inputs = row[:-1]
insert_distances(inputs,train)
train.sort()
prediction = k_nearest_neighbours(10,train)
print('prediction: ', prediction)
print('accuracy:',accuracy(20,test,train))