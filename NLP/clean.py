from uralic import lemmaus
import tokenisointi
from pathlib import Path
import os

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "
neljas_taso = "        "

# Funktiosanojen poisto
def funktiosanojen_poisto(korpus):
    tiedosto = open(os.path.join(os.path.dirname(__file__), "sanalistat/funktiosanat.txt"), "r")
    data = tiedosto.read()
    # Muutetaan tiedosto listaksi
    funktiosanat = data.split("\n")

    # Lemmataan korpus, jotta funktiosanoja voidaan vertailla ja poistaa
    lemmat = lemmaus(korpus)

    print("Sanastotiheys teksteittäin")
    for blogi in lemmat:
        print(eka_taso, blogi)
        for teksti in lemmat[blogi]:
            maara = 0
            for lemma in lemmat[blogi][teksti]:
                if lemma in funktiosanat:
                    maara += 1
            print(kolmas_taso, teksti)
            print(neljas_taso, "Funktiosanoja yhteensä:", maara)
            sanamaara = len(lemmat[blogi][teksti])
            print(neljas_taso, "Funktiosanoja prosentteina:", round(maara/sanamaara*100, 2))
            
    return lemmat

def poistot(asetukset, korpus):
    if asetukset["Sanaston tiheys"] == True:
        funktiosanojen_poisto(korpus)
