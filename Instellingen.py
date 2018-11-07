import tkinter as tk
from tkinter import ttk
from Startpage import StartPage

"""
Hier kunnen de instellingen geregeld worden van de uitrol/inrolstand. 

ToDo:
Hoe groot is het zonnescherm? (dus tot hoe ver kan het maximaal uitgerold worden?)
Een aantal standen bedenken voor tot hoe ver je het scherm wil inrollen (standaard 0cm)  en uitrollen (standaard max)
Dit moet doorgegeven worden om op het display te kunnen laten zien hoe ver het rolluik is uitgerold.
"""


class Instellingen(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Instellingen", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        self.uitrol_label = tk.Label(self, text=" Maximale uitrolstand:")
        self.uitrol_label.pack()
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol_choices = ("Stand 1", "Stand 2", "Stand 3", "Stand 4")
        self.uitrol_choiceVar.set(self.uitrol_choices[0])
        self.uitrol_cb = ttk.Combobox(self, textvariable=self.uitrol_choiceVar, values=self.uitrol_choices, width=15)
        self.uitrol_cb.pack(pady=10)

        self.inrol_label = tk.Label(self, text="Maximale inrolstand:")
        self.inrol_label.pack()
        self.inrol_choiceVar = tk.StringVar()
        self.inrol_choices = ("Stand 1", "Stand 2", "Stand 3", "Stand 4")
        self.inrol_choiceVar.set(self.inrol_choices[3])
        self.inrol_cb = ttk.Combobox(self, textvariable=self.inrol_choiceVar, values=self.inrol_choices, width=15)
        self.inrol_cb.pack(pady=10)

        toepassen = tk.Button(self, text="Toepassen", command=lambda: self.toepassen(), width=10)
        toepassen.pack(fill="y", pady=10)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=10)
        terug.pack(fill="y", pady=10)

    def toepassen(self):
        print("De maximale uirolstand is nu:", self.uitrol_choiceVar.get())
        print("De maximale inrolstand is nu:", self.inrol_choiceVar.get())
