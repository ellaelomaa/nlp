import ella_tokenisointi as token
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
    merkkeja = 0
    sanoja = 0
    #lemmatisointi
    #grafeemeja per sana --> keskiarvo

    print("Sanojen keskimääräinen pituus:")
    for arvo in korpus:
        print(eka_taso, arvo)
        sanalista = token.tokenisoi_sanat(korpus[arvo])
        sanoja = len(sanalista)
        for sana in sanalista:
            merkkeja =+ len(sana)
        print(toka_taso, merkkeja/sanoja)


# def sanasto():
#     #lemmatisointi
#     #remove duplicates
#     #count

# def virkemäärä():
#     #count virkkeet

# def virkepituus():
#     # laske virkkeet sanoina
#     # laske virkkeet grafeemeina
#     # laske virkkeet lauseina
#     # keskiarvo kaikista

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
