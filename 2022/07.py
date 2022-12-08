#!/usr/bin/python3

from aoctools import InputReader

input = InputReader.strings('./input/07.txt')

class Node(object):
    def __init__(self, data, is_directory, size=0):
        self.data = data
        self.is_directory = is_directory
        self.size = size
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

# prints the whole tree recursively
def print_tree(node, indent=''):
    print(indent + '- ' + node.data + ' ' + ('(dir, ' if node.is_directory else '(file, ') + 'size=' + str(node.size) + ')') 
    for item in node.children:
        print_tree(item, indent + '  ')

# sums the directory sizes within the tree recursively
def sum_tree(node):
    for item in node.children:
        item = sum_tree(item)
    if node.is_directory:
        node.size = sum([e.size for e in node.children])
    return node

# parse the input into a tree
tree = Node('/', True)
currNode, prevNodes = tree, []
for line in input:
    if line == '$ cd /':
        continue
    elif line.startswith('$') and 'cd ..' in line:
        currNode = prevNodes.pop()
    elif line.startswith('$') and 'cd' in line:
        prevNodes.append(currNode)
        currNode = [c for c in currNode.children if c.data.split()[1] == line.split()[2]][0]
    elif line.startswith('dir'):
        currNode.add_child(Node(line, True))
    elif not(line.startswith('$') and 'ls' in line):
        currNode.add_child(Node(line, False, int(line.split()[0])))

# sum the directory sizes within the tree and print the whole tree
tree = sum_tree(tree)
print_tree(tree)

def part1(node, results=[]):
    if node.is_directory and node.size < 100000:
        results.append(node)
    for item in node.children:
        results = part1(item, results)
    return results

print('\nPart 1:', sum([i.size for i in part1(tree)]))

# part 2
TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000

def part2(node, results=[], free_space=None):
    if free_space == None:
        free_space = TOTAL_DISK_SPACE - node.size
    if node.is_directory and (free_space + node.size) >= REQUIRED_UNUSED_SPACE:
        results.append(node)
    for item in node.children:
        results = part2(item, results, free_space)
    return results

print('Part 2:', min([i.size for i in part2(tree)]))
