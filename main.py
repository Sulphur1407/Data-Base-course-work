import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

months = ("січень", "лютий", "березень", "квітень", "травень", "червень",
          "липень", "серпень", "вересень", "жовтень", "листопад", "грудень")
years = (2020, 2021, 2022, 2023)


class DataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abunaraze",
            database="db_sol"
        )
        self.mycursor = self.mydb.cursor()
        self.delete_nulls()

    def get_sizes(self):
        self.mycursor.execute("SELECT DISTINCT size FROM Shoes_variant ORDER BY size")
        result = self.mycursor.fetchall()
        sizes = []

        if not result:
            return None

        for sequence in result:
            sizes.append(sequence[0])
        return sizes

    def get_fashions(self):
        self.mycursor.execute("SELECT DISTINCT fashion FROM Shoes_variant ORDER BY fashion")
        result = self.mycursor.fetchall()
        fashions = []

        if not result:
            return None

        for sequence in result:
            fashions.append(sequence[0])
        return fashions

    def get_type_defect(self):
        self.mycursor.execute("SELECT DISTINCT type_of_defect FROM type_of_defect")
        result = self.mycursor.fetchall()
        defects = []

        if not result:
            return None

        for sequence in result:
            defects.append(sequence[0])
        return defects

    def delete_nulls(self):
        self.mycursor.execute("DELETE FROM plan_db WHERE number = 0")
        self.mycursor.execute("DELETE FROM accounting_for_defective_products WHERE number_of_defective = 0")
        self.mydb.commit()


class MainApplication(tk.Frame):
    def __init__(self, *args, **kwargs):
        window = tk.Tk()
        tk.Frame.__init__(self, window, *args, **kwargs)

        self.db = DataBase()

        window.title("Курсова робота")
        window.geometry("1425x940")

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

        self.create_table1()

        #   TAB2
        ttk.Label(self.tab2, text="Дані про брак за:").place(x=20, y=20)

        self.tab2_com_month = ttk.Combobox(self.tab2, values=months)
        self.tab2_com_month.place(x=130, y=20)

        self.tab2_com_year = ttk.Combobox(self.tab2, values=years)
        self.tab2_com_year.place(x=290, y=20)

        defects = self.db.get_type_defect()

        ttk.Label(self.tab2, text="Тип браку:").place(x=450, y=20)

        self.tab2_com_defect = ttk.Combobox(self.tab2, values=defects)
        self.tab2_com_defect.place(x=530, y=20)

        self.tab2_get_data_button = ttk.Button(self.tab2, text="Отримати дані", command=self.tab2_get_data)
        self.tab2_get_data_button.place(x=690, y=18)

        self.tab2_put_data_button = ttk.Button(self.tab2, text="Завантажити дані", command=self.tab2_put_data)
        self.tab2_put_data_button.place(x=800, y=18)

        self.create_table2()

        #   TAB3
        ttk.Label(self.tab3, text="Дані про брак за:").place(x=20, y=20)

        self.tab3_com_month = ttk.Combobox(self.tab3, values=months)
        self.tab3_com_month.place(x=130, y=20)

        self.tab3_com_year = ttk.Combobox(self.tab3, values=years)
        self.tab3_com_year.place(x=290, y=20)

        self.tab3_get_data_button = ttk.Button(self.tab3, text="Отримати звіт", command=self.tab3_get_report)
        self.tab3_get_data_button.place(x=450, y=18)

        self.create_table3()

        #  TAB4
        self.create_frame4()

        window.mainloop()

    def refresh(self):
        self.db.delete_nulls()

        for child in self.tab1_table_frame.winfo_children():
            child.destroy()
        self.create_table1()

        for child in self.tab2_table_frame.winfo_children():
            child.destroy()
        self.create_table2()

        for child in self.tab3_table_frame.winfo_children():
            child.destroy()
        self.create_table3()

        for child in self.tab4.winfo_children():
            child.destroy()
        self.create_frame4()

    def clear_table(self):
        self.db.delete_nulls()
        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        for i in range(len(fashions)):
            for j in range(len(sizes)):
                self.tab1_table[i][j].delete(0, 100)
                self.tab2_table[i][j].delete(0, 100)
                self.tab3_table[i][j].config(text="")

    def max_defective(self, fashion, size, month, year):
        max_defect = 0
        for type_of_defect in self.db.get_type_defect():
            GetNumberOfDefectiveFormula = """SELECT number_of_defective
                                             FROM accounting_for_defective_products
                                             JOIN plan_db as pdb
                                                 USING(id_Plan_DB)
                                             JOIN shoes_variant as sv
                                                  USING(id_shoes_variant)
                                             JOIN type_of_defect tod
                                                USING(id_type_of_defect)
                                             WHERE sv.fashion = %s and sv.size = %s
                                               and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s 
                                               and tod.type_of_defect = %s
                                          """

            self.db.mycursor.execute(GetNumberOfDefectiveFormula, (fashion, size, month, year, type_of_defect))
            result = self.db.mycursor.fetchone()
            if result and result[0] > max_defect:
                max_defect = result[0]
        return max_defect

    def create_table1(self):
        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        #  Фрейм для таблиці
        self.tab1_table_frame = tk.Frame(self.tab1)
        self.tab1_table_frame.place(x=0, y=50)

        self.tab1_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(self.tab1_table_frame, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(self.tab1_table_frame, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(self.tab1_table_frame, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Entry(self.tab1_table_frame, relief=tk.RIDGE)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab1_table.append(cols)

    def create_table2(self):
        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        #  Фрейм для таблиці
        self.tab2_table_frame = tk.Frame(self.tab2)
        self.tab2_table_frame.place(x=0, y=50)

        self.tab2_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(self.tab2_table_frame, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(self.tab2_table_frame, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(self.tab2_table_frame, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Entry(self.tab2_table_frame, relief=tk.RIDGE)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab2_table.append(cols)

    def create_table3(self):
        sizes = self.db.get_sizes()
        fashions = self.db.get_fashions()

        #  Фрейм для таблиці
        self.tab3_table_frame = tk.Frame(self.tab3)
        self.tab3_table_frame.place(x=0, y=50)

        self.tab3_table = []
        for i in range(len(fashions) + 1):
            cols = []
            for j in range(len(sizes) + 1):
                if i == 0 and j == 0:
                    tk.Label(self.tab3_table_frame, text="Фасон").grid(row=i, column=j, sticky=tk.NSEW)
                elif i == 0:
                    tk.Label(self.tab3_table_frame, text=sizes[j - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                elif j == 0:
                    tk.Label(self.tab3_table_frame, text=fashions[i - 1]).grid(row=i, column=j, sticky=tk.NSEW)
                else:
                    e = tk.Label(self.tab3_table_frame, relief=tk.RIDGE, width=17, height=1)
                    e.grid(row=i, column=j, sticky=tk.NSEW)
                    cols.append(e)
            if i:
                self.tab3_table.append(cols)

    def create_frame4(self):
        fashions = self.db.get_fashions()


        ttk.Label(self.tab4, text="Додати фасон:").place(x=20, y=20)

        self.tab4_entry_fashion_add = tk.Entry(self.tab4, relief=tk.RIDGE, width=23)
        self.tab4_entry_fashion_add.place(x=140, y=20)

        self.tab4_button_fashion_add = ttk.Button(self.tab4, text="Додати фасон", command=self.tab4_add_fashion)
        self.tab4_button_fashion_add.place(x=290, y=18)


        ttk.Label(self.tab4, text="Видалити фасон:").place(x=20, y=60)

        self.tab4_com_fashion = ttk.Combobox(self.tab4, values=fashions)
        self.tab4_com_fashion.place(x=140, y=60)

        self.tab4_get_data_button = ttk.Button(self.tab4, text="Видалити фасон", command=self.tab4_delete_fashion)
        self.tab4_get_data_button.place(x=290, y=58)

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
                        if value < self.max_defective(fashions[i], sizes[j], month, year):
                            messagebox.showerror("Помилка!", "При редагуванні кількість виготовленого буде більша за "
                                                             "кількість виготовленого!")
                            return None
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
                                               WHERE fashion = %s and size = %s
                                            """

                        self.db.mycursor.execute(GetIdFormula, (fashions[i], sizes[j]))

                        id_shoes_variant = self.db.mycursor.fetchone()[0]

                        InsertNumber = """INSERT INTO plan_db
                                               VALUES(DEFAULT, %s, %s, %s)
                                            """

                        self.db.mycursor.execute(InsertNumber, (value, date, id_shoes_variant))
                        self.db.mydb.commit()

    #  TAB2 Buttons
    def tab2_get_data(self):
        if not self.tab2_com_month.get():
            messagebox.showerror("Помилка!", "Ви не вказали місяць!")
            return None

        if not self.tab2_com_year.get():
            messagebox.showerror("Помилка!", "Ви не вказали рік!")
            return None

        if not self.tab2_com_defect.get():
            messagebox.showerror("Помилка!", "Ви не вказали тип дефекту!")
            return None

        month = months.index(self.tab2_com_month.get()) + 1
        year = self.tab2_com_year.get()
        type_of_defect = self.tab2_com_defect.get()

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
                                                 JOIN type_of_defect tod
                                                    USING(id_type_of_defect)
                                                 WHERE sv.fashion = %s and sv.size = %s
                                                   and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s 
                                                   and tod.type_of_defect = %s
                                              """

                self.db.mycursor.execute(GetNumberOfDefectiveFormula, (fashions[i], sizes[j], month, year, type_of_defect))
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

        if not self.tab2_com_defect.get():
            messagebox.showerror("Помилка!", "Ви не вказали тип дефекту!")
            return None

        month = months.index(self.tab2_com_month.get()) + 1
        year = self.tab2_com_year.get()
        type_of_defect = self.tab2_com_defect.get()

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
                            messagebox.showerror("Помилка!", "Бракованих виробів не може бути більше, ніж загальна "
                                                             "кількість виробів!")
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
                                              JOIN type_of_defect tod
                                                    USING(id_type_of_defect)
                                              WHERE sv.fashion = %s and sv.size = %s
                                                and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                                                and tod.type_of_defect = %s
                                           """

                    self.db.mycursor.execute(GetNumberOfDevective, (fashions[i], sizes[j], month, year, type_of_defect))
                    result = self.db.mycursor.fetchone()

                    if result:

                        UpdateNumberOfDevective = """UPDATE accounting_for_defective_products
                                                     JOIN plan_db as pdb
                                                         USING(id_Plan_DB)
                                                     JOIN shoes_variant as sv
                                                         USING(id_shoes_variant)
                                                     JOIN type_of_defect tod
                                                         USING(id_type_of_defect)
                                                     SET number_of_defective = %s
                                                     WHERE sv.fashion = %s and sv.size = %s
                                                       and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                                                       and tod.type_of_defect = %s
                                                  """

                        self.db.mycursor.execute(UpdateNumberOfDevective, (value, fashions[i], sizes[j], month, year, type_of_defect))
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

                        GetIdOfDefect = """SELECT id_type_of_defect
                                           FROM type_of_defect
                                           WHERE type_of_defect = %s
                                        """
                        self.db.mycursor.execute(GetIdOfDefect, (type_of_defect,))

                        id_type_of_defect = self.db.mycursor.fetchone()[0]

                        InsertDefective = """INSERT INTO accounting_for_defective_products
                                             VALUES(DEFAULT, %s, %s, %s)"""

                        self.db.mycursor.execute(InsertDefective, (value, id_type_of_defect, id_Plan_DB))
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

                GetNumberOfDevective = """SELECT number_of_defective
                                          FROM accounting_for_defective_products
                                          JOIN plan_db as pdb
                                              USING(id_Plan_DB)
                                          JOIN shoes_variant as sv
                                               USING(id_shoes_variant)
                                          JOIN type_of_defect tod
                                                USING(id_type_of_defect)
                                          WHERE sv.fashion = %s and sv.size = %s
                                            and MONTH(pdb.data) = %s and YEAR(pdb.data) = %s
                                            and tod.type_of_defect = %s
                                            """
                number_def = []
                for type_of_defect in self.db.get_type_defect():
                    self.db.mycursor.execute(GetNumberOfDevective, (fashions[i], sizes[j], month, year, type_of_defect))
                    number_defected = self.db.mycursor.fetchone()
                    if number_defected:
                        number_def.append(number_defected)
                    else:
                        number_def.append("-")

                if number:
                    ind = False
                    stat = f"В: {number[0]} | Р:{number_def[0][0]} С:{number_def[1][0]} Т:{number_def[2][0]}"
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
        messagebox.showinfo("", f"Фасон {fashion} було успішно додано!")

        self.refresh()

    def tab4_delete_fashion(self):
        self.db.delete_nulls()

        if not self.tab4_com_fashion.get():
            messagebox.showerror("Помилка!", "Ви не вказали модель для видалення!")
            return None

        fashion = self.tab4_com_fashion.get()

        DeleteFashion = """DELETE FROM shoes_variant
                           where fashion = %s
        """

        try:
            self.db.mycursor.execute(DeleteFashion, (fashion,))
            self.db.mydb.commit()
            self.refresh()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Помилка!", "Неможливо видалити фасон, до якого є записи!")
            return None


if __name__ == "__main__":
    MainApplication().pack(side="top", fill="both", expand=True)
