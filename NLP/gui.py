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
    count.tilasto_maarat(korpus)

    # Korpus, josta poistettu sanat.
    # siistikorpus = clean.poistot(korpus, asetukset["funktiosanat"], asetukset["funktiosanapolku"])

    if asetukset["grafeemeina"] == True:
        count.grafeemeina(korpus)

    if asetukset["sanoina"] == True:
        count.sanoina(korpus)

    if asetukset["lauseina"] == True:
        count.lauseina(korpus)


# Sanakirjan alustus
asetukset = {
    "funktiosanat": False,
    "sisaltosanat": False,
    "erisnimet": False,
    "funktiosanapolku": "",
    "sisaltosanapolku": "",
    "erisnimipolku": "",
    "korpuspolku": "",
    "grafeemeina": False,
    "sanoina": False,
    "lauseina": False,
    "funktiomaara": False,
    "funktiotyyppimaara": False,
    "sisaltomaara": False,
    "sisaltotyyppimaara": False,
    "lemmamaara": False
}

alkuaika = time.time()

# PySimpleGuin eräs perusteemoista, saadaanpahan jotain söpöä hetkeksi :)
sg.theme("LightGreen10")

tulostus_layout = [
                   [sg.Checkbox(text="funktiosanojen määrä (N, %)",
                                default=False, key="funktiomaara")],
                   [sg.Checkbox(text="funktiosanatyyppien määrä (N)",
                                default=False, key="funktiotyyppimaara")],
                   [sg.Checkbox(text="sisältösanojen määrä (N, %)",
                                default=False, key="sisaltomaara")],
                   [sg.Checkbox(text="sisältösanatyyppien määrä (N)",
                                default=False, key="sisaltotyyppimaara")],
                   [sg.Checkbox(text="kaikkien lemmojen määrät (N)",
                                default=False, key="lemmamaara")]
                   ]

misc_layout = [
    [sg.Checkbox(text="TTR (Type-Token-Ratio)", default=False, key="TTR")],
    [sg.Checkbox(text="LD (Lexical Density)", default=False, key="LD")]
]

menetelma_layout = [
    [sg.Checkbox(text="Jaccard similarity", default=False, key="jaccard")],
    [sg.Checkbox(text="Cosine similarity", default=False, key="cosine")],
    [sg.Checkbox(text="Eucledian distance", default=False, key="eucledian")],

]

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Asetukset", font=("Bebas Neue", 20))],

    # Käsiteltävien tekstien valinta
    [
        sg.Text("Valitse korpuksen sisältävä kansio:"),
        sg.Input(enable_events=True, key="korpuspolku"),
        sg.FolderBrowse()
    ],

    [sg.Text("Sana-, lause- ja virkepituus (keskiarvo)"),
     sg.Checkbox(text=("grafeemeina"), default=(False),
                 key="grafeemeina", enable_events=True),
     sg.Checkbox(text=("sanoina"), default=(False),
                 key="sanoina", enable_events=True),
     sg.Checkbox(text=("lauseina"), default=(False),
                 key="lauseina", enable_events=True),
     ],

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

    [sg.Frame("Tulostetaanko", tulostus_layout, title_location=sg.TITLE_LOCATION_TOP)],
    [sg.Frame("Misc :D", misc_layout, title_location=sg.TITLE_LOCATION_TOP), sg.Frame("Menetelmä", menetelma_layout, title_location=sg.TITLE_LOCATION_TOP)],

    [sg.Button("Käynnistä ohjelma")],
    [sg.Button("Sulje")]
]

# Luodaan ikkuna
window = sg.Window("Helmin NLP-ohjelma",
                   layout, icon="99_85283.ico")

# Ikkuna on auki ja käyttäjä silmukassa, kunnes itse sulkee ohjelman
while True:
    event, values = window.read()
    if event == "Sulje" or event == sg.WIN_CLOSED:
        break

    if event == "Käynnistä ohjelma":
        if values["korpuspolku"] == "":
            sg.popup_ok("Valitse korpuskansio.")
        else:
            kaynnista()

    asetukset["funktiosanat"] = values["funktio"]
    asetukset["sisaltosanat"] = values["sisalto"]
    asetukset["erisnimet"] = values["erisnimet"]
    asetukset["grafeemeina"] = values["grafeemeina"]
    asetukset["sanoina"] = values["sanoina"]
    asetukset["lauseina"] = values["lauseina"]
    asetukset["funktiomaara"] = values["funktiomaara"]
    asetukset["funktiotyyppimaara"] = values["funktiotyyppimaara"]
    asetukset["sisaltomaara"] = values["sisaltomaara"]
    asetukset["sisaltotyyppimaara"] = values["sisaltotyyppimaara"]
    asetukset["lemmamaara"] = values["lemmamaara"]


    # Haetaan poistettavien sanalistojen polut
    asetukset["funktiosanapolku"] = values["funktiosanapolku"]
    asetukset["sisaltosanapolku"] = values["sisaltosanapolku"]
    asetukset["erisnimipolku"] = values["erisnimipolku"]
    asetukset["korpuspolku"] = values["korpuspolku"]


window.close()
