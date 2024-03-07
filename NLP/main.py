import clean
import count
import fetch
import os
import queue
import tkinter as tk
import ttkbootstrap as ttk
import uralic
from enum import Enum, auto
from functools import partial
from threading import Thread, Event
from tkinter import Menu
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *


# -----------

# ----------- GLOBAALIT MUUTTUJAT JA FUNKTIOT-----------

# Asetussanakirjan alustus
asetukset = {}

tulos =""

# Asetusten päivittämisfunktio
def valitse(bool, asetus):
    asetukset[asetus] = bool.get()

pysayta = False

class TicketPurpose(Enum):
    UPDATE_RESULT_TEXT = auto()

class Ticket:
    def __init__(self, ticket_type: TicketPurpose,
                 ticket_value: str):
        self.ticket_type = ticket_type
        self_ticket_value = ticket_value
        

class Vasen():
    jono = queue.Queue()
    stop = False

    def __init__(self, master, vasen_grid):
        # super().__init__(master)

        # ----------- FUNKTIOT -----------

        # Kaikkien osioiden valintalaatikot luodaan
        # listasta silmukassa.
        def luo_valintalaatikot(sijainti, sanasto):
            for vaihtoehto in sanasto:
                asetukset[vaihtoehto] = False
                checkbox_var = tk.BooleanVar()
                checkbox_var.set(False)
                ttk.Checkbutton(sijainti, variable=checkbox_var,
                            text=vaihtoehto, command=partial(valitse, checkbox_var, vaihtoehto)).pack(anchor="w")
        
        def kaynnista():
            print("Käynnistä")
            global pysayta
            path = os.path.abspath(os.path.curdir)
            folder = "corpora"
            korpus = fetch.hae_korpus(os.path.join(path, folder))

            kutsut = [count.tilastoja(asetukset, korpus), uralic.uralic(asetukset, korpus), clean.poistot(asetukset, korpus)]

            while not pysayta:
                for kutsu in kutsut:
                    kutsu

                    
        def stop():
            global pysayta
            pysayta = True
            print("Pysäytetty")
        
        ttk.Label(vasen_grid, text="Asetukset", font=("Garamond", 28)).grid(row=0, columnspan=2)


        # ----------- PERUSTILASTOT -----------
        perustilastot = ["Sanamäärä", "Virkemäärä",
                        "Grafeemeja sanoissa", "Morfeemeja sanoissa", 
                        "Virkepituus sanoina", 
                        "Virkepituus lauseina"]

        # Luodaan Frame Framen sisään osiolle
        tilastot_frame = ttk.Frame(vasen_grid)
        tilastot_frame.grid(row = 1, column=1, pady=10, padx=10, sticky="w")

        perustilastot_label = ttk.Label(vasen_grid, text="Perustilastoja", font=("Garamond 15 italic"))
        perustilastot_label.grid(row=1, column=0)

        luo_valintalaatikot(tilastot_frame, perustilastot)

        # ----------- SANASTOASETUKSET -----------
        sanasto = ["Type-token ratio", "Sanaston tiheys", "Sanaluokkien frekvenssit", "HFL", "Hapax Legomena", "Erisnimet"]    
            
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

        # ----------- PYSÄYTÄ OHJELMA -----------
            
        stop_frame = ttk.Frame(vasen_grid, bootstyle="primary")
        stop_frame.grid(row = 4, column=1, pady=20, columnspan=2)

        stop_nappi = ttk.Button(stop_frame, text="Pysäytä", bootstyle="danger outline", command=stop)
        stop_nappi.pack(anchor="w")        

class Oikea:
    def __init__(self, oikea_grid):
        global tulos

        ttk.Label(oikea_grid, text="Tulokset", font=("Garamond", 28)).grid(row=0)

        tulokset_frame = ttk.Frame(oikea_grid, bootstyle="secondary")
        tulokset_frame.grid(row = 1, column=0)

        tuloslaatikko = ttk.ScrolledText(tulokset_frame, pady=5, padx=5)
        tuloslaatikko.pack(fill=BOTH, expand=YES)
        tuloslaatikko.insert(END, "Testi")

class Sovellus(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        # ------------ FUNKTIOT ------------

        # Funktio sovelluksen teeman vaihtamiseen
        style = ttk.Style()

        def vaihdavari(vari):
            style.theme_use(vari)
        
        def naytainfo():
            Messagebox.ok("""Sovelluksessa käytetyt kirjastot:
NLTK, Pandas, Scikit-learn, Spacy, TTKBootstrap, UralicNLP.
Github: https://github.com/ellaelomaa/nlp
Tekijät: Ella Elomaa ja Helmi Siiroinen (2024)
""")                          
            
        # ----------- TYÖKALUPALKKI ------------
    
        menubar = Menu(master)
        master.config(menu=menubar)

        # Infoikkuna

        self.info_vaihtoehdot = Menu(menubar)
        self.info_vaihtoehdot.add_command(label="Käyttöohje")
        self.info_vaihtoehdot.add_command(label="Tietoa sovelluksesta", command=naytainfo)

        # Työkalupalkin sisältö
        menubar.add_cascade(label="Info", menu=self.info_vaihtoehdot)

        # Sovelluksen teeman vaihto
        varit = Menu(menubar)
        for x in  ["flatly", "minty", "morph", "solar", "superhero", "darkly"]:
            varit.add_command(label=x, command=lambda x=x: vaihdavari(x))

        menubar.add_cascade(label="Teemat", menu=varit)

        # ----------- KÄYTTÖÖLIITTYMÄN PÄÄRAKENNE ----------
        # Ikkuna jakautuu kahteen puoliskoon: vasemmalla on asetukset,
        # oikealla tekstien käsittelyn tuloslaatikko

        self.vasen_frame = ttk.Frame(master)
        self.vasen_frame.grid(row=0, column=0, sticky="ns", pady=50)

        self.vasen_sisalto = Vasen(self, self.vasen_frame)

        self.oikea_frame = ttk.Frame(master)
        self.oikea_frame.grid(row=0, column=1, sticky="ns", pady=50)

        self.oikea_sisalto = Oikea(self.oikea_frame)

        # Molemmat puoliskojen paino on sama, eli molemmat saavat 50 % ikkunan leveydestä
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

if __name__ == "__main__":
    # PÄÄIKKUNA

    root = ttk.Window(title="Helmin NLP-ohjelma", 
                      themename="minty")
    
    # Alustetaan ikkunan koko suhteessa näytön kokoon
    width  = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%sx%s' % (int(width/1.5), int(height/1.5)))
    root.iconbitmap("99_85283.ico") 

    Sovellus(root)
    root.mainloop()