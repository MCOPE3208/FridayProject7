import tkinter as tk
from tkinter import ttk
import sqlite3
root = tk.Tk()

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)''')
conn.commit()
conn.close()

email_label = ttk.Label(root, text='Email:')
email_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
email_entry = ttk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = ttk.Label(root, text='Password:')
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
password_entry = ttk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=5)

confirm_password_label = ttk.Label(root, text='Confirm Password:')
confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
confirm_password_entry = ttk.Entry(root, show='*')
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

signup_button = ttk.Button(root, text='Sign Up', command=signup)
signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

error_label = ttk.Label(root, text='', foreground='red')
error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

signin_button = ttk.Button(root, text='Already have an account? Sign in here.', command=open_signin_window)
signin_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
