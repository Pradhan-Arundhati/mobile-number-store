#11(insert mobile number from user and insert that into text)
from tkinter import *
import tkinter as tk
from tkinter import Label
from tkinter import messagebox

window = Tk()
window.resizable(True, True)
window.geometry('520x500')
window.title("*****DETAILS*****")


Information = Label(window, text="ENTER YOUR DETAILS", background="lightyellow", font=("Arial Bold", 15)).place(x=150, y=5)
name = Label(window, text="Enter your Name", font=("Arial Bold", 10)).place(x=60, y=80)
entry1 = Entry(window, width=16)
entry1.place(x=250, y=80)
number = Label(window, text="Enter your Number", font=("Arial Bold", 10)).place(x=60, y=120)
entry2 = Entry(window, width=16)
entry2.place(x=250, y=120)
View = Label(window, text="View Your Information", background="lightyellow", font=("Arial Bold", 15)).place(x=150,y=260)
text1 = Text(window, height=10, width=62)
text1.place(x=10, y=300)


def inserting_details():
    write_name = str(entry1.get())
    write_number = str(entry2.get())
    if len(write_number) == 10:
        check = open('mobile.txt', 'a')
        check1 = open('mobile.txt', 'r')
        test = check1.read()
        if write_number in test:
            messagebox.showwarning("Duplicate", "Number already exists")
        else:
            check.write(f"{write_name} - \t{write_number}\n")
            messagebox.showinfo("Information", "Data added successfully")
    elif write_number == str(write_number):
        messagebox.showerror("Error", "Enter the correct details")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)


def checking_details():
    check = open('mobile.txt', 'r')
    rest = check.read()
    for a in rest[::-1]:
        text1.insert(0.0, a)


def clear_details():
    text1.delete(0.0, tk.END)


def exit_frame():
    window.destroy()


submit_bt = Button(window, text="Insert", command=inserting_details, height=3, width=9, font=("Arial Bold", 10)).place(x=40, y=180)
check_bt = Button(window, text="Check", command=checking_details, height=3, width=9, font=("Arial Bold", 10)).place(x=130, y=180)
clear_bt = Button(window, text="Clear", command=clear_details, height=3, width=9, font=("Arial Bold", 10)).place(x=220, y=180)
exit_button = Button(window, text="Exit", command=exit_frame, height=3, width=9, font=("Arial Bold", 10)).place(x=320, y=180)

window.mainloop()
