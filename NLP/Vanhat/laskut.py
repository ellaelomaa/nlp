import spacy
import tokenisointi
import hae
import uralic
import statistics
import nltk
import statistics
from uralicNLP import uralicApi
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from itertools import groupby
import main
# import numpy as np

# Tässä tiedostossa lasketaan kaikki perustilastot ilman kielen
# käsittelyä ja NLP-kirjastoja

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

# Kokonaissanamäärä blogiteksteittäin ja blogeittain
def sanamaara(korpus):
    for kirjoittaja in korpus:
        sanojaKirjoittaja = 0
        for teksti in korpus[kirjoittaja]:
            sanojaTekstissa = len(tokenisointi.tokenisoi_sanat(korpus[kirjoittaja][teksti]))
            main.lisaaTaulukkoon("Teksteittäin", sanojaTekstissa, "Sanamäärä", teksti)
            sanojaKirjoittaja += sanojaTekstissa
        main.lisaaTaulukkoon("Teksteittäin", sanojaKirjoittaja, "Sanamäärä", kirjoittaja)

# Lasketaan lauseiden määrä ja sanojen määrän keskiarvo,
# mediaani, moodi, minimi, maksimi, vaihteluväli, keskihajonta
# ja varianssi lauseissa teksteittäin
def lausetilastoja():
    print("Lausetilastoja: ")
    korpus = hae.hae_jasennetty()

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
    for kirjoittaja in korpus:
        lauseitaBlogissa = 0
        for teksti in korpus[kirjoittaja]:
            lauseitaTekstissa = len(tokenisointi.tokenisoi_virkkeet(korpus[kirjoittaja][teksti]))
            main.lisaaTaulukkoon("Teksteittäin", lauseitaTekstissa, "Virkemäärä", teksti)
            lauseitaBlogissa += lauseitaTekstissa
        main.lisaaTaulukkoon("Teksteittäin", lauseitaBlogissa, "Virkemäärä", kirjoittaja)

# Sanojen määrien keskiarvo ja keskihajonta teksteittäin ja blogeittain
def sanojaVirkkeissa(korpus):
    print("Keskimääräinen virkkeiden pituus teksteissä:")
    for kirjoittaja in korpus:
        sanatBlogissaLista = []
        print(eka_taso, kirjoittaja)
        for teksti in korpus[kirjoittaja]:
            print(toka_taso, teksti)
            
            virkkeet = tokenisointi.tokenisoi_virkkeet(korpus[kirjoittaja][teksti])
            sanojaVirkkeissa = []
            for virke in virkkeet:
                virke = tokenisointi.tokenisoi_sanat(virke)
                sanojaVirkkeissa.append(len(virke))
                sanatBlogissaLista.append(len(virke))

            print(kolmas_taso, "Tekstissä keskimäärin sanoja virkkeissä: ", round(statistics.mean(sanojaVirkkeissa), 2))
            main.lisaaTaulukkoon("Teksteittäin", round(statistics.mean(sanojaVirkkeissa), 2), "Virkepituus sanoina (avg)", teksti)
            main.lisaaTaulukkoon("Teksteittäin", round(statistics.stdev(sanojaVirkkeissa), 2), "Virkepituus sanoina (keskihajonta)", teksti)
            print(kolmas_taso, "Keskihajonta: ", round(statistics.stdev(sanojaVirkkeissa), 2))
        print(toka_taso, "Blogissa keskimäärin sanoja virkkeissä: ", round(statistics.mean(sanatBlogissaLista), 2))
        main.lisaaTaulukkoon("Teksteittäin", round(statistics.mean(sanatBlogissaLista), 2), "Virkepituus sanoina (avg)", kirjoittaja)
        main.lisaaTaulukkoon("Teksteittäin", round(statistics.stdev(sanatBlogissaLista), 2), "Virkepituus sanoina (keskihajonta)", kirjoittaja)
        print(toka_taso, "Keskihajonta: ", round(statistics.stdev(sanatBlogissaLista), 2))

# Lauseiden määrien keskiarvo, mediaani, moodi, minimi, maksimi,
# vaihteluväli, keskihajonta ja varianssi teksteittäin
def lauseitaVirkkeissa():
    print("Lauseita virkkeissä:")
    korpus = hae.hae_jasennetty()
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
    # Käydään korpus blogi kerrallaan läpi

    for kirjoittaja in korpus:
        # Alustetaan muuttujat koko blogia koskeville muuttujille.
        sanojaKirjoittaja = 0
        merkkejaKirjoittaja = 0

        # Käydään blogin tekstit kerrallaan läpi
        for teksti in korpus[kirjoittaja]:
            merkkejaTekstissa = 0

            # Keskiarvoa varten lasketaan sanojen määrä tekstissä
            sanalista = tokenisointi.tokenisoi_sanat(korpus[kirjoittaja][teksti])
            sanojaTekstissa = len(sanalista)

            # Kasvatetaan samalla koko blogin sanamäärää laskevaa muuttujaa
            sanojaKirjoittaja += len(sanalista)

            # Lasketaan, kuinka pitkiä sanat ovat teksteittäin
            for sana in sanalista:
                merkkejaTekstissa += len(sana)
                merkkejaKirjoittaja += len(sana)

            main.lisaaTaulukkoon("Teksteittäin", round(merkkejaTekstissa/sanojaTekstissa, 2), "Grafeemeja sanoissa", teksti)
        main.lisaaTaulukkoon("Teksteittäin", round(merkkejaKirjoittaja/sanojaKirjoittaja, 2), "Grafeemeja sanoissa", kirjoittaja)

    #print("Keskimäärin grafeemeja virkkeissä:")
    
    for kirjoittaja in korpus:
        # Alustetaan muuttujat keskiarvon laskua varten
        virkkeetKirjoittaja = 0
        merkkejaKirjoittaja = 0


        for teksti in korpus[kirjoittaja]:
            # Grafeemeja ovat myös välimerkit, joten niitä ei tarvitse poistaa
            merkkejaTekstissa = len(korpus[kirjoittaja][teksti])
            merkkejaKirjoittaja += merkkejaTekstissa

            virkkeitaTekstissa = len(tokenisointi.tokenisoi_lauseet(korpus[kirjoittaja][teksti]))
            virkkeetKirjoittaja += virkkeitaTekstissa
            main.lisaaTaulukkoon("Teksteittäin", round(merkkejaTekstissa/virkkeitaTekstissa, 2), "Grafeemeja virkkeissä", teksti)
        main.lisaaTaulukkoon("Teksteittäin", round(merkkejaKirjoittaja/virkkeetKirjoittaja, 2), "Grafeemeja virkkeissä", kirjoittaja)  

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
            rivi = 2
            tokenit = tokenisointi.tokenisoi_sanat(korpus[blogi][teksti])
            dist = nltk.FreqDist(sana.lower() for sana in tokenit)
            yleisimmat = dist.most_common(maara)

            # Muutetaan tuple merkkijonoksi
            for tup in yleisimmat:
                arvo = " : "
                arvo = arvo.join(map(str, tup))

                main.lisaaHFL(arvo, rivi, teksti)
                rivi += 1

# Yule K'n funktio kertoo kielen rikkaudesta. Mitä suurempi luku, sitä vähemmän
# kompleksisuutta. Yule I:ssä käänteinen: korkeampi luku, enemmän rikkautta.
def yulelaskut(teksti, otsikko,valinta):
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
            main.lisaaTaulukkoon("Teksteittäin", 10000*(M2-M1)/(M1*M1), "Yule K", otsikko)
            print(kolmas_taso, "Yule K: ", 10000*(M2-M1)/(M1*M1))
        except ZeroDivisionError:
            print("Virhe Yule K:n laskennassa.")
    else:
        try:
            print(kolmas_taso, "Yule I: ", (M1*M1)/(M2-M1))
            main.lisaaTaulukkoon("Teksteittäin", (M1*M1)/(M2-M1), "Yule I", otsikko)

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
                yulelaskut(korpus[blogi][teksti], teksti, "k")
            else:
                yulelaskut(korpus[blogi][teksti], teksti,"i")


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
    main.dataframeTaulukkoon("Kosinisimilaarisuus", df)

def tilastoja(asetukset, korpus):
    tulos = ""
    nlp = spacy.load("fi_core_news_sm")

    if asetukset["Sanamäärä"] == True:
        sanamaara(korpus)
    if asetukset["Virkemäärä"] == True:
        virkemaara(korpus)
    if asetukset["Grafeemeja sanoissa ja virkkeissä"] == True:
        grafeemeina(korpus)
    if asetukset["Virkepituus sanoina"] == True:
        sanojaVirkkeissa(korpus)
    # if asetukset["lausetilastot"] == True:
    #     lausetilastoja()
    # if asetukset["Virkepituus lauseina"] == True:
    #     lauseitaVirkkeissa()
    # if asetukset["erikoismerkit"] == True:
    #     erikoismerkit(korpus)
    if asetukset["HFL 50"] == True:
        hfl(korpus, 50)
    if asetukset["HFL 100"] == True:
        hfl(korpus, 100)
    if asetukset["Yule K"] == True:
        yule(korpus, "K")
    if asetukset["Yule I"] == True:
        yule(korpus, "I")
    if asetukset["Kosinisimilaarisuus"] == True:
        kosinisimilaarisuus(korpus, nlp)

    return tulos