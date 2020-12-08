#!/usr/bin/python3

import string

class Instruction:
    def __init__(self, command, value, index):
        self.executed = False
        self.value = value
        self.command = command
        self.index = index

    def setExecuted(self):
        self.executed = True

    def getCommand(self):
        return self.command

    def getExecuted(self):
        return self.executed

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

def execute(instruction):
    currentIndex = instruction.getIndex()

    if(instruction.getExecuted()):
        raise StopIteration("Instruction was already executed.")

    instruction.setExecuted()

    if (instruction.getCommand() == 'nop'):
        return [0, currentIndex + 1]

    elif(instruction.getCommand() == 'acc'):
        return [instruction.getValue(), currentIndex + 1]

    elif(instruction.getCommand() == 'jmp'):
        currentIndex = currentIndex + int(instruction.getValue())
        return [0, currentIndex]

    else:
        raise RuntimeError("Unknown instruction.")

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

instructions = []
index = 0
for line in lines:
    words = line.split()
    instructions.append(Instruction(words[0], int(words[1]), index))
    index += 1

accumulator = 0
nextIndex = 0

try:
    while True:
        instruction = instructions[nextIndex]
        #print(str(instruction.getIndex()) + '  ' + instruction.getCommand() + '  ' +  str(instruction.getValue()))
        [increase, nextIndex] = execute(instruction)
        accumulator += increase

except StopIteration: 
    pass

print('Accumulator is: ' + str(accumulator))