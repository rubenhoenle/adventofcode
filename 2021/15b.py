#!/usr/bin/python3

from aoctools import InputReader
import heapq

# get the input and parse it
input = [[int(n) for n in i] for i in InputReader.strings('./input/15.txt')]

# define the lengths
len_y, len_x = len(input), len(input[0])
total_len_y, total_len_x = len_y * 5, len_x * 5

def cost_of(y, x):
    return ((input[y % len_y][x % len_x] + int(y / len_y) + int(x / len_x)) - 1) % 9 + 1

visited = [[None] * total_len_x for y in range(0, total_len_y)]
cost = {} 
queue = [(0, 0, 0)]

# convert the iterable into a heap data structure
heapq.heapify(queue)

while len(queue) > 0:
    # remove and return the smallest element from heap (the order is adjusted, so as heap structure is maintained)
    current_cost, y, x = heapq.heappop(queue)

    if visited[y][x]: continue
    
    visited[y][x] = True
    cost[(y, x)] = current_cost

    # if the destination node was found stop the algorithm
    if y == total_len_y - 1 and x == total_len_x - 1: break

    for neighbor_y, neighbor_x in [[y+1, x], [y, x+1], [y-1, x], [y, x-1]]:
        if (0 <= neighbor_y < total_len_y and 0 <= neighbor_x < total_len_x) and not visited[neighbor_y][neighbor_x]:
            # insert the element mentioned in its arguments into heap (order is adjusted, so as heap structure is maintained)
            heapq.heappush(queue, (current_cost + cost_of(neighbor_y, neighbor_x), neighbor_y, neighbor_x))

print(cost[(total_len_y - 1, total_len_x - 1)])  # 2976