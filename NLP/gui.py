import PySimpleGUI as sg
import os
import fetch

# Tässä ajetaan itse ohjelma asetusten mukaan läpi
def kaynnista():
    korpus = fetch.hae_korpus2(asetukset["korpuspolku"])
    print(korpus)


# Ehdotan, että asetuksia varten luodaan sanakirja.
# Esim. jos mahdolliset asetukset ovat alustavasti lemmaus, stemmaus ja hukkasanat,
# olisi sanakirjan default-arvoina False, False ja False. Asetuksia muuttamalla
# saisi esimerkiksi listan False, True ja True. Tämä lista välitettäisiin
# parametrina main-funktioon, tai missä ikinä päätetäänkään mitä
# korpukselle/tekstille halutaan tehdä.

# Sanakirjan alustus
asetukset = {
    "lemmaus": False,
    "stemmaus": False,
    "hukkasanat": False,
    "funktiosanat": False,
    "hukkasanapolku": "",
    "sisaltosanapolku": "",
    "korpuspolku": ""
}

# PySimpleGuin eräs perusteemoista, saadaanpahan jotain söpöä hetkeksi :)
sg.theme("LightGreen10")

# Ulkoasu. Jokainen [ ] on yksi rivi. Jokaiseen asetukseen pitää laittaa
# avain ja enable_events
layout = [
    [sg.Text("Asetukset", font=("Arial Bold", 20))],

    # Käsiteltävien tekstien valinta
    [
        sg.Text("Valitse korpuksen sisältävä kansio:"),
        sg.LBox([], size=(50, 5), expand_x=True,
                expand_y=True, key="lista"),
        sg.Input(visible=False, enable_events=True, key="korpuspolku",
                 font=("Arial Bold", 10), expand_x=True),
        sg.FolderBrowse()
    ],

    # Normalisointitavan valinta
    [
        sg.Radio("Perusmuotoista", "stemlem",
                 enable_events=True, key='lemmaa'),
        sg.Radio('Stemmaa', "stemlem", enable_events=True, key='stemmaa'),
        sg.Radio('Ei mitään', "stemlem", enable_events=True,
                 key='eistemlem', default=True)
    ],

    # Poistettavien sanojen valinta
    [sg.Checkbox(text=("Poista hukkasanat"), default=(
        False), key="hukka", enable_events=True),
        sg.Input( enable_events=True, key="hukkasanapolku"),
        sg.FileBrowse()],
    [sg.Checkbox(text=("Poista sisältösanat"), default=(
        False), key="sisältö", enable_events=True),
        sg.Input( enable_events=True, key="sisaltosanapolku"),
        sg.FileBrowse()],

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

    # Päivitetään laatikkoon valittujen tiedostojen polut
    if event == "korpuspolku":
        window["lista"].Update(values["korpuspolku"].split(";"))

    # Päivitetään valintojen perusteella asetussanakirjaa
    if values["stemmaa"] == True:
        asetukset["lemmaus"] = False
        asetukset["stemmaus"] = True

    elif values["lemmaa"] == True:
        asetukset["stemmaus"] = False
        asetukset["lemmaus"] = True

    elif values["eistemlem"] == True:
        asetukset["lemmaus"] = False
        asetukset["stemmaus"] = False

    # Haetaan poistettavien sanalistojen polut
    asetukset["hukkasanapolku"] = values["hukkasanapolku"]
    asetukset["sisaltosanapolku"] = values["sisaltosanapolku"]
    asetukset["korpuspolku"] = values["korpuspolku"]

window.close()
