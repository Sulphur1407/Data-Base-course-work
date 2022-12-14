import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import mysql.connector

class MainApplication(tk.Frame):
    def __init__(self, *args, **kwargs):
        parent = tk.Tk()
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


        window = self.parent
        window.title("Курсова робота")
        window.geometry("1425x940")

        tabControl = ttk.Notebook(window)
        self.tab1 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)


        tabControl.add(self.tab1, text="Визначити план диспетчирського відділу")
        tabControl.add(self.tab2, text="Внести дані про брак")
        tabControl.pack(expand=1, fill="both")
        window.mainloop()

if __name__ == "__main__":

    MainApplication().pack(side="top", fill="both", expand=True)




