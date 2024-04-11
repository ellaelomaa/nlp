import tkinter as tk
import ttkbootstrap as ttk
import main
from functools import partial
from threading import Thread
from tkinter import Menu
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *

# ----------- GLOBAALIT MUUTTUJAT JA FUNKTIOT-----------

# Asetussanakirjan alustus
asetukset = {}

# Edistymispalkin muuttujat
prog_yht = 0
prog_valmiita = 0

# Asetusten päivittämisfunktio
def valitse(arvo, asetus):
    global asetukset
    asetukset[asetus] = arvo.get()

# Edistymispalkin muuttujien laskenta

def laske_prog_yht():
    print("")

# ----------- GUI-----------

class Vasen():
    def __init__(self, master, vasen_grid):
        # ----------- FUNKTIOT -----------

        # Kaikkien osioiden valintalaatikot luodaan
        # listasta silmukassa.
        def luo_valintalaatikot(sijainti, vaihtoehdot):
            global asetukset
            for vaihtoehto in vaihtoehdot:
                asetukset[vaihtoehto] = False # Alustetaan kaikki sanakirjaan
                checkbox_var = tk.BooleanVar()
                checkbox_var.set(False)
                ttk.Checkbutton(sijainti, variable=checkbox_var,
                            text=vaihtoehto, command=partial(valitse, checkbox_var, vaihtoehto)).pack(anchor="w")
        
        def kaynnista():
            # Ohjelman suorituksen ajaksi otetaan käynnistysnappi pois käytöstä
            kaynnista_nappi.config(state="disabled")
            main.logiikka(asetukset)
            kaynnista_nappi.config(state="normal")

        ttk.Label(vasen_grid, text="Asetukset", font=("Garamond", 28)).grid(row=0, columnspan=2)


        # ----------- PERUSTILASTOT -----------
        perustilastot = ["Sanamäärä", "Virkemäärä",
                        "Grafeemeja sanoissa ja virkkeissä", "Morfeemeja sanoissa", 
                        "Virkepituus sanoina", ]

        # Luodaan Frame Framen sisään osiolle
        tilastot_frame = ttk.Frame(vasen_grid)
        tilastot_frame.grid(row = 1, column=1, pady=10, padx=10, sticky="w")

        perustilastot_label = ttk.Label(vasen_grid, text="Perustilastoja", font=("Garamond 15 italic"))
        perustilastot_label.grid(row=1, column=0)

        luo_valintalaatikot(tilastot_frame, perustilastot)

        # ----------- SANASTOASETUKSET -----------
        sanasto = ["Type-token ratio", "Sanaston tiheys", 
                   "Sanaluokkien frekvenssit", "HFL 50", "HFL 100", "Hapax Legomena", "Erisnimet"]    
            
        # Luodaan Frame Framen sisään osiolle
        sanasto_frame = ttk.Frame(vasen_grid)
        sanasto_frame.grid(row = 2, column=1,pady=10, padx=10, sticky="w")

        sanasto_label = ttk.Label(vasen_grid, text="Sanastotilastoja", font=("Garamond 15 italic"))
        sanasto_label.grid(row=2, column=0)

        luo_valintalaatikot(sanasto_frame, sanasto)

        # ----------- KIRJOITTAJIEN VERTAILU -----------
        vertailu = ["Yule K", "Yule I", "Kosinisimilaarisuus"] 

        # Luodaan Frame Framen sisään osiolle
        vertailu_frame = ttk.Frame(vasen_grid)
        vertailu_frame.grid(row = 3, column=1, pady=10, padx=10, sticky="w")

        vertailu_label = ttk.Label(vasen_grid, text="Kirjoittajien vertailu", font=("Garamond 15 italic"))
        vertailu_label.grid(row=3, column=0)

        luo_valintalaatikot(vertailu_frame, vertailu)

        # ----------- KÄYNNISTÄ -----------
            
        kaynnista_frame = ttk.Frame(vasen_grid, bootstyle="primary")
        kaynnista_frame.grid(row = 4, column=0, pady=20, columnspan=2)

        kaynnista_nappi = ttk.Button(kaynnista_frame, text="Käynnistä", command=lambda: Thread(target=kaynnista, daemon=True).start())
        kaynnista_nappi.pack(anchor="w") 

class Oikea:
    def __init__(self, master, oikea_grid):
        ttk.Label(oikea_grid, text="Ohjeet", 
                  font=("Garamond", 28)).grid(row=0)

        ohje =  """Helmin NLP-ohjelma on työkalu suomenkielisten tekstien yksinkertaiseen analyysiin ja vertailuun. 
                      
Ohjelman suorituskansiosta löytyy "corpora"-niminen kansio, johon voit tiputtaa haluamasi UTF-8 -muotoiset tekstit. Mikäli haluat vertailla useampaa kirjoittajaa, luo jokaiselle kirjailijalle oma alikansio. Älä kuitenkaan luo kirjailijan alakansion sisälle sisempiä alakansioita. Kansioiden ja tiedostojen nimillä ei ole merkitystä. 
                      
Kaikki tilastot ja vertailujen tulokset tallennetaan samaan, myöskin ohjelman suorituskansiosta löytyvään tiedostoon nimeltä "tulokset.xlsx."

Tulevia toimintoja:
    - lauseiden tunnistaminen ja analyysi
    - latauspalkki
    - painike ohjelman suorituksen keskeyttämiseksi               
                      """
        
        teksti = ttk.Text(oikea_grid, wrap=WORD,)
        teksti.grid(row=1)
        teksti.insert(END, ohje)
        teksti.config(state=DISABLED) # Vain-luku -tilainen teksti

class Sovellus(ttk.Window):

    def __init__(self):
        super().__init__(themename="minty")
        self.title("Helmin NLP-ohjelma")
        self.iconbitmap("99_85283.ico") 

        # Alustetaan ikkunan koko suhteessa näytön kokoon
        leveys  = self.winfo_screenwidth()
        korkeus = self.winfo_screenheight()  
        self.position_center()  
        self.geometry('%sx%s' % (int(leveys/1.5), int(korkeus/1.5)))

        # ------------ PÄÄIKKUNAN FUNKTIOT ------------

        # Funktio sovelluksen teeman vaihtamiseen
        tyyli = ttk.Style()

        def vaihdavari(vari):
            tyyli.theme_use(vari)
        
        def naytainfo():
            Messagebox.ok("""Sovelluksessa käytetyt kirjastot:
NLTK, Openypxl, Pandas, Scikit-learn, Spacy, TTKBootstrap, UralicNLP.
Github: https://github.com/ellaelomaa/nlp
Tekijät: Ella Elomaa ja Helmi Siiroinen (2024)
""")                          
            
        # ----------- TYÖKALUPALKKI ------------
    
        menubar = Menu(self)
        self.config(menu=menubar)

        # Infoikkuna

        info_vaihtoehdot = Menu(menubar)
        info_vaihtoehdot.add_command(label="Käyttöohje")
        info_vaihtoehdot.add_command(label="Tietoa sovelluksesta", command=naytainfo)

        # Työkalupalkin sisältö
        menubar.add_cascade(label="Info", menu=info_vaihtoehdot)

        # Sovelluksen teeman vaihto
        varit = Menu(menubar)
        for x in  ["flatly", "minty", "morph", "solar", "superhero", "darkly"]:
            varit.add_command(label=x, command=lambda x=x: vaihdavari(x))

        menubar.add_cascade(label="Teemat", menu=varit)

        # ----------- KÄYTTÖÖLIITTYMÄN PÄÄRAKENNE ----------
        # Ikkuna jakautuu kahteen puoliskoon: vasemmalla on asetukset,
        # oikealla tekstien käsittelyn tuloslaatikko

        self.vasen_frame = ttk.Frame(self)
        self.vasen_frame.grid(row=0, column=0, sticky="ns", pady=50)

        self.vasen_sisalto = Vasen(self, self.vasen_frame)

        self.oikea_frame = ttk.Frame(self)
        self.oikea_frame.grid(row=0, column=1, sticky="ns", pady=50)

        self.oikea_sisalto = Oikea(self, self.oikea_frame)

        # Molemmat puoliskojen paino on sama, eli molemmat saavat 50 % ikkunan leveydestä
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    sovellus = Sovellus()
    sovellus.mainloop()