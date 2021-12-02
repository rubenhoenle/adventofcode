#!/usr/bin/python3

class InputReader:
    @staticmethod
    def strings(filename):
        lines = []
        with open(filename) as inputFile:
            lines = inputFile.readlines()
            lines = [line.rstrip() for line in lines]
        return lines
    
    @staticmethod
    def integers(filename):
        numbers = []
        with open(filename) as inputFile:
            numbers = list(map(int, inputFile.readlines()))
        return numbers