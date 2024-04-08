import tkinter as tk
import sqlite3

# Function to connect to SQLite Database
def connect_to_sqlite():
    try:
        conn = sqlite3.connect('database.db')  # Create or connect to a SQLite database file
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite Database: {e}")
        return None

# Function to create a table in SQLite Database
def create_table():
    try:
        conn = connect_to_sqlite()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE Persons (
                    ID NIUMBERS PRIMARY KEY,
                    Name VARCHAR2(25),
                    Age NUMBER
                )''')
            conn.commit()
            conn.close()
            result_label.config(text="Table created successfully")
    except sqlite3.Error as e:
        result_label.config(text=f"Error creating table: {e}")

# Function to insert data into SQLite Database
def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    try:
        conn = connect_to_sqlite()
        if conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Persons (Name, Age) VALUES (?, ?)', (name, age))
            conn.commit()
            conn.close()
            result_label.config(text="Data inserted successfully")
    except sqlite3.Error as e:
        result_label.config(text=f"Error inserting data: {e}")

# Function to view data from SQLite Database
def view_data():
    try:
        conn = connect_to_sqlite()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Persons')
            rows = cursor.fetchall()
            conn.close()
            print("Data from SQLite Database:")
            result_label.config(text="Data from SQLite Database:")
            output_text = ""
            for row in rows:
                output_text += str(row) + "\n"
            output_label.config(text=output_text)
    except sqlite3.Error as e:
        result_label.config(text=f"Error viewing data: {e}")

# Function to update data in SQLite Database
def update_data():
    try:
        name = name_entry.get()
        new_age = age_entry.get()
        conn = connect_to_sqlite()
        if conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Persons SET Age=? WHERE Name=?', (new_age, name))
            conn.commit()
            conn.close()
            result_label.config(text="Data updated successfully")
    except sqlite3.Error as e:
        result_label.config(text=f"Error updating data: {e}")

# Function to delete data from SQLite Database
def delete_data():
    try:
        name = name_entry.get()
        conn = connect_to_sqlite()
        if conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Persons WHERE Name=?', (name,))
            conn.commit()
            conn.close()
            result_label.config(text="Data deleted successfully")
    except sqlite3.Error as e:
        result_label.config(text=f"Error deleting data: {e}")

# GUI Setup
root = tk.Tk()
root.title("Database Application")

label1 = tk.Label(root, text="Name:")
label1.pack()
name_entry = tk.Entry(root)
name_entry.pack()

label2 = tk.Label(root, text="Age:")
label2.pack()
age_entry = tk.Entry(root)
age_entry.pack()

create_table_button = tk.Button(root, text="Create Table", command=create_table)
create_table_button.pack()

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

view_button = tk.Button(root, text="View Data", command=view_data)
view_button.pack()

update_button = tk.Button(root, text="Update Data", command=update_data)
update_button.pack()

delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
