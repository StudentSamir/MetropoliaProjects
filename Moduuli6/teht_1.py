import random

sides= int(input("Anna nopan tahkojen lukumäärä:"))

def throw_dice():
    return random.randint(1,sides)

noppa=0
while noppa!= sides:

    noppa=throw_dice()
    print(noppa)