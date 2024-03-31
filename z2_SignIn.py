import tkinter as tk
from tkinter import ttk
import sqlite3
import sys

# Prevent __pycache__ creation
sys.dont_write_bytecode = True

def login():
    email = email_entry.get()
    password = password_entry.get()
    
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Query the database for the entered email and password
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    if user:
        message_label.config(text="Log in successful", foreground="green")
    else:
        message_label.config(text="Email or password incorrect", foreground="red")
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def open_signup_window():
    root.withdraw()  # Hide the sign-up window
    import z1_SignUp  # Import and run the sign-in window
    z1_SignUp.run_signup_window()

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
