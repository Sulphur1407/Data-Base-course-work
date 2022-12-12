import logic
import tkinter as tk
from tkinter import ttk


def main():
    window = tk.Tk()
    window.title("Курсова робота")
    window.geometry("960x540")

    tabControl = ttk.Notebook(window)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1, text="Визначити план диспетчирського відділу")
    tabControl.add(tab2, text="Внести дані про брак")
    tabControl.add(tab3, text="Отримати звіт")
    tabControl.pack(expand=1, fill="both")

    # tab1
    ttk.Label(tab1, text="План диспетчирського відділу за:").place(x=20, y=20)
    months = ("січень", "лютий", "березень", "квітень", "травень", "червень",
               "липень", "серпень", "вересень", "жовтень", "листопад", "грудень")
    com_month = ttk.Combobox(tab1, values=months).place(x=220, y=20)
    com_year = ttk.Combobox(tab1, values=(2020, 2021, 2022, 2023)).place(x=380, y=20)
    ttk.Button(tab1, text="Отримати дані", command=logic.get_data()).place(x=540, y=18)
    ttk.Button(tab1, text="Завантажити дані").place(x=645, y=18)

    sizes = logic.get_sizes()
    fashions = logic.get_fashions()


    # Table:
    table = tk.Frame(tab1)
    table.pack
    table.place(x=0, y=50)

    rows = []
    for i in range(len(fashions) + 1):
        cols = []
        for j in range(len(sizes) + 1):
            if i == 0 and j == 0:
                #e = tk.Entry(table, relief=tk.RIDGE)
                #e.grid(row=i, column=j, sticky=tk.NSEW)
                #e.insert(tk.END, "Фасон")
                #cols.append(e)
                tk.Label(table, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
            elif i == 0:
                tk.Label(table, text=sizes[j-1]).grid(row=i, column=j, sticky=tk.NSEW)
            elif j == 0:

                tk.Label(table, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
            else:
                e = tk.Entry(table, relief=tk.RIDGE)
                e.grid(row=i, column=j, sticky=tk.NSEW)
                cols.append(e)
        rows.append(cols)

    window.mainloop()
    """
    for row in range(len(fashions)+1):
        for column in range(len(sizes)+1):
            if row == 0:
                if column == 0:
                    label = tk.Label(tab1, text="Фасон")
                    label.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
                else:
                    label = tk.Label(tab1, text=str(sizes[column-1]))
                    #label.grid(row=row, column=column, sticky="nsew", padx=1, pady=50)
                    label.place(x=50*column, y=50)

            if column == 0:
                if row > 0:
                    label = tk.Label(tab1, text=str(fashions[row - 1]))
                    #label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    label.place(x=50, y=50*row)
    

                #label = tk.Entry(tab1, text="Heading : " + str(column))
                #label.config(font=('Arial', 14))
                #label.grid(row=row, column=column, sticky="nsew", padx=1, pady=50)
                #tab1.grid_columnconfigure(column, weight=1)
            else:
                label = tk.Entry(tab1, text="Row : " + str(row) + " , Column : " + str(column))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
    """

    """  
            
    # tab2
    ttk.Label(tab2, text="План диспетчирського відділу за:").place(x=20, y=20)
    ttk.Combobox(tab2, values=(1, 2, 3, 4)).place(x=220, y=20)
    ttk.Combobox(tab2, values=(2020, 2021, 2022)).place(x=380, y=20)
    ttk.Button(tab2, text="Отримати дані").place(x=580, y=18)
    ttk.Button(tab2, text="Завантажити дані").place(x=720, y=18)"""


if __name__ == "__main__":
    main()
