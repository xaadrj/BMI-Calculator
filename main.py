from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=400)
window.config(bg="orange")
window.config(pady=30)

weight_label = Label(text="Weight", fg="dark slate gray", bg="orange", font=(' Helvetica ', 30, "normal"))
weight_label.pack()

kg_label = Label(text="Kg", bg="orange", fg="dark slate gray", font=(' Helvetica ', 10, "normal"))
kg_label.config(pady=5)
kg_label.pack()


def calculate():
    feet = feet_spinbox.get()
    inches = inches_spinbox.get()
    weight = float(weight_entry.get())
    print(weight)
    height = float(f"{feet}.{inches}")
    print(height)
    height_in_meters = round(height / 3.281, 2)
    print(height_in_meters)
    bmi = round(weight / (height_in_meters * height_in_meters), 2)
    result.config(text=bmi)
    if bmi < 18.5:
        review.config(text="Underweight")
    elif 18.5 <= bmi <= 24.9:
        review.config(text="Normal Weight")
    elif 25.0 <= bmi <= 29.9:
        review.config(text="Overweight")
    else:
        review.config(text="Obese")


weight_entry = Entry(bd=0, justify="center", font=(' Helvetica ', 13, "bold"))
weight_entry.insert(END, string=5)
weight_entry.pack()

height_label = Label(text="Height", bg="orange", fg="dark slate gray", font=(' Helvetica ', 30, "normal"))
height_label.config(pady=10)
height_label.pack()

feet_label = Label(text="Feet", bg="orange", fg="dark slate gray",  font=(' Helvetica ', 10, "normal"))
feet_label.pack()

feet_spinbox = Spinbox(from_=4, to=200, width=25, justify="center", bd=0, command=calculate,
                       font=('Helvetica', 10, "bold"))
feet_spinbox.pack()

inches_label = Label(text="Inches", bg="orange", fg="dark slate gray",  font=(' Helvetica ', 10, "normal"))
inches_label.pack()

inches_spinbox = Spinbox(from_=0, to=200, justify="center", width=25, bd=0, command=calculate,
                         font=('Helvetica', 10, "bold"))
inches_spinbox.pack()

result = Label(text=0, bg="orange", fg="dark slate gray",  font=(' Helvetica ', 30, "normal"))
result.config(pady=20)
result.pack()

review = Label(text="", bg="orange", fg="red4", font=(' Helvetica ', 30, "bold"))

review.pack()

window.mainloop()
