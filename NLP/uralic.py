# Tiedosto, jossa käsitellään kaikki UralicNLP-kirjaston funktiot

from uralicNLP import uralicApi
from tokenisointi import tokenisoi_sanat, tokenisoi_virkkeet
from nltk import Counter
import statistics
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy


# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

# Tulostetaan teksteittäin ja blogeittain löydettyjen sanaluokkien määrät
def sanaluokat(korpus):
    for blogi in korpus:
        print(eka_taso, blogi)

        saneitaBlogi = 0

        # Sanaluokkamuuttujat (UD2) blogille
        adj = 0
        adv = 0
        noun = 0
        verb = 0
        num = 0
        part = 0
        pron = 0
        acr = 0

        for teksti in korpus[blogi]:
            print(toka_taso, teksti, ":")

            #Sanaluokkamuuttujat tekstille
            adjTeksti= 0
            advTeksti = 0
            nounTeksti = 0
            verbTeksti = 0
            numTeksti = 0
            partTeksti = 0
            pronTeksti = 0
            acrTeksti = 0

            saneet = tokenisoi_sanat(korpus[blogi][teksti])

            # Lasketaan saneiden määrä teksteittäin...
            saneitaTeksti = len(saneet)

            # ...ja samalla kasvatetaan koko blogin saneiden määrää.
            saneitaBlogi += saneitaTeksti

            for sane in saneet:
                try:
                    # Morfologinen analyysi uralicNLP:n avulla,
                    # josta erotellaan sanaluokka
                    tulos = uralicApi.analyze(sane, "fin")
                    if (len(tulos) > 0):
                        analyysi = tulos[0][0]
                        osat = analyysi.split("+", 2)
                        lauseenjasen = ""
                        if len(osat) > 1:
                            lauseenjasen = osat[1]
                            match lauseenjasen:
                                case "A":
                                    adj += 1
                                    adjTeksti += 1
                                case "ACR":
                                    acr += 1
                                    acrTeksti += 1
                                case "Adv":
                                    adv += 1
                                    advTeksti += 1
                                case "N":
                                    noun += 1
                                    nounTeksti += 1
                                case "Num":
                                    num += 1
                                    numTeksti += 1
                                case "V":
                                    verb += 1
                                    verbTeksti += 1
                                case "Pcle":
                                    part += 1
                                    partTeksti += 1
                                
                                #En tiedä mikä on Pcle#voi, mutta niitä löytyi paljon :D
                                case "Pcle#voi":
                                    part += 1
                                    partTeksti += 1
                                case "Po":
                                    adj += 1
                                    adjTeksti += 1
                                case "Pron":
                                    pron += 1
                                    pronTeksti += 1
                except:
                    print(kolmas_taso, "Virhe sanaluokkajäsennyksessä. Vian aiheuttanut sane: ", sane)

            print(kolmas_taso, "Adj ", adjTeksti)
            print(kolmas_taso, "Adj (%) ", round((adjTeksti)/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "ACR ", acrTeksti)
            print(kolmas_taso, "ACR (%) ", round(acrTeksti/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "N ", nounTeksti)
            print(kolmas_taso, "N (%) ", round(nounTeksti/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "Num ", numTeksti)
            print(kolmas_taso, "Num (%) ", round(numTeksti/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "V ", verbTeksti)
            print(kolmas_taso, "V (%) ", round(verbTeksti/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "Pcle & Pcle#voi", partTeksti)
            print(kolmas_taso, "Pcle & Pcle#voi (%) ", round(partTeksti/saneitaTeksti*100, 2), " %")
            print(kolmas_taso, "Pron ", pronTeksti)
            print(kolmas_taso, "Pron (%) ", round(pronTeksti/saneitaTeksti*100, 2), " %")

    print(toka_taso, "Blogissa: ")
    print(kolmas_taso, "Adj ", round((adj)/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "ACR ", round(acr/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "N ", round(noun/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "Num ", round(num/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "V ", round(verb/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "Pcle & Pcle#voi", round(part/saneitaBlogi*100, 2), " %")
    print(kolmas_taso, "Pron ", round(pron/saneitaBlogi*100, 2), " %")

# Etsitään erisnimet tekstistä.
# Helmi on manuaalisesti myös luonut erisnimitiedoston, mutta
# tämä funktio pätee kaikkiin manhdollisiin teksitiedostoihin.
def erisnimetTeksti(teksti, nlp):
    tagit = nlp(teksti)

    # Lista kaikista NER-tägeistä
    ners = ["PERSON", "GPE", "LOC", "DATE", "TIME", "MONEY", "QUANTITY", "ORDINAL"
            "CARDINAL"] 

    erisnimet = []
    for sana in tagit.ents:
        if (sana.label_ in ners):
            erisnimet.append(sana.text)
    
    return erisnimet

# Käydään korpus läpi silmukassa ja muodostetaan jokaiselle
# tekstille lista siinä esiintyvistä erisnimistä
def erisnimetKorpus(korpus):
    nlp = spacy.load("fi_core_news_sm")
    tulos = {}
    for blogi in korpus:

        print(eka_taso, blogi)
        tulos[blogi] = {}
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)

            erisnimet = erisnimetTeksti(teksti, nlp)

            print(kolmas_taso, erisnimet)
            korpus[blogi][teksti] = erisnimet
    
    return tulos

# 
def hapaxlegomenon(korpus):
    print("Hapax legomena:")
    hapax = {}
    for blogi in korpus:
        print(eka_taso, blogi)

        # Käydään blogitekstit yksi kerrallaan läpi.
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            saneet = tokenisoi_sanat(korpus[blogi][teksti])
    
            # Alustetaan muuttuja, johon kerätään yhden tekstin kaikki lemmat.
            lemmat = []

            # Käydään tekstin saneet kerrallaan läpi.
            for sane in saneet:
                try:
                    # Lemmataan jokainen sane. 
                    lemma = uralicApi.lemmatize(sane.lower(), "fin", word_boundaries=False)
                    if (len(lemma) > 0):
                        # Lisätään sane lemmalistaan.
                        lemmat.append(lemma[0])

                    # Mikäli lemmaa ei löydy, lisätään sane sellaisenaan tyyppilistaan.
                    elif (len(lemma) == 0):
                        lemmat.append(sane)
                except:
                    print(kolmas_taso, "Virhe lemmauksessa. Vian aiheuttanut sane: ", sane)

            # Haetaan uniikit lemmat saneista muuttamalla lemmalista setiksi.
            tyypit = set(lemmat)
            print(kolmas_taso, "Uniikkeja sanoja: ", len(tyypit))

# TTR = tekstin tyypit (= uniikit sanat) / tokeneilla (saneilla)
# Mitä lähempänä TTR on numeroa 1, sitä enemmän sanastollista monipuolisuutta.
def ttr(korpus):
    for blogi in korpus:
        print(eka_taso, blogi)

        # Koko blogia koskevat laskurit.
        saneitaBlogi = 0
        tyypitBlogi = 0

        # Käydään blogitekstit yksi kerrallaan läpi.
        for teksti in korpus[blogi]:
            print(toka_taso, teksti)
            saneet = tokenisoi_sanat(korpus[blogi][teksti])

            # Lasketaan saneiden määrä teksteittäin...
            saneitaTeksti = len(saneet)

            # ...ja samalla kasvatetaan koko blogin saneiden määrää.
            saneitaBlogi += saneitaTeksti
            print(kolmas_taso, "saneita: ", saneitaTeksti)
            
            # Alustetaan muuttuja, johon kerätään yhden tekstin kaikki lemmat.
            lemmat = []

            # Käydään tekstin saneet kerrallaan läpi.
            for sane in saneet:
                try:
                    # Lemmataan jokainen sane. 
                    lemma = uralicApi.lemmatize(sane.lower(), "fin", word_boundaries=False)
                    if (len(lemma) > 0):
                        # Lisätään sane lemmalistaan.
                        lemmat.append(lemma[0])

                    # Mikäli lemmaa ei löydy, lisätään sane sellaisenaan tyyppilistaan.
                    elif (len(lemma) == 0):
                        lemmat.append(sane)
                except:
                    print(kolmas_taso, "Virhe lemmauksessa. Vian aiheuttanut sane: ", sane)

            # Haetaan uniikit lemmat saneista muuttamalla lemmalista setiksi.
            tyypit = set(lemmat)
            print(kolmas_taso, "tyyppejä: ", len(tyypit))
            print(kolmas_taso, "TTR: ", len(tyypit)/saneitaTeksti)
            
            tyypitBlogi += len(tyypit)
        print(toka_taso, "Blogissa saneita: ", saneitaBlogi)
        print(toka_taso, "Blogissa tyyppejä: ", tyypitBlogi)
        print(toka_taso, "Blogin TTR: ",tyypitBlogi/saneitaBlogi)

# Sanoissa morfeemien määrien keskiarvo, moodi, mediaani, minimi, maksimi,
# vaihteluväli, keskihajonta ja varianssi teksteittäin ja blogeittain
def morfeemit(korpus):
    print("Morfeemitilastoja:")
    for blogi in korpus:
        morfeemejaBlogissa = 0
        sanojaBlogissa = 0

        # Listamuuttuja, johon laitetaan kaikkien blogien tekstien sanojen morfeemien määrät.
        morfeemejaBlogiLista = []

        print(eka_taso, blogi, ":")
        for teksti in korpus[blogi]:
            print(toka_taso, teksti, ":")
            sanojaTekstissa = len(tokenisoi_sanat(korpus[blogi][teksti]))
            sanojaBlogissa += sanojaTekstissa 
            morfeemeja = 0

            # Listamuuttuja, johon laitetaan kaikki tekstin sanojen morfeemien määrät.
            morfeemejaTekstiLista = []

            # Tokenisoidaan teksti sanoiksi.
            tokenit = tokenisoi_sanat(korpus[blogi][teksti])

            # Käydään tokenit kerralla läpi ja uralicAPI-kirjaston avulla etsitään niistä morfeemit.
            
            for token in tokenit:
                try: 
                    morfeemit = uralicApi.segment(token, "fin")
                    if (len(morfeemit) > 0):
                        # Funktio palauttaa kaikki sanan mahdolliset morfeemiyhdistelmät.
                        # Laskennan ja analyysin helpottamiseksi valitaan aina ensimmäinen vaihtoehto.
                        morfeemeja += len(morfeemit[0])
                        morfeemejaBlogissa += len(morfeemit[0])

                        # Lisätään löydettyjen morfeemien määrät listoihin.
                        morfeemejaBlogiLista.append(len(morfeemit[0]))
                        morfeemejaTekstiLista.append(len(morfeemit[0]))
                except:
                    print(kolmas_taso, "Virhe morfologisessa analyysissa. Vian aiheuttanut tokeni: ", token)

            # Tekstikohtaiset tilastot.
            minMorf = min(morfeemejaTekstiLista)
            maxMorf = max(morfeemejaTekstiLista)        

            print(kolmas_taso, "morfeemeja (avg)", round(morfeemeja/sanojaTekstissa, 2))
            print(kolmas_taso, "morfeemeja (median)", statistics.median(morfeemejaTekstiLista))
            print(kolmas_taso, "morfeemeja (moodi)", statistics.mode(morfeemejaTekstiLista))
            print(kolmas_taso, "morfeemeja (min)", minMorf)
            print(kolmas_taso, "morfeemeja (max)", maxMorf)
            print(kolmas_taso, "vaihteluväli: ", maxMorf-minMorf)
            print(kolmas_taso, "keskihajonta: ", statistics.stdev(morfeemejaTekstiLista))
            print(kolmas_taso, "varianssi: ", statistics.variance(morfeemejaTekstiLista))

        # Blogikohtaiset tilastot.
        minMorfBlogi = min(morfeemejaBlogiLista)
        maxMorfBlogi = max(morfeemejaBlogiLista)  
        print(toka_taso, "Blogin sanoissa morfeemeja (avg): ", round(morfeemejaBlogissa/sanojaBlogissa, 2))
        print(toka_taso, "Blogin sanoissa morfeemeja (median): ", statistics.median(morfeemejaBlogiLista))
        print(toka_taso, "Blogin sanoissa morfeemeja (moodi): ", statistics.mode(morfeemejaBlogiLista) )
        print(toka_taso, "Blogin sanoissa morfeemeja (min): ", minMorfBlogi)
        print(toka_taso, "Blogin sanoissa morfeemeja (max): ", maxMorfBlogi)
        print(toka_taso, "Blogin morfeemien määrän vaihteluväli: ", maxMorfBlogi-minMorfBlogi)
        print(toka_taso, "Blogin morfeemien määrän keskihajonta: ", statistics.stdev(morfeemejaBlogiLista))
        print(toka_taso, "Blogin morfeemien määrän varianssi: ", statistics.variance(morfeemejaBlogiLista))

# Lemmausfunktio. jossa jokaisen tekstin sana lemmataan. 
# Mikäli sanalle tarjoaan useampaa lemmaa,
# valitaan ensimmäinen. Virheitä siis tulee, mutta ohjelma
# porskuttaa eteenmpäin.
def lemmaus(korpus):
    lemmaDictKorpus = {}
    for blogi in korpus:
        lemmaDictKorpus[blogi] = {}
        for teksti in korpus[blogi]:
            # Tokenisoidaan teksti sanalistaksi
            saneet = tokenisoi_sanat(korpus[blogi][teksti])

            # Lista, johon tallennetaan yhden tekstin saneet
            lemmalista = []
            for sane in saneet:
                try:
                    lemma = uralicApi.lemmatize(sane, "fin", word_boundaries=False)
                    if (len(lemma) > 0):
                        lemmalista.append(lemma[0])
                except:
                    print("Lemmaus epäonnistui, sane: ", sane)
            
            lemmaDictKorpus[blogi][teksti] = lemmalista
        
    return lemmaDictKorpus

# Pääohjelmassa kutsuttava funktio, joka kutsuu kaikkia muita asetusten mukaan.
def uralic(asetukset, korpus):
    #lemmat(korpus)
    if asetukset["Morfeemeja sanoissa"] == True:
        morfeemit(korpus)
    if asetukset["Type-token ratio"] == True:
        ttr(korpus)
    if asetukset["Sanaluokkien frekvenssit"] == True:
        sanaluokat(korpus)
    if asetukset["Hapax Legomena"] == True:
        hapaxlegomenon(korpus)
    if asetukset["Erisnimet"] == True:
        erisnimetKorpus(korpus)
        