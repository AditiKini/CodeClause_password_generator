from tkinter import *
from tkinter import messagebox
import tkinter.font as tk_font
from random import choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR -------------------------------


# Password Generator Project
def generate_password():
    if letters_count.get() == "" or number_count.get() == "" or symbols_count.get() == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        password_input.delete(0, END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        pass_letters = [choice(letters) for _ in range(int(letters_count.get()))]
        pass_symbols = [choice(symbols) for _ in range(int(number_count.get()))]
        pass_numbers = [choice(numbers) for _ in range(int(symbols_count.get()))]
        password_list = pass_letters + pass_symbols + pass_numbers
        shuffle(password_list)
        if len(password_list) < 8:
            messagebox.showinfo(title="Oops", message="Please make sure that password must be minimum 8 characters.")
        else:
            password = "".join(password_list)
            password_input.insert(0, password)
            pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_input.get()
    password = password_input.get()

    if letters_count.get() == "" or number_count.get() == "" or symbols_count.get() == "" or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif email[-10:] != "@gmail.com":
        messagebox.showinfo(title="Oops", message="Invalid Email!")
    else:
        is_ok = messagebox.askokcancel(message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f" {email} | {password}\n")
                letters_count.delete(0, END)
                number_count.delete(0, END)
                email_input.delete(0, END)
                symbols_count.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- USER-INTERFACE ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
bold_font = tk_font.Font(weight="bold", size=8)
letters_count = Label(text="Letter count:", font=bold_font)
letters_count.grid(row=1, column=0, sticky="w")
number_count = Label(text="Number count:", font=bold_font)
number_count.grid(row=2, column=0, sticky="w")
symbols_count = Label(text="Symbol count:", font=bold_font)
symbols_count.grid(row=3, column=0, sticky="w")
email_label = Label(text="Email:", font=bold_font)
email_label.grid(row=4, column=0, sticky="w")
password_label = Label(text="Password:", font=bold_font)
password_label.grid(row=5, column=0, sticky="w")

# Entries
letters_count = Entry(width=20)
letters_count.grid(row=1, column=0, columnspan=2)
letters_count.focus()
number_count = Entry(width=20)
number_count.grid(row=2, column=0, columnspan=2)
number_count.focus()
symbols_count = Entry(width=20)
symbols_count.grid(row=3, column=0, columnspan=2)
symbols_count.focus()
email_input = Entry(width=20)
email_input.grid(row=4, column=0, columnspan=2)
email_input.insert(0, "")
password_input = Entry(width=30)
password_input.grid(row=5, column=1, sticky="w")

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=5, column=2, sticky="w")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=6, column=1, columnspan=2, sticky="w")

window.mainloop()
