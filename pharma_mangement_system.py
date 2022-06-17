from email import message
from tkinter import *
from turtle import width
from PIL import ImageTk, Image
from time import strftime
from tkinter import ttk
from datetime import date
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import psycopg2


class PharamacyManagement(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Pharmacy Management System")

        container = Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # img = ImageTk.PhotoImage(Image.open(" pharam_img.jpg "))
        # label = Label(container, image=img)
        # label.place()

        self.frames = {}
        all_frame = (MainPage, Admin, NewUser, RegisteredUser, Admin_Panel)
        for F in all_frame:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.title = Label(
            self,
            text="Welcome Pharmacy Management System",
            font=("times new roman", 17, "bold"),
            width=105,
            relief=GROOVE,
        )
        self.title.pack(padx=10, pady=10)
        switch_window_button = Button(
            self,
            text="Admin",
            font=("sans serif", 24, "bold"),
            command=lambda: controller.show_frame(Admin),
        )
        switch_window_button.place(x=550, y=170, anchor="center")
        switch_window_button = Button(
            self,
            text="New User",
            font=("sans serif", 24, "bold"),
            command=lambda: controller.show_frame(NewUser),
        )
        switch_window_button.place(x=550, y=240, anchor="center")
        switch_window_button = Button(
            self,
            text="Registered User",
            font=("sans serif", 24, "bold"),
            command=lambda: controller.show_frame(RegisteredUser),
        )
        switch_window_button.place(x=550, y=320, anchor="center")


# Admin
class Admin(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.title = Label(
            self,
            text="Admin Login",
            font=("times new roman", 20, "bold"),
            width=105,
            relief=GROOVE,
        )
        self.title.pack(padx=10, pady=10)
        switch_window_button = Button(
            self,
            text="Main Page",
            font=("times new roman", 18, "bold"),
            relief=RIDGE,
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.place(x=450, y=260)

        self.Admin_login()

    def Admin_login(self):
        self.admin_user_name = Label(
            self, text="Username : ", font=("times new roman", 18, "bold")
        )
        self.admin_user_name.place(x=250, y=120)

        self.admin_user_name_text = Entry(
            self, font=("times new roman", 18, "bold"), width=35
        )
        self.admin_user_name_text.place(x=430, y=120)

        self.admin_password = Label(
            self, text="Password : ", font=("times new roman", 18, "bold")
        )
        self.admin_password.place(x=250, y=190)

        self.admin_password_text = Entry(
            self, font=("times new roman", 18, "bold"), width=35, show="*"
        )
        self.admin_password_text.place(x=430, y=190)

        self.admin_login_button = Button(
            self,
            text="Login",
            font=("times new roman", 18, "bold"),
            relief=RIDGE,
            command=lambda: self.login_func(),
        )
        self.admin_login_button.place(x=350, y=260)

    def login_func(self):
        self._adminUserName = "Aditya"
        self._adminPassword = "Aditya@2001"

        self.adminName = self.admin_user_name_text.get()
        self.adminPassword = self.admin_password_text.get()

        if (self._adminUserName == self.adminName) and (
            self._adminPassword == self.adminPassword
        ):
            messagebox.showinfo("Admin", "Login Successfully")
            self.controller.show_frame(Admin_Panel)

        else:
            messagebox.showerror("Error", "Unable To Login")


class Admin_Panel(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        self.admin_title = Label(
            self,
            text="Admin Panel",
            font=("times new roman", 19, "bold"),
            width=105,
            relief=GROOVE,
        )
        self.admin_title.pack(padx=10, pady=10)
        self.Medicine_Frame()
        self.Medicine_Details_Frame()

    def Medicine_Frame(self):
        self.med_id_var = StringVar()
        self.med_name_var = StringVar()
        self.med_price_var = StringVar()
        self.exp_var = StringVar()
        self.desc_var = StringVar()
        self.medicine_frame = Frame(
            self, height=530, width=460, bg="skyblue", relief=GROOVE, bd=3
        )
        self.medicine_frame.place(x=20, y=60)

        self.add_medicine = Label(
            self.medicine_frame,
            text="Add Medicine",
            font=("times new roman", 19, "bold"),
            bg="pale turquoise",
            relief=GROOVE,
            bd=3,
        )
        self.add_medicine.place(x=100, y=3)
        # Medicine Name Label and Entry
        Label(
            self.medicine_frame,
            text="Id",
            font=("times new roman", 15),
            bg="skyblue",
        ).place(x=10, y=50)
        self.id = Entry(
            self.medicine_frame,
            font=("times new roman", 12),
            width=30,
            textvariable=self.med_id_var,
        )
        self.id.place(x=170, y=50)
        Label(
            self.medicine_frame,
            text="Medicine Name",
            font=("times new roman", 15),
            bg="skyblue",
        ).place(x=10, y=90)
        self.medicine_name = Entry(
            self.medicine_frame,
            font=("times new roman", 12),
            width=30,
            textvariable=self.med_name_var,
        )
        self.medicine_name.place(x=170, y=90)

        # Expiry date Label and Calender
        todays_day = date.today()
        Label(
            self.medicine_frame,
            text="Expiry Date",
            font=("times new roman", 15),
            bg="skyblue",
        ).place(x=10, y=130)
        self.expiry_date = DateEntry(
            self.medicine_frame,
            selectmode="day",
            year=todays_day.year,
            month=todays_day.month,
            day=todays_day.day,
            font=("times new roman", 15),
            width=12,
            textvariable=self.exp_var,
        )
        self.expiry_date.place(x=170, y=130)

        Label(
            self.medicine_frame,
            text="Price : ",
            font=("times new roman", 15),
            bg="skyblue",
        ).place(x=10, y=170)
        self.price = Entry(
            self.medicine_frame,
            font=("times new roman", 12),
            width=30,
            textvariable=self.med_price_var,
        )
        self.price.place(x=170, y=170)

        Label(
            self.medicine_frame,
            text="Specification : ",
            font=("times new roman", 15),
            bg="skyblue",
        ).place(x=10, y=210)
        self.description = Text(
            self.medicine_frame, font=("times new roman", 12), width=30, height=4
        )
        self.description.place(x=170, y=210)

        # Buttons for Add Update Delete and View Costumers Order and Logout
        self.add_med = Button(
            self.medicine_frame,
            text="Add",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
            command=self.Add_medicine,
        )
        self.add_med.place(x=30, y=320)

        self.del_med = Button(
            self.medicine_frame,
            text="Delete",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
            command=self.delete_medicine,
        )
        self.del_med.place(x=170, y=320)

        self.update_med = Button(
            self.medicine_frame,
            text="Update",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
            command=self.update_medicine
        )
        self.update_med.place(x=320, y=320)

        self.vew_costumer_order = Button(
            self.medicine_frame,
            text="View Order",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
        )
        self.vew_costumer_order.place(x=30, y=390)

        self.logout = Button(
            self.medicine_frame,
            text="Logout",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
            command=self.logout,
        )
        self.logout.place(x=170, y=390)

        self.clear_btn = Button(
            self.medicine_frame,
            text="Clear",
            font=("times new roman", 18),
            relief=GROOVE,
            bg="skyblue",
            command=self.clear,
        )
        self.clear_btn.place(x=320, y=390)

    def Medicine_Details_Frame(self):
        self.medicine_detail_frame = Frame(
            self, height=530, width=740, bg="skyblue", relief=RIDGE, bd=2
        )
        self.medicine_detail_frame.place(x=490, y=60)
        # Search Frame
        self.search_label = Label(
            self.medicine_detail_frame, bg="skyblue", width=103, height=3, relief=GROOVE
        )
        self.search_label.place(x=3, y=2)

        self.searchby_label = Label(
            self.search_label,
            text="Search By.",
            bg="skyblue",
            font=("verdana", 13, "bold"),
        )
        self.searchby_label.place(x=3, y=2)

        self.combo_search = ttk.Combobox(
            self.search_label,
            width=13,
            font=("times new roman", 12, "bold"),
            state="readonly",
        )  # textvariable=searchby
        self.combo_search["values"] = ["Medicine Name", "Expiry Date"]
        self.combo_search.place(x=150, y=2)

        self.text_search = Entry(
            self.search_label, width=18, font=("times new roman", 12, "bold")
        )  # textvariable=search_txt
        self.text_search.place(x=330, y=2)

        self.search_button = Button(
            self.search_label, text="Search", font=("verdana", 13, "bold")
        )  # command=search_data
        self.search_button.place(x=500, y=2)

        self.showall_button = Button(
            self.search_label,
            text="Show All",
            font=("verdana", 13, "bold"),
            command=self.fetch_data,
        )  # command=fetch_data
        self.showall_button.place(x=600, y=2)

        # Medicine Detail Table Frame
        self.table_frame = Frame(
            self.medicine_detail_frame, bd=4, relief=RIDGE, bg="pale turquoise"
        )
        self.table_frame.place(x=3, y=70, width=720, height=450)

        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.medicine_table = ttk.Treeview(
            self.table_frame,
            columns=("Id", "Medicine Name", "Price", "Expiry Date", "Description"),
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set,
        )

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.medicine_table.xview)
        self.scroll_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Id", text="Id")
        self.medicine_table.heading("Medicine Name", text="Medicine Name")
        self.medicine_table.heading("Price", text="Price")
        self.medicine_table.heading("Expiry Date", text="Expiry Date")
        self.medicine_table.heading("Description", text="Description")
        self.medicine_table["show"] = "headings"
        self.medicine_table.column("Medicine Name", width="115")
        self.medicine_table.column("Price", width="115")
        self.medicine_table.column("Expiry Date", width="120")
        self.medicine_table.column("Description", width="115")

        self.medicine_table.pack(fill=BOTH, expand=1)
        self.medicine_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def Add_medicine(self):

        # print(type(self.med_id),type(self.med_name),type(self.med_price),type(self.exp_date),type(self.des))
        if (
            self.med_id_var.get() == ""
            and self.med_name_var.get() == ""
            and self.med_price_var.get() == ""
            and self.exp_var.get() == ""
            and self.description.get("1.0", END) == ""
        ):
            messagebox.showerror("OPMS", "All fields are required")
        else:
            # med_id = self.med_id_var.get()
            # med_name = self.med_name_var.get()
            # med_price = self.med_price_var.get()
            # exp_date = self.exp_var.get()
            # des = self.description.get("1.0", END)
            self.mydb = psycopg2.connect(
                database="opms",
                user="postgres",
                password="aditya@2001",
                host="localhost",
                port="5432",
            )
            self.mycursor = self.mydb.cursor()
            self.details = """INSERT INTO medicine_details(id,medicine_name, price, expiry_date, description) VALUES(%s,%s,%s,%s,%s)"""
            self.val = (
                self.med_id_var.get(),
                self.med_name_var.get(),
                self.med_price_var.get(),
                self.exp_var.get(),
                self.description.get("1.0", END),
            )
            self.mycursor.execute(self.details, self.val)
            # cur.execute('''INSERT INTO medicine_details(id VALUES (%s,%s, %s, %s, %s)''', (self.med_name, self.med_price, self.exp_date, self.des))
            # cur.execute(
            #     """insert into medicine_details(id, medicine_name, price, expiry_date, description) values('5', 'disprin1', 40, '6/14/2023', 'pain');"""
            # )
            self.mydb.commit()
            self.fetch_data()
            self.mydb.close()
            messagebox.showinfo("OPMS", "Data Inserted Successfully")

    # Function for clear all
    def clear(self):
        self.med_id_var.set("")
        self.med_name_var.set("")
        self.med_price_var.set("")
        self.exp_var.set("")
        self.description.set("1.0", END)

    def fetch_data(self):
        self.mydb = psycopg2.connect(
            database="opms",
            user="postgres",
            password="aditya@2001",
            host="localhost",
            port="5432",
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM medicine_details")
        self.rows = self.mycursor.fetchall()
        if len(self.rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for self.row in self.rows:
                self.medicine_table.insert("", END, values=self.row)
            self.mydb.commit()
        self.mydb.close()

    def get_cursor(self, eve):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.med_id_var.set(row[0])
        self.med_name_var.set(row[1])
        self.med_price_var.set(row[2])
        self.exp_var.set(row[3])
        self.description.delete("1.0", END)
        self.description.insert(END, row[4])

    def logout(self):
        Admin_Panel.quit
        messagebox.showinfo(
            "Admin Panel",
            "Logout from admin panel successfully\nYou are being redirected to Home Page",
        )
        self.controller.show_frame(MainPage)

    def clear(self):
        self.med_id_var.set("")
        self.med_name_var.set("")
        self.med_price_var.set("")
        self.exp_var.set("")
        self.description.delete("1.0", END)

    # Function for delete medicine
    def delete_medicine(self):
        self.mydb = psycopg2.connect(
            database="opms",
            user="postgres",
            password="aditya@2001",
            host="localhost",
            port="5432",
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            "DELETE FROM medicine_details WHERE medicine_details.id=%s",
            self.med_id_var.get(),
        )
        self.mydb.commit()
        self.mydb.close()
        self.fetch_data()
        self.clear()

    # function for update message
    def update_medicine(self):
        self.mydb = psycopg2.connect(
            database="opms",
            user="postgres",
            password="aditya@2001",
            host="localhost",
            port="5432",
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(
            "UPDATE medicine_details SET medicine_name=%s,price=%s,expiry_date=%s,description=%s WHERE id=%s",
            (
                self.med_name_var.get(),
                self.med_price_var.get(),
                self.exp_var.get(),
                self.description.get("1.0", END),
                self.med_id_var.get(),
            ),
        )
        self.mydb.commit()
        self.fetch_data()
        self.mydb.close()
        self.clear()
        messagebox.showinfo("Admin Panel","Medicine Update Successfully")


# End Of admin function


class NewUser(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.title = Label(
            self,
            text="New User",
            font=("times new roman", 17, "bold"),
            width=105,
            relief=GROOVE,
        )
        self.title.pack(padx=10, pady=10)
        switch_window_button = Button(
            self, text="Main Page", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=X)
        self.New_user()

    def New_user(self):
        registration = Label(
            self, text="New Registration", font=("sans serif", 18, "bold")
        )
        registration.place(anchor="center", x=550, y=100)
        self.user_name = Label(self, text="User Name")
        self.user_name.place(x=30, y=190)


class RegisteredUser(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.title = Label(
            self,
            text="Registered User",
            font=("times new roman", 17, "bold"),
            width=105,
            relief=GROOVE,
        )
        self.title.pack(padx=10, pady=10)
        switch_window_button = Button(
            self, text="Main Page", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=X)
        switch_window_button.pack(side="bottom", fill=X)


if __name__ == "__main__":
    pharamApp = PharamacyManagement()
    # root.title("Pharmacy Management System")
    pharamApp.geometry("1250x600+0+0")
    pharamApp.maxsize(1250, 600)
    pharamApp.minsize(1250, 600)
    pharamApp.mainloop()
