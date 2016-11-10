#!/usr/bin/bash python3

from random import randint

def getitem(player, t1, t2, t3, t4, t5):

    slotrng = randint(1,7)

    slots = {1: "head",
            2: "body",
            3: "hands",
            4: "legs",
            5: "feet",
            6: "left",
            7: "right",
            }

    slot = slots[slotrng]
    rng = randint(1,100)

    if rng >= 0 and rng <= 40:
        bonus = t1
        
    elif rng >= 41 and rng <= 60:
        bonus = t2
        
    elif rng >= 61 and rng <= 74:
        bonus = t3
        
    elif rng >= 75 and rng <= 90:
        bonus = t4
        
    else:
        bonus = t5 

    input("You found: " + slot + " with a bonus of " + str(bonus) + "!")
    if slotrng == 1:
        player.head = equip(player, slot, player.head, bonus)
    elif slotrng == 2:
        player.body = equip(player, slot, player.body, bonus)
    elif slotrng == 3:
        player.hand = equip(player, slot, player.hand, bonus)
    elif slotrng == 4:
        player.leg = equip(player, slot, player.leg, bonus)
    elif slotrng == 5:
        player.foot = equip(player, slot, player.foot, bonus)
    elif slotrng == 6:
        player.left = equip(player, slot, player.left, bonus)
    elif slotrng == 7:
        player.right = equip(player, slot, player.right, bonus)

def equip(player, slot, slotval, bonus):

    plvl = player.level
    ilvl = player.head + player.body + player.hand + player.leg + player.foot + player.left + player.right

    current = slotval

    if slotval == 0:
        input(player.name + ' has gained ' + str(bonus) + ' power! (Current: ' + str(plvl + ilvl + bonus) + ')')
        return bonus

    else:
        print("You currently have: " + slot + " with a bonus of " + str(slotval) + ".")
        switch = input("Would you like to switch? (Y/N)")

        if switch.lower == 'y':
            input("Your " + slot + " has been switched!")
            return bonus

        elif switch.lower == 'n':
            input("Selling " + slot + " for ___ gold.")
            return current

        else:
            print("Please choose again")
            return current
