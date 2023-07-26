import tkinter as tk
import random
import string
from tkinter.messagebox import *
from tkinter import messagebox

font = ('Times', '22', 'bold')


def generated_password():
    try:
        username = username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror(
                "Error", "Password length should be at least 6 characters")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        generated_password_entry.delete(0, tk.END)
        generated_password_entry.insert(0, password)
    except:
        messagebox.showerror("Error", "Please Enter Legth of the password")
        return


def accept_password():
    username = username_entry.get()
    password = generated_password_entry.get()
    if not password:
        messagebox.showerror("Error", "No password generated")
        return
    messagebox.showinfo("Success", "Password accepted!")


def reset_password():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Password Generator by Mayank Rajput")
window.config(bg="#f7a34f")
window.geometry('550x450')
window.resizable(0, 0)

heading = tk.Label(window, bg="#f7a34f", text="Password Generator By Mayank Rajput", font=font)
heading.place(y=25, x=25)


# Create labels and tepadxt fields
username_label = tk.Label(
    window, text="Enter user name :", font=('Helvetica', 14, 'bold'), bg="#f7a34f")
username_label.place(x=70, y=85)
username_entry = tk.Entry(window, font=(
    'arial', 14, 'bold'))
username_entry.place(x=250, y=90)

length_label = tk.Label(window, text="Enter Password length :",
                        font=('Helvetica', 14, 'bold'), bg="#f7a34f")
length_label.place(x=5, y=145)
length_entry = tk.Entry(window, font=(
    'arial', 14, 'bold'))
length_entry.place(x=250, y=145)

generated_password_label = tk.Label(window, text="Generated Password :",
                                    font=('Helvetica', 14, 'bold'), bg="#f7a34f")
generated_password_label.place(x=20, y=195)
generated_password_entry = tk.Entry(window, font=(
    'Helvetica', 14, 'bold'))
generated_password_entry.place(x=250, y=200)

# Create buttons
generate_button = tk.Button(window, text='Generated Password',
                            height=2, width=20,  relief='groove', command=generated_password, activebackground="orange", activeforeground="white", fg="Black", bg="#9ba3ba")
generate_button.place(x=180, y=250)

accept_button = tk.Button(window, text='Accept',
                          height=2, width=9,  relief='groove', command=accept_password, activebackground="green", activeforeground="white", fg="Black", bg="#ebe5df")

accept_button.place(x=210, y=300)

reset_button = tk.Button(window, text='Reset',
                         height=2, width=9,  relief='groove', activebackground="red", command=reset_password, activeforeground="white", fg="Black", bg="#ebe5df")
reset_button.place(x=210, y=350)

# Start the Tkinter event loop
window.mainloop()
