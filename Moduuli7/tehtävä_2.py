nimi= input("Anna nimi:")
nimet= set()
nimet.add(nimi)

print("Uusi nimi")

while nimi !=(""):
    nimi = input("Anna nimi: ")

    if nimi in nimet:
        print("Aiemmin syotetty nimi!")

    else:
        nimet.add(nimi)
        print("Uusi nimi!")

for n in nimet:
    print(n)
