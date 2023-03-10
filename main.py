from tkinter import *


def button_clicked():
    try:
        result_km = 1.60934*float(input.get())
        l_kmval.config(text=result_km)
    except ValueError:
        l_kmval.config(text="Must be a number")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# LABEL
l_equal = Label(text="is equal to")
l_equal.config(padx=10, pady=10)

l_kmval = Label(text="0")
l_kmval.config(padx=10, pady=10)

l_km = Label(text="Km")
l_km.config(padx=10, pady=10)

l_miles = Label(text="Miles")
l_miles.config(padx=10, pady=10)


# BUTTON

btn_cal = Button(text="Calculate", command=button_clicked)
btn_cal.grid(column=1, row=1)

# ENTRY
input = Entry(width=10)
input.grid(column=3, row=3)
input.insert(END, string="0")


l_equal.grid(column=0, row=1)
l_kmval.grid(column=1, row=1)
l_km.grid(column=2, row=1)
l_miles.grid(column=2, row=0)
btn_cal.grid(column=1, row=2)
input.grid(column=1, row=0)

window.mainloop()