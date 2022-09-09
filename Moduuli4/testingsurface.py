import random

def heitänoppaa(lkm):
    return random.randint(1,lkm)

lkm=7
noppa=0

while noppa != lkm:

        noppa=heitänoppaa(lkm)
        print(noppa)