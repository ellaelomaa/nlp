import PySimpleGUI as sg
import os
import fetch
import ella_tokenisointi as tokenisointi

# Tässä ajetaan itse ohjelma asetusten mukaan läpi
def kaynnista():
    print(asetukset["tokenisointi"])
    korpus = fetch.hae_korpus(asetukset["korpuspolku"])
    tokenisointi.tokenisoi(korpus, asetukset["tokenisointi"])


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
    "korpuspolku": "",
    "tokenisointi": "sanoiksi"
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
        sg.LBox([], size=(50, 1), expand_x=True,
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

    # Tokenisointitavan valinta

    # Normalisointitavan valinta
    [
        sg.Text("Tokenisoi "),
        sg.Radio("sanoiksi", "token",
                 enable_events=True, key='sanoiksi', default=True),
        sg.Radio('lauseiksi', "token", enable_events=True, key='lauseiksi'),
        sg.Radio('virkkeiksi', "token", enable_events=True,
                 key='virkkeiksi')
    ],


    # Poistettavien sanojen valinta
    [sg.Checkbox(text=("Poista hukkasanat"), default=(
        False), key="hukka", enable_events=True),
        sg.Input(enable_events=True, key="hukkasanapolku"),
        sg.FileBrowse()],
    [sg.Checkbox(text=("Poista sisältösanat"), default=(
        False), key="sisältö", enable_events=True),
        sg.Input(enable_events=True, key="sisaltosanapolku"),
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

    if values["lemmaa"] == True:
        asetukset["stemmaus"] = False
        asetukset["lemmaus"] = True

    if values["eistemlem"] == True:
        asetukset["lemmaus"] = False
        asetukset["stemmaus"] = False

    if values["sanoiksi"] == True:
        asetukset["tokenisointi"] = "sanoiksi"

    if values["lauseiksi"] == True:
        asetukset["tokenisointi"] = "lauseiksi"
        
    if values["virkkeiksi"] == True:
        asetukset["tokenisointi"] = "virkkeiksi"

    # Haetaan poistettavien sanalistojen polut
    asetukset["hukkasanapolku"] = values["hukkasanapolku"]
    asetukset["sisaltosanapolku"] = values["sisaltosanapolku"]
    asetukset["korpuspolku"] = values["korpuspolku"]

window.close()
