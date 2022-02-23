import random
import math
import csv
import os

def load_csv_raw(filename):
	file = open(filename, 'r')
	return list(csv.reader(file))

def load_csv(filename):
	dataset = []
	file = open(filename, 'r')
	for row in csv.reader(file):
		if row: dataset.append(row)		
	return dataset

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = list(dict.fromkeys(class_values))
    labels = {}
    for i,value in enumerate(unique):
        labels[value] = i
    for row in dataset:
        row[column] = labels[row[column]]

def delete_column(dataset,column):
	for row in dataset:
		del row[column]

def delete_columns(dataset,*columns):
    for row in dataset:
        for i, column in enumerate(columns):
            del row[column - i]

def delete_row(dataset,row):
	del dataset[row]

def delete_null(dataset):
	dataset[:] = [row for row in dataset if all(row)]			

def dataset_minmax(dataset):
	stats = [[min(column), max(column)] for column in zip(*dataset)]
	return stats

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)-1):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = []
	dataset_copy = dataset.copy()
	fold_size = int(len(dataset) / n_folds)
	print('fold size =',fold_size)
	print(n_folds,'folds')
	for i in range(n_folds):
		fold = []
		while len(fold) < fold_size:
			index = random.randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split


#=================================================================


# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = []
	hidden_layer = [{'weights':[random.random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random.random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + math.e ** -activation)

# Forward propagate input to a network output
def forward_propagate(network, row):  
	inputs = row 
	for layer in network: 
		outputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs) 
			neuron['output'] = transfer(activation) 
			outputs.append(neuron['output']) 
		inputs = outputs 
	return outputs

# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network,expected):
	for i,layer in reversed(list(enumerate(network))):
		errors = []
		#output layer
		if i == len(network)-1:
			for j,neuron in enumerate(layer):
				errors.append(expected[j] - neuron['output'])
		#hidden layer
		else:
			for k in range(len(layer)):
				error = 0
				for neuron in network[i+1]:
					error += neuron['weights'][k] * neuron['delta']
				errors.append(error)
		for neuron,error in zip(layer,errors):
			neuron['delta'] = error * transfer_derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1] 
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

# Train network + show error
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		if epoch == 0 or (epoch + 1) % 100 == 0: 
			print('epoch', str(epoch).rjust(3,'0'), 'error', str(round(error,4)).ljust(7,'0'), 'error/sample', str(round(error/len(train),4)))
	print()	
		
# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, test, l_rate, n_epoch, n_hidden):
	n_inputs, n_outputs = len(train[0]) - 1, len({row[-1] for row in train})
	network = initialize_network(n_inputs, n_hidden, n_outputs)
	train_network(network, train, l_rate, n_epoch, n_outputs)
	return network

# Evaluate an algorithm using a k-fold cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	accuracy_scores = []
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, []) 
		test_set = []
		for row in fold:
			# test_set.append(row)
			row_copy = row.copy() 
			test_set.append(row_copy)
			row_copy[-1] = None
		network = algorithm(train_set, test_set, *args)
		predicted = [predict(network,row) for row in test_set]
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		accuracy_scores.append(accuracy)
	accuracy_scores = [round(score,5) for score in accuracy_scores]
	return accuracy_scores

# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

#=================================================================


# load CSV file data
filename_end = '/heart.csv'
filename = os.path.dirname(__file__) + filename_end
dataset = load_csv(filename)

print('\ndataset =', filename_end)
print('len(dataset) =', len(dataset))

delete_null(dataset)
delete_row(dataset,0)

dataset = dataset[:int(1 * len(dataset))]
random.shuffle(dataset)

for i in range(len(dataset[0])):
	try: str_column_to_float(dataset, i)
	except: str_column_to_int(dataset, i)

str_column_to_int(dataset, len(dataset[0])-1)

minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)


#=================================================================


# evaluate algorithm w/ k-fold cross validation
n_folds = 3
l_rate = 0.3
n_epoch = 500
n_hidden = 5
scores = evaluate_algorithm(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)
print('Scores: {}'.format(scores))
print('Mean Accuracy: {}'.format(round(sum(scores)/len(scores),4)))

print()

#=================================================================


#evaluate algorithm w/ train + test dataset
train = dataset[:int(0.8 * len(dataset))]
test = dataset[int(0.8 * len(dataset)):]

#initialize and train network
n_inputs, n_outputs = len(train[0]) - 1, len({row[-1] for row in train})
network = initialize_network(n_inputs, n_hidden, n_outputs)
train_network(network, train, l_rate, n_epoch, n_outputs)

#evaluate network accuracy
predictions = [predict(network,row) for row in test]
actual = [row[-1] for row in test]

evaluation = accuracy_metric(actual, predictions)
print('manual evaluation = {}'.format(round(evaluation,4)),'\n')
print(actual[:30])
print(predictions[:30])

#=================================================================

#visually inspect outputs
for row in test[:10]:
	inputs, expected = row[:-1], row[-1]
	outputs = forward_propagate(network,inputs)
	outputs = [round(output,5) for output in outputs]
	prediction = predict(network,inputs)
	print(outputs, expected, prediction)
