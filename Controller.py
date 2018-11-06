import tkinter as tk
import Pages
import Instellingen

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
        self.frames["StartPage"] = Pages.StartPage(parent=container, controller=self)
        self.frames["Arduino1"] = Pages.Arduino1(parent=container, controller=self)
        self.frames["Arduino2"] = Pages.Arduino2(parent=container, controller=self)
        self.frames["Arduino3"] = Pages.Arduino3(parent=container, controller=self)
        self.frames["Arduino4"] = Pages.Arduino4(parent=container, controller=self)
        self.frames["Arduino5"] = Pages.Arduino5(parent=container, controller=self)
        self.frames["Instellingen"] = Instellingen.Instellingen(parent=container, controller=self)

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