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

auto1 = Auto("ABC-123")

auto1.kiihtyvyys(10)
auto1.kiihtyvyys(70)
auto1.kiihtyvyys(50)

print(f"Auton nopeus on {auto1.nopeus:d} km/h.")

auto1.kiihtyvyys(-200)

print(f"Hätäjarrutuksen jälkeen auton nopeus on {auto1.nopeus:d}km/h.")
