number=str(input("Anna lukuarvo:"))

while number != (""):

    maximum_value = max(number)
    minimum_value = min(number)

    number = str(input("Anna lukuarvo:"))

print("Pienin luku on "+str(maximum_value)+" ja"+" suurin luku on "+str(minimum_value)+"!")
