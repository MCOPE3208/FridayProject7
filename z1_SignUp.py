import tkinter as tk
from tkinter import ttk
import sqlite3
root = tk.Tk()

email_label = ttk.Label(root, text='Email:')
email_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
email_entry = ttk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()
