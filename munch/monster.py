#!/usr/bin/bash python3

from random import randint
import item

def fight(player):

    mlvl = randint(1,20)
    plvl = player.level
    ilvl = player.head + player.body + player.hand + player.leg + player.foot + player.left + player.right
    lvl = plvl + ilvl

    print('Monster Level: ' + str(mlvl))
    print('Your Level: ' + str(plvl + ilvl) + '(Level: ' + str(plvl) + ' + Power: ' + str(ilvl) + ')')

    action = input("(F)ight or (R)un")

    if action.lower() == 'f':
        if lvl >= mlvl: 
            print("You win!")
            input("Reward: Level +1")
            player.level += 1
            item.getitem(player, 1, 2, 3, 4, 5)            

        else:
            print("You lost....")
            input("Lost a Level! (Current level: " + str(player.level - 1) + ")")
            player.level -= 1

    if action.lower() == 'r':
        run = randint(1,6)

        if run == 5 or run == 6:
            print("Failed to run!")
            input("Lost a Level! (Current level: " + str(player.level - 1) + ")")
            player.level -= 1

        else:
            input("You ran away!")

    return

def win(player):

    if player.level >= 12:
        input(player.name + " has won!")

    elif player.level <= 0:
        input(player.name + " has died!")

