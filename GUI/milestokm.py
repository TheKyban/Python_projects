from tkinter import *

def milestokm():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=str(km))
window = Tk()
window.title("Mile to Km Converter")

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="calculate",command=milestokm)
calculate_button.grid(column=1 , row=2)

window.mainloop()