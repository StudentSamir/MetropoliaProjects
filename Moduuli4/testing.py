#5.osio

nimet=[]

nimi="---"
while(nimi!=""):
    nimi=input("Syötä nimi:")
    if nimi!="":
        nimet.append(nimi)
nimet.sort()

for nimi in nimet:
    print(nimi)

nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for n in nimet:
    print (f"Moi, {n}!")




import random
arpa = int(input('Anna noppien määrä: '))

nopat = []

for noppa in range(arpa):
    silmaluku = random.randint(1, 6)
    print(silmaluku)
    nopat.append(silmaluku)

print(f'Silmälukujen summa: {sum(nopat)}.')



import random

arpakuutio= int(input("Syötä arpakuudioiden lukumäärä:"))

nopat = []

for noppa in range(arpakuutio):
    silmaluku = random.randint(1,6)
    print(silmaluku)
    nopat.append(silmaluku)

print(f'Silmälukujen summa: {sum(nopat)}.')




luku = input('Anna luku: ')

luvut = []

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input('Anna luku: ')

luvut.sort(reverse=True)
print(f'5 suurinta: {luvut[0:5]}.')






#t.2

numbers_string = []

number = input("Anna lukuarvo:")

while number!="":
    numbers_string.append(number)
    number = input("Anna lukuarvo:")


numbers_string.sort(reverse=True)
print("Viisi suurinta lukua ovat:"+str(numbers_string[0:5]))


numbers_string = []
numbers_int = []

number = input("Anna lukuarvo:")

while number!="":
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

for n in numbers_string:
    numbers_int.append(int(n))

numbers_int.sort(reverse=True)
print("Viisi suurinta lukua ovat:"+str(numbers_int[0:5]))