import os

def hae_tiedosto(polku):
    print(polku)
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

def hae_korpus2(polku):
    korpus = dict()
    for kansio, alakansiot, tiedostot in os.walk(polku):
        bloginimi = os.path.basename(kansio)

        teksti = ""

        for tiedosto in tiedostot:
            tiedostopolku = os.path.join(kansio, tiedosto)
            if tiedostopolku.endswith(".txt"):
                teksti += hae_tiedosto(tiedostopolku)
                teksti += " "
        
        korpus[bloginimi] = teksti
        # teksti = ""
        # for tiedosto in tiedostot:
        #     print(os.path.join(kansio, tiedosto))
        # tiedostopolku = os.path.join(kansio, tiedosto)
        
        # if tiedostopolku.endswith(".txt"):
        #     print(tiedostopolku)
        #     teksti += hae_tiedosto(tiedostopolku)
        # korpus[kansio] = teksti
   
    return korpus