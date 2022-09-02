inch_unit=float(input("Anna lukuarvo:"))
while inch_unit >= 0:
    print(str(inch_unit)+ " tuumaa on senttimetreinä " +  str(2.54*inch_unit)+" cm")
    inch_unit = float(input("Anna lukuarvo:"))
print("Ohjelma pysäytetty!")
