from players import Player, Tekoaly, TekoalyParannettu
from kps_game import KPS

def main():
    options = {
        "a": Player,
        "b": Tekoaly,
        "c": TekoalyParannettu
        }

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()
        if vastaus not in ["a", "b", "c"]:
            break
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli = KPS(options[vastaus])
        peli.pelaa()

if __name__ == "__main__":
    main()
