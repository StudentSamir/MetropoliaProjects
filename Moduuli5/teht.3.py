number=int(input("Anna kokonaisluku:"))

for n in range(2,number):
    if number % n== 0:
        print("Not prime number")
        break
    number = int(input("Anna kokonaisluku:"))
else:
    print("Prime number")