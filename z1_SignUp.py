import tkinter as tk
from tkinter import ttk
import sqlite3
root = tk.Tk()

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

root.mainloop()
