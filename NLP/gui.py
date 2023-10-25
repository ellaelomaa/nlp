import PySimpleGUI as sg
import fetch
import ella_tokenisointi as tokenisointi
import clean
import count

# Tässä ajetaan itse ohjelma asetusten mukaan läpi
def kaynnista():
    korpus = fetch.hae_korpus(asetukset["korpuspolku"])
    tokenisointi.tokenisoi(korpus, asetukset["tokenisointi"])
    clean.poistot(korpus, asetukset["funktiosanat"], asetukset["funktiosanapolku"], asetukset["sisaltosanat"], asetukset["sisaltosanapolku"])

    if asetukset["keskiarvot"] == True:
        count.tilastoja(korpus)

# Ehdotan, että asetuksia varten luodaan sanakirja.
# Esim. jos mahdolliset asetukset ovat alustavasti lemmaus, stemmaus ja funktiosanat,
# olisi sanakirjan default-arvoina False, False ja False. Asetuksia muuttamalla
# saisi esimerkiksi listan False, True ja True. Tämä lista välitettäisiin
# parametrina main-funktioon, tai missä ikinä päätetäänkään mitä
# korpukselle/tekstille halutaan tehdä.

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
    "tokenisointi": "sanoiksi",
    "keskiarvot": False,
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
        sg.Radio("Perusmuotoista", "lemmaus",
                 enable_events=True, key='lemmaa'),
        sg.Radio('Ei mitään', "lemmaus", enable_events=True,
                 key='eilemmaa', default=True)
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
    
    [sg.Checkbox("Tulosta keskiarvotietoja", default=False, key="keskiarvot")],

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
    if values["sanoiksi"] == True:
        asetukset["tokenisointi"] = "sanoiksi"

    if values["lauseiksi"] == True:
        asetukset["tokenisointi"] = "lauseiksi"
        
    if values["virkkeiksi"] == True:
        asetukset["tokenisointi"] = "virkkeiksi"


    asetukset["funktiosanat"] = values["funktio"]
    asetukset["sisaltosanat"] = values["sisalto"]
    asetukset["erisnimet"] = values["erisnimet"]
    asetukset["lemmaus"] = values["lemmaa"]

    # Haetaan poistettavien sanalistojen polut
    asetukset["funktiosanapolku"] = values["funktiosanapolku"]
    asetukset["sisaltosanapolku"] = values["sisaltosanapolku"]
    asetukset["erisnimipolku"] = values["erisnimipolku"]
    asetukset["korpuspolku"] = values["korpuspolku"]
    asetukset["keskiarvot"] = values["keskiarvot"]

window.close()
