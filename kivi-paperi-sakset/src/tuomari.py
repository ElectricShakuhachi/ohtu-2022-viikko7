import constants as consts

class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def tulkitse(self, ekan_siirto, tokan_siirto):
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit = self.tasapelit + 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1
        print(self.pelitilanteen_kuvaus())

    def pelitilanteen_kuvaus(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    def _tasapeli(self, eka, toka):
        if eka == toka:
            return True
        return False

    def _eka_voittaa(self, eka, toka):
        if consts.STRONG_AGAINST[eka] == toka:
            return True
        return False
