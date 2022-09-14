nimi= input("Anna nimi:")
nimet= set()
nimet.add(nimi)

print("Uusi nimi")

while nimi !=(""):
    nimi = input("Anna nimi: ")

    if nimi in nimet:
        print("Aiemmin syotetty nimi!")

    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi!")

for n in nimet:
    print(n)
