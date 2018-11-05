from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.pyplot as plt

"""In deze klasse wordt de layout geinitialiseerd. 
Er word gebruik gemaakt van een canvas om de grafieken op te tekenen
en er zijn tabbladen gemaakt voor de verschillende arduino's"""


class Controller(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Centrale')
        self.controller = self

        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["Arduino1"] = Arduino1(parent=container, controller=self)
        self.frames["Arduino2"] = Arduino2(parent=container, controller=self)
        self.frames["Arduino3"] = Arduino3(parent=container, controller=self)
        self.frames["Arduino4"] = Arduino4(parent=container, controller=self)
        self.frames["Arduino5"] = Arduino5(parent=container, controller=self)
        self.frames["Instellingen"] = Instellingen(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino1"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino2"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino3"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino4"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino5"].grid(row=0, column=0, sticky="nsew")
        self.frames["Instellingen"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """"Show a frame for the given page name"""""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Startpagina", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        a1 = tk.Button(self, text="Arduino 1", command=lambda: self.arduino1())
        a1.pack(side="top", pady=5)

        a2 = tk.Button(self, text="Arduino 2", command=lambda: self.arduino2())
        a2.pack(side="top", pady=5)

        a3 = tk.Button(self, text="Arduino 3", command=lambda: self.arduino3())
        a3.pack(side="top", pady=5)

        a4 = tk.Button(self, text="Arduino 4", command=lambda: self.arduino4())
        a4.pack(side="top", pady=5)

        a5 = tk.Button(self, text="Arduino 5", command=lambda: self.arduino5())
        a5.pack(side="top", pady=5)

        instellen = tk.Button(self, text="Instellingen", command=lambda: self.instellingen())
        instellen.pack(side="top", pady=5)

    def add_ui(self):
        uitrollen = tk.Button(self, text="  Uitrollen   ", command=lambda: self.rolluik_uitrollen())
        uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        inhalen = tk.Button(self, text="   Inhalen    ", command=lambda: self.rolluik_inhalen())
        inhalen.grid(column=1, row=0, sticky=N, pady=180)

        stoppen = tk.Button(self, text="  Stoppen   ", command=lambda: self.stoppen())
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="     Terug     ", command=lambda: self.home())
        terug.grid(column=1, row=0, sticky=N, pady=240)

    def rolluik_uitrollen(self):
        print("Aan het uitrollen")

    def rolluik_inhalen(self):
        print("Aan het inhalen")

    def stoppen(self):
        print("De rolluiken stoppen")

    def home(self):
        self.controller.show_frame("StartPage")

    def arduino1(self):
        self.controller.show_frame("Arduino1")

    def arduino2(self):
        self.controller.show_frame("Arduino2")

    def arduino3(self):
        self.controller.show_frame("Arduino3")

    def arduino4(self):
        self.controller.show_frame("Arduino4")

    def arduino5(self):
        self.controller.show_frame("Arduino5")

    def instellingen(self):
        self.controller.show_frame("Instellingen")


class Arduino1(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Arduino 1", font='Helvetica 18 bold')
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


class Arduino2(StartPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Arduino 2", font='Helvetica 18 bold')
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


class Arduino3(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

        label = tk.Label(self, text="Arduino 3", font='Helvetica 18 bold')
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

        label = tk.Label(self, text="Arduino 4", font='Helvetica 18 bold')
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

        label = tk.Label(self, text="Arduino 5", font='Helvetica 18 bold')
        label.grid(column=1, row=0, sticky=N)

        #  Empty graph
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.graph = FigureCanvasTkAgg(figure, self)
        self.graph.get_tk_widget().grid(column=0, row=0)


class Instellingen(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Instellingen", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        self.uitrol_label = tk.Label(self, text=" Maximale uitrolstand:")
        self.uitrol_label.pack()
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol = ttk.Entry(self, textvariable=self.uitrol_choiceVar)
        self.uitrol.pack(pady=10)

        self.inrol_label = tk.Label(self, text="Maximale inrolstand:")
        self.inrol_label.pack()
        self.inrol_choiceVar = tk.StringVar()
        self.inrol = ttk.Entry(self, textvariable=self.inrol_choiceVar)
        self.inrol.pack(pady=10)

        toepassen = tk.Button(self, text="Toepassen", command=lambda: self.toepassen())
        toepassen.pack(fill="y", pady=10)

        terug = tk.Button(self, text="     Terug     ", command=lambda: self.home())
        terug.pack(fill="y", pady=10)

    def toepassen(self):
        print("De maximale uirolstand is nu:", self.uitrol_choiceVar.get())
        print("De maximale inrolstand is nu:", self.inrol_choiceVar.get())
