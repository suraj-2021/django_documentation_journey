# add_data.py
import sqlite3

# Connect to the database (creates a new one if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Execute an INSERT INTO command
cursor.execute("INSERT INTO my_table (column1, column2) VALUES (?, ?)", ('value1', 'value2'))

# Commit changes and close the connection
conn.commit()
conn.close()
