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
        tab1 = ttk.Frame(master)
        tab2 = ttk.Frame(master)
        self.notebook.add(tab1, text='Arduino1')
        self.notebook.add(tab2, text='Arduino2')
        self.notebook.pack(expand=1, fill='both')

        self.graph1 = Canvas(tab1, width=1000,height=500)
        self.graph1.create_rectangle([10, 10, 650, 630], fill='blue') #placeholder voor grafiek
        self.graph1.pack(fill=BOTH, expand=1)

        self.graph2 = Canvas(tab2, width=1000,height=500)
        self.graph2.create_rectangle([10, 10, 650, 630], fill='red') #placeholder voor grafiek
        self.graph2.pack(fill=BOTH, expand=1)

        self.graph1.pack
        self.graph2.pack


root = Tk()
app = App(root)
root.mainloop()
