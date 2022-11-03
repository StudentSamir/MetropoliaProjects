
class Auto:
    def __init__(self, rekisteritunnus , huippunopeus = 222, nopeus = 0, kuljettu_matka = 0):
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

class sähköauto(Auto):

    def __init__(self,  rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class polttomoottori(Auto):

    def __innit__(self,  rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)

Sähköauto = sähköauto("ABC", 180, 180)
Polttomoottori = polttomoottori("ABC", 120, 120)


Sähköauto.kiihtyvyys(60)
Polttomoottori.kiihtyvyys(45)

Sähköauto.kulje(3)
Polttomoottori.kulje(3)

print(f"{Sähköauto.kuljettu_matka}")
print(f"{Polttomoottori.kuljettu_matka}")
