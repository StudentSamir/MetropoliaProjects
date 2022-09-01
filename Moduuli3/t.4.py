year=int(input("Anna vuosiluku:"))

if   year % 4==0   and year % 100!= 0:
        print("Karkausvuosi")
elif year % 100==0 and year % 400==0:
        print("karkausvuosi")
else:
        print("Error")

