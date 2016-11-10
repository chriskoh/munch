#!/usr/bin/env python3

class newplayer:

    level = 1

    head = 0
    body = 0
    hand = 0
    leg = 0
    foot = 0
    left = 0
    right = 0

    def __init__(self, name):
        self.name = name

def addplayers():

    players = []

    while True:
        check = input('Add player? (Y/N)')

        if check.lower() == 'y':
            name = input('Player Name: ')
            players.append(newplayer(name))

        elif check.lower() == 'n':
            done = input('Start Game? (Y/N)')

            if done.lower() == 'y':
                return players

