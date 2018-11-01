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
        self.addtabs()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

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

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Instellingen", command=lambda: instellingen())
        button1.pack(side="right", padx=30)

        def instellingen():
            app.notebook.destroy()
            controller.show_frame("Instellingen")

        uitrollen = tk.Button(self, text="  Uitrollen   ", command=lambda: rolluik_uitrollen(self))
        uitrollen.pack(side="left", padx=10)

        inhalen = tk.Button(self, text="  Inhalen   ", command=lambda: rolluik_inhalen(self))
        inhalen.pack(side="left", padx=10)

        stoppen = tk.Button(self, text="  Stoppen   ", command=lambda: stoppen(self))
        stoppen.pack(side="left", padx=10)

        def rolluik_uitrollen(self):
            print("Aan het uitrollen")

        def rolluik_inhalen(self):
            print("Aan het inhalen")

        def stoppen(self):
            print("De rolluiken stoppen")

class Instellingen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Instellingen", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        uitrol_label = tk.Label(self, text="Maximale uitrolstand")
        uitrol_label.pack()
        uitrol_choiceVar = tk.StringVar()
        uitrol_choices = ("10", "20", "30", "40")
        uitrol_choiceVar.set(uitrol_choices[0])
        uitrol_cb = ttk.Combobox(self, textvariable=uitrol_choiceVar, values=uitrol_choices)
        uitrol_cb.pack()

        inrol_label = tk.Label(self, text="Maximale inrolstand")
        inrol_label.pack()
        inrol_choiceVar = tk.StringVar()
        inrol_choices = ("10", "20", "30", "40")
        inrol_choiceVar.set(inrol_choices[0])
        inrol_cb = ttk.Combobox(self, textvariable=inrol_choiceVar, values=inrol_choices)
        inrol_cb.pack()

        startpage = tk.Button(self, text="Terug", command=lambda: start())
        startpage.pack(side="left", padx=10)

        def start():
            controller.show_frame("StartPage")
            app.addtabs()

        toepassen = tk.Button(self, text="Toepassen", command=lambda: toepassen(self))
        toepassen.pack(side="right", padx=10)

        def toepassen(self):
            print("De instellingen zijn toegepast.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
