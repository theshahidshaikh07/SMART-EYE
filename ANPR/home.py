import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
import os

root = tk.Tk()
root.geometry("1200x600")
root.resizable(False, False)
root.title("SMART EYE")

# Load the background image and create a tkinter-compatible image object
bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label and add it to the root window to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=200, y=0, relwidth=1, relheight=1)

# Load the logo image and create a tkinter-compatible image object
logo_image = Image.open("l.jpg")
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label and add it to the root window to display the logo image
logo_label = tk.Label(root, image=logo_photo)
logo_label.place(x=290, y=140)

def open_count():
    subprocess.Popen(['python', 'count_excel.py'])

def open_speed():
    subprocess.Popen(['python', 'SpeedRadar2.py'])

def open_category():
    subprocess.Popen(['python', 'category.py'])

def open_number_plate():
    subprocess.Popen(['python', 'number_excel.py'])

def open_records():
    subprocess.Popen(['explorer', 'C:\ANPR Dataset'])


def open_LogOut():
    subprocess.Popen(['python', 'loginpage.py'])
    root.destroy()  #root.destroy()  #

label = ttk.Label(root, text="SMART EYE", font=("Verdana", 32, "bold"))
label.pack()
label.place(x=280, y=50)

button_frame = tk.Frame(root, bg="#f5f5f5", width=150)
button_frame.pack(fill="y", side="left")

btn1 = tk.Button(button_frame, text="Count", command=open_count , font=("Arial", 18, "bold"), bg="Black", fg="white", relief="raised", width=12, height=2)
btn1.pack(padx=15, pady=10)

btn2 = tk.Button(button_frame, text="Speed", command=open_speed ,font=("Arial", 18, "bold"), bg="Black", fg="White", relief="raised", width=12, height=2)
btn2.pack(padx=15, pady=10)

btn3 = tk.Button(button_frame, text="Category",  command=open_category ,font=("Arial", 18, "bold"), bg="Black", fg="White", relief="raised", width=12, height=2)
btn3.pack(padx=15, pady=10)

btn4 = tk.Button(button_frame, text="Number Plate",  command=open_number_plate ,font=("Arial", 18, "bold"), bg="Black", fg="white", relief="raised", width=12, height=2)

btn4.pack(padx=15, pady=10)

btn5 = tk.Button(button_frame, text="Records", command= open_records, font=("Arial", 18, "bold"), bg="Black", fg="White", relief="raised", width=12, height=2)
btn5.pack(padx=15, pady=10)

btn6 = tk.Button(button_frame, text="Log Out", command=open_LogOut ,font=("Arial", 18, "bold"), bg="Black", fg="White", relief="raised", width=12, height=2)
btn6.pack(padx=15, pady=10)

root.mainloop()
