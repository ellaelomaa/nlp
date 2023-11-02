import string
import tokenisointi

# To do:
# hukkasanojen poisto (listasta)
# erisnimien poisto
# normalisointi

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
