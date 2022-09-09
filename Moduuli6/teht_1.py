import random

def throw_dice():
    return random.randint(1,6)

noppa=0
while noppa!= 6:

    noppa=throw_dice()
    print(noppa)