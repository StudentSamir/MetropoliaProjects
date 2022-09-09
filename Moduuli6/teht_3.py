def convertor(usergallons):
    liters= (3.7854 * usergallons)
    return liters

usergallons = float(input("Anna lukuarvo:"))
while usergallons>=0:
    print(str(usergallons)+ " galloona on litroina "+str(convertor(usergallons))+"l" )
    usergallons = float(input("Anna lukuarvo:"))
print("Error!")