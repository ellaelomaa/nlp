import string
import tokenisointi
from uralicNLP import uralicApi #uralicApi.download(fin) josset oo ladannu suomem kieli mälliä

# To do:
# hukkasanojen poisto (listasta)
# erisnimien poisto

# Normalisointi/lemmaus-funktio
def normalisointi(tokenit):
    lang = "fin"  # kielivalinta
    analyzer = uralicApi.Analyzer() # tää haluaa listan nii pitää tehdä tästä uus oma muuttujansa tms.
    normalisoitu = []
    for token in tokenit:
        lemmatized = analyzer.analyze(token, lang)
        if lemmatized:
            normalisoitu.append(lemmatized[0]['lemma'])
        else:
            normalisoitu.append(token)

    return normalisoitu

# Erisnimien poisto. Tää täytyy tehdä sitten tokenisoimattomalle tiedostolle (joissain erisnimissä monia osia)
def erisnimien_poisto(korpus): 
    erisnimet_poistettu = []
    with open("erisnimet.txt", "r") as file:
        erisnimet_tiedostossa = file.read().splitlines()
    for erisnimi in korpus:
        if erisnimi in erisnimet_tiedostossa:
            erisnimet_poistettu.append(erisnimi)
    return erisnimet_poistettu


# Funktiosanojen poisto
def funktiosanojen_poisto(korpus, polku):
    tiedosto = open(polku, "r")
    data = tiedosto.read()
    # Muutetaan tiedosto listaksi
    funktiosanat = data.split("\n")

    for avain in korpus:
        sanalista = tokenisointi.tokenisoi_sanat(korpus[avain])
        print("Ennen: ", len(sanalista))
        temp = [sana for sana in sanalista if sana not in funktiosanat]
        print("Jälkeen: ", len(temp))
        korpus[avain] = temp

    return korpus


# Sisältösanojen poisto
def sisaltosanojen_poisto(korpus, polku):
    tiedosto = open(polku, "r")
    data = tiedosto.read()
    sisaltosanat = data.split("\n")
    
    for avain in korpus:
        sanalista = tokenisointi.tokenisoi_sanat(korpus[avain])
        print("Ennen: ", len(sanalista))
        temp = [sana for sana in sanalista if sana not in sisaltosanat]
        print("Jälkeen: ", len(temp))
        korpus[avain] = temp

    return korpus

def poistot(korpus, funktiobool, funktiopolku, sisaltobool, sisaltopolku):
    if funktiobool == True:
        funktiosanojen_poisto(korpus, funktiopolku)
