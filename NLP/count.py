import tokenisointi
import regex as re
# import numpy as np

# Tässä tiedostossa lasketaan kaikki perustilastot ilman kielen
# käsittelyä ja NLP-kirjastoja

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

# Kokonaissanamäärä blogiteksteittäin
def sanamaara(korpus):
    print("Kokonaissanamäärät:")
    
    for blogi in korpus:
        sanoja = 0
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            tekstiPituus = len(tokenisointi.tokenisoi_sanat(korpus[blogi][teksti]))
            print(toka_taso, teksti, ": ", tekstiPituus)
            sanoja += tekstiPituus
        print(toka_taso, "Sanoja yhteensä blogissa: ", sanoja)

def sanapituus(korpus):
    print("Sanojen keskimääräinen pituus:")

    for blogi in korpus:
        sanojaBlogissa = 0
        merkkejaBlogissa = 0
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            sanalista = tokenisointi.tokenisoi_sanat(korpus[blogi][teksti])
            sanojaTekstissa = len(sanalista)
            merkkejaTekstissa = 0
            sanojaBlogissa += sanojaTekstissa

            for sana in sanalista:
                merkkejaTekstissa += len(sana)
                merkkejaBlogissa += len(sana)
            print(toka_taso, teksti, round(merkkejaTekstissa/sanojaTekstissa, 2))

        if (sanojaBlogissa > 0 and merkkejaBlogissa > 0):
            print(toka_taso, blogi, "yleensä: ", round(merkkejaBlogissa/sanojaBlogissa, 2))

def virkemaara(korpus):
    print("Virkkeiden määrä:")
    for blogi in korpus:
        lauseita = 0
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            lausepituus = len(tokenisointi.tokenisoi_lauseet(korpus[blogi][teksti]))
            print(toka_taso, teksti, ": ", lausepituus)
            lauseita += lausepituus
        print(toka_taso, "Virkkeitä yhteensä blogissa : ", lauseita)

def sanojaVirkkeissa(korpus):
    print("Keskimääräinen virkkeiden pituus teksteissä:")
    for blogi in korpus:
        sanojaBlogissa = 0
        virkkeitaBlogissa = 0
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            sanojaTekstissa = len(tokenisointi.tokenisoi_sanat(korpus[blogi][teksti]))
            sanojaBlogissa += sanojaTekstissa
            virkkeitaTekstissa = len(tokenisointi.tokenisoi_virkkeet(korpus[blogi][teksti]))
            virkkeitaBlogissa += virkkeitaTekstissa
            print(toka_taso, teksti, ": ", round(sanojaTekstissa/virkkeitaTekstissa, 2))
        print(toka_taso, "Blogissa keskimäärin sanoja virkkeissä: ", round(sanojaBlogissa/virkkeitaBlogissa, 2))

def grafeemeina(korpus):
    print("Keskimäärin grafeemeja sanoissa:")
    # Käydään korpus blogi kerrallaan läpi

    for blogi in korpus:
        # Alustetaan muuttujat koko blogia koskeville muuttujille.
        sanojaBlogissa = 0
        merkkejaBlogissa = 0
        print(eka_taso, blogi)

        # Käydään blogin tekstit kerrallaan läpi
        for teksti in korpus[blogi]:
            merkkejaTekstissa = 0

            # Keskiarvoa varten lasketaan sanojen määrä tekstissä
            sanalista = tokenisointi.tokenisoi_sanat(korpus[blogi][teksti])
            sanojaTekstissa = len(sanalista)

            # Kasvatetaan samalla koko blogin sanamäärää laskevaa muuttujaa
            sanojaBlogissa += len(sanalista)

            # Lasketaan, kuinka pitkiä sanat ovat teksteittäin
            for sana in sanalista:
                merkkejaTekstissa += len(sana)
                merkkejaBlogissa += len(sana)

            print(toka_taso, teksti, round(merkkejaTekstissa/sanojaTekstissa, 2))
        print(toka_taso, blogi, "yleensä: ", round(merkkejaBlogissa/sanojaBlogissa, 2))

    print("Keskimäärin grafeemeja virkkeissä:")
    
    
    for blogi in korpus:
        # Alustetaan muuttujat keskiarvon laskua varten
        virkkeitaBlogissa = 0
        merkkejaBlogissa = 0

        print(eka_taso, blogi)

        for teksti in korpus[blogi]:
            # Grafeemeja ovat myös välimerkit, joten niitä ei tarvitse poistaa
            merkkejaTekstissa = len(korpus[blogi][teksti])
            merkkejaBlogissa += merkkejaTekstissa

            virkkeitaTekstissa = len(tokenisointi.tokenisoi_lauseet(korpus[blogi][teksti]))
            virkkeitaBlogissa += virkkeitaTekstissa
            print(toka_taso, teksti, round(merkkejaTekstissa/virkkeitaTekstissa, 2))
        print(toka_taso, blogi, "yleensä: ", round(merkkejaBlogissa/virkkeitaBlogissa, 2))

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

def keskiarvot(korpus, graf, sanat, lauseet):
    print("Sana-, lause- ja virkepituus keskiarviona:")
    if graf == True:
        grafeemeina(korpus)
    if sanat == True:
        sanoina(korpus)
    if lauseet == True:
        lauseina(korpus)

def tilastoja(asetukset, korpus):
    if asetukset["sanamaarat"] == True:
        sanamaara(korpus)
    if asetukset["virkemaarat"] == True:
        virkemaara(korpus)
    if asetukset["sanapituus"] == True:
        sanapituus(korpus)
    if asetukset["grafeemit"] == True:
        grafeemeina(korpus)
    if asetukset["virkesana"] == True:
        sanojaVirkkeissa(korpus)
        

# def varianssi():
#     data = 
#     variance = np.var(data)

# def keskihajonta():
#     data = 
#     standard_deviation = np.std(data)
