class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 222, nopeus = 60, kuljettu_matka = 2000):
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


auto1 = Auto("ABC-123")
auto1.kulje(1.5)

print(f"Kuljettu matka: {auto1.kuljettu_matka} km")
