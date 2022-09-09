import random

sides= int(input("Anna mielivaltaisen nopan tahkojen lukumäärä:"))

def throw_dice():
    return random.randint(1,sides)

noppa=0
while noppa!= sides:

    noppa=throw_dice()
    print(noppa)

