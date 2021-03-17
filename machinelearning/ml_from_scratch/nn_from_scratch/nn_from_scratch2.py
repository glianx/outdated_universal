# neural network with multiple hidden layers
# code not complete
# check out nn_from_scratch.py for my highly optimized code

from random import seed
from random import random
from math import exp
from icecream import ic

# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
  network = list()
  for n_hidden_layer in n_hidden:
      hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden_layer)]
      network.append(hidden_layer)
  output_layer = [{'weights':[random() for i in range(n_hidden_layer + 1)]} for i in range(n_outputs)]
  network.append(output_layer)
  return network

# network = initialize_network(1,[2,1,2,2],3)
# for layer in network:
#     ic(layer)

def initialize_network2(*layers):
    network = []
    for i,n_hidden_layer in enumerate(layers[1:-1]):
        # ic(n_hidden_layer)
        hidden_layer = [{'weights':[inputs for inputs in range(layers[i-1]+1)]} for neuron in range(n_hidden_layer)]
        # ic(hidden_layer)
        network.append(hidden_layer) 
    output_layer = [{'weights':[inputs for inputs in range(layers[-2]+1)]} for neuron in range(layers[-1])]
    # ic(output_layer)
    network.append(output_layer)
    return network

network = initialize_network2(1,2,3,4,5,6)
for layer in network:
    ic(layer)

# def func(*args):
#     ic(args,len(args),args[0])
#     for arg in args:
#         ic(arg**2)
# func(0,1,2,3,4)

