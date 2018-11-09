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

        self.uitrol_label = tk.Label(self, text=" Maximale uitrolstand:")
        self.uitrol_label.pack()
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol_choices = ("max", "-10 cm", "-20 cm", "-30 cm")
        self.uitrol_choiceVar.set(self.uitrol_choices[0])
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=15)
        self.uitrol_cb.pack(pady=10)

        self.inrol_label = tk.Label(self, text="Maximale inrolstand:")
        self.inrol_label.pack()
        self.inrol_choiceVar = tk.StringVar()
        self.inrol_choices = ("min", "10 cm", "20 cm", "30 cm")
        self.inrol_choiceVar.set(self.inrol_choices[0])
        self.inrol_cb = ttk.Combobox(self, textvariable=self.inrol_choiceVar, values=self.inrol_choices, width=15)
        self.inrol_cb.pack(pady=10)

        toepassen = tk.Button(self, text="Toepassen", command=lambda: self.toepassen(), width=10)
        toepassen.pack(fill="y", pady=10)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=10)
        terug.pack(fill="y", pady=10)

    def toepassen(self):
        if self.uitrol_choiceVar.get() == self.uitrol_choices[0]:
            Startpage.uitrolstand = 0
            print("De maximale uitrolstand is nu -", Startpage.uitrolstand, "cm.")
        else:
            s = self.uitrol_choiceVar.get().split(' ')
            Startpage.uitrolstand = int(s[0])
            print("De maximale uitrolstand is nu:", Startpage.uitrolstand, "cm.")

        if self.inrol_choiceVar.get() == self.inrol_choices[0]:
            Startpage.inrolstand = 0
            print("De maximale inrolstand is nu", Startpage.inrolstand, "cm.")
        else:
            s = self.inrol_choiceVar.get().split(' ')
            Startpage.inrolstand = int(s[0])
            print("De maximale inrolstand is nu:", Startpage.inrolstand, "cm.")
