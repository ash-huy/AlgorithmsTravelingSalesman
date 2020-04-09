import sys
import time
from turtle import *
import random

# Reference and algorithm help for code: courtesy of geeksforgeeks.org
def travellingSalesmanAlgo(graph):
    # this will cover vertices we need to visit
    vertices = []

    # in this loop, we'll add basically every index of vertices that isn't the first one to vertices
    # this denotes the ones we need to visit
    for i in range(len(graph[0])): 
        if i != 0: 
            vertices.append(i) 

    # make this some crazy arbitrarily large # - in our case
    # we can use maxsize, represents the maximum value
    # representable by a signed word (is equal to 9223372036854775807)
    min_path = sys.maxsize
  
    while True: # infinite loop, only cancelled out if there are no permutations found next
        current_pathweight = 0
        index = 0

        # loop through each datapoint and explore
        for i in range(len(vertices)): 
            # the current path equals the index in the vertex we're at
            current_pathweight += graph[index][vertices[i]] 
            # then assign index to whatever vertices we're currently on
            index = vertices[i]

        # add the current index to our current pathweight -
        # basically going through and trying to keep track of the various paths
        current_pathweight += graph[index][0]

        # get the minimum 
        min_path = min(min_path, current_pathweight)
        
        # if the vertices do not have another permutation, then break this
        if not next_permutation(vertices): 
           break
  
    return min_path 

# see if the given vertices have another permutation
def next_permutation(vertices): 
  
    vertices_length = len(vertices)
    i = vertices_length - 2

    while i >= 0 and vertices[i] >= vertices[i + 1]: 
        i -= 1
  
    if i == -1: 
        return False
  
    j = i + 1

    while j < vertices_length and vertices[j] > vertices[i]: 
        j += 1

    # subtract the value of j
    j = j - 1
  
    vertices[i], vertices[j] = vertices[j], vertices[i] 
  
    left_vertex = i + 1
    right_vertex = vertices_length - 1
  
    while left_vertex < right_vertex: 
        vertices[left_vertex], vertices[right_vertex] = vertices[right_vertex], vertices[left_vertex] 
        left_vertex += 1
        right_vertex -= 1
  
    return True

start_time = time.time()
graph = [[0, 10, 15, 20, 15, 11, 25],
[10, 0, 11, 15, 11, 20, 25],
[11, 15, 0, 10, 20, 35, 25],
[10, 11, 15, 0, 20, 5, 6],
[11, 10, 25, 35, 0, 35, 11],
[35, 10, 15, 20, 11, 0, 14],
[11, 10, 25, 35, 25, 35, 0]]
# manually input some matrices here
print("number of nodes:" ),len(graph)
print("min weight:" ),travellingSalesmanAlgo(graph)
print("time took to run:"), (time.time() - start_time)