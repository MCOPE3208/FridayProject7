import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Execute a SELECT query to retrieve user information
c.execute('SELECT * FROM users')

# Fetch all rows (users) from the query result
users = c.fetchall()

# Print or process the retrieved user information
for user in users:
    print(user)  # Or process each user data as needed

# Close the database connection
conn.close()
