import math

def calculator1():
    value1 = pizza2_hinta / ((math.pi * ((pizza2_halkaisija/2)) / 100) ** 2)
    return value1

def calculator2():
    value2 = pizza1_hinta / ((math.pi * ((pizza1_halkaisija / 2)) / 100) ** 2)
    return value2

pizza1_halkaisija = float(input("Anna ensimmaisen pizzan halkaisija: "))
pizza1_hinta = float(input("Anna ensimmaisen pizzan hinta: "))
pizza2_halkaisija = float(input("Anna toisen pizzan halkaisija: "))
pizza2_hinta = float(input("Anna toisen pizzan hinta: "))

if calculator1() < calculator2():
    print("Ensimmainen pitsalla on rahallisesti parempi vastine.")
elif calculator1() > calculator2():
    print("Toisella pitsalla on rahallisesti parempi vastine.")
else:
    print("Pitsat ovat rahallisesti yhtä arvokkaita.")







