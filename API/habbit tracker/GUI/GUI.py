from tkinter import *
from PIL import Image, ImageTk


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Habit Tracker")
        # self.window.geometry("500x500")

        self.canvas = Canvas(width=200, height=100)
        self.img = Image.open("logo.png")
        self.resized_image = self.img.resize((200, 100), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(100, 50, image=self.new_image)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # label
        self.username_label = Label(text="username:", font=("Ariel", 15))
        self.username_label.grid(row=1, column=0)

        # Entry
        self.username_entry = Entry(width=30)
        self.username_entry.grid(row=1, column=1)
        self.window.mainloop()


gui = Gui()
