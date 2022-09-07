number=int(input("Anna kokonaisluku:"))

for n in range(2,number):
    if number % n== 0:
        print("Luku "+str(number) + " 4ei ole alkuluku!")
        break
else:
    print("Luku "+str(number) + " on alkuluku!")