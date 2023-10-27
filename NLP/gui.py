import PySimpleGUI as sg
import fetch
import tokenisointi
import clean
import count
import time
import NLP_sanalista

# Tässä ajetaan itse ohjelma asetusten mukaan läpi
def kaynnista():
    korpus = fetch.hae_korpus(asetukset["korpuspolku"])
    
    # Korpus, josta poistettu sanat.
    #siistikorpus = clean.poistot(korpus, asetukset["funktiosanat"], asetukset["funktiosanapolku"])

    if asetukset["keskiarvot"] == True:
        count.tilastoja(korpus)
    
    if asetukset["sanasto"] == True:
        NLP_sanalista.sanasto(korpus)

    if asetukset["virkkeet"] == True:
        count.virkemäärä(korpus)

    if asetukset["virkepituus"] == True:
        count.virkepituus(korpus)

    if asetukset["lausemaara"] == True:
        count.lausemäärä(korpus)
    
    if asetukset["lausepituus"] == True:
        count.lausepituus(korpus)

# Sanakirjan alustus
asetukset = {
    "lemmaus": False,
    "funktiosanat": False,
    "sisaltosanat": False,
    "erisnimet": False,
    "funktiosanapolku": "",
    "sisaltosanapolku": "",
    "erisnimipolku": "",
    "korpuspolku": "",
    "keskiarvot": False,
    "sanasto": False,
    "virkkeet": False,
    "virkepituus": False,
    "lausemaara": False,
    "lausepituus": False
}

alkuaika = time.time()

# PySimpleGuin eräs perusteemoista, saadaanpahan jotain söpöä hetkeksi :)
sg.theme("LightGreen10")

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Asetukset", font=("Arial Bold", 20))],

    # Käsiteltävien tekstien valinta
    [
        sg.Text("Valitse korpuksen sisältävä kansio:"),
        sg.Input(enable_events=True, key="korpuspolku"),
        sg.FolderBrowse()
    ],

    # Normalisointitavan valinta
    [
        sg.Radio("Perusmuotoista", "lemmaus",
                 enable_events=True, key='lemmaa'),
        sg.Radio('Ei mitään', "lemmaus", enable_events=True,
                 key='eilemmaa', default=True)
    ],

    # Tokenisointitavan valinta

    # Poistettavien sanojen valinta
    [sg.Checkbox(text=("Poista funktiosanat"), default=(
        False), key="funktio", enable_events=True),
        sg.Input(enable_events=True, key="funktiosanapolku"),
        sg.FileBrowse()],
    [sg.Checkbox(text=("Poista sisältösanat"), default=(
        False), key="sisalto", enable_events=True),
        sg.Input(enable_events=True, key="sisaltosanapolku"),
        sg.FileBrowse()],
    [sg.Checkbox(text=("Poista erisnimet"), default=(
        False), key="erisnimet", enable_events=True),
        sg.Input(enable_events=True, key="erisnimipolku"),
        sg.FileBrowse()],
    
    [sg.Text("Tulosta "),
        sg.Checkbox("keskiarvotietoja", default=False, key="keskiarvot"),
        sg.Checkbox("sanaston laajuus", default=False, key="sanasto"),
        sg.Checkbox("virkemäärä", default=False, key="virkkeet"),                
        sg.Checkbox("virkepituus", default=False, key="virkepituus"),                
        sg.Checkbox("lausemäärä", default=False, key="lausemaara"),                
        sg.Checkbox("lausepituus", default=False, key="lausepituus"),                
        ],

    [sg.Button("Käynnistä ohjelma")],
    [sg.Button("Sulje")]
]

# Luodaan ikkuna
window = sg.Window("Helmin NLP-ohjelma",
                   layout, )

# Ikkuna on auki ja käyttäjä silmukassa, kunnes itse sulkee ohjelman
while True:
    event, values = window.read()
    if event == "Sulje" or event == sg.WIN_CLOSED:
        break

    if event == "Käynnistä ohjelma":
        kaynnista()

    asetukset["funktiosanat"] = values["funktio"]
    asetukset["sisaltosanat"] = values["sisalto"]
    asetukset["erisnimet"] = values["erisnimet"]
    asetukset["lemmaus"] = values["lemmaa"]
    asetukset["keskiarvot"] = values["keskiarvot"]
    asetukset["sanasto"] = values["sanasto"]
    asetukset["virkkeet"] = values["virkkeet"]
    asetukset["virkepituus"] = values["virkepituus"]
    asetukset["lausemaara"] = values["lausemaara"]
    asetukset["lausepituus"] = values["lausepituus"]

    # Haetaan poistettavien sanalistojen polut
    asetukset["funktiosanapolku"] = values["funktiosanapolku"]
    asetukset["sisaltosanapolku"] = values["sisaltosanapolku"]
    asetukset["erisnimipolku"] = values["erisnimipolku"]
    asetukset["korpuspolku"] = values["korpuspolku"]


window.close()
