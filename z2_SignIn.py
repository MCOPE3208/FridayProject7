import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Sign In")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

root.mainloop()
