#!/usr/bin/python3

from enum import Enum

# Author: Ruben Hönle
# Collection of some tools I'm using for the adventofcode.com challenges.

class Part(Enum):
    ONE = 1
    TWO = 2

class InputReader:
    @staticmethod
    def strings(filename):
        with open(filename) as inputFile:
            return [line.rstrip() for line in inputFile.readlines()]
    
    @staticmethod
    def integers(filename):
        with open(filename) as inputFile:
            return list(map(int, inputFile.readlines()))

    @staticmethod
    def integers_in_first_line(filename):
        return list(map(int, InputReader.strings(filename)[0].split(",")))