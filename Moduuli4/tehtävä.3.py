number=str(input("Anna lukuarvo:"))

smallest=str(0)
largest=str(0)

while number != "":
    print("Enter new number")

     if number != '':

        number = str(input("Anna lukuarvo:"))
         if number>largest:
            largest = number
         if number<smallest:
            smallest= number

print(str(smallest)+ str(largest))

