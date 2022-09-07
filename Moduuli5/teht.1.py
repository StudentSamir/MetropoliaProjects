import random

arpakuutio= int(input("Syötä arpakuutioiden lukumäärä:"))

arpakuutiot = []

for n in range(arpakuutio):

    silmaluku = random.randint(1,6)
    print(silmaluku)
    arpakuutiot.append(silmaluku)

print("Silmälukujen summa:")
print(sum(arpakuutiot))