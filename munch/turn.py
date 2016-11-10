#!/usr/bin/env python3

import draw
import monster
import item

def taketurn(player):

    while player.level > -10:
        print(player.name + "'s turn!")

        while True:

            action = input('Action: (D)raw, Check (L)evel, Check (I)tem')

            if action.lower() == 'd':
                card = draw.drawcard()
    
                if card == 'Monster':
                    monster.fight(player)
                    monster.win(player)    
                    return

                elif card == 'Item':
                    item.getitem(player, 1, 2, 3, 2, 4)                
                    return

            elif action.lower() == 'l':
                plvl = player.level
                ilvl = player.head + player.body + player.hand + player.leg + player.foot + player.left + player.right

                print("Your level is: " + str(player.level) + '!')
                print("Your Head Gear has " + str(player.head) + "!")
                print("Your Body Gear has " + str(player.body) + "!")
                print("Your Hands Gear has " + str(player.hand) + "!")
                print("Your Leg Gear has " + str(player.leg) + "!")
                print("Your Foot Gear has " + str(player.foot) + "!")
                print("Your Left Hand Gear has " + str(player.left) + "!")
                print("Your Right Hand Gear has " + str(player.right) + "!")
                print("Your total power level is " + str(plvl + ilvl) + "!")
            elif action.lower() == 'i':
                print('TBA')

            else:
                print('Select again.') 
