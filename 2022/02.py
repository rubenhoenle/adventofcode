#!/usr/bin/python3

from aoctools import InputReader
from enum import Enum

class EnemyShape(str, Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class MyShape(str, Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'

class RoundEnding(str, Enum):
    LOOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'

class ShapeScores(str, Enum):
    A = 1,
    X = 1,
    B = 2,
    Y = 2,
    C = 3,
    Z = 3

class ScoreForSelectedShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def part1(enemy, my):
    # draw
    if((enemy == EnemyShape.ROCK and my == MyShape.ROCK) or (enemy == EnemyShape.PAPER and my == MyShape.PAPER) or (enemy == EnemyShape.SCISSORS and my == MyShape.SCISSORS)):
        return 3
    # lost
    elif((enemy == EnemyShape.ROCK and my == MyShape.SCISSORS) or (enemy == EnemyShape.SCISSORS and my == MyShape.PAPER) or (enemy == EnemyShape.PAPER and my == MyShape.ROCK)):
        return 0
    # won
    else:
        return 6

def part2(enemy, result):
    # loose
    if(result == RoundEnding.LOOSE):
        if(enemy == EnemyShape.ROCK):
            return ScoreForSelectedShape.SCISSORS.value
        elif(enemy == EnemyShape.PAPER):
            return ScoreForSelectedShape.ROCK.value
        else:
            return ScoreForSelectedShape.PAPER.value
    # draw
    elif(result == RoundEnding.DRAW):
        if(enemy == EnemyShape.ROCK):
            return ScoreForSelectedShape.ROCK.value
        elif(enemy == EnemyShape.PAPER):
            return ScoreForSelectedShape.PAPER.value
        else:
            return ScoreForSelectedShape.SCISSORS.value
    # win
    else:
        if(enemy == EnemyShape.ROCK):
            return ScoreForSelectedShape.PAPER.value
        elif(enemy == EnemyShape.PAPER):
            return ScoreForSelectedShape.SCISSORS.value
        else:
            return ScoreForSelectedShape.ROCK.value



# get the input
input = InputReader.strings('./input/02.txt')

# part 1
totalScore = 0
for line in input:
    arr = line.split()
    roundScore = part1(arr[0], arr[1])
    shapeScore = int(ShapeScores[arr[1]].value)
    totalScore += shapeScore + roundScore

print('Part 1:', totalScore)

# part 2
totalScore = 0
for line in input:
    arr = line.split()
    shapeScore = part2(arr[0], arr[1])
    roundScore = 0
    if(arr[1] == RoundEnding.DRAW): roundScore = 3
    elif(arr[1] == RoundEnding.WIN): roundScore = 6
    totalScore += shapeScore + roundScore

print('Part 2:', totalScore)