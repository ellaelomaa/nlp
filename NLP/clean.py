import tokenisointi
from uralicNLP import uralicApi

# Normalisointi
def normalisointi(tokenit):
    normalisoitu = []
    for word in tokenit:
        normalisoitu = uralicApi.lemmatize(word, "fin")
        if normalisoitu:
            normalisoitu.append(normalisoitu[0]['lemma'])
    return normalisoitu

# Siivoa tekstistä tarvittavat asiat?? Tätä saa ja pitää muokata
def siivoa():
    siivottu_teksti = []
    for erikoismerkit in korpus:
        # Korvaa ja-merkit ja-sanalla
        erikoismerkit = erikoismerkit.replace('&', 'ja')
        # Poistaa hipsut
        erikoismerkit = erikoismerkit.replace('"', '')
        siivottu_teksti.append(erikoismerkit)
    return siivottu_teksti


# poista tekstistä erisnimet (sanalista?)
def poista_erisnimet(korpus):
    erisnimet = []
    with open('erisnimet.txt', 'r') as file:
    erisnimet = file.read().splitlines()
    korpus_ei_erisnimiä = [token for token in erisnimet if token not in erisnimet]
    return korpus_ei_erisnimiä