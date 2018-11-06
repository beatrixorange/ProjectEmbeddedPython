from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.pyplot as plt

"""
In deze file staan meerdere klassen. Elke klasse is een pagina opzich.
Er is een StartPage daar kun je terecht voor de navigatie tussen de pagina's
Verder zijn er 5 Arduino pagina's voor de 5 mogelijke besturingseenheden.
Als laatste is er nog een instelling pagina. Hier kunnen de instellingen voor de eenheden geregeld worden.
"""

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Startpagina", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        a1 = tk.Button(self, text="Temperatuur", command=lambda: self.arduino1(), width=20)
        a1.pack(side="top", pady=5)
        a1.config(state=DISABLED)

        a2 = tk.Button(self, text="Lichtintensiteit", command=lambda: self.arduino2(), width=20)
        a2.pack(side="top", pady=5)
        a1.config(state=DISABLED)

        a3 = tk.Button(self, text="Sensor 3", command=lambda: self.arduino3(), width=20)
        a3.pack(side="top", pady=5)
        a3.config(state=DISABLED)

        a4 = tk.Button(self, text="Sensor 4", command=lambda: self.arduino4(), width=20)
        a4.pack(side="top", pady=5)
        a4.config(state=DISABLED)

        a5 = tk.Button(self, text="Sensor 5", command=lambda: self.arduino5(), width=20)
        a5.pack(side="top", pady=5)
        a5.config(state=DISABLED)

        instellen = tk.Button(self, text="Instellingen", command=lambda: self.instellingen(), width=20)
        instellen.pack(side="top", pady=5)

        """ Alleen besturingseenheden weergeven die aangesloten zijn.
            Wanneer een van de besturingseenheden wordt aangesloten moet de knop klikbaar worden.
            a1 en a2 zijn zogenaamd aangesloten. """

        def aangesloten():
            if 1 == True:
                a1.config(state=NORMAL)
            if 1 == True:
                a2.config(state=NORMAL)
            if 0 == True:
                a3.config(state=NORMAL)
            if 0 == True:
                a4.config(state=NORMAL)
            if 0 == True:
                a4.config(state=NORMAL)

        aangesloten()

    def add_ui(self):
        uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(), width=8)
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(), width=8)
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)

    @staticmethod
    def rolluik_uitrollen():
        print("Aan het uitrollen")

    @staticmethod
    def rolluik_inhalen():
        print("Aan het inhalen")

    @staticmethod
    def stoppen():
        print("De rolluiken stoppen")

    #Deze functie zorgt ervoor dat je naar de StartPage gaat.
    def home(self):
        self.controller.show_frame("StartPage")

    # Deze functie zorgt ervoor dat je naar de eerste Arduino pagina gaat.
    def arduino1(self):
        self.controller.show_frame("Arduino1")

    # Deze functie zorgt ervoor dat je naar de tweede Arduino pagina gaat.
    def arduino2(self):
        self.controller.show_frame("Arduino2")

    # Deze functie zorgt ervoor dat je naar de derde Arduino pagina gaat.
    def arduino3(self):
        self.controller.show_frame("Arduino3")

    # Deze functie zorgt ervoor dat je naar de vierde Arduino pagina gaat.
    def arduino4(self):
        self.controller.show_frame("Arduino4")

    # Deze functie zorgt ervoor dat je naar de vijfde Arduino pagina gaat.
    def arduino5(self):
        self.controller.show_frame("Arduino5")

    # Deze functie zorgt ervoor dat je naar de instellingen pagina gaat.
    def instellingen(self):
        self.controller.show_frame("Instellingen")


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
        self.uitrol_choiceVar.set(self.uitrol_choices[3])  # standaard op 30°C
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=7)
        self.uitrol_cb.grid(column=1, row=0, sticky=N, pady=70)

        uitrolgrens_t = tk.Button(self, text="Toepassen", command=lambda: self.uitrolgrens_t(), width=8)
        uitrolgrens_t.grid(column=1, row=0, sticky=N, pady=100)

    def uitrolgrens_t(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            print("Het zonnescherm wordt automatisch uitgerold wanneer het warmer dan", self.uitrol_choiceVar.get(), "is.")


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
        self.uitrol_choices = ("uit", "50 klx", "60 klx", "70 klx", "80 klx", "90 klx", "100 klx", "110 klx", "120 klx", "130 klx")
        self.uitrol_choiceVar.set(self.uitrol_choices[6])  # standaard op 100 klx
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=7)
        self.uitrol_cb.grid(column=1, row=0, sticky=N, pady=70)

        uitrolgrens_l = tk.Button(self, text="Toepassen", command=lambda: self.uitrolgrens_l(), width=8)
        uitrolgrens_l.grid(column=1, row=0, sticky=N, pady=100)

    def uitrolgrens_l(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            print("Automatisch uitrollen is uitgeschakeld.")
        else:
            print("Het zonnescherm wordt automatisch uigerold wanneer de lichtintesiteit", self.uitrol_choiceVar.get(), "overschrijdt.")


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
