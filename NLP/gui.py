import os
import PySimpleGUI as sg
import fetch
import tokenisointi
import clean
import count
import uralic
import time

# Tässä ajetaan itse ohjelma asetusten mukaan läpi


def kaynnista():
    # Haetaan polku corpora-kansioon, jonne käyttäjä itse
    # kiltisti tiputtelee ja lajittelee tekstitiedostonsa
    path = os.path.abspath(os.path.curdir)
    folder = "corpora"
    korpus = fetch.hae_korpus(os.path.join(path, folder))

    count.tilastoja(asetukset, korpus)
    uralic.uralic(asetukset, korpus)
    clean.poistot(asetukset, korpus)

    # Korpus, josta poistettu sanat.
    # siistikorpus = clean.poistot(korpus, asetukset["funktiosanat"], asetukset["funktiosanapolku"])


# Sanakirjan alustus
asetukset = {
    "sanamaarat": False,
    "virkemaarat": False,
    "tokenit": False,
    "sanapituus": False,
    "grafeemit": False,
    "morfeemit": False,
    "lausetilastot": False,
    "virkesana": False,
    "virkelause": False,
    "TTR": False,
    "LD": False,
    "sanaluokat": False,
    "pituusvarianssi": False,
    "hapax": False,
    "erikoismerkit": False,
    "negaatiot": False,
    "tiheys": False,
    "erikoismerkit": False,
    "hfl": False,
    "50": False,
    "100": False,
    "erisnimet": False,
    "yule": False,
    "yulek": False,
    "yulei": False,
    "kosini": False,
    }

# PySimpleGuin eräs perusteemoista, saadaanpahan jotain söpöä hetkeksi :)
# sg.theme("LightGreen10")

sg.LOOK_AND_FEEL_TABLE['teema'] = {'BACKGROUND': '#5c9ead',
                                   'TEXT': '#faf9f9',
                                   'INPUT': '#b3dee2',
                                   'TEXT_INPUT': '#5e503f',
                                   'SCROLL': '#B3F2DD',
                                   'BUTTON': ('#5e503f', '#fcca46'),
                                   'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                   'BORDER': 0, 'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0,
                                   'ACCENT1': '#FF0266',
                                   'ACCENT2': '#FF5C93',
                                   'ACCENT3': '#C5003C'}

sg.theme("teema")

# GUI:n asetusten järjestys ja avaimet
muuttujat = [
    [sg.Checkbox(text="Sanojen määrä", default=False, key="sanamaarat")],
    [sg.Checkbox(text="Virkkeiden määrä", default=False, key="virkemaarat")],
    [sg.Checkbox(text="Sanapituus", default=False, key="sanapituus")],
    [sg.Checkbox(text="Grafeemeja sanoissa", default=False, key="grafeemit")],
    [sg.Checkbox(text="Morfeemien määrä sanoissa", default=False, key="morfeemit")],
    [sg.Checkbox(text="Lausetilastoja", default=False, key="lausetilastot")],
    [sg.Checkbox(text="Virkepituus sanoina", default=False, key="virkesana")],
    [sg.Checkbox(text="Virkepituus lauseina", default=False, key="virkelause")],
    [sg.Checkbox(text="TTR", default=False, key="TTR")],
    [sg.Checkbox(text="Sanaston tiheys", default=False, key="tiheys")],
    [sg.Checkbox(text="Sanaluokkien frekvenssit", default=False, key="sanaluokat")],
    [sg.Checkbox(text="Erikoismerkkien määrä", default=False, key="erikoismerkit")],
    [sg.Checkbox(text="HFL, sanoja: ", default=False, key="hfl"), sg.Radio("50", "maara", key="50", default=True), sg.Radio("100", "maara", key="100", default=False)],
    [sg.Checkbox(text="Hapax Legomena", default=False, key="hapax")],
    [sg.Checkbox(text="Erisnimet", default=False, key="erisnimet")],
    [sg.Checkbox(text="Yule, metodi: ", default=False, key="yule"), sg.Radio("Yule K", "yule", key="yulek", default=True), sg.Radio("Yule I", "yule", key="yulei", default=False)],
    [sg.Checkbox(text="Kosinisimilaarisuus", default=False, key="kosini")],

]

osio3 = [
    [sg.Frame("Muuttujat", muuttujat, title_location=sg.TITLE_LOCATION_TOP)]
]

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Pudota kaikki käsiteltävät tekstit corpus-kansioon. Luo omat alakansiot jokaiselle kirjailijalle. Tekstien pitää olla .txt-muodossa. Valitse alla olevista asetuksista mitä tulosteita haluat.")],
    [sg.Text("Asetukset", font=("Bebas Neue", 20))],

    # Käsiteltävien tekstien valinta
    [osio3],

    [sg.Button("Käynnistä ohjelma")],
    [sg.Button("Sulje")]
]

# Luodaan ikkuna
window = sg.Window("Helmin NLP-ohjelma", layout,
                   icon="99_85283.ico", resizable=True)

# Ikkuna on auki ja käyttäjä silmukassa, kunnes itse sulkee ohjelman
while True:
    event, values = window.read()
    if event == "Sulje" or event == sg.WIN_CLOSED:
        break

    if event == "Käynnistä ohjelma":
        kaynnista()
    
    # Valintalaatikkojen asetukset
    asetukset["sanamaarat"] =values["sanamaarat"]
    asetukset["virkemaarat"] = values["virkemaarat"]
    asetukset["sanapituus"] = values["sanapituus"]
    asetukset["lausetilastot"] = values["lausetilastot"]
    asetukset["grafeemit"] = values["grafeemit"]
    asetukset["morfeemit"] = values["morfeemit"]
    asetukset["virkesana"] = values ["virkesana"]
    asetukset["TTR"] = values["TTR"]
    asetukset["sanaluokat"] = values["sanaluokat"]
    asetukset["tiheys"] = values["tiheys"]
    asetukset["virkelause"] = values["virkelause"]
    asetukset["erikoismerkit"] = values["erikoismerkit"]
    asetukset["hfl"] = values["hfl"]
    asetukset["50"] = values["50"]
    asetukset["100"] = values["100"]
    asetukset["hapax"] = values["hapax"],
    asetukset["erisnimet"] = values["erisnimet"]
    asetukset["yule"] = values["yule"]
    asetukset["yulek"] = values["yulek"]
    asetukset["yulei"] = values["yulei"]
    asetukset["kosini"] = values["kosini"]

window.close()
