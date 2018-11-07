from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.pyplot as plt
from Startpage import StartPage

"""
In deze file staan meerdere klassen. 
Elke klasse is een van de 5 Arduino pagina's voor de 5 mogelijke besturingseenheden.

ToDo:
Live grafieken toevoegen die de data van de sensoren laten zien. 
Grafiek 1: temperatuur per 40 seconden, grafiek 2: lichtintensiteit per 30 seconden.
Er moet gekeken worden wannneer een grens berijkt wordt.
Er moet doorgegeven worden dat de roluiken uitgerold moeten worden wanneer deze grens berijkt wordt.
Er moet doorgegeven worden dat de roluiken ingerold moeten worden wanneer de temperatuur/lichtintensiteit zich weer
onder de grens bevindt.
"""


class Arduino1(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Temperatuur", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Voorbeeld grafiek temperatuur
        data = {'Tijd': [14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'Temperatuur': [11, 10, 9, 8, 7, 5, 4, 4, 4, 4]}
        df = DataFrame(data, columns=['Tijd', 'Temperatuur'])
        df = df[['Tijd', 'Temperatuur']].groupby('Tijd').sum()
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        self.graph1 = FigureCanvasTkAgg(figure, self)
        df.plot(kind='line', legend=True, ax=ax, color='b', fontsize=10)
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

    def uitrolgrens_t(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            self.temp_grens = None
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            s = self.uitrol_choiceVar.get().split('°')
            self.temp_grens = int(s[0])
            print("Het zonnescherm wordt automatisch uitgerold wanneer het warmer dan", self.uitrol_choiceVar.get(),
                  "is.")

    def check_grens(self):  # temperatuur moet ergens opgehaald worden
        if self.temp_grens is not None and 'Temperatuur' > self.uitrol_choiceVar.get():
            StartPage.rolluik_uitrollen()


class Arduino2(StartPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Lichtintensiteit", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Voorbeeld grafiek lichtintensiteit
        data2 = {'Tijd': [14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                 'Lichtintensiteit': [10, 8, 6, 3, 2.5, 2, 1.5, 1, 1, 1]}
        df2 = DataFrame(data2, columns=['Tijd', 'Lichtintensiteit'])
        df2 = df2[['Tijd', 'Lichtintensiteit']].groupby('Tijd').sum()
        figure2 = plt.Figure(figsize=(7, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        self.graph2 = FigureCanvasTkAgg(figure2, self)
        df2.plot(kind='line', legend=True, ax=ax2, color='b', fontsize=10)
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

    def uitrolgrens_l(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            self.licht_grens = None
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            s = self.uitrol_choiceVar.get().split(' ')
            self.licht_grens = int(s[0])
            print("Het zonnescherm wordt automatisch uigerold wanneer de lichtintesiteit", self.uitrol_choiceVar.get(),
                  "overschrijdt.")

    def check_grens(self):  # Lichtintensiteit moet ergens opgehaald worden
        if self.licht_grens is not None and 'Lichtintensiteit' > self.licht_grens:
            StartPage.rolluik_uitrollen()


class Arduino3(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Sensor 3", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)


class Arduino4(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Sensor 4", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)


class Arduino5(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Sensor 5", font='Helvetica 18 bold', width=12)
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)
