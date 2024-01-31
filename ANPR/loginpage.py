from tkinter import *
import subprocess
from PIL import ImageTk, Image

def authenticate():
    username = entry_username.get()
    password = entry_password.get()
    if username == "Admin" and password == "ANPR":
        label_result.config(text="Login successful. Opening homepage...", fg="green")
        # Open homepage.py
        subprocess.Popen(["python", "home.py"])
        root.destroy()

    else:
        label_result.config(text="Incorrect username or password. Please try again.", fg="red")

root = Tk()

root.title("Login Page")
root.geometry("900x600")
root.resizable(False, False)


# create a custom color scheme
bg_color = "#D3D3D3"
fg_color = "black"
btn_bg_color = "black"
btn_fg_color = "white"

# create a custom font
font_style = ("Times", 22, "bold italic")
button_font_style = ("Times", 18, "italic")
normal_font = ("Times", 14, "bold")

# create a label widget for the title
title_label = Label(root, text="SMART EYE", font=("Verdana", 34, "bold"), fg=fg_color, bg=bg_color)
title_label.pack(pady=10)


logo_image = Image.open("l.jpg")
logo_image = ImageTk.PhotoImage(logo_image)
image_label = Label(root, image=logo_image, bg=bg_color)
image_label.pack(pady=10)

title_label1 = Label(root, text="Login Page", font=("Times", 26, "bold"), fg=fg_color, bg=bg_color)
title_label1.pack(pady=10)



# create a frame widget for the input fields
input_frame = Frame(root, bg=bg_color)
input_frame.pack(pady=10)


# create label widgets for the input fields
username_label = Label(input_frame, text="Username:", font=font_style, fg=fg_color, bg=bg_color)
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

password_label = Label(input_frame, text="Password:", font=font_style, fg=fg_color, bg=bg_color)
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# create entry widgets for the input fields
entry_username = Entry(input_frame, font=font_style)
entry_username.grid(row=0, column=1, padx=10, pady=10)

entry_password = Entry(input_frame, font=font_style, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# create a frame widget for the buttons
button_frame = Frame(root, bg=bg_color)
button_frame.pack(pady=10)

# create button widgets for the login and quit buttons
login_button = Button(button_frame, text="Login", font=button_font_style, bg=btn_bg_color, fg=btn_fg_color, command=authenticate)
login_button.pack(side="left", padx=5)

quit_button = Button(button_frame, text="Quit", font=button_font_style, bg=btn_bg_color, fg=btn_fg_color, command=root.destroy)
quit_button.pack(side="right", padx=5)


# create a label widget for the result
label_result = Label(root, text="", font=normal_font, fg=fg_color, bg=bg_color)
label_result.pack(pady=10)

# set the background color of the root window
root.config(bg=bg_color)

# main loop
root.mainloop()
  
