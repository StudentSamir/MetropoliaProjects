import math

leivisköt=float(input("Anna leivisköt:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))

leivisköt_weight=(leivisköt*20)
leivisköt_naulat_weight=(leivisköt_weight*32+naulat*32)
total=(leivisköt_naulat_weight*13.3+luodit*13.3)
print(total)

weight_kilograms=(total/1000)
roundedkilograms = math.floor(weight_kilograms)

print("Massa nykymittojen mukaan:")
print(str(roundedkilograms) +" kilogrammaa"+" grammaa")












