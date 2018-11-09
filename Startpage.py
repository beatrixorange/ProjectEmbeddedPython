from tkinter import *
import tkinter as tk
import Connection

"""
Dit is de StartPage daar kun je terecht voor de navigatie tussen de pagina's

ToDo:
Serie nummer van de arduino toevoegen aan de 'aangesloten' functie om te kunnen detecteren of deze is aangesloten.
Uitrollen, inhalen, stoppen functies werkend maken.
"""

uitrolstand = 0
inrolstand = 0
id_list = []


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
            # a1 en a2 zijn zogenaamd aangesloten.
            if len(Connection.connections) >= 1:  # find_arduino(serial nummer) moet hier komen met het juiste serie nummer
                a1.config(state=NORMAL)
                print(len(Connection.connections))
            if len(Connection.connections) >= 2:
                a2.config(state=NORMAL)
            if len(Connection.connections) == 3:
                a3.config(state=NORMAL)
            if len(Connection.connections) == 4:
                a4.config(state=NORMAL)
            if len(Connection.connections) == 5:
                a5.config(state=NORMAL)

        def find_arduino(serial_number):
            for pinfo in Connection.serial.tools.list_ports.comports():
                if pinfo.serial_number == serial_number:
                    return True
                else:
                    return False
        aangesloten()

    def rolluik_uitrollen(self, id):
        i = 1
        while i < 6:
            if id == i:
                c = Connection.connections[i-1]
                char1 = ('&').encode()
                char2 = ('d').encode()
                char3 = ('&').encode()
                c.write(char1)
                c.write(char2)
                c.write(char3)
                print(id)
            i += 1



    def stuur_id(self):
        i = 1
        for c in Connection.connections:
            c.write("&").encode()
            c.write(i).encode()
            c.write("&").encode()
            id_list.append(i)
            i + 1

    def rolluik_inhalen(self, id):
        i = 1
        while i < 6:
            if id == i:
                c = Connection.connections[i-1]
                char1 = ('&').encode()
                char2 = ('u').encode()
                char3 = ('&').encode()
                c.write(char1)
                c.write(char2)
                c.write(char3)
                print(id)
            i += 1

    def stoppen(self, id):
        i = 1
        while i < 6:
            if id == i:
                c = Connection.connections[i-1]
                char1 = ('&').encode()
                char2 = ('s').encode()
                char3 = ('&').encode()
                c.write(char1)
                c.write(char2)
                c.write(char3)
                print(id)
            i += 1

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
