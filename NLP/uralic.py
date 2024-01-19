# Tiedosto, jossa käsitellään kaikki UralicNLP-kirjaston funktiot

from uralicNLP import uralicApi
from tokenisointi import tokenisoi_sanat

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "

def morfeemit(korpus):
    print("Keskimäärin morfeemeja sanassa:")
    for kirjoittaja in korpus:
        
        lkm = 0
        tokenit = tokenisoi_sanat(korpus[kirjoittaja])
        for token in tokenit:
            morfeemit = uralicApi.segment(token, "fin")
            if (len(morfeemit) > 0):
                lkm += len(morfeemit[0])
        keskiarvo = len(korpus[kirjoittaja]) / lkm
        print(eka_taso, kirjoittaja, ": ", round(keskiarvo, 2))

# Lemmausfunktio. Mikäli sanalle tarjoaan useampaa lemmaa,
# valitaan ensimmäinen. Virheitä siis tulee, mutta ohjelma
# porskuttaa eteenmpäin.
def lemmat(korpus):
    lemmaDict = {}
    for kirjoittaja in korpus:
        sanat = tokenisoi_sanat(korpus[kirjoittaja])
        lemmalista = []
        for sana in sanat:
            lemma = uralicApi.lemmatize(sana, "fin", word_boundaries=False)
            if (len(lemma) > 0):
                lemmalista.append(lemma[0])
        lemmaDict[kirjoittaja] = lemmalista
    return lemmaDict

# Pääohjelmassa kutsuttava funktio, joka kutsuu kaikkia muita asetusten mukaan.
def uralic(asetukset, korpus):
    lemmat(korpus)
    if asetukset["morfeemit"] == True:
        morfeemit(korpus)
        