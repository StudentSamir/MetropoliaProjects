gender=input("Anna biologinen sukupuolesi:")

gender_nainen=str("nainen")
gender_mies = str("mies")

if (gender==gender_nainen and not gender==gender_mies):
    hemoglobiiniarvo1 = float(input("Anna hemoglobiininiarvosi(g/l):"))

if (gender == gender_mies and not gender == gender_nainen):
    hemoglobiiniarvo2 = float(input("Anna hemoglobiininiarvosi(g/l):"))


elif 117 <=hemoglobiiniarvo1<=175:
    print("Hemogboliiniarvosi on normaali.")
elif 117>hemoglobiiniarvo1:
    print("Hemogboniiniarvosi on alhainen.")
elif 175<hemoglobiiniarvo1:
    print("Hemogboliiniarvosi on korkea.")

elif 134<=hemoglobiiniarvo2<=195:
    print("Hemogboliiniarvosi on normaali.")
elif 134>hemoglobiiniarvo2:
    print("Hemogboniiniarvosi on alhainen.")
elif 195<hemoglobiiniarvo2:
    print("Hemogboliiniarvosi on korkea.")