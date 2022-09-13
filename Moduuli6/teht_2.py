import random

sides= int(input("Anna mielivaltaisen nopan tahkojen lukumäärä:"))

def throw_dice():
   nopat = random.randint(1,sides)
   return nopat


noppa=0
while noppa!= sides:

    noppa=throw_dice()
    print(noppa)