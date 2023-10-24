from nltk.tokenize import sent_tokenize
import nltk
import regex as re
from re import split

# Tarvitaan sent_tokenizen toimimiseen. Lataa vain kerran, sitten voi poistaa :)
#nltk.download("punkt")

testi = "raa'an aika-kausi Meidän vauva alkaa olla jo lähempänä kymmentä, kuin yhdeksää kuukautta, joten otetaanpas tähän väliin vähän 9kk raporttia, ennen kuin siirrytään uusille kuukausille. Kai synnytyksen lähestymisen jotenkin aavisti, nyt kun jälkikäteen ajattelee. H-hetkeä edeltävän päivän olen vihdoin malttanut viettää rentoa äitiyslomaa, kuten ennen vauvan syntymää pitääkin. Luuhailemme Minimen, miehen ja äitini kanssa kaupungilla lounastaen, kakkukahvitellen ja puistossa vaahteralehtien seassa kirmaten. Illalla hämmästytän esikoista pomppimalla hyppynarulla, jonka myöhemmin brändään synnytyshyppynaruksi. Esikoisen mentyä yöpuulle ja äitini lähdettyä hotellille nukkumaan, kirjoitan vielä postauksen ja kahistelen itseni lakanoiden väliin vähän jälkeen puolenyön raskausviikkojen raksuttaessa lukemia 39+5. Vatsassa tuntuu hassulta. Ei kipeältä, vaan enemmänkin kuin perhosten tanssilta."

# Funktio tokenisoimaan sanat, eli erottelemaan ne listaksi.
# Poistetaan samalla välimerkit, paitsi - ja '. 
def tokenisoi_sanat(teksti):
    valimerkiton = re.sub(r"[^\P{P}-']+", "", teksti)

    # Erotellaan välilyönnistä sanat listaksi.
    tokenit = valimerkiton.split()
    return tokenit

# Virkkeiden tokenisointifunktio, eli isosta alkukirjaimesta pisteeseen, 
# huutomerkkiin tai kysymyksmerkkiin.
def tokenisoi_virkkeet(teksti):
    return sent_tokenize(teksti)

# Lauseiden tokenisointifunktio, eli lauseet erikoismerkistä erikoismerkkiin
# : , . ; ajatusviiva ! ?
#TODO: vielä on joitakin välilyöntejä mukana.
def tokenisoi_lauseet(teksti):
    return re.split(', |-|! |\. |\.|\? |\(|\)|–|—|:', teksti)

tokenisoi_lauseet(testi)
