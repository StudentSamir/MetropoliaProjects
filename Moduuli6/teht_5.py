
def calculator(numbers_int):
    sum_x =(numbers_int)
    return sum_x

numbers_string = []
numbers_int = []
even = []


number = input("Anna lukuarvo:")
while number != (""):
    numbers_string.append(number)
    number = input("Anna lukuarvo:")

for n in numbers_string:
    numbers_int.append(int(n))

for i in numbers_int:
    if (i % 2 == 0):
        even.append(i)

print("Alkuperäinen lista:"+str(calculator(numbers_int))+" ja karsittu lista:" + str(even)+"!")
