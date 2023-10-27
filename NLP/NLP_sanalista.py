import clean
import tokenisointi
from nltk.probability import FreqDist

# Funktiosanalista
def funktiosanat(normalisoitu):
    funktiosanalista = []
    with open("funktiosanat.txt", "r") as file:
        funktiosanat_tiedostossa = file.read().splitlines()
    for funktiosana in normalisoitu:
        if funktiosana in funktiosanat_tiedostossa:
            funktiosanalista.append(funktiosana)
    return funktiosanalista

# Sisältösanalista 
def sisältösanat(normalisoitu):
    sisältösanalista = []
    with open("funktiosanat.txt", "r") as file:
        funktiosanat_tiedostossa = file.read().splitlines()
    for funktiosana in normalisoitu:
        if funktiosana in funktiosanat_tiedostossa:
            sisältösanalista.append(funktiosana)
    return sisältösanalista


# High frequency lexicon 30/50/100 (lemmattu, funktiosanat poistettu)
def taajuussanasto(tokenit):
    # öööööhh miten tehdään toi että saa valita ton määrän? tehäänkö taa vasta gui-hommassa?
    taajuussanalista = []
    # poista erisnimet
    # normalisointi
    # poista funktiosanat
    # freqdist
    return taajuussanalista

# Hapax legomena (sanat jotka esiintyy vaan kerran tai harvoin, lemmatuista ja ei lemmatuista listoista)
def hapakslegomena(taajuussanalista):
    # saisko tän niin että sort freqdist-lista vaa nousevasti ja siitä sitte?
    return hapakslegomena

# Sanaston laajuus (lemmatusta listasta ja remove duplicates jne eli uniikit sanat jne.)
def saneet(tokenit):
    sanelista = []
    # poista erisnimet
    # normalisointi
    # remove duplicates
    return sanelista

def sanasto(korpus):
    #lemmatisointi
    #remove duplicates
    #count
    fdist = FreqDist()
    print("Sanaston laajuus (lemmaamaton):")
    for arvo in korpus:
        print("  ", arvo)
        sanalista = tokenisointi.tokenisoi_sanat(korpus[arvo])
        for sana in sanalista:
            fdist[sana.lower()] += 1
        print("    ", fdist.B())