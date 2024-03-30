import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Sign In")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=0, column=0, sticky="w")

email_entry = ttk.Entry(main_frame, width=30)
email_entry.grid(row=0, column=1, sticky="w")

root.mainloop()
