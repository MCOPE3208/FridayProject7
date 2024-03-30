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

password_label = ttk.Label(main_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")

password_entry = ttk.Entry(main_frame, show="*")  # Show asterisks for password
password_entry.grid(row=1, column=1, sticky="w")

login_button = ttk.Button(main_frame, text="Sign In", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

message_label = ttk.Label(main_frame, text="", foreground="red")
message_label.grid(row=3, column=0, columnspan=2)

signin_button = ttk.Button(root, text='Need an Account? Sign up here.', command=open_signup_window)
signin_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
