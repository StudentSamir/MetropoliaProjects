numbers_string = []

number = input("Anna lukuarvo:")

while number!="":
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

numbers_string.sort(reverse=True)
print("Viisi suurinta lukua ovat:"+str(numbers_string[0:5]))

