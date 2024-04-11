from nltk.tokenize import sent_tokenize
import nltk
import regex as re
from re import split

# Tarvitaan sent_tokenizen toimimiseen. Lataa vain kerran, sitten voi poistaa :)
#nltk.download("punkt")

def tokenisoi_sanat(teksti):
    """
    Tokenisoi tekstin sanoiksi ja poistaa välimerkit, lukuun ottamatta - ja '.
    Palauttaa listan.
    """
    valimerkiton = re.sub(r"[^\P{P}-'&]+", "", teksti)
    valimerkiton.replace("&", "ja")

    # Erotellaan välilyönnistä sanat listaksi.
    tokenit = valimerkiton.split()

    # # Muutetaan kaikki vielä pieniksi kirjaimiksi
    # tokenit = [sana.lower() for sana in tokenit]
    
    return tokenit

# Lauseiden tokenisointifunktio, eli lauseet erikoismerkistä erikoismerkkiin
# : , . ; ajatusviiva ! ?s
def tokenisoi_lauseet(teksti):
    """
    Tokenisoi tekstin lauseiksi, eli erokoismerkistä erikoismerkkiin,
    lukuun ottamatta - ja '. 
    Palauttaa listan.
    """
    # Poistetaan ensin rivinvaihdot.
    teksti = teksti.replace("\n", "")
    valimerkiton = re.sub(r"[^\P{P}-'&|]+", "", teksti)
    lauseet = re.split("\|", valimerkiton)
    # Poistetaan tyhjät alkiot.
    lauseet = list(filter(None, lauseet))
    
    return lauseet


def tokenisoi_virkkeet(teksti):
    """
    Tokenisoi tekstin virkkeiksi. Palauttaa listan.
    """
    virkkeet= sent_tokenize(teksti, language="finnish")
    return virkkeet

def tokenisoi(korpus, valinta):
    for avain in korpus:
        if valinta == "sanoiksi":
            korpus[avain] = tokenisoi_sanat(korpus[avain])
        elif valinta == "lauseiksi":
            korpus[avain] = tokenisoi_lauseet(korpus[avain])
        elif valinta == "virkkeiksi":
            korpus[avain] = tokenisoi_virkkeet(korpus[avain])
