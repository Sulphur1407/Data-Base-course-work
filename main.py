import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import mysql.connector

months = ("січень", "лютий", "березень", "квітень", "травень", "червень",
          "липень", "серпень", "вересень", "жовтень", "листопад", "грудень")
years = (2020, 2021, 2022, 2023)


class DataBase():
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abunaraze",
            database="db_sol"
        )
        self.mycursor = self.mydb.cursor()

    def get_sizes(self):
        self.mycursor.execute("SELECT DISTINCT size FROM Shoes_variant ORDER BY size")
        result = self.mycursor.fetchall()
        sizes = []
        for sequence in result:
            sizes.append(sequence[0])
        return sizes

    def get_fashions(self):
        self.mycursor.execute("SELECT DISTINCT fashion FROM Shoes_variant ORDER BY fashion")
        result = self.mycursor.fetchall()
        fashions = []
        for sequence in result:
            fashions.append(sequence[0])
        return fashions

    @property
    def mydb(self):
        return self.__mydb

    @mydb.setter
    def mydb(self, value):
        self.__mydb = value


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.db = DataBase()

        window = self.parent
        window.title("Курсова робота")
        window.geometry("1425x840")

        tabControl = ttk.Notebook(window)
        self.tab1 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)
        self.tab3 = ttk.Frame(tabControl)
        self.tab4 = ttk.Frame(tabControl)

        tabControl.add(self.tab1, text="Визначити план диспетчирського відділу")
        tabControl.add(self.tab2, text="Внести дані про брак")
        tabControl.add(self.tab3, text="Отримати звіт")
        tabControl.add(self.tab4, text="Управління фасонами")
        tabControl.pack(expand=1, fill="both")
        #   TAB1
        ttk.Label(self.tab1, text="План диспетчирського відділу за:").place(x=20, y=20)

        self.tab1_com_month = ttk.Combobox(self.tab1, values=months)
        self.tab1_com_month.place(x=220, y=20)

        self.tab1_com_year = ttk.Combobox(self.tab1, values=years)
        self.tab1_com_year.place(x=380, y=20)

        self.tab1_get_data_button = ttk.Button(self.tab1, text="Отримати дані", command=self.tab1_get_data)
        self.tab1_get_data_button.place(x=540, y=18)

        self.tab1_put_data_button = ttk.Button(self.tab1, text="Завантажити дані", command=self.tab1_put_data)
        self.tab1_put_data_button.place(x=645, y=18)

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        #  Фрейм для таблиці
        tab1_table = tk.Frame(self.tab1)
        tab1_table.pack
        tab1_table.place(x=0, y=50)

        # Table:
        self.tab1_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(tab1_table, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(tab1_table, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(tab1_table, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Entry(tab1_table, relief=tk.RIDGE)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab1_table.append(cols)

        #   TAB2
        ttk.Label(self.tab2, text="Дані про брак за:").place(x=20, y=20)

        self.tab2_com_month = ttk.Combobox(self.tab2, values=months)
        self.tab2_com_month.place(x=130, y=20)

        self.tab2_com_year = ttk.Combobox(self.tab2, values=years)
        self.tab2_com_year.place(x=290, y=20)

        self.tab2_get_data_button = ttk.Button(self.tab2, text="Отримати дані", command=self.tab2_get_data)
        self.tab2_get_data_button.place(x=450, y=18)

        self.tab2_put_data_button = ttk.Button(self.tab2, text="Завантажити дані", command=self.tab2_put_data)
        self.tab2_put_data_button.place(x=555, y=18)

        #  Фрейм для таблиці
        tab2_table = tk.Frame(self.tab2)
        tab2_table.pack
        tab2_table.place(x=0, y=50)

        # Table:
        self.tab2_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(tab2_table, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(tab2_table, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(tab2_table, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Entry(tab2_table, relief=tk.RIDGE)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab2_table.append(cols)

        #   TAB3
        ttk.Label(self.tab3, text="Дані про брак за:").place(x=20, y=20)
        self.tab3_com_month = ttk.Combobox(self.tab3, values=months)
        self.tab3_com_month.place(x=130, y=20)
        self.tab3_com_year = ttk.Combobox(self.tab3, values=years)
        self.tab3_com_year.place(x=290, y=20)
        self.tab3_get_data_button = ttk.Button(self.tab3, text="Отримати звіт", command=self.tab3_get_report)
        self.tab3_get_data_button.place(x=450, y=18)
        #  Фрейм для таблиці
        tab3_table = tk.Frame(self.tab3)
        tab3_table.pack
        tab3_table.place(x=0, y=50)
        # Table:
        self.tab3_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(tab3_table, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(tab3_table, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(tab3_table, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Label(tab3_table, relief=tk.RIDGE, width=17, height=1)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab3_table.append(cols)

        #  TAB4
        ttk.Label(self.tab4, text="Додати фасон:").place(x=20, y=20)
        self.tab4_entry_fashion_add = tk.Entry(self.tab4, relief=tk.RIDGE, width=23)
        self.tab4_entry_fashion_add.place(x=140, y=20)
        self.tab4_button_fashion_add = ttk.Button(self.tab4, text="Додати фасон", command=self.tab4_add_fashion)
        self.tab4_button_fashion_add.place(x=290, y=18)

        ttk.Label(self.tab4, text="Видалити фасон:").place(x=20, y=60)
        self.tab4_com_fashion = ttk.Combobox(self.tab4, values=years)
        self.tab4_com_fashion.place(x=140, y=60)
        self.tab4_get_data_button = ttk.Button(self.tab4, text="Видалити фасон", command=self.tab4_delete_fashion)
        self.tab4_get_data_button.place(x=290, y=58)

    def refresh(self):
        self.weight_entry.delete(0, "end")
        self.text.delete("1.0", "end")

    def clear_table(self):
        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                self.tab1_table[i][j].delete(0, 100)
                self.tab2_table[i][j].delete(0, 100)
                self.tab3_table[i][j].config(text="")

    def tab1_get_data(self):

        if not self.tab1_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None
        if not self.tab1_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        month = months.index(self.tab1_com_month.get()) + 1
        year = self.tab1_com_year.get()

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        self.clear_table()

        ind = True

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                GetNumberFormula = """SELECT number
                                          FROM plan_db
                                          JOIN shoes_variant as sv
                                              USING(id_shoes_variant)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(data) = %s and YEAR(data) = %s
                    """
                self.db.mycursor.execute(GetNumberFormula, (fashions[i], sizes[j], month, year))
                result = self.db.mycursor.fetchone()
                if result:
                    ind = False
                    self.tab1_table[i][j].insert(0, result[0])

        if ind:
            messagebox.showinfo("", "Дані відсутні!")

    #  TAB1 Buttons
    def tab1_put_data(self):
        if not self.tab1_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None
        if not self.tab1_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        month = months.index(self.tab1_com_month.get()) + 1
        year = self.tab1_com_year.get()

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                if self.tab1_table[i][j].get():

                    try:
                        value = int(self.tab1_table[i][j].get())
                    except ValueError:
                        messagebox.showerror("Помилка!", "В коміркках маєть бути цілі числа!")
                        return None
                    if value > 9999:
                        messagebox.showerror("Помилка!", "Максимальна кількьсть 9999!")
                        return None

                    if value < 0:
                        messagebox.showerror("Помилка!", "Мінімальна кількість 0!")
                        return None

                    GetNumberFormula = """SELECT number
                                          FROM plan_db
                                          JOIN shoes_variant as sv
                                              USING(id_shoes_variant)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(data) = %s and YEAR(data) = %s
                                        """

                    self.db.mycursor.execute(GetNumberFormula, (fashions[i], sizes[j], month, year))
                    result = self.db.mycursor.fetchone()

                    if result:
                        UpdateNumber = """UPDATE plan_db
                                          JOIN shoes_variant as sv
                                              USING(id_shoes_variant)
                                          SET number = %s
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(data) = %s and YEAR(data) = %s
                                        """

                        self.db.mycursor.execute(UpdateNumber, (value, fashions[i], sizes[j], month, year))
                        self.db.mydb.commit()

                    else:
                        date = str(year) + "-" + str(month) + "-1"

                        GetIdFormula = """SELECT id_shoes_variant
                                          FROM shoes_variant
                                          WHERE fashion = %s and size = %s"""

                        self.db.mycursor.execute(GetIdFormula, (fashions[i], sizes[j]))

                        id_shoes_variant = self.db.mycursor.fetchone()[0]

                        UpdateNumber = """INSERT INTO plan_db
                                          VALUES(DEFAULT, %s, %s, %s)"""

                        self.db.mycursor.execute(UpdateNumber, (value, date, id_shoes_variant))
                        self.db.mydb.commit()

    #  TAB2 Buttons
    def tab2_get_data(self):

        if not self.tab2_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None
        if not self.tab2_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        month = months.index(self.tab2_com_month.get()) + 1
        year = self.tab2_com_year.get()

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        self.clear_table()

        ind = True

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                GetNumberOfDefectiveFormula = """SELECT number_of_defective
                                                     FROM accounting_for_defective_products
                                                     JOIN plan_db as pdb
                                                         USING(id_Plan_DB)
                                                     JOIN shoes_variant as sv
                                                          USING(id_shoes_variant)
                                                     WHERE sv.fashion = %s and sv.size = %s
                                                       and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                    """
                self.db.mycursor.execute(GetNumberOfDefectiveFormula, (fashions[i], sizes[j], month, year))
                result = self.db.mycursor.fetchone()
                if result:
                    ind = False
                    self.tab2_table[i][j].insert(0, result[0])

        if ind:
            messagebox.showinfo("", "Дані відсутні!")

    def tab2_put_data(self):
        if not self.tab2_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None
        if not self.tab2_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        month = months.index(self.tab2_com_month.get()) + 1
        year = self.tab2_com_year.get()

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                if self.tab2_table[i][j].get():

                    try:
                        value = int(self.tab2_table[i][j].get())
                    except ValueError:
                        messagebox.showerror("Помилка!", "В коміркках маєть бути цілі числа!")
                        return None
                    if value > 9999:
                        messagebox.showerror("Помилка!", "Максимальна кількьсть 9999!")
                        return None

                    if value < 0:
                        messagebox.showerror("Помилка!", "Мінімальна кількість 0!")
                        return None

                    GetNumberFormula = """SELECT number
                                          FROM plan_db
                                          JOIN shoes_variant as sv
                                              USING(id_shoes_variant)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(data) = %s and YEAR(data) = %s
                                          """
                    self.db.mycursor.execute(GetNumberFormula, (fashions[i], sizes[j], month, year))
                    result = self.db.mycursor.fetchone()

                    if result:
                        if value > result[0]:
                            messagebox.showerror("Помилка!",
                                                 "Бракованих виробів не може бути більше, ніж загальна кількість виробів!")
                            return None
                    else:
                        messagebox.showerror("Помилка!", "Ви намагаєтесь ввести брак для невиготовленої продукції!")
                        return None

                    GetNumberOfDevective = """SELECT number_of_defective
                                          FROM accounting_for_defective_products
                                          JOIN plan_db as pdb
                                              USING(id_Plan_DB)
                                          JOIN shoes_variant as sv
                                               USING(id_shoes_variant)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                                        """

                    self.db.mycursor.execute(GetNumberOfDevective, (fashions[i], sizes[j], month, year))
                    result = self.db.mycursor.fetchone()

                    if result:

                        UpdateNumberOfDevective = """UPDATE accounting_for_defective_products
                                                     JOIN plan_db as pdb
                                                         USING(id_Plan_DB)
                                                     JOIN shoes_variant as sv
                                                         USING(id_shoes_variant)
                                                     SET number_of_defective = %s
                                                     WHERE sv.fashion = %s and sv.size = %s
                                                       and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                                                     """

                        self.db.mycursor.execute(UpdateNumberOfDevective, (value, fashions[i], sizes[j], month, year))
                        self.db.mydb.commit()

                    else:

                        GetIdFormula = """SELECT id_Plan_DB
                                          FROM plan_db
                                          JOIN shoes_variant sv
                                            USING (id_shoes_variant)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(data) = %s and YEAR(data) = %s
                                          """

                        self.db.mycursor.execute(GetIdFormula, (fashions[i], sizes[j], month, year))

                        id_Plan_DB = self.db.mycursor.fetchone()[0]

                        InsertDefective = """INSERT INTO accounting_for_defective_products
                                             VALUES(DEFAULT, %s, 1, %s)"""

                        self.db.mycursor.execute(InsertDefective, (value, id_Plan_DB))
                        self.db.mydb.commit()

    def tab3_get_report(self):
        if not self.tab3_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None
        if not self.tab3_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        month = months.index(self.tab3_com_month.get()) + 1
        year = self.tab3_com_year.get()

        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        self.clear_table()

        ind = True

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                GetNumberFormula = """SELECT number
                                      FROM plan_db
                                      JOIN shoes_variant as sv
                                          USING(id_shoes_variant)
                                      WHERE sv.fashion = %s and sv.size = %s
                                        and MONTH(data) = %s and YEAR(data) = %s
                                                          """
                self.db.mycursor.execute(GetNumberFormula, (fashions[i], sizes[j], month, year))
                number = self.db.mycursor.fetchone()

                GetNumberOfDefectiveFormula = """SELECT number_of_defective
                                                FROM accounting_for_defective_products
                                                JOIN plan_db as pdb
                                                    USING(id_Plan_DB)
                                                JOIN shoes_variant as sv
                                                     USING(id_shoes_variant)
                                                WHERE sv.fashion = %s and sv.size = %s
                                                  and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                            """
                self.db.mycursor.execute(GetNumberOfDefectiveFormula, (fashions[i], sizes[j], month, year))
                number_def = self.db.mycursor.fetchone()

                if number and number_def:
                    ind = False
                    stat = f"{number[0]}/{number_def[0]} Брак: {round(number_def[0] / number[0] * 100, 1)}%"
                    self.tab3_table[i][j].config(text=stat)
                else:
                    self.tab3_table[i][j].config(text="----------")

        if ind:
            messagebox.showinfo("", "Дані відсутні!")

    def tab4_add_fashion(self):
        fashion = self.tab4_entry_fashion_add.get()

        if not fashion:
            return None

        if len(fashion) > 10:
            tk.messagebox.showinfo("", "Назва фасону задовга!")
            return None

        fashions = self.db.get_fashions()
        if fashion in fashions:
            tk.messagebox.showinfo("", "Цей фасон вже існує!")
            return None

        AddFashion = """INSERT INTO shoes_variant
                        VALUES (DEFAULT, %s, %s)
                        """
        for i in range(35, 46):
            self.db.mycursor.execute(AddFashion, (fashion, i))

        self.db.mydb.commit()

        self.refresh()

    def tab4_delete_fashion(self):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
