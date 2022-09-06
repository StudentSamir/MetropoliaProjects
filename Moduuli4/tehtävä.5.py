user=input("Anna käyttäjätunnus:")
password=input("Anna salasana:")
attempts=0

while   user!=str("python") and password!= str("rules"):

    print("Pääsy evätty!")
    attempts = attempts + 1
    if attempts == 5:
        break
    user = input("Anna käyttäjätunnus:")
    password = input("Anna salasana:")

if user == str("python") and password == str("rules"):
    print("Tervetuloa!")