import tokenisointi

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

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
    for arvo in korpus:
        virkelista = tokenisointi.tokenisoi_virkkeet(korpus[arvo])
        print(eka_taso, arvo)
        print(toka_taso, "Virkkeiden määrä: ", len(virkelista))
    #count virkkeet

def virkepituus(korpus):
    for arvo in korpus:
        # Virkkeiden pituus sanoina
        virkkeita = len(virkemäärä(korpus[arvo]))
        sanoja = 0
        for virke in korpus[arvo]:
            sanoja += len(virke)
        print("S")

        # laske virkkeet grafeemeina
        # laske virkkeet lauseina
        # keskiarvo kaikista

# def lausemäärä():
#     #count lauseet

# def lausepituus():
#     #laske lauseet sanoina
#     #laske lauseet grafeemeina
#     #laske keskiarvo kummastakin


def tilastoja(korpus):
    print("Tilastoja: ")

    sanamäärä(korpus)
    sanapituus(korpus)
