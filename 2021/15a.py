#!/usr/bin/python3

from aoctools import InputReader

# get the input and parse it
input = [[int(n) for n in i] for i in InputReader.strings('./input/15.txt')]

class Node:
    def __init__(self, cost, y, x):
        self.x = x
        self.y = y
        self.cost = cost
        self.cost_sum = float('inf')

nodes = []
for y in range(0, len(input)):
    for x in range(0, len(input[y])):
        nodes.append(Node(input[y][x], y, x))
unvisited_set = nodes

current_node = nodes[0]
current_node.cost_sum, current_node.cost = 0, 0

target_node = [n for n in nodes if n.y == len(input) - 1 and n.x == len(input[0]) - 1][0]

while True:
    y, x = current_node.y, current_node.x 
    for [neighbor_y, neighbor_x] in [[y+1, x], [y, x+1], [y-1, x], [y, x-1]]:
        if neighbor_y < len(input) and neighbor_x < len(input[0]) and neighbor_x >= 0 and neighbor_y >= 0:
            if(len([n for n in unvisited_set if n.x == neighbor_x and n.y == neighbor_y]) < 1): continue
            neighbor_node = [n for n in unvisited_set if n.x == neighbor_x and n.y == neighbor_y][0]
            new_cost_sum = neighbor_node.cost + current_node.cost_sum
            if neighbor_node.cost_sum > new_cost_sum: neighbor_node.cost_sum = new_cost_sum
    
    unvisited_set.remove(current_node)

    if current_node.x == target_node.x and current_node.y == target_node.y: break
    
    current_node = unvisited_set[[node.cost_sum for node in unvisited_set].index(min([node.cost_sum for node in unvisited_set]))]

print(current_node.cost_sum) # 741