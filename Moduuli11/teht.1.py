class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")


class Kirja(Julkaisu):

    def __init__(self,nimi,kirjoittaja, sivumäärä):

        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.kirjoittaja, self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):

       self.päätoimittaja = päätoimittaja
       super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.päätoimittaja}")

l1 = Lehti("Aku Ankka", "Aki Hyyppä")
l1.tulosta_tiedot()

k1 = Kirja("Hytti n:o 6", "Rosa Liksom", "200")
k1.tulosta_tiedot()
