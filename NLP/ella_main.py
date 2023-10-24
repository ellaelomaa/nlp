import gui
import fetch

asetukset = gui.asetukset

def kaynnista():
    korpus = fetch.hae_korpus(asetukset["avattavat_tiedostot"])
    print(korpus)