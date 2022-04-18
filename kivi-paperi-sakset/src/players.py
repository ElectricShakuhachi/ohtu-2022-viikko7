import constants as consts

class Player:
    def anna_siirto(self, pelaajan_1_siirto):
        move = input("Toisen pelaajan siirto: ")
        return move

class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self, pelaajan_1_siirto):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3
        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"

class TekoalyParannettu:
    def __init__(self):
        self._muisti = []
        self._muistin_koko = consts.AI_MEMORY_SIZE

    def _muista_pelaajan_siirto(self, siirto):
        if len(self._muisti) == self._muistin_koko:
            self._muisti.pop(0)
        self._muisti.append(siirto)

    def _most_reps(self, options):
        max = 0
        most = "k"
        for key, value in options.items():
            if value > max:
                max = value
                most = key
        return most

    def _laske_siirto(self):
        if len(self._muisti) < 2:
            return "k"
        viimeisin_siirto = self._muisti[-1]
        options = {"k": 0, "p": 0, "s": 0}
        for i in range(len(self._muisti) - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                options[seuraava] += 1
        result = consts.WEAK_AGAINST[self._most_reps(options)]
        return result

    def anna_siirto(self, pelaajan_1_siirto):
        siirto = self._laske_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._muista_pelaajan_siirto(pelaajan_1_siirto)
        return siirto

