number=int(input("Anna kokonaisluku:"))

if number >= 1:
    for n in range(2,number):
        if number % n==0:
            print("Luku "+str(number) + " ei ole alkuluku!")
            break
    else:
        print("Luku "+str(number) + " on alkuluku!")