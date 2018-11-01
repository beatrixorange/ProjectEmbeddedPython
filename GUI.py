from tkinter import *
from tkinter import ttk
import tkinter as tk

"""In deze klasse wordt de layout geinitialiseerd. 
Er word gebruik gemaakt van een canvas om de grafieken op te tekenen
en er zijn tabbladen gemaakt voor de verschillende arduino's"""

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Centrale')
        self.controller = self

        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["Instellingen"] = Instellingen(parent=container, controller=self)
        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Instellingen"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.addtabs()

        button1 = tk.Button(self, text="Instellingen", command=lambda: self.instellingen())
        button1.pack(side="right", padx=30)

        uitrollen = tk.Button(self, text="  Uitrollen   ", command=lambda: self.rolluik_uitrollen())
        uitrollen.pack(side="left", padx=10)

        inhalen = tk.Button(self, text="  Inhalen   ", command=lambda: self.rolluik_inhalen())
        inhalen.pack(side="left", padx=10)

        stoppen = tk.Button(self, text="  Stoppen   ", command=lambda: self.stoppen())
        stoppen.pack(side="left", padx=10)

    def addtabs(self):
        self.notebook = ttk.Notebook(self.controller)
        self.tab1 = ttk.Frame(self.controller)
        self.tab2 = ttk.Frame(self.controller)
        self.tab3 = ttk.Frame(self.controller)
        self.tab4 = ttk.Frame(self.controller)
        self.tab5 = ttk.Frame(self.controller)
        self.notebook.add(self.tab1, text='Arduino1')
        self.notebook.add(self.tab2, text='Arduino2')
        self.notebook.add(self.tab3, text='Arduino3')
        self.notebook.add(self.tab4, text='Arduino4')
        self.notebook.add(self.tab5, text='Arduino5')
        self.notebook.pack()

        self.graph1 = Canvas(self.tab1, width=675, height=475)
        self.graph1.create_rectangle([10, 10, 650, 450], fill='blue')  # placeholder voor grafiek
        self.graph1.grid(column=1, row=0)

        self.graph2 = Canvas(self.tab2, width=675, height=475)
        self.graph2.create_rectangle([10, 10, 650, 450], fill='red')  # placeholder voor grafiek
        self.graph2.grid(column=2, row=0)

        self.graph3 = Canvas(self.tab3, width=675, height=475)
        self.graph3.grid(column=3, row=0)

        self.graph4 = Canvas(self.tab4, width=675, height=475)
        self.graph4.grid(column=4, row=0)

        self.graph5 = Canvas(self.tab5, width=675, height=475)
        self.graph5.grid(column=5, row=0)

    def instellingen(self):
        self.notebook.hide(self.tab1)
        self.notebook.hide(self.tab2)
        self.notebook.hide(self.tab3)
        self.notebook.hide(self.tab4)
        self.notebook.hide(self.tab5)
        self.controller.show_frame("Instellingen")

    def rolluik_uitrollen(self):
        print("Aan het uitrollen")

    def rolluik_inhalen(self):
        print("Aan het inhalen")

    def stoppen(self):
        print("De rolluiken stoppen")

class Instellingen(StartPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Instellingen")
        label.pack(side="top", fill="x", pady=10)

        startpage = tk.Button(self, text="Terug", command=lambda: self.start())
        startpage.pack(side="left", padx=10)

        toepassen = tk.Button(self, text="Toepassen", command=lambda: self.toepassen())
        toepassen.pack(side="right", padx=10)

    def start(self):
        self.controller.show_frame("StartPage")
        self.addtabs()

    def toepassen(self):
        print("De instellingen zijn toegepast.")

