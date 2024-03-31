import tkinter as tk
from tkinter import ttk
import sqlite3
import sys

# Prevent __pycache__ creation
sys.dont_write_bytecode = True

def signup():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate email format
    if '@' not in email or '.' not in email:
        error_label.config(text='Invalid email address!', foreground='red')
        return

    # Check if passwords match
    if password != confirm_password:
        error_label.config(text='Passwords do not match!', foreground='red')
        return

    # Insert user into database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        conn.commit()
        error_label.config(text='Signup successful!', foreground='green')
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)
    except sqlite3.IntegrityError:
        error_label.config(text='Email already exists!', foreground='red')
    conn.close()

def open_signin_window():
    root.withdraw()  # Hide the sign-up window
    import z2_SignIn  # Import and run the sign-in window
    z2_SignIn.run_signin_window()

root = tk.Tk()
root.title('Sign Up')

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
