class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
            self.kuljettu_matka = kuljettu_matka

auto1= Auto("ABC-123", 142)

print (f"Auton rekisteritunnus {auto1.rekisteritunnus:s}, huippunopeus {auto1.huippunopeus:d} km/h, nopeus {auto1.tämänhetkinen_nopeus:d} km/h ja kuljettu matka {auto1.kuljettu_matka:d} km" )
