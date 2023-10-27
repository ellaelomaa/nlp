import clean.py

# Funktiosanalista
def funktiosanat(normalisoitu):
    funktiosanalista = []
    with open("funktiosanat.txt", "r") as file:
        funktiosanat_listassa = file.read().splitlines()
    for funktiosana in normalisoitu:
        if funktiosana in funktiosanat_listassa:
            funktiosanalista.append(funktiosana)
    return funktiosanalista

# Sisältösanalista 
def sisältösanat(normalisoitu):
    sisältösanalista = []
    with open("funktiosanat.txt", "r") as file:
        funktiosanat_listassa = file.read().splitlines()
    for funktiosana in normalisoitu:
        if funktiosana in funktiosanat_listassa:
            sisältösanalista.append(funktiosana)
    return sisältösanalista


# High frequency lexicon 30/50/100 (lemmattu, funktiosanat poistettu) määrävalinta gui:hin
def taajuussanasto(tokenit):
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