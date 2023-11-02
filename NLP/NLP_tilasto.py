import NLP_sanalista
import NLP.tokenisointi as tokenisointi

# TTR, type-token-ratio eli saneiden määrä jaetaan tokenien määrällä ja kerrotaan sadalla
def type_token_ratio(sanelista, tokenit):
    type = len(sanelista)
    token = len(tokenit)
    TTR = (type / tokenit)
    return TTR

# Sanaston tiheysfunktio
def lexical_density(sisältösanalista, tokenit):
    token = len(tokenit)
    lekseemit = len(sisältösanalista)
    LD = ((lekseemit / token) * 100)
    return LD

# Yulen K ja I, ei vielä korjattu 
# https://gist.github.com/magnusnissel/d9521cb78b9ae0b2c7d6
def get_yules():
    """ 
    Returns a tuple with Yule's K and Yule's I.
    (cf. Oakes, M.P. 1998. Statistics for Corpus Linguistics.
    International Journal of Applied Linguistics, Vol 10 Issue 2)
    In production this needs exception handling.
    """
    tokens = tokenize()
    token_counter = collections.Counter(tok.upper() for tok in tokens)
    m1 = sum(token_counter.values())
    m2 = sum([freq ** 2 for freq in token_counter.values()])
    i = (m1*m1) / (m2-m1)
    k = 1/i * 10000
    return (k, i)

# Yksittäisen tekstin sanaston samankaltaisuus kirjoittajan sanastoon nähden (yleisesti)
# tarvitsee normalisoidut sanalistat yksittäisistä teksteistä ja kirjoittajakorpuksesta
def jaccard_similarity(set1, set2):
    # intersection of two sets
    intersection = len(set1.intersection(set2))
    # Unions of two sets
    union = len(set1.union(set2))
     
    return intersection / union
 similarity = jaccard_similarity(set_a, set_b)

# Yksittäisen tekstin sanaston samankaltiasuus kirjoittajan sanastoon nähden (huomioi myös frekvenssit)
def cosine_similarity():
    

# Euklediaanin etäisyys
def eucledian_distance():


