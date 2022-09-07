numbers_string = []

number = input("Anna lukuarvo:")

while number!="":
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

numbers_string.sort(reverse=True)
print(("Suurin luku on ")+str(numbers_string[0])+(" ja pienin luku on ")+str(numbers_string[-1])+("!"))
