#!/usr/bin/python3

from aoctools import InputReader

# get the input and parse it
input = InputReader.strings('./input/08.txt')
grid = [[int(c) for c in list(line)] for line in input]

def check_visible(grid, x, y, direction='DEFAULT', orig_val=-1, c=0):
    if direction == 'DEFAULT':
        up =    check_visible(grid, x, y, 'u', grid[y][x])
        down =  check_visible(grid, x, y, 'd', grid[y][x])
        left =  check_visible(grid, x, y, 'l', grid[y][x])
        right = check_visible(grid, x, y, 'r', grid[y][x])
        return up[0] or down[0] or left[0] or right[0], up[1] * down[1] * left[1] * right[1]

    if x == 0 or x == len(grid[y]) - 1 or y == 0 or y == len(grid) - 1:
        return True, c

    if direction == 'u':
        return check_visible(grid, x, y - 1, 'u', orig_val, c + 1) if orig_val > grid[y - 1][x] else (False, c + 1)

    if direction == 'd':
        return check_visible(grid, x, y + 1, 'd', orig_val, c + 1) if orig_val > grid[y + 1][x] else (False, c + 1)

    if direction == 'l':
        return check_visible(grid, x - 1, y, 'l', orig_val, c + 1) if orig_val > grid[y][x - 1] else (False, c + 1)

    if direction == 'r':
        return check_visible(grid, x + 1, y, 'r', orig_val, c + 1) if orig_val > grid[y][x + 1] else (False, c + 1)

views = []
for row in range(0, len(grid)):
    for col in range(0, len(grid)):
        res = check_visible(grid, col, row)
        if res[0]:
            views.append(res[1])

print('Part 1:', len(views))
print('Part 2:', max(views))
