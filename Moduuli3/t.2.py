hyttiluokka=input("Anna hyttiluokkasi:")
hyttiluokka1=str("LUX")
hyttiluokka2=str("A")
hyttiluokka3=str("B")
hyttiluokka4=str("C")
if hyttiluokka==hyttiluokka1:
    print(str(hyttiluokka1)+" on parvekkeellinen hytti yläkannella.")
elif hyttiluokka==hyttiluokka2:
    print(str(hyttiluokka2)+ " on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka==hyttiluokka3:
    print(str(hyttiluokka3)+" on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka==hyttiluokka4:
    print(str(hyttiluokka4)+" on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka.")