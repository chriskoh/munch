#!/usr/bin/bash python3

from random import randint

def drawcard():
    
    rng = randint(1,100)
    
    if rng <= 60:
        card = 'Item'
    else:
        card = 'Monster'
        
    return card

