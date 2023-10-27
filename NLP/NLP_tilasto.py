import NLP_sanalista
import NLP.tokenisointi as tokenisointi

# TTR, type-token-ratio eli saneiden määrä jaetaan tokenien määrällä ja kerrotaan sadalla
# Yksi mahdollinen tapa mitata leksikon laajuutta
def type_token_ratio(sanelista, tokenit):
    type = len(sanelista)
    token = len(tokenit)
    TTR = (type / token) 
    return TTR

# Sanaston tiheys, eli paljonko sisältösanoja on suhteessa funktiosanoihin.
# Älä kysy miksi näin mutta tää nyt vaan menee näin.
def lexical_density(sisältösanalista, tokenit):
    token = len(tokenit)
    leksikko = len(sisältösanalista)
    LD = ((leksikko / token) * 100)
    return LD
    
