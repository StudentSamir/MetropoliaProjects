numbers_string = []
numbers_int = []

number = input("Anna lukuarvo:")

while number!="":
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

for n in numbers_string:
    numbers_int.append(int(n))

numbers_int.sort(reverse=True)
print(("Suurin luku on ")+str(numbers_int[0])+(" ja pienin luku on ")+str(numbers_int[-1])+("!"))
