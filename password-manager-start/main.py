import json
from tkinter import *
from tkinter import messagebox
import random
from letters import letters


class PassManager:
    def __init__(self):

        self.company_get = None
        self.pass_text = None
        self.pass_string = None
        self.window = Tk()
        self.window.title("Password")
        self.window.config(padx=50, pady=10)

        self.canvas = Canvas(width=200, height=200)
        self.logo = PhotoImage(file="dir/logo.png")
        self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(row=0, column=0, columnspan=3)

        # Labels
        self.company_label = Label(text="Company :")
        self.company_label.grid(row=1, column=0)

        self.email_label = Label(text="Email :")
        self.email_label.grid(row=2, column=0)

        self.password_label = Label(text="Password :")
        self.password_label.grid(row=3, column=0)

        # Entry
        self.company_entry = Entry(width=20)
        self.company_entry.grid(row=1, column=1)

        self.email_entry = Entry(width=30)
        self.email_entry.grid(row=2, column=1, columnspan=2)

        self.password_entry = Entry(width=20)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        self.generate_button = Button(text="Generate", width=7, command=self.generate_pass)
        self.generate_button.grid(row=3, column=2)

        self.check_button = Button(text="Check", width=7, command=self.check)
        self.check_button.grid(row=1, column=2)

        self.submit_button = Button(text="Submit", width=7, command=self.submit_pass)
        self.submit_button.grid(row=4, column=1)

        self.window.mainloop()

    def generate_pass(self):
        self.password_entry.delete(0, END)
        self.pass_string = [random.choice(letters) for _ in range(18)]
        random.shuffle(self.pass_string)
        self.pass_text = ""
        for symbol in self.pass_string:
            self.pass_text += symbol
        self.password_entry.insert(1, self.pass_text)

    def submit_pass(self):
        company = self.company_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {
            company: {
                "email": email,
                "password": password
            }
        }

        if len(company) == 0 or len(email) == 0:
            messagebox.showinfo(title="oops", message="please fill all entry")
        else:
            messagebox.askokcancel(title=company,
                                   message=f"These are the details: \nEmail:{email}\nPassword:{password}")
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

            except json.JSONDecodeError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

            self.company_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.password_entry.delete(0, END)

    # check
    def check(self):
        self.company_get = self.company_entry.get()
        try:
            with open("data.json") as data:
                info = json.load(data)
                if self.company_get in info:
                    check_email = info[self.company_get]["email"]
                    check_pass = info[self.company_get]["password"]
                    messagebox.showinfo(title="Info", message=f"email:{check_email}\npassword:{check_pass}")
                else:
                    messagebox.showinfo(title="oops", message="There are no such account")

        except json.JSONDecodeError:
            messagebox.showinfo(title="oops", message="There are no such account")


password_manager = PassManager()
