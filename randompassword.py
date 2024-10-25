import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied!", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=0, pady=5, padx=5)
length_entry.insert(0, "12")  

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=0, pady=5, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.grid(row=3, column=0, pady=5)

root.mainloop()
