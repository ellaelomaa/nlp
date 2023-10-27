import os

def hae_tiedosto(polku):
    tiedosto = open(polku, "r", encoding="utf-8")
    teksti = tiedosto.read()
    return teksti

def hae_korpus(polku):
    korpus = dict()
    for kansio, alakansiot, tiedostot in os.walk(polku):
        bloginimi = os.path.basename(kansio)

        teksti = ""

        for tiedosto in tiedostot:
            tiedostopolku = os.path.join(kansio, tiedosto)
            if tiedostopolku.endswith(".txt"):
                teksti += hae_tiedosto(tiedostopolku)
                teksti += " "
        
        if len(teksti) > 0:
            korpus[bloginimi] = teksti
   
    return korpus