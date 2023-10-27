import tokenisointi
import regex as re

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "

# listayksköiden määrä (sanasto)
def sanamäärä(korpus):
    print("Kokonaissanamäärät:")
    for arvo in korpus:
        print(eka_taso, arvo)
        print(toka_taso, len(korpus[arvo]))

def sanapituus(korpus):
    #lemmatisointi
    #grafeemeja per sana --> keskiarvo

    print("Sanojen keskimääräinen pituus:")

    for arvo in korpus:
        merkkeja = 0
        sanoja = 0
        print(eka_taso, arvo)
        sanalista = tokenisointi.tokenisoi_sanat(korpus[arvo])

        sanoja = len(sanalista)

        for sana in sanalista:
            merkkeja += len(sana)
            ++sanoja

        print(toka_taso, "Merkkejä: ", merkkeja)
        print(toka_taso, "Sanoja: ", sanoja)
        if (merkkeja > 0 and sanoja > 0):
            print(toka_taso, "Sanojen keskiarvoinen pituus: ", round(merkkeja/sanoja, 2))

def virkemäärä(korpus):
    print("Virkkeiden määrä:")
    for arvo in korpus:
        virkelista = tokenisointi.tokenisoi_virkkeet(korpus[arvo])
        print(eka_taso, arvo)
        print(toka_taso, "Virkkeiden määrä: ", len(virkelista))

def virkepituus(korpus):
    print("Virkkeiden pituus:")
    virkkeita = 0
    for arvo in korpus:
        print(eka_taso, arvo)
        virkkeita = tokenisointi.tokenisoi_virkkeet(korpus[arvo])

        # Virkkeiden pituus lauseina
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[arvo])
        print(toka_taso, "Keskimäärin lauseita virkkeessä: ", round(len(lauseita)/len(virkkeita),2))

        # Virkkeiden pituus sanoina
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[arvo]))
        print(toka_taso, "Keskimäärin sanoja virkkeessä: ", round(sanoja/len(virkkeita), 2))

        # Virkkeiden pituus grafeemeina, mukaan lukien erikoismerkit
        grafeemeja = len(korpus[arvo])
        print(toka_taso, "Keskimäärin grafeemeja virkkeessä: ", round(grafeemeja/len(virkkeita), 2))


    # Lauseiden määrä blogissa
def lausemäärä(korpus):
    print("Lauseiden määrä: ")
    for arvo in korpus:
        print(eka_taso, arvo, "lauseita: ", len(tokenisointi.tokenisoi_lauseet(korpus[arvo])))


def lausepituus(korpus):
    print("Lauseiden pituus:")
    for arvo in korpus:
        print(eka_taso, arvo)
        lauseita = tokenisointi.tokenisoi_lauseet(korpus[arvo])

        # Lauseiden pituus sanoina
        sanoja = len(tokenisointi.tokenisoi_sanat(korpus[arvo]))
        print(toka_taso, "Keskimäärin sanoja lauseessa: ", round(sanoja/len(lauseita)))

        # Lauseiden pituus grafeemeina, eli ilman erikoismerkkejä
        valimerkiton = re.sub(r"[^\P{P}-'&]+", "", korpus[arvo])
        valimerkiton.replace("&", "ja")
        print(toka_taso, "Keskimäärin grafeemeja lauseessa: ", round(len(valimerkiton)/len(lauseita)))

def tilastoja(korpus):
    print("Tilastoja: ")

    sanamäärä(korpus)
    sanapituus(korpus)
