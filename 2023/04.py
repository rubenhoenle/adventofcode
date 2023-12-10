#!/usr/bin/python3

import re
from aoctools import InputReader

cards = [card.split(": ")[1] for card in InputReader.strings('./input/04.txt')]

def get_card_points(card: str): 
    winning_numbers = [int(i) for i in card.split(" | ")[0].split()]
    card_numbers = [int(i) for i in card.split(" | ")[1].split()]
    points = 0
    for num in card_numbers:
        if num in winning_numbers and points == 0:
            points = 1
        elif num in winning_numbers:
            points = points * 2
    return points

total_points = 0
for card in cards:
    total_points += get_card_points(card)

print("Part 1:", total_points)

