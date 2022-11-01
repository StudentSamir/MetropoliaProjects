class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_alas(self):

        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        else:
            self.alin_kerros = self.alin_kerros

    def kerros_ylös(self):

        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        else:
            self.ylin_kerros = self.ylin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros < kohdekerros:
            self.kerros_ylös()

        while self.kerros > kohdekerros:
            self.kerros_alas()


h = Hissi(1, 15)
h.siirry_kerrokseen(8)
print(h.kerros)
h.siirry_kerrokseen(3)
print(h.kerros)
h.siirry_kerrokseen(5)
print(h.kerros)
h.siirry_kerrokseen(2)
print(h.kerros)
h.siirry_kerrokseen(1)
print(h.kerros)




class Talo:

    def __init__(self,alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit= []
        for n in range(hissi_lkm):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self,hissinumero, kohdekerros):

        hissi_numerointi = self.hissit[hissinumero - 1]
        print(f"Hissin numero:{hissinumero} ")
        hissi_numerointi.siirry_kerrokseen(kohdekerros)


t = Talo(1, 20, 7)
t.aja_hissiä(4, 10)
t.aja_hissiä(5, 10)
