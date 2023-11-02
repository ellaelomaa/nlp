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

osio1 = [
        [
            sg.Text("Valitse korpuksen sisältävä kansio:"),
            sg.Input(enable_events=True, key="korpuspolku"),
            sg.FolderBrowse()
        ],
    [sg.Text("Tulosta"),
            sg.Radio("kirjoittajan", "osiotulostus",
                     key="kirjoittaja", default=True),
            sg.Radio("tekstin", "osiotulostus", key="teksti", default=False),
            sg.Text("mukaan")
     ],

]

osio2 = [
    [sg.Text("Vertailukohde 1:"),
        sg.Radio("Teksti:", "vertailu1", key="tekstiv1", default="True"),
     sg.Radio("Kirjailija", "vertailu1", key="kirjailijav1")],
    [sg.Text("Vertailukohde 2:"),
        sg.Radio("Teksti:", "vertailu2", key="tekstiv2", default="True"),
     sg.Radio("Kirjailija", "vertailu2", key="kirjailijav2")],
    [sg.Text("Sanalistan tyyppi:"),
     sg.Radio("Kaikki sanat (tokenit)", "tyyppi", key="sanat", default=True),
     sg.Radio("Kaikki lemmat (typet)", "tyyppi", key="lemmat"),
     sg.Radio("Sisältösanat", "tyyppi", key="sisalto"),
     sg.Radio("Funktiosanat", "tyyppi", key="funktiosanat"),
     ],
    [sg.Text("Samankaltaisuusfunktio:"),
     sg.Radio("Jaccard", "samankaltaisuus", key="jaccard", default="True"),
     sg.Radio("Cosine", "samankaltaisuus", key="cosine"),
     sg.Radio("Eucledian", "samankaltaisuus", key="eucledian"),
     ]
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

muuttujat = [
    [sg.Checkbox(text="Sanapituus", default=False, key="sanapituus")],
    [sg.Checkbox(text="Lausepituus", default=False, key="lausepituus")],
    [sg.Checkbox(text="Virkepituus", default=False, key="virkepituus")],
    [sg.Checkbox(text="Sanaston laajuus", default=False, key="laajuus")],
    [sg.Checkbox(text="TTR", default=False, key="ttr")],
    [sg.Checkbox(text="LD", default=False, key="ld")],
]

analyysimenetelma = [
    [sg.Checkbox("PCA", default=False, key="PCA")],
    [sg.Checkbox("Cluster", default=False, key="cluster")],

]

osio3 = [
    [sg.Frame("Muuttujat", muuttujat, title_location=sg.TITLE_LOCATION_TOP),
    sg.Frame("Analyysimenetelmä", analyysimenetelma, title_location=sg.TITLE_LOCATION_TOP)]
]

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Asetukset", font=("Bebas Neue", 20))],

    # Käsiteltävien tekstien valinta

    [sg.Frame("Perustunnusluvut", osio1, title_location=sg.TITLE_LOCATION_TOP)
     ],
    [sg.Frame("Sanalistojen vertailu", osio2,
              title_location=sg.TITLE_LOCATION_TOP)],
    [sg.Frame("Tilastolliset menetelmät", osio3,
              title_location=sg.TITLE_LOCATION_TOP)],

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
    asetukset["korpuspolku"] = values["korpuspolku"],
    asetukset["kirjoittaja"] = values["kirjoittaja"],
    asetukset["teksti"] = values["teksti"]


window.close()
