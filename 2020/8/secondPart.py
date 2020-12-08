#!/usr/bin/python3

import string

class Instruction:
    def __init__(self, command, value, index):
        self.executed = False
        self.value = value
        self.command = command
        self.oldCommand = command
        self.index = index

    def setExecuted(self):
        self.executed = True

    def resetExecuted(self):
        self.executed = False

    def getCommand(self):
        return self.command

    def getExecuted(self):
        return self.executed

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

    def swapCommand(self):
        self.oldCommand = self.command
        if (self.command == 'nop'):
            self.command = 'jmp'
        elif (self.command == 'jmp'):
            self.command = 'nop'

    def resetCommand(self):
        self.command = self.oldCommand

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

def check(instructions, index):
    accumulator = 0
    nextIndex = 0

    instructions[index].swapCommand()

    try:
        while True:
            instruction = instructions[nextIndex]
            #print(str(instruction.getIndex()) + '  ' + instruction.getCommand() + '  ' +  str(instruction.getValue()))
            [increase, nextIndex] = execute(instruction)
            accumulator += increase
            if(nextIndex == len(instructions)):
                instructions[index].resetCommand()
                return [True, accumulator]

    except StopIteration: 
        instructions[index].resetCommand()
        return [False, -1]

for i in range(len(instructions)):
    [terminated, accumulator] = check(instructions, i)
    if(terminated):
        print('Accumulator is: ' + str(accumulator))
        break
    for instruction in instructions:
        instruction.resetExecuted()