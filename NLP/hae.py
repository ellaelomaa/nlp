import os

def hae_tiedosto(polku):
    tiedosto = open(polku, "r", encoding="utf-8")
    teksti = tiedosto.read()
    return teksti

# Helmin manuaalisesti lauseiksi jäsennetyn tiedoston haku
def hae_jasennetty():
    path = os.path.abspath(os.path.curdir)
    folder = "jasennettu"
    korpus = hae_korpus(os.path.join(path, folder))
    return korpus

def hae_korpus(polku):
    korpus = dict()
    
    for kansio, alakansiot, tiedostot in os.walk(polku):
        bloginimi = os.path.basename(kansio)
        blogikorpus = dict()

        teksti = ""

        for tiedosto in tiedostot:
            tiedostopolku = os.path.join(kansio, tiedosto)
            if tiedostopolku.endswith(".txt"):
                teksti = hae_tiedosto(tiedostopolku)
                tekstiNimi = os.path.basename(tiedostopolku)

                blogikorpus[os.path.splitext(tekstiNimi)[0]] = teksti
        
        if (len(blogikorpus) > 0):
            korpus[bloginimi] = blogikorpus
            
    return korpus