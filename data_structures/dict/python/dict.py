#dict is a data structure similar to a javascript object, with key: value pairs.
# This is to generate a dictionary with random number of keys with a random number of values for each of them.
# d={a:1, b:2} a and b are keys, 1 and 2 are values. d.a = 1

import random

#function that takes in no. of nodes as argument

def rand_dict_generator (number_of_nodes):
    graph = dict()  #empty dictionary
    for i in range(number_of_nodes):
       graph[i] = random.sample(range(0, number_of_nodes), random.randint(0, number_of_nodes))
    return graph

print(rand_dict_generator(10))
