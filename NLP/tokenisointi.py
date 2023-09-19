import nltk 
from nltk.tokenize import word_tokenize
from fetch import corpus_content #onks tää oikein?

# tokenisoi sanat
def tokenisoi_sanat(corpus_content):
    sanalista = word.tokenize(corpus_content)
    return sanalista


#tokenisoi lauseet (erikoismerkistä erikoismerkkiin: : , . ; ajatusviiva ! ?)
# jos monta erikoismerkkiä peräkkäin (?? !! ...) niin poista --> entä jos "ei!" <- poistaako?
def tokenisoi_lauseet(corpus_content):
    erikoismerkit = r'[^.!?]+[.!?]+' #tätä täytyy miettiä
    lauselista = re.split(erikoismerkit, corpus_content)
    return lauselista

#tokenisoi virkkeet (isosta kirjaimesta pisteeseen, huutomerkkiin, kysymysmerkkiin)
def virkkeet():