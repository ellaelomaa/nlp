import NLP_sanalista
import NLP.tokenisointi as tokenisointi

# TTR, type-token-ratio eli saneiden määrä jaetaan tokenien määrällä ja kerrotaan sadalla
def type_token_ratio(sanelista, tokenit):
    type = len(sanelista)
    token = len(tokenit)
    TTR = ((type / tokenit) * 100)
    return TTR



