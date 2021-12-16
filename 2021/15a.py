#!/usr/bin/python3

from aoctools import InputReader

# FYI: This is just my simple, own implementation of the Dijkstra's algorithm for practice. I didn't know the algorithm before.
# All steps are explained here: https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Algorithm

# get the input and parse it
input = [[int(n) for n in i] for i in InputReader.strings('./input/15.txt')]

class Node:
    def __init__(self, cost, y, x):
        self.x = x
        self.y = y
        self.cost = cost
        self.cost_sum = float('inf')

# 1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
nodes = []
for y in range(0, len(input)):
    for x in range(0, len(input[y])):
        nodes.append(Node(input[y][x], y, x))
unvisited_set = nodes

# 2. Set the initial node as current. Assign to every node a tentative distance value: 
#    set it to zero for our initial node and to infinity for all other nodes.
#    [-> infinity is set as default in Node class constructor]
current_node = nodes[0]
current_node.cost_sum, current_node.cost = 0, 0

while True:
    y, x = current_node.y, current_node.x 

    # 3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
    for [neighbor_y, neighbor_x] in [[y+1, x], [y, x+1], [y-1, x], [y, x-1]]:
        if neighbor_y < len(input) and neighbor_x < len(input[0]) and neighbor_x >= 0 and neighbor_y >= 0:
            # check if neighbour is unvisited
            if(len([n for n in unvisited_set if n.x == neighbor_x and n.y == neighbor_y]) < 1): continue

            neighbor_node = [n for n in unvisited_set if n.x == neighbor_x and n.y == neighbor_y][0]

            # Compare the newly calculated tentative distance to the current assigned value and assign the smaller one
            new_cost_sum = neighbor_node.cost + current_node.cost_sum
            if neighbor_node.cost_sum > new_cost_sum: neighbor_node.cost_sum = new_cost_sum
    
    # 4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it 
    #    from the unvisited set. A visited node will never be checked again.
    unvisited_set.remove(current_node)

    # 5. If the destination node has been marked visited (when planning a route between two specific nodes) [...], then stop. The algorithm
    #    has finished.
    if current_node.y == len(input) - 1 and current_node.x == len(input[0]) - 1: break
    
    # 6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, 
    #    and go back to step 3.
    current_node = unvisited_set[[node.cost_sum for node in unvisited_set].index(min([node.cost_sum for node in unvisited_set]))]

# print the result
print(current_node.cost_sum) # 741