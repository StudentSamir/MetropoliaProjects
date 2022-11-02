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



autolista = []
for k in range (1,10):
    auto = Auto(f"ABC-{k + 1}",randint(100, 200))
    autolista.append(auto)


class Kilpailu:

    def __init__(self,kilpailu_nimi, pituus_km, autolista):
            self.kilpailu_nimi = kilpailu_nimi
            self.pituus_km = pituus_km
            self.autolista = autolista

    def tunti_kuluu(self):

        for auto in autolista:
            auto.kiihtyvyys(randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):

        taulukko2 = []
        for auto in autolista:
            taulukko2.append([auto.rekisteritunnus, auto.huippunopeus,auto.nopeus, auto.kuljettu_matka])

        taulukko2.sort(key=lambda k: k[1], reverse=True)
        print(taulukko2)



kilpailu22= Kilpailu("Suuri romuralli",8000, 10)
kilpailu22.tulosta_tilanne()


kilpailu2 = True

tunnit = 10
while kilpailu2:
    kilpailu22.tunti_kuluu()
    if auto.kuljettu_matka > 8000:
        kilpailu22.tulosta_tilanne()
        kilpailu2 = False
    if tunnit == 10:
        tunnit = 0
        kilpailu22.tulosta_tilanne()
    tunnit += 1
kilpailu2 = False
