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
    "korpuspolku": "",
    "kirjoittaja": True,
    "teksti": False,
    "grafeemeina": False,
    "sanoina": False,
    "lauseina": False,
    "funktiomaara": False,
    "funktiotyyppimaara": False,
    "sisaltomaara": False,
    "sisaltotyyppimaara": False,
    "lemmamaara": False,
    "kaikki": False,
    "tokenit": False,
    "sisaltolista": False,
    "funktiolista": False,
    "hfl30": False,
    "hfl50": False,
    "hfl100": False,
    "hapax": False
}

# PySimpleGuin eräs perusteemoista, saadaanpahan jotain söpöä hetkeksi :)
# sg.theme("LightGreen10")

sg.LOOK_AND_FEEL_TABLE['teema'] = {'BACKGROUND': '#E3F2FD',
                                   'TEXT': '#000000',
                                   'INPUT': '#86A8FF',
                                   'TEXT_INPUT': '#000000',
                                   'SCROLL': '#86A8FF',
                                   'BUTTON': ('#FFFFFF', '#5079D3'),
                                   'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                   'BORDER': 0, 'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0,
                                   'ACCENT1': '#FF0266',
                                   'ACCENT2': '#FF5C93',
                                   'ACCENT3': '#C5003C'}

sg.theme("teema")

osio1 = [
        [
            sg.Text("Valitse korpuksen sisältävä kansio:"),
            sg.Input(enable_events=True, key="korpuspolku"),
            sg.FolderBrowse()
        ],
    [sg.Text("Tulosta"),
     sg.Radio("kirjoittajan", "osiotulostus", key="kirjoittaja", default=True),
     sg.Radio("tekstin", "osiotulostus", key="teksti", default=False),
     sg.Text("mukaan")
     ],

]

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

vertailu_layout = [

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

samankaltaisuus_layout = [
    [sg.Checkbox(text="Kaikki sanat (normalisoitu)",
                 default=False, key="kaikki")],
    [sg.Checkbox(text="Tokenit (normalisoitu)", default=False, key="tokenit")],
    [sg.Checkbox(text="Sisältösanat", default=False, key="sisaltolista")],
    [sg.Checkbox(text="Funktiosanat", default=False, key="funktiolista")],
    [sg.Checkbox(text="HFL 30", default=False, key="hfl30")],
    [sg.Checkbox(text="HFL 50", default=False, key="hfl50")],
    [sg.Checkbox(text="HFL 100", default=False, key="hfl100")],
    [sg.Checkbox(text="Hapax legomena", default=False, key="hapax"),]
]

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Asetukset", font=("Bebas Neue", 20))],

    # Käsiteltävien tekstien valinta

    [sg.Frame("Perustunnusluvut", osio1, title_location=sg.TITLE_LOCATION_TOP)
     ],
    # [sg.Text("Sana-, lause- ja virkepituus (keskiarvo)"),
    #  sg.Checkbox(text=("grafeemeina"), default=(False),
    #              key="grafeemeina", enable_events=True),
    #  sg.Checkbox(text=("sanoina"), default=(False),
    #              key="sanoina", enable_events=True),
    #  sg.Checkbox(text=("lauseina"), default=(False),
    #              key="lauseina", enable_events=True),
    #  ],

    [sg.Frame("Tulostetaanko", tulostus_layout,
              title_location=sg.TITLE_LOCATION_TOP)],
    [sg.Frame("Misc :D", misc_layout, title_location=sg.TITLE_LOCATION_TOP),
        sg.Frame("Menetelmä", menetelma_layout,
                 title_location=sg.TITLE_LOCATION_TOP),
        sg.Frame("Sanaston samankaltaisuus", samankaltaisuus_layout, title_location=sg.TITLE_LOCATION_TOP)],
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
        if values["korpuspolku"] == "":
            sg.popup_ok("Valitse korpuskansio.")
        else:
            kaynnista()

    # Valintalaatikkojen asetukset
    asetukset["perustunnusluvut"] = values["perustunnusluvut"]
    asetukset["grafeemeina"] = values["grafeemeina"]
    asetukset["sanoina"] = values["sanoina"]
    asetukset["lauseina"] = values["lauseina"]
    asetukset["funktiomaara"] = values["funktiomaara"]
    asetukset["funktiotyyppimaara"] = values["funktiotyyppimaara"]
    asetukset["sisaltomaara"] = values["sisaltomaara"]
    asetukset["sisaltotyyppimaara"] = values["sisaltotyyppimaara"]
    asetukset["lemmamaara"] = values["lemmamaara"]
    asetukset["korpuspolku"] = values["korpuspolku"],
    asetukset["kirjoittaja"] = values["kirjoittaja"],
    asetukset["teksti"] = values["teksti"]


window.close()
