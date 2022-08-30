import math

leivisköt=float(input("Anna leivisköt:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))

leivisköt_weight=(leivisköt*20)
leivisköt_naulat_weight=(leivisköt_weight*32+naulat*32)
total=(leivisköt_naulat_weight*13.3+luodit*13.3)

totalweight_kilograms=(total/1000)
roundedkilograms = math.floor(totalweight_kilograms)
roundedgrams=(total-roundedkilograms*1000)

print("Massa nykymittojen mukaan:")
print(str(roundedkilograms) +" kilogrammaa "+ "ja "+str(roundedgrams)+ " grammaa")












