
def calculator(numbers_int):
    sum_x = sum(numbers_int)
    return sum_x


numbers_string = []
numbers_int = []

number = input("Anna lukuarvo:")
while number != (""):
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

for n in numbers_string:
    numbers_int.append(int(n))

print("Summa on "+str(calculator(numbers_int)))

