# Carps game with displaying what is rolled
# the game carps is running. now i need to show whats happening so it an feel like playing a game, just like in book

import random

def dice_roll(die1,die2):
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1,die2)  #packing both values in a tuple

def display(dice):
    die1 , die2 = dice   #here the previous functions die1,die2 variable are already destroyed(cause they were in a function) so this is a completely new variable(can use other names as well)
    print('You rolled ', die1,' + ', die2, ' = ', die1 + die2)

dice = dice_roll(0,0)
display(dice)
total = sum(dice)
point = total
#no need of semi colon while calling function
a = 5
if total in (7,11):
    print('You win on first try')
elif total in (2,3,12):
    print('You Lose on first try')
else:
 while a == 5:
    a = a - 1
    
    dice = dice_roll(0,0)
    display(dice)
    total = sum(dice)
    if total == point:
       print('You Won')
    elif total == 7:
       print('You Lose')
    else:
       a = a + 1

