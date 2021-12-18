#!/usr/bin/python3

from aoctools import InputReader
import re

# get the input
input = InputReader.strings('./input/17.txt')[0]

# parse the input
values = re.findall('target area: x=(-?\d+..-?\d+), y=(-?\d+..-?\d+)', input)[0]

x_values = list(map(int, re.findall('(-?\d+)..(-?\d+)', values[0])[0]))
x_start, x_end = min(x_values), max(x_values)

y_values = list(map(int, re.findall('(-?\d+)..(-?\d+)', values[1])[0]))
y_start, y_end = min(y_values), max(y_values)

x_target_area_values = [x for x in range(x_start, x_end + 1, 1 if x_start < x_end else -1)]
y_target_area_values = [y for y in range(y_start, y_end + 1, 1 if y_start < y_end else -1)]

count_part_2 = 0
overall_probe_y_history = []
for count_y in range(y_start, 250):
    for count_x in range(0, 250):
        y_velocity = count_y
        x_velocity = count_x
        probe_y, probe_x = 0, 0
        probe_y_history = []
        for step in range(0, 1000):
            # The probe's x position increases by its x velocity.
            probe_x += x_velocity

            # The probe's y position increases by its y velocity.
            probe_y += y_velocity
            probe_y_history.append(probe_y)

            # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is: 
            #   - it decreases by 1 if it is greater than 0, 
            #   - increases by 1 if it is less than 0,
            #   - or does not change if it is already 0.
            if x_velocity > 0:
                x_velocity -= 1
            elif x_velocity < 0:
                x_velocity += 1

            # Due to gravity, the probe's y velocity decreases by 1.
            y_velocity -= 1

            # check if the probe is whithin the target area after this step
            if probe_y in y_target_area_values and probe_x in x_target_area_values:
                #print(count_x, count_y)
                overall_probe_y_history.append(max(probe_y_history))
                count_part_2 += 1
                break

            # check if the target area was missed already to avoid unnecessary steps
            if probe_y < min(y_target_area_values) or probe_x > max(x_target_area_values):
                break

print('Part 1: ' + str(max(overall_probe_y_history))) #12246
print('Part 2: ' + str(count_part_2)) # 3528