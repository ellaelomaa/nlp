# Käytettävät kirjastot ja muut lähteet
- Sanojen käsittelyyn UralicNLP (https://github.com/mikahama/uralicNLP)
  - sanaluokkajakaumat,
  - sijamuotojakaumat,
  - sanaston tiheys (lexical density, eli sisältösanojen ja funktiosanojen suhde),
  - lemmaus,
  - morfeemien laskeminen,
  - lausepituus?,
  - lauseenvastikkeiden määrä?,
- NLTK (https://www.nltk.org/)
- Käyttöliittymän tekemiseen PySimpleGUI (https://www.pysimplegui.org/en/latest/).
- Mahdollisesti Murre (https://github.com/mikahama/murre)
- POS-tägit ja muut (https://universaldependencies.org/u/feat/index.html) selitettynä

# Tavoitteet
- Korkean tason tavoitteena tutkia, voiko ihmisen ja LLM:n tuottaman tekstin erottaa toisistaan? Kielioppi, informaatiorakenne, kappaleiden pituus.

# Toiminnot:
## Kompleksisuus
- sanapituus,
- sanojen kompleksisuus eli morfeemien määrä sanassa,
- lausepituus sanoina,
- virkepituus lauseina ja sanoina,
## Sanaston laajuus
- type/token -ratio eli TTR
## Sanaston tiheys
- Lexical Density eli LD; sisältösanojen ja funktiosanojen suhteet
## Sanaluokkajakso
- verbit,
- substantiivit,
- adjektiivit,
- pronominit,
- numeraalit,
- adverbit,
- adpositiot, ja
- partikkelit (konkunktiot ja interjektiot)
## Muita laskettavia
- tekstien pituuksien varianssi,
- hapax legomena,
- erikoismerkkien frekvenssit,
- negaatiot
- tunnusluvut

# Tilastoihin (morfeemimäärä)
- moodi,
- mediaani,
- vaihteluväli,
- varianssi,
- keskihajonta,
- keskiarvo,
- kokonaismäärät

# Käsin tehdään
- lauseiden erottelu
- Mikä on tekstilajille ominaista ja mikä taas kirjoittajan tyyliä?
