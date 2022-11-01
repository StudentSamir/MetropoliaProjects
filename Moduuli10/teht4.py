from random import randint

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 222, nopeus = 0, kuljettu_matka = 0):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = nopeus
            self.kuljettu_matka = kuljettu_matka


    def kiihtyvyys(self, nopeus_muutos):

        self.nopeus += nopeus_muutos
        if self.nopeus < 0:
           self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
             self.nopeus = self.huippunopeus


    def kulje(self, tunnit):
            self.kuljettu_matka += self.nopeus * tunnit


autot = []
for k in range (1,10):
    auto = Auto(f"ABC-{k + 1}",randint(100, 200))
    autot.append(auto)



class Kilpailu:

    def __init__(self,kilpailu_nimi, pituus_km, autolista):
            self.kilpailu_nimi = kilpailu_nimi
            self.pituus_km = pituus_km
            self.autolista = autolista
            self.os_auto_lista = []
            self.tunti = 0

            for n in range(autolista):
                autolista = Auto((f"ABC-{n + 1}"), randint(100, 200))
                self.os_auto_lista.append(autolista)


    def kilpailu_ohi(self):

        kilpailu2 = True

        while kilpailu2:
            for auto in autot:
                if auto.kuljettu_matka > 8000:

                    kilpailu2 = False


    def tunti_kuluu(self):

        self.tunti += 1
        for autolista in os_auto_lista:
            autolista.kiihtyvyys(randint(-10, 15))
            autolista.kulje(1)

    def tulosta_tilanne(self):

        taulukko2 = []
        for auto in autot:
            taulukko2.append([auto.rekisteritunnus, auto.huippunopeus,auto.nopeus, auto.kuljettu_matka,self.tunti])

        taulukko2.sort(key=lambda k: k[1], reverse=True)
        print(taulukko2)

kilpailu3= Kilpailu("Suuri romuralli",8000, 10)
