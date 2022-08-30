import math

leivisköt=float(input("Anna leivisköt:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))

leivisköt_sum=(leivisköt*20)
naulat_sum=(leivisköt_sum*32+naulat*32)
luodit_sum=(naulat_sum*13.3+luodit*13.3)

print(luodit_sum)

weight_kilograms=(luodit_sum/1000)
roundedkilograms = math.floor(weight_kilograms)

roundedgrams=math.floor(luodit_sum)
grams=float(roundedkilograms+roundedgrams)
print(grams)

print("Massa nykymittojen mukaan:")
print(str(roundedkilograms) +" kilogrammaa"+" grammaa")











