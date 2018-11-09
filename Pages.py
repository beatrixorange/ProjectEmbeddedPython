from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Startpage import StartPage
import temperature_graph
import light_graph
"""
In deze file staan meerdere klassen. 
Elke klasse is een van de 5 Arduino pagina's voor de 5 mogelijke besturingseenheden.

ToDo:
Live grafieken toevoegen die de data van de sensoren laten zien. 
Er moet gekeken worden wannneer een grens berijkt wordt.
Er moet doorgegeven worden dat de roluiken uitgerold moeten worden wanneer deze grens berijkt wordt.
Er moet doorgegeven worden dat de roluiken ingerold moeten worden wanneer de temperatuur/lichtintensiteit zich weer
onder de grens bevindt.
"""

class Arduino1(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Temperatuur", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Voorbeeld grafiek temperatuur
        self.graph1 = FigureCanvasTkAgg(temperature_graph.fig, self)
        self.graph1.get_tk_widget().grid(column=0, row=0)

        self.uitrol_label = tk.Label(self, text=" Uitrolgrens:")
        self.uitrol_label.grid(column=1, row=0, sticky=N, pady=50)
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol_choices = ("uit", "20°C", "25°C", "30°C", "35°C", "40°C")
        self.uitrol_choiceVar.set(self.uitrol_choices[3])  # standard 30°C
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=7)
        self.uitrol_cb.grid(column=1, row=0, sticky=N, pady=70)

        uitrolgrens_t = tk.Button(self, text="Toepassen", command=lambda: self.uitrolgrens_t(), width=8)
        uitrolgrens_t.grid(column=1, row=0, sticky=N, pady=100)

        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(1), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(1), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(1), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)

        self.uitrol_afstand = tk.Label(self, text="Het rolluik is 2 meter uitgerold")
        self.uitrol_afstand.grid(column=1, row=0, sticky=N, pady=300)


    def uitrolgrens_t(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            self.temp_grens = 0
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            s = self.uitrol_choiceVar.get().split('°')
            self.temp_grens = int(s[0])
            print("Het zonnescherm wordt automatisch uitgerold wanneer het warmer dan", self.uitrol_choiceVar.get(),
                  "is.")

    def check_grens(self):  # temperatuur moet ergens opgehaald worden
        if self.temp_grens != 0 and 'Temperatuur' > self.uitrol_choiceVar.get():
            StartPage.rolluik_uitrollen(self)
            self.t_grens = True
        else:
            self.t_grens = False

    def get_uitrol_afstand(self):
        return self.uitrol_afstand


class Arduino2(StartPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text="Lichtintensiteit", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Voorbeeld grafiek lichtintensiteit
        self.graph2 = FigureCanvasTkAgg(light_graph.fig, self)
        self.graph2.get_tk_widget().grid(column=0, row=0)

        self.uitrol_label = tk.Label(self, text=" Uitrolgrens:")
        self.uitrol_label.grid(column=1, row=0, sticky=N, pady=50)
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol_choices = ("uit", "50 klx", "60 klx", "70 klx", "80 klx", "90 klx", "100 klx", "110 klx", "120 klx",
                               "130 klx")
        self.uitrol_choiceVar.set(self.uitrol_choices[6])  # standaard op 100 klx
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=7)
        self.uitrol_cb.grid(column=1, row=0, sticky=N, pady=70)

        uitrolgrens_l = tk.Button(self, text="Toepassen", command=lambda: self.uitrolgrens_l(), width=8)
        uitrolgrens_l.grid(column=1, row=0, sticky=N, pady=100)

        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(2), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(2), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(2), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)

        self.uitrol_afstand = tk.Label(self, text="Het rolluik is 2 meter uitgerold")
        self.uitrol_afstand.grid(column=1,row=0,sticky=N,pady=100)

    def uitrolgrens_l(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            self.licht_grens = 0
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            s = self.uitrol_choiceVar.get().split(' ')
            self.licht_grens = int(s[0])
            print("Het zonnescherm wordt automatisch uigerold wanneer de lichtintesiteit", self.uitrol_choiceVar.get(),
                  "overschrijdt.")

    def check_grens(self):  # Lichtintensiteit moet ergens opgehaald worden
        if self.licht_grens != 0 and 'Lichtintensiteit' > self.licht_grens:
            StartPage.rolluik_uitrollen(self)
            self.l_grens = True
        else:
            self.l_grens = False


class Arduino3(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Sensor 3", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)

        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(3), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(3), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(3), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)


class Arduino4(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Sensor 4", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)

        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(4), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(4), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(4), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)


class Arduino5(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Sensor 5", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)

        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(5), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(5), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(5), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)
