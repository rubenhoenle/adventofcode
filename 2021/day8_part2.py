#!/usr/bin/python3

from aoctools import InputReader

class SignalPattern: A = ''; B = ''; C = ''; D = ''; E = ''; F = ''; G = ''
class Digit: ONE = 2; FOUR = 4; SEVEN = 3; EIGHT = 7
digits = [Digit.ONE, Digit.FOUR, Digit.SEVEN, Digit.EIGHT]
switch_digits={Digit.ONE: 1, Digit.FOUR: 4, Digit.SEVEN: 7, Digit.EIGHT: 8}

def count(arr, c): return len([a for a in arr if c in a])

sum = 0
for line in InputReader.strings('./input/8.txt'):
    output_values = [''.join(sorted(v)) for v in line.split('|')[1].split(' ') if len(v)]
    input_signal_patterns = [''.join(sorted(v)) for v in line.split('|')[0].split(' ') if len(v)]
    signal_patterns = ['', '', '', '', '', '', '', '', 'abcdefg', '']

    #        A
    #     -------
    #  B |       | C
    #    |   D   |
    #     -------
    #  E |       | F
    #    |       |
    #     -------
    #        G

    for p in signal_patterns:
        for val in [v for v in input_signal_patterns if len(v) in digits]:
            signal_patterns[switch_digits.get(len(val))] = val

    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if c in signal_patterns[7] and c not in signal_patterns[1]:
            SignalPattern.A = c
        elif count(input_signal_patterns, c) == 6:
            SignalPattern.B = c
        elif count(input_signal_patterns, c) == 8:
            SignalPattern.C = c
        elif count(input_signal_patterns, c) == 4:
            SignalPattern.E = c
        elif count(input_signal_patterns, c) == 9:
            SignalPattern.F = c
        elif c in signal_patterns[8] and c not in signal_patterns[4]:
            SignalPattern.G = c
        else:
            SignalPattern.D = c

    switch_patterns={
       0: SignalPattern.A + SignalPattern.B + SignalPattern.C + SignalPattern.E + SignalPattern.F + SignalPattern.G,
       2: SignalPattern.A + SignalPattern.C + SignalPattern.D + SignalPattern.E + SignalPattern.G,
       3: SignalPattern.A + SignalPattern.C + SignalPattern.D + SignalPattern.F + SignalPattern.G,
       5: SignalPattern.A + SignalPattern.B + SignalPattern.D + SignalPattern.F + SignalPattern.G,
       6: SignalPattern.A + SignalPattern.B + SignalPattern.D + SignalPattern.E + SignalPattern.F + SignalPattern.G,
       9: SignalPattern.A + SignalPattern.B + SignalPattern.C + SignalPattern.D + SignalPattern.F + SignalPattern.G
    }

    for i in range(0, len(signal_patterns)):
        if not signal_patterns[i]: signal_patterns[i] = ''.join(sorted(switch_patterns.get(i)))

    number = ''
    for val in output_values:
        number += str(signal_patterns.index(val))
    sum += int(number)

print(sum) #908067