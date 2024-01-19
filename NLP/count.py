import tokenisointi
import regex as re
# import numpy as np

# Tässä tiedostossa lasketaan kaikki perustilastot ilman kielen
# käsittelyä ja NLP-kirjastoja

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "

# Kokonaissanamäärä
def sanamäärä(korpus):
    print("Kokonaissanamäärät:")
    for avain in korpus:
        print(eka_taso, avain)
        print(toka_taso, len(korpus[avain]))

def sanapituus(korpus):
    #lemmatisointi
    #grafeemeja per sana --> keskiavain

    print("Sanojen keskimääräinen pituus:")

    for avain in korpus:
        merkkeja = 0
        print(eka_taso, avain)
        sanalista = tokenisointi.tokenisoi_sanat(korpus[avain])

        sanoja = len(sanalista)

        for sana in sanalista:
            merkkeja += len(sana)
            ++sanoja

        print(toka_taso, "Merkkejä: ", merkkeja)
        print(toka_taso, "Sanoja: ", sanoja)
        if (merkkeja > 0 and sanoja > 0):
            print(toka_taso, "Sanojen keskimääräinen pituus: ", round(merkkeja/sanoja, 2))

def virkemäärä(korpus):
    print("Virkkeiden määrä:")
    for avain in korpus:
        virkelista = tokenisointi.tokenisoi_virkkeet(korpus[avain])
        print(eka_taso, avain)
        print(toka_taso, "Virkkeiden määrä: ", len(virkelista))

def virkelausepituus(korpus):
    print("Virkkeiden pituus sanoina:")
    for kirjoittaja in korpus:
        print(eka_taso, kirjoittaja)
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[kirjoittaja]))
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[kirjoittaja])
        print(toka_taso, "Keskimäärin sanoja virkkeessä: ", round(sanoja/len(virkkeita), 2))


def virkepituus(korpus):
    print("Virkkeiden pituus:")
    virkkeita = 0
    for avain in korpus:
        print(eka_taso, avain)
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[avain])

        # Virkkeiden pituus lauseina
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[avain])
        print(toka_taso, "Keskimäärin lauseita virkkeessä: ", round(len(lauseita)/len(virkkeita),2))

        # Virkkeiden pituus sanoina
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[avain]))
        print(toka_taso, "Keskimäärin sanoja virkkeessä: ", round(sanoja/len(virkkeita), 2))

        # Virkkeiden pituus grafeemeina, mukaan lukien erikoismerkit
        grafeemeja = len(korpus[avain])
        print(toka_taso, "Keskimäärin grafeemeja virkkeessä: ", round(grafeemeja/len(virkkeita), 2))


    # Lauseiden määrä blogissa
def lausemäärä(korpus):
    print("Lauseiden määrä: ")
    for avain in korpus:
        print(eka_taso, avain, "lauseita: ", len(tokenisointi.tokenisoi_lauseet(korpus[avain])))


def lausepituus(korpus):
    print("Lauseiden pituus:")
    for avain in korpus:
        print(eka_taso, avain)
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[avain])

        # Lauseiden pituus sanoina
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[avain]))
        print(toka_taso, "Keskimäärin sanoja lauseessa: ", round(sanoja/len(lauseita)))

        # Lauseiden pituus grafeemeina, eli ilman erikoismerkkejä
        valimerkiton = re.sub(r"[^\P{P}-'&]+", "", korpus[avain])
        valimerkiton.replace("&", "ja")
        print(toka_taso, "Keskimäärin grafeemeja lauseessa: ", round(len(valimerkiton)/len(lauseita)))

def grafeemeina(korpus):
    print("Grafeemit:")
    for avain in korpus:
        print(eka_taso, avain)

        # Grafeemeja sanassa
        merkkeja = 0
        
        sanalista = tokenisointi.tokenisoi_sanat(korpus[avain])
        sanoja = len(sanalista)

        for sana in sanalista:
            merkkeja += len(sana)
            ++sanoja

        print(toka_taso, "Grafeemeja sanassa: ", round(merkkeja/sanoja, 2))

        # Grafeemeja lauseessa
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[avain])
        valimerkiton = re.sub(r"[^\P{P}-'&]+", "", korpus[avain])
        valimerkiton.replace("&", "ja")
        print(toka_taso, "Grafeemeja lauseessa: ", round(len(valimerkiton)/len(lauseita)))

        # Grafeemeja virkkeessä
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[avain])
        grafeemeja = len(korpus[avain])
        print(toka_taso, "Grafeemeja virkkeessä: ", round(grafeemeja/len(virkkeita), 2))

def sanoina(korpus):
    print("Sanat:")
    for avain in korpus:
        print(eka_taso, avain)

        #Sanoja lauseessa
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[avain])

        # Lauseiden pituus sanoina
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[avain]))
        print(toka_taso, "Keskimäärin sanoja lauseessa: ", round(sanoja/len(lauseita)))        

        # Virkkeiden pituus sanoina
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[avain])
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[avain]))
        print(toka_taso, "Keskimäärin sanoja virkkeessä: ", round(sanoja/len(virkkeita), 2))

def lauseina(korpus):
    print("Lauseet:")
    for avain in korpus:
        print(eka_taso, avain)
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[avain])

        # Virkkeiden pituus lauseina
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[avain])
        print(toka_taso, "Keskimäärin lauseita virkkeessä: ", round(len(lauseita)/len(virkkeita),2))        

def tilasto_maarat(korpus):
    print("Tilastoja: ")

    sanamäärä(korpus)
    # TODO: lauseiden laskeminen, ei ollutkaan niin helppoa!
    # lausemäärä(korpus)
    virkemäärä(korpus)

def keskiarvot(korpus, graf, sanat, lauseet):
    print("Sana-, lause- ja virkepituus keskiarviona:")
    if graf == True:
        grafeemeina(korpus)
    if sanat == True:
        sanoina(korpus)
    if lauseet == True:
        lauseina(korpus)

def laskut(asetukset, korpus):
    tilasto_maarat(korpus)
    if asetukset["sanapituus"] == True:
        sanapituus(korpus)
    if asetukset["grafeemit"] == True:
        grafeemeina(korpus)
    if asetukset["virkesana"] == True:
        virkelausepituus(korpus)
        

# def varianssi():
#     data = 
#     variance = np.var(data)

# def keskihajonta():
#     data = 
#     standard_deviation = np.std(data)
