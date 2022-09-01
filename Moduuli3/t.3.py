gender=input("Anna biologinen sukupuolesi:")
userhemoglobiini= float(input("Anna hemoglobiiniarvosi:"))

gender_nainen=str("nainen")
gender_mies = str("mies")

if   (gender==gender_nainen  and 117 <=userhemoglobiini<=175):
    print("Hemogboliiniarvosi on normaali.")
elif (gender==gender_nainen  and 117 > userhemoglobiini):
    print("Hemogboniiniarvosi on alhainen.")
elif (gender==gender_nainen  and 175 < userhemoglobiini):
    print("Hemogboliiniarvosi on korkea.")

elif (gender==gender_mies    and 134 <= userhemoglobiini <= 195):
    print("Hemogboliiniarvosi on normaali.")
elif (gender==gender_mies    and 134 > userhemoglobiini):
    print("Hemogboniiniarvosi on alhainen.")
elif (gender==gender_mies    and 195 < userhemoglobiini):
    print("Hemogboliiniarvosi on korkea.")
else:
    print("Error")














