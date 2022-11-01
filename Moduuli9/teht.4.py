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



kilpailu = True

while kilpailu:
    for auto in autot:
        auto.kiihtyvyys(randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka > 10000:

            kilpailu = False


rekisteri = "rekisteritunnus:"
huippunopeus = "huippunopeus:"
nopeus = "nopeus:"
kuljettu_matka = "kuljettu_matka:"
print(rekisteri, huippunopeus, nopeus, kuljettu_matka)

taulukko = []
for auto in autot:
    taulukko.append([auto.rekisteritunnus, auto.huippunopeus,auto.nopeus, auto.kuljettu_matka])


taulukko.sort(key=lambda k: k[1], reverse = True)
print(taulukko)
