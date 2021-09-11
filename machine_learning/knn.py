import os
import math
import csv
import random
os.system('clear')

def return_distance(a,b):
    squares = [(a[i]-b[i])**2 for i in range(len(a))]
    return math.sqrt(sum(squares))

data = list(csv.reader(open("ml_from_scratch/seeds.csv"), quoting=csv.QUOTE_NONNUMERIC))
random.shuffle(data)

training = data[:int(0.8*len(data))]
test = data[int(0.8*len(data)):]

labels = [row[-1] for row in training]
unique_labels = list(set(labels))

k = 7

def predict(input_):
    distances = [return_distance(input_,point) for point in training]
    nearest_labels = [label for _, label in sorted(zip(distances, labels))][:k]

    class_votes = [nearest_labels.count(class_) for class_ in unique_labels]

    regression = sum(nearest_labels)/k
    classification = unique_labels[class_votes.index(max(class_votes))]
    return [regression,classification]

def evaluate(test):
    regression_error = 0
    true,false = 0,0
    for input_ in test:
        regression,classification = predict(input_)
        regression_error += regression - input_[-1]
        if classification == input_[-1]: true += 1
        else: false += 1
        print(regression,classification,input_[-1])
    return [regression_error,true,false]

regression_error,true,false = evaluate(test)
average_regression_error = regression_error/len(test)
print(regression_error,average_regression_error)

print(true,false,true/(true+false))