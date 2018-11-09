from tkinter import *
import tkinter as tk
import Connection
import itertools

"""
Dit is de StartPage daar kun je terecht voor de navigatie tussen de pagina's

ToDo:
Serie nummer van de arduino toevoegen aan de 'aangesloten' functie om te kunnen detecteren of deze is aangesloten.
Uitrollen, inhalen, stoppen functies werkend maken.
"""

uitrolstand = 0
inrolstand = 0


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
        a2.config(state=DISABLED)

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
            Wanneer een van de besturingseenheden wordt aangesloten moet de knop klikbaar worden."""

        def aangesloten():
            if not Connection.result:
                print("No Arduino found")

            # a1 en a2 zijn zogenaamd aangesloten.
            if 1 == 1:  # find_arduino(serial nummer) moet hier komen met het juiste serie nummer
                a1.config(state=NORMAL)
                a2.config(state=NORMAL)
            if len(Connection.result) == 3:
                a3.config(state=NORMAL)
            elif len(Connection.result) == 4:
                a4.config(state=NORMAL)
            elif len(Connection.result) == 5:
                a5.config(state=NORMAL)

        def find_arduino(serial_number):
            for pinfo in Connection.serial.tools.list_ports.comports():
                if pinfo.serial_number == serial_number:
                    return True
                else:
                    return False

        aangesloten()

    def add_ui(self):
        self.uitrollen = tk.Button(self, text="Uitrollen", command=lambda: self.rolluik_uitrollen(), width=8)
        self.uitrollen.grid(column=1, row=0, sticky=N, pady=150)

        self.inhalen = tk.Button(self, text="Inhalen", command=lambda: self.rolluik_inhalen(), width=8)
        self.inhalen.grid(column=1, row=0, sticky=N, pady=180)
        self.inhalen.config(state=DISABLED)

        stoppen = tk.Button(self, text="Stoppen", command=lambda: self.stoppen(), width=8)
        stoppen.grid(column=1, row=0, sticky=N, pady=210)

        terug = tk.Button(self, text="Terug", command=lambda: self.home(), width=8)
        terug.grid(column=1, row=0, sticky=N, pady=240)

        self.uitgerold = False

    def inlezen(self):
        # TODO Uitvinden wat we met het ID doen.
        for c in itertools.cycle(Connection.connections):
            x = c.read()
            if '#' in x:
                l1 = x.split(".")
                afstand = int(l1[1].replace("#",""))
            if '$' in x:
                l2 = x.split(".")
                licht = int(l2[1].replace("&",""))
            if '%' in x:
                l3 = x.split(".")
                temp = int(l3[1].replace("%",""))

    def rolluik_uitrollen(self):
        print("Aan het uitrollen...")
        self.uitrollen.config(state=DISABLED)
        self.inhalen.config(state=NORMAL)
        if uitrolstand == 0:
            print("Het rolluik is helemaal uitgerold.")
        else:
            print("Het rolluik is uitgerold", uitrolstand, "cm.")

    def rolluik_inhalen(self):
        print("Aan het inhalen...")
        self.inhalen.config(state=DISABLED)
        self.uitrollen.config(state=NORMAL)
        if inrolstand == 0:
            print("Het rolluik is helemaal ingerold.")
        else:
            print("De stand van het rolluik is", inrolstand, "cm.")

    def stoppen(self):
        print("De rolluiken stoppen")

    # Deze functie zorgt ervoor dat je naar de StartPage gaat.
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
