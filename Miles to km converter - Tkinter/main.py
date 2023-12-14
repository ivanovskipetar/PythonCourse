from tkinter import *
def calculate():
    miles = miles_input.get()
    km = round(float(miles) * 1.6, 2)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
