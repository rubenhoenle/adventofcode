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

print("Part 1:", sum([get_card_points(card) for card in cards])) 

def get_count_matching_numbers(card: str): 
    winning_numbers = [int(i) for i in card.split(" | ")[0].split()]
    card_numbers = [int(i) for i in card.split(" | ")[1].split()]
    return len([1 for num in card_numbers if num in winning_numbers])

count = [1 for card in cards]
for i in range(0, len(cards)):
    copies = get_count_matching_numbers(cards[i])
    for t in range(i, i+copies):
        count[t+1] += count[i]

print("Part 2:", sum(count))

