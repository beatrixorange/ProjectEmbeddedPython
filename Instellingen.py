import tkinter as tk
from tkinter import ttk
from Startpage import StartPage
import Startpage
import Connection
"""
Hier kunnen de instellingen geregeld worden van de uitrol/inrolstand. 

ToDo:
Hoe groot is het zonnescherm? (dus tot hoe ver kan het maximaal uitgerold worden?)
"""

class Instellingen(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Instellingen", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        text = tk.Label(self, text="Op deze pagina kan je instellen wat de stand van het rolluik moet zijn na het "
                                   "inrollen of uitrollen.\n _________________________")
        text.pack(side="top", fill="x", pady=10)

        self.uitrol_label = tk.Label(self, text="Inrolstand in cm:")
        self.uitrol_label.pack()
        self.inrolstand = tk.Entry(self)
        self.inrolstand.pack(pady=10)

        self.inrol_label = tk.Label(self, text="Uitrolstand in cm:")
        self.inrol_label.pack()
        self.uitrolstand = tk.Entry(self)
        self.uitrolstand.pack(pady=10)

        toepassen1 = tk.Button(self, text="Toepassen inrolstand", command=lambda: self.toepassen_in(), width=20)
        toepassen1.pack(fill="y", pady=10)

        toepassen2 = tk.Button(self, text="Toepassen uitrolstand", command=lambda: self.toepassen_uit(), width=20)
        toepassen2.pack(fill="y", pady=5)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=10)
        terug.pack(fill="y", pady=10)

        self.error = tk.Label(self, text="Error: input moet een getal zijn", fg="red")

    def toepassen_in(self):
        self.error.pack_forget()
        if self.inrolstand.get().isdigit():
            min = self.inrolstand.get()
            i = 0
            if min != None:
                a = str(min)
                char1 = "#".encode()
                for c in Connection.connections:
                    c.write(char1)
                    while len(a) > i:
                        numbers = a[i].encode()
                        c.write(numbers)
                        i = i + 1
                    c.write(char1)
        else:
            self.error.pack(side="top", pady=10)


    def toepassen_uit(self):
        self.error.pack_forget()
        if self.uitrolstand.get().isdigit():
            max = self.uitrolstand.get()
            i = 0
            if min != None:
                a = str(max)
                char1 = "#".encode()
                for c in Connection.connections:
                    c.write(char1)
                    while len(a) > i:
                        numbers = a[i].encode()
                        c.write(numbers)
                        i = i + 1
                    c.write(char1)
        else:
            self.error.pack(side="top", pady=10)

