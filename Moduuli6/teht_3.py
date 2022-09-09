usergallons=float(input("Anna lukuarvo:"))
def convertor():
    return(3.79*gallons)

while gallons >= 0:
    galloona = convertor()
    print(str(gallons)+ " galloonaa on litroina "+ str(galloona)+ "l")
    gallons = float(input("Anna lukuarvo:"))
print("Ohjelma pysäytetty!")