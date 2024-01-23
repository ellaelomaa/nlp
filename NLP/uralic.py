# Tiedosto, jossa käsitellään kaikki UralicNLP-kirjaston funktiot

from uralicNLP import uralicApi
from tokenisointi import tokenisoi_sanat, tokenisoi_virkkeet
from nltk import Counter
import statistics
from collections import Counter

eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

# Muuttujat sisentämään tulosteiden rivejä luettavuuden helpottamiseksi.
eka_taso = "  "
toka_taso = "    "
kolmas_taso = "      "

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
                # Lemmataan jokainen sane. 
                lemma = uralicApi.lemmatize(sane.lower(), "fin", word_boundaries=False)
                if (len(lemma) > 0):
                    # Lisätään sane lemmalistaan.
                    lemmat.append(lemma[0])

                # Mikäli lemmaa ei löydy, lisätään sane sellaisenaan tyyppilistaan.
                elif (len(lemma) == 0):
                    lemmat.append(sane)

            # Haetaan uniikit lemmat saneista muuttamalla lemmalista setiksi.
            tyypit = set(lemmat)
            print(kolmas_taso, "tyyppejä: ", len(tyypit))
            print(kolmas_taso, "TTR: ", len(tyypit)/saneitaTeksti)
            
            tyypitBlogi += len(tyypit)
        print(toka_taso, "Blogissa saneita: ", saneitaBlogi)
        print(toka_taso, "Blogissa tyyppejä: ", tyypitBlogi)
        print(toka_taso, "Blogin TTR: ",tyypitBlogi/saneitaBlogi)

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
                morfeemit = uralicApi.segment(token, "fin")
                if (len(morfeemit) > 0):
                    # Funktio palauttaa kaikki sanan mahdolliset morfeemiyhdistelmät.
                    # Laskennan ja analyysin helpottamiseksi valitaan aina ensimmäinen vaihtoehto.
                    morfeemeja += len(morfeemit[0])
                    morfeemejaBlogissa += len(morfeemit[0])

                    # Lisätään löydettyjen morfeemien määrät listoihin.
                    morfeemejaBlogiLista.append(len(morfeemit[0]))
                    morfeemejaTekstiLista.append(len(morfeemit[0]))

            # Tekstikohtaiset tilastot.
            minMorf = min(morfeemejaTekstiLista)
            maxMorf = max(morfeemejaTekstiLista)        

            print(kolmas_taso, "morfeemeja (avg)", round(morfeemeja/sanojaTekstissa, 2))
            print(kolmas_taso, "morfeemeja (median)", statistics.median(morfeemejaTekstiLista))
            print(kolmas_taso, "morfeemeja (moodi)", statistics.mode(morfeemejaTekstiLista))
            print(kolmas_taso, "morfeemeja (min)", minMorf)
            print(kolmas_taso, "morfeemeja (max)", maxMorf)
            print(kolmas_taso, "vaihteluväli: ", maxMorf-minMorf)
            print(kolmas_taso, "keskihajonta: ", statistics.stdev(morfeemejaTekstiLista), 4)
            print(kolmas_taso, "varianssi: ", statistics.variance(morfeemejaTekstiLista), 4)

        # Blogikohtaiset tilastot.
        minMorfBlogi = min(morfeemejaBlogiLista)
        maxMorfBlogi = max(morfeemejaBlogiLista)  
        print(toka_taso, "Blogin sanoissa morfeemeja (avg): ", round(morfeemejaBlogissa/sanojaBlogissa, 2))
        print(toka_taso, "Blogin sanoissa morfeemeja (median): ", statistics.median(morfeemejaBlogiLista))
        print(toka_taso, "Blogin sanoissa morfeemeja (moodi): ", statistics.mode(morfeemejaBlogiLista) )
        print(toka_taso, "Blogin sanoissa morfeemeja (min): ", minMorfBlogi)
        print(toka_taso, "Blogin sanoissa morfeemeja (max): ", maxMorfBlogi)
        print(toka_taso, "Blogin morfeemien määrän vaihteluväli: ", maxMorfBlogi-minMorfBlogi)
        print(toka_taso, "Blogin morfeemien määrän keskihajonta: ", statistics.stdev(morfeemejaBlogiLista), 4)
        print(toka_taso, "Blogin morfeemien määrän varianssi: ", statistics.variance(morfeemejaBlogiLista), 4)

# Lemmausfunktio. jossa jokaisen tekstin sana lemmataan. 
# Mikäli sanalle tarjoaan useampaa lemmaa,
# valitaan ensimmäinen. Virheitä siis tulee, mutta ohjelma
# porskuttaa eteenmpäin.
def lemmat(korpus):
    lemmaDictKorpus = {}
    for blogi in korpus:
        for teksti in korpus[blogi]:
            lemmaDictTeksti = {}
            saneet = tokenisoi_sanat(korpus[blogi][teksti])

            # Lista, johon tallennetaan yhden tekstin saneet
            lemmalista = []
            for sane in saneet:
                lemma = uralicApi.lemmatize(sane, "fin", word_boundaries=False)
                if (len(lemma) > 0):
                    lemmalista.append(lemma[0])
            
            lemmaDictTeksti[teksti] = lemmalista
            lemmaDictKorpus[blogi] = lemmaDictTeksti
        
    return lemmaDictKorpus

# Pääohjelmassa kutsuttava funktio, joka kutsuu kaikkia muita asetusten mukaan.
def uralic(asetukset, korpus):
    #lemmat(korpus)
    if asetukset["morfeemit"] == True:
        morfeemit(korpus)
    if asetukset["TTR"] == True:
        ttr(korpus)
        