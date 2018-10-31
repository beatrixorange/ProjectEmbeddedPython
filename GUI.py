from tkinter import *
from tkinter import ttk

"""In deze klasse wordt de layout geinitialiseerd. 
Er word gebruik gemaakt van een canvas om de grafieken op te tekenen
en er zijn tabbladen gemaakt voor de verschillende arduino's"""
class App:
    def __init__(self, master):
        self.master = master
        master.title('Centrale')
        self.notebook = ttk.Notebook(master)
        self.tab1 = ttk.Frame(master)
        self.tab2 = ttk.Frame(master)
        self.tab3 = ttk.Frame(master)
        self.tab4 = ttk.Frame(master)
        self.tab5 = ttk.Frame(master)

        self.graph1 = Canvas(self.tab1, width=675, height=475)
        self.graph2 = Canvas(self.tab2, width=675, height=475)
        self.graph3 = Canvas(self.tab3, width=675, height=475)
        self.graph4 = Canvas(self.tab4, width=675, height=475)
        self.graph5 = Canvas(self.tab5, width=675, height=475)

    def initialiseren(self):
        self.notebook.add(self.tab1, text='Arduino1')
        self.notebook.add(self.tab2, text='Arduino2')
        self.notebook.add(self.tab3, text='Arduino3')
        self.notebook.add(self.tab4, text='Arduino4')
        self.notebook.add(self.tab5, text='Arduino5')
        self.notebook.grid(column=0, row=0)

        self.graph1.create_rectangle([10, 10, 650, 450], fill='blue')   #placeholder voor grafiek
        self.graph1.grid(column=1, row=0)
        self.graph2.create_rectangle([10, 10, 650, 450],fill='red')     #placeholder voor grafiek
        self.graph2.grid(column=2, row=0)
        self.graph3.grid(column=3, row=0)
        self.graph4.grid(column=4, row=0)
        self.graph5.grid(column=5, row=0)

        self.uitrollen = Button(self.master, text="  Uitrollen   ", command=self.rolluik_uitrollen)
        self.uitrollen.grid(column=0, row=1,sticky=W)

        self.inhalen = Button(self.master, text="    Inhalen    ", command=self.rolluiken_inhalen)
        self.inhalen.grid(column=0, row=1,sticky=W,padx=100)

        self.stoppen = Button(self.master, text="    Stoppen    ", command=self.stoppen)
        self.stoppen.grid(column=0, row=1,sticky=W,padx=200)

        self.instellingen = Button(self.master, text="   Instellingen    ", command=self.instellingen)
        self.instellingen.grid(column=1,row=0,sticky=N,pady=25)

    def rolluik_uitrollen(self):
        print("Aan het uitrollen")

    def rolluiken_inhalen(self):
        print("Aan het inhalen")

    def stoppen(self):
        print("De rolluiken stoppen")

    def instellingen(self):
        print("Naar instelingen pagina gaan")




