#!/usr/bin/python3

from aoctools import InputReader


class Player:
    total_score = 0
    space = 0
    name = ''

    def __init__(self, starting_space, name):
        self.space = starting_space
        self.name = name

    def increment_space(self, incr: int):
        for _ in range(0, incr):
            self.space += 1
            if self.space > 10:
                self.space = self.space % 10


# get the input
player1 = Player(int(InputReader.strings('./input/21.txt')[0].split(' ').pop()), 'player1')
player2 = Player(int(InputReader.strings('./input/21.txt')[1].split(' ').pop()), 'player2')

die, die_roll_counter = 1, 0
while True:
    for player in [player1, player2]:
        sum = 0
        # roll the die three times
        for i in range(0, 3):
            die_roll_counter += 1
            sum += die
            die += 1
            if die > 100:
                die = 1

        # add the scores of the player
        player.increment_space(sum)
        player.total_score += player.space

        # check if the player has won
        if player.total_score >= 1000:
            loosing_player = [p for p in [player1, player2] if p.name != player.name][0]
            print(loosing_player.total_score * die_roll_counter)  # 921585
            quit()
