#!/usr/bin/env python3

from random import randint
import player
import turn
import os

def main():

    os.system('clear')
    players = player.addplayers()

    while len(players) != 0:

        for x in players:
            os.system('clear')
            turn.taketurn(x)            

if __name__ == "__main__":
    main()
