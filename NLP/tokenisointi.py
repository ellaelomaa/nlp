from nltk.tokenize import sent_tokenize
import nltk
import regex as re
from re import split

# Tarvitaan sent_tokenizen toimimiseen. Lataa vain kerran, sitten voi poistaa :)
#nltk.download("punkt")

# Funktio tokenisoimaan sanat, eli erottelemaan ne listaksi.
# Poistetaan samalla välimerkit, paitsi - ja '. 
def tokenisoi_sanat(teksti):
    valimerkiton = re.sub(r"[^\P{P}-'&]+", "", teksti)
    valimerkiton.replace("&", "ja")

    # Erotellaan välilyönnistä sanat listaksi.
    tokenit = valimerkiton.split()
    return tokenit

# Lauseiden tokenisointifunktio, eli lauseet erikoismerkistä erikoismerkkiin
# : , . ; ajatusviiva ! ?s
def tokenisoi_lauseet(teksti):

    # Poistetaan ensin rivinvaihdot.
    teksti = teksti.replace("\n", "")
    lauseet = re.split(', |-|! |\. |\.|\? |\(|\)|–|—|:', teksti)
    # Poistetaan tyhjät alkiot.
    lauseet = list(filter(None, lauseet))
    return lauseet

# Virkkeiden tokenisointifunktio, eli isosta alkukirjaimesta pisteeseen, 
# huutomerkkiin tai kysymyksmerkkiin.
def tokenisoi_virkkeet(teksti):
    virkkeet= sent_tokenize(teksti)
    return virkkeet

def tokenisoi(korpus, valinta):
    for avain in korpus:
        if valinta == "sanoiksi":
            korpus[avain] = tokenisoi_sanat(korpus[avain])
        elif valinta == "lauseiksi":
            korpus[avain] = tokenisoi_lauseet(korpus[avain])
        elif valinta == "virkkeiksi":
            korpus[avain] = tokenisoi_virkkeet(korpus[avain])
