#!/usr/bin/python3

import re
from inputreader import InputReader

lines = InputReader.strings("./input/4.txt")

def number_string_to_int_list(input, seperator = " "):
    return list(map(int, [a for a in input.split(seperator) if not a == ""]))

def mark_numbers_on_board(board, number):
    for i in range(0, len(board)):
        for t in range(0, len(board[i])):
            if(board[i][t] == number):
                board[i][t] = [board[i][t], True]
    return board

def check_if_board_won_horizontal(board):
    for i in range(0, len(board)):
        won = False
        for t in range(0, len(board[i])):
            if(type(board[i][t]) is list):
                won = True
            else:
                won = False
                break
        if(won):
            return True
    return False

def check_if_board_won_vertical(board):
    for t in range(0, len(board[0])):
        won = False
        for i in range(0, len(board)):
            if(type(board[i][t]) is list):
                won = True
            else:
                won = False
                break
        if(won):
            return True
    return False

def calc_score_for_board(board, number):
    unmarked_sum = 0
    # get the sum of unmarked numbers
    for i in range(0, len(board)):
        for t in range(0, len(board[i])):
            if(not type(board[i][t]) is list):
                unmarked_sum += board[i][t]
    # calc the score of the board and return it
    return unmarked_sum * number

numbers = number_string_to_int_list(lines[0], ",")
boards = []

# parse the board input
i = 2
while(i <= len(lines)):
    temp = []
    for t in range(i, i+5):
        temp.append(number_string_to_int_list(lines[t]))
    boards.append(temp)
    i += 6

# play the bingo
for number in numbers:
    for board in boards:
        board = mark_numbers_on_board(board, number)
        if(check_if_board_won_horizontal(board) or check_if_board_won_vertical(board)):
            print(calc_score_for_board(board, number))
            quit()
        
