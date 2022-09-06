number=str(input("Anna lukuarvo:"))

maximum = min (number)
minimum = max (number)

while number != (""):
    print("Enter new number:")
    number = str(input("Anna lukuarvo:"))

print("Pienin luku on "+str(maximum)+" ja"+" suurin luku on "+str(minimum)+"!")
