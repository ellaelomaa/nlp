import tokenisointi
import regex as re
import os
import fetch
import statistics
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

def lausetilastoja():
    print("Lausetilastoja: ")
    korpus = fetch.hae_jasennetty()

    for blogi in korpus:
        lauseita = 0
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            print(toka_taso, teksti, ":")
            lauseet = tokenisointi.tokenisoi_lauseet(korpus[blogi][teksti])
            lauseita = len(lauseet)
            sanamaarat = []
            for lause in lauseet:
                sanat = tokenisointi.tokenisoi_sanat(lause)
                sanamaarat.append(len(sanat))

            # Tekstikohtaiset tilastot
            print(kolmas_taso, "lauseita tekstissä: ", lauseita)
            print(kolmas_taso, "sanoja (mean): ", statistics.mean(sanamaarat))
            print(kolmas_taso, "sanoja (median): ", statistics.median(sanamaarat))
            print(kolmas_taso, "sanoja (moodi): ", statistics.mode(sanamaarat))
            print(kolmas_taso, "sanoja (min): ", min(sanamaarat))
            print(kolmas_taso, "sanoja (max): ", max(sanamaarat))
            print(kolmas_taso, "vaihteluväli: ", max(sanamaarat)-min(sanamaarat))
            print(kolmas_taso, "keskihajonta: ", statistics.stdev(sanamaarat))
            print(kolmas_taso, "varianssi: ", statistics.variance(sanamaarat))

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

def lauseitaVirkkeissa():
    korpus = fetch.hae_jasennetty()
    for blogi in korpus:
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            virkkeet = tokenisointi.tokenisoi_virkkeet(korpus[blogi][teksti])
            lausemaarat = []
            for virke in virkkeet:
                lauseet = tokenisointi.tokenisoi_lauseet(virke)
                lausemaarat.append(len(lauseet))
            
            # Tekstikohtaiset tilastot
            print(kolmas_taso, "lauseita (mean): ", statistics.mean(lausemaarat))
            print(kolmas_taso, "lauseita (median): ", statistics.median(lausemaarat))
            print(kolmas_taso, "lauseita (moodi): ", statistics.mode(lausemaarat))
            print(kolmas_taso, "lauseita (min): ", min(lausemaarat))
            print(kolmas_taso, "lauseita (max): ", max(lausemaarat))
            print(kolmas_taso, "vaihteluväli: ", max(lausemaarat)-min(lausemaarat))
            print(kolmas_taso, "keskihajonta: ", statistics.stdev(lausemaarat))
            print(kolmas_taso, "varianssi: ", statistics.variance(lausemaarat))


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
    if asetukset["lausetilastot"] == True:
        lausetilastoja()
    if asetukset["virkelause"] == True:
        lauseitaVirkkeissa()