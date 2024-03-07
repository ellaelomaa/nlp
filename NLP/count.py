import spacy
import tokenisointi
import regex as re
import fetch
import uralic
import statistics
import nltk
import statistics
from uralicNLP import uralicApi
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from itertools import groupby
# import numpy as np

# Tässä tiedostossa lasketaan kaikki perustilastot ilman kielen
# käsittelyä ja NLP-kirjastoja

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

# Kokonaissanamäärä blogiteksteittäin ja blogeittain
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
    

# Lasketaan sanojen pituuden keskiarvo ja keskihajonta
def sanapituus(korpus):
    print("Sanojen keskimääräinen pituus:")

    for blogi in korpus:
        sanojaBlogissa = 0
        merkkejaBlogissa = 0
        pituudetBlogissa = []
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            pituudetTeksti = []
            sanalista = tokenisointi.tokenisoi_sanat(korpus[blogi][teksti])
            sanojaTekstissa = len(sanalista)
            merkkejaTekstissa = 0
            sanojaBlogissa += sanojaTekstissa

            for sana in sanalista:
                merkkejaTekstissa += len(sana)
                merkkejaBlogissa += len(sana)
                pituudetTeksti.append(len(sana))
                pituudetBlogissa.append(len(sana))
            print(kolmas_taso, "Keskiarvo: ", round(merkkejaTekstissa/sanojaTekstissa, 2))
            print(kolmas_taso, "Keskihajonta: ", statistics.stdev(pituudetTeksti))

        if (sanojaBlogissa > 0 and merkkejaBlogissa > 0):
            print(toka_taso, "Keskiarvo: ", round(merkkejaBlogissa/sanojaBlogissa, 2))
            print(toka_taso, "keskihajonta: ", statistics.stdev(pituudetBlogissa))

# Lasketaan lauseiden määrä ja sanojen määrän keskiarvo,
# mediaani, moodi, minimi, maksimi, vaihteluväli, keskihajonta
# ja varianssi lauseissa teksteittäin
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

# Virkkeiden määrä tekteittäin ja blogeittain
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

# Sanojen määrien keskiarvo ja keskihajonta teksteittäin ja blogeittain
def sanojaVirkkeissa(korpus):
    print("Keskimääräinen virkkeiden pituus teksteissä:")
    for blogi in korpus:
        sanatBlogissaLista = []
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            
            virkkeet = tokenisointi.tokenisoi_virkkeet(korpus[blogi][teksti])
            sanojaVirkkeissa = []
            for virke in virkkeet:
                virke = tokenisointi.tokenisoi_sanat(virke)
                sanojaVirkkeissa.append(len(virke))
                sanatBlogissaLista.append(len(virke))

            print(kolmas_taso, "Tekstissä keskimäärin sanoja virkkeissä: ", round(statistics.mean(sanojaVirkkeissa), 2))
            print(kolmas_taso, "Keskihajonta: ", round(statistics.stdev(sanojaVirkkeissa), 2))
        print(toka_taso, "Blogissa keskimäärin sanoja virkkeissä: ", round(statistics.mean(sanatBlogissaLista), 2))
        print(toka_taso, "Keskihajonta: ", round(statistics.stdev(sanatBlogissaLista), 2))

# Lauseiden määrien keskiarvo, mediaani, moodi, minimi, maksimi,
# vaihteluväli, keskihajonta ja varianssi teksteittäin
def lauseitaVirkkeissa():
    print("Lauseita virkkeissä:")
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

# Funktio erikoismerkkien määrän laskemiseen teksteittäin
def erikoismerkit(korpus):
    print("Erikoismerkit teksteittäin:")
    for blogi in korpus:
        print(eka_taso, blogi, ":")
        for teksti in korpus[blogi]:
            print(toka_taso, teksti, ":")
            merkit = 0
            for merkki in korpus[blogi][teksti]:
                if merkki.isalpha() == False and merkki != " " and merkki != "\n":
                    merkit += 1
            
            print(kolmas_taso, "Yhteensä erikoismerkkejä: ", merkit)

# Tulostetaan x määrä yleisintä sanaa 
def hfl(korpus, maara):
    hfl = {}
    for blogi in korpus:
        print(eka_taso, blogi)
        hfl[blogi] = {}
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            tokenit = tokenisointi.tokenisoi_sanat(korpus[blogi][teksti])
            dist = nltk.FreqDist(sana.lower() for sana in tokenit)
            yleisimmat = dist.most_common(maara)
            hfl[blogi][teksti] = yleisimmat
            print(kolmas_taso, yleisimmat)
    
    return hfl

# Yule K'n funktio kertoo kielen rikkaudesta. Mitä suurempi luku, sitä vähemmän
# kompleksisuutta. Yule I:ssä käänteinen: korkeampi luku, enemmän rikkautta.
def yulelaskut(teksti, valinta):
    # M1: kaikkien saneiden määrä
    # M2: summa kaikkien lemmojen tuloista, (lemma * esiintymät^2)
    esiintymat = {}
    tokenit = tokenisointi.tokenisoi_sanat(teksti)

    for sane in tokenit:
        try:
            lemma = uralicApi.lemmatize(sane, "fin", word_boundaries=False)
            if (len(lemma) > 0):
                try:
                    avain = lemma[0]
                    esiintymat[avain] += 1
                except KeyError:
                    esiintymat[avain] = 1
        except:
            print("Lemmaus epäonnistui, sane: ", sane)
    
    M1 = float(len(esiintymat))
    M2 = sum([len(list(g)) * (freq**2) for freq, g in groupby(sorted(esiintymat.values()))])

    if (valinta == "k"):
        try:
            print(kolmas_taso, "Yule K: ", 10000*(M2-M1)/(M1*M1))
        except ZeroDivisionError:
            print("Virhe Yule K:n laskennassa.")
    else:
        try:
            print(kolmas_taso, "Yule I: ", (M1*M1)/(M2-M1))
        except ZeroDivisionError:
            print("Virhe Yule I:n laskennassa.")

# Käydään korpus teksteittäin läpi ja kutsutaan apufunktiota laskuihin
# https://swizec.com/blog/measuring-vocabulary-richness-with-python/
def yule(korpus, kirjain):
    print("Yule")
    for blogi in korpus:
        print(eka_taso, blogi)
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)

            if kirjain == "K":
                yulelaskut(korpus[blogi][teksti], "k")
            else:
                yulelaskut(korpus[blogi][teksti], "i")


# Funktio, jossa mistä tahansa listasta A voidaan poistaa lista B
def poistaLista(tokenit, poistettavat):
    lista = [sana for sana in tokenit if sana not in poistettavat]
    return lista

# Apufunktio kosinisimilaarisuuden laskentaan
def kirjailijapipeline(nlp, teksti):
    erisnimet = uralic.erisnimetTeksti(teksti, nlp)
    tokenit = tokenisointi.tokenisoi_sanat(teksti)
    ilmanErisnimia = poistaLista(tokenit, erisnimet)
    lemmat = []
    for sane in ilmanErisnimia:
        try:
            lemma = uralicApi.lemmatize(sane, "fin", word_boundaries=False)
            if (len(lemma) > 0):
                lemmat.append(lemma[0])
        except:
            print("Lemmaus epäonnistui, sane: ", sane)
    return lemmat

# Kosinisimilaarisuudella lasketaan kahden tekstin samankaltaisuutta.
# Vertailtavista teksteistä on erisnimet poistettu ja sanat lemmattu.
def kosinisimilaarisuus(korpus, nlp):
    print("Kosinisimilaarisuus")
    data = []
    nimet = []

    # Yhdistetään kaikki saman kirjailijan tekstit samaan muuttujaan
    for blogi in korpus:
        print("Käsiteltävä blogi: ", blogi)
        nimet.append(blogi)
        tekstit = ""
        for teksti in korpus[blogi]:
            tekstit = tekstit + korpus[blogi][teksti]
        sanalista = kirjailijapipeline(nlp, tekstit)
        data.append(" ".join(sanalista))

    Tfidf_vektori = TfidfVectorizer()
    vektorimatriisi = Tfidf_vektori.fit_transform(data)

    kosinimatriisi = cosine_similarity(vektorimatriisi)
    df = pd.DataFrame(data=kosinimatriisi, index= nimet, columns = nimet)
    print(df)

def tilastoja(asetukset, korpus):
    tulos = ""
    nlp = spacy.load("fi_core_news_sm")

    asetuslista = ["Sanamäärä", "Virkemäärä", "Grafeemeja sanoissa", 
                   "Virkepituus sanoina", "Virkepituus lauseina",
                   "Kosinisimilaarisuus"]
    

    if asetukset["Sanamäärä"] == True:
        sanamaara(korpus)
    if asetukset["Virkemäärä"] == True:
        virkemaara(korpus)
    if asetukset["Grafeemeja sanoissa"] == True:
        grafeemeina(korpus)
    if asetukset["Virkepituus sanoina"] == True:
        sanojaVirkkeissa(korpus)
    # if asetukset["lausetilastot"] == True:
    #     lausetilastoja()
    if asetukset["Virkepituus lauseina"] == True:
        lauseitaVirkkeissa()
    # if asetukset["erikoismerkit"] == True:
    #     erikoismerkit(korpus)
    # if asetukset["hfl"] == True:
    #     if asetukset["50"] == True:
    #         hfl(korpus, 50)
    #     else:
    #         hfl(korpus, 100)
    if asetukset["Yule K"] == True:
        yule(korpus, "K")
    if asetukset["Yule I"] == True:
        yule(korpus, "I")
    if asetukset["Kosinisimilaarisuus"] == True:
        kosinisimilaarisuus(korpus, nlp)

    return tulos