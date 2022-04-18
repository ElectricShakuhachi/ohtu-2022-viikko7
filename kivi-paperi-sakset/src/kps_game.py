from tuomari import Tuomari
import constants as consts

class KPS:
    def __init__(self, opponent):
        self.opponent = opponent()
        self.tuomari = Tuomari()

    def pelaa(self):
        while True:
            first_move = input("Ensimmäisen pelaajan siirto: ")
            second_move = self.opponent.anna_siirto(first_move)
            if first_move not in consts.STRONG_AGAINST or second_move not in consts.STRONG_AGAINST:
                break
            self.tuomari.tulkitse(first_move, second_move)
        print("Kiitos")
        print(self.tuomari.pelitilanteen_kuvaus())
