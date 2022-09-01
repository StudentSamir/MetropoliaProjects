year=int(input("Anna vuosiluku:"))

if   year % 4==0   and year % 100!= 0:
        print("Vuosi "+str(year)+ " on karkausvuosi.")
elif year % 100==0 and year % 400==0:
        print("Vuosi "+str(year)+ " on karkausvuosi.")
else:
        print("Vuosi "+str(year)+" ei ole karkausvuosi.")

