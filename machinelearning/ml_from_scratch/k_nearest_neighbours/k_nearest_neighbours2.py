import os
import math
import csv
# return Euclidean distance
def return_distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i]-b[i])**2
    return math.sqrt(sum)

def insert_distances(inputs,dataset):
    for row in dataset:
        distance = return_distance(inputs, row[:-1])
        row.insert(0,distance)

def sort_distances(dataset):
    dataset.sort()

def k_nearest_neighbours(k,dataset):
    k_nearest = []
    for row in dataset[:k]:
        k_nearest.append(row[-1])
    unique_labels = set(k_nearest) 
    label_frequencies = [[k_nearest.count(label), label] for label in unique_labels]
    label_frequencies.sort()
    label_frequencies.reverse()
    print('label frequencies:', label_frequencies)c
    return label_frequencies[0][1]


dataset = [[66.0, 1.0, 0.0, 160.0, 228.0, 0.0, 0.0, 138.0, 0.0, 2.3, 2.0, 0.0, 1.0, 0],
[71.0, 0.0, 0.0, 112.0, 149.0, 0.0, 1.0, 125.0, 0.0, 1.6, 1.0, 0.0, 2.0, 0],
[64.0, 1.0, 3.0, 170.0, 227.0, 0.0, 0.0, 155.0, 0.0, 0.6, 1.0, 0.0, 3.0, 0],
[66.0, 0.0, 2.0, 146.0, 278.0, 0.0, 0.0, 152.0, 0.0, 0.0, 1.0, 1.0, 2.0, 0],
[39.0, 0.0, 2.0, 138.0, 220.0, 0.0, 1.0, 152.0, 0.0, 0.0, 1.0, 0.0, 2.0, 0],
[60.0, 1.0, 0.0, 117.0, 230.0, 1.0, 1.0, 160.0, 1.0, 1.4, 2.0, 2.0, 3.0, 1],
[64.0, 1.0, 2.0, 140.0, 335.0, 0.0, 1.0, 158.0, 0.0, 0.0, 2.0, 0.0, 2.0, 1],
[43.0, 1.0, 0.0, 120.0, 177.0, 0.0, 0.0, 120.0, 1.0, 2.5, 1.0, 0.0, 3.0, 1],
[57.0, 1.0, 0.0, 150.0, 276.0, 0.0, 0.0, 112.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1],
[55.0, 1.0, 0.0, 132.0, 353.0, 0.0, 1.0, 132.0, 1.0, 1.2, 1.0, 1.0, 3.0, 1]]

len_inputs = len(dataset[0])-1
row = [71.0, 0.0, 0.0, 112.0, 149.0, 0.0, 1.0, 125.0, 0.0, 1.6, 1.0, 0.0, 2.0, 0]
inputs = row[:-1]
# insert_distances([0 for x in range(len_inputs)], dataset)
insert_distances(inputs, dataset)

print('distances inserted')
# for row in dataset[:10]:
#     print(row)
sort_distances(dataset)

print('distances sorted')
# for row in dataset[:10]:
#     print(row)

prediction = k_nearest_neighbours(5,dataset)
print(prediction)