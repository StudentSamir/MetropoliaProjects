import random

number = (random.randint(1, 10))
guess = int(input("Arvaa luku väliltä 1-10: "))

while guess != number:

    if guess < number:
        print("Liiän pieni arvaus!")
    if guess > number:
        print("Liiän suuri arvaus!")

    guess = int(input("Arvaa uudestaan:"))

print("Oikein!")
