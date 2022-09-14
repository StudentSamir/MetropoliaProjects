vuodenajat = ("talvi", "kevät", "kesä","syksy")
järjestysnumero = int(input("Anna kuukauden numero (1-12):"))


if järjestysnumero == 12 or järjestysnumero == 1 or järjestysnumero == 2:
    print(str(järjestysnumero)+".kuukauden vuodenaika "+ str(vuodenajat[0])+"!")

elif järjestysnumero == 3 or järjestysnumero == 4 or järjestysnumero== 5:
    print(str(järjestysnumero) + ".kuukauden vuodenaika " + str(vuodenajat[1])+"!")

elif järjestysnumero == 6 or järjestysnumero == 7 or järjestysnumero == 8:
    print(str(järjestysnumero) + ".kuukauden vuodenaika " + str(vuodenajat[2])+"!")

elif järjestysnumero == 9 or järjestysnumero== 10 or järjestysnumero == 11:
    print(str(järjestysnumero) + ".kuukauden vuodenaika " + str(vuodenajat[3])+"!")
else:
    print("Error")

