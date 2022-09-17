from tkinter import *
from turtle import title

window = Tk()
window.title("Calculator")


def one_pressed():
    blank_space.insert(1, "1")


def two_pressed():
    blank_space.insert([-1], "2")


def three_pressed():
    blank_space.insert(1, "3")


# Entry
blank_space = Entry(width=37)
blank_space.grid(row=0, column=0, columnspan=4)

# buttons

button_1 = Button(text="1", font=(30), width=5, command=one_pressed)
button_1.grid(row=1, column=0)

button_2 = Button(text="2", font=(30), width=5, command=two_pressed)
button_2.grid(row=1, column=1)

button_3 = Button(text="3", font=(30), width=5, command=three_pressed)
button_3.grid(row=1, column=2)

button_4 = Button(text="4", font=(30), width=5)
button_4.grid(row=2, column=0)

button_5 = Button(text="5", font=(30), width=5)
button_5.grid(row=2, column=1)

button_6 = Button(text="6", font=(30), width=5)
button_6.grid(row=2, column=2)

button_7 = Button(text="7", font=(30), width=5)
button_7.grid(row=3, column=0)

button_8 = Button(text="8", font=(30), width=5)
button_8.grid(row=3, column=1)

button_9 = Button(text="9", font=(30), width=5)
button_9.grid(row=3, column=2)

button_0 = Button(text="0", font=(30), width=5)
button_0.grid(row=4, column=0)

button_point = Button(text=".", font=(30), width=5)
button_point.grid(row=4, column=1)

button_plus = Button(text="+", font=(30), width=5)
button_plus.grid(row=4, column=2)

button_minus = Button(text="-", font=(30), width=5)
button_minus.grid(row=3, column=3)

button_divide = Button(text="/", font=(30), width=5)
button_divide.grid(row=1, column=3)

button_multiply = Button(text="*", font=(30), width=5)
button_multiply.grid(row=2, column=3)

button_enter = Button(text="Enter", font=(15), width=5)
button_enter.grid(row=4, column=3)

window.mainloop()
