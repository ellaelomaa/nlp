def hae_tiedosto(polku):
    tiedosto = open(polku, "r", encoding="utf-8")
    teksti = tiedosto.read()
    return teksti

def hae_korpus(polut):
    teksti = ""
    tiedostot = polut.split(";")

    for polku in tiedostot:
        teksti += hae_tiedosto(polku)
        teksti += " "

    return teksti