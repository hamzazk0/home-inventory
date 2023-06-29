from tkinter import *
from openpyxl import *
import sqlite3

# Database and Excel file paths
db_name = "./home-inventory/development.db"
wb_name = "./home-inventory/export.xlsx"

# Connect to the database
db_con = sqlite3.connect(db_name)
db_cur = db_con.cursor()

# Initialize the Excel workbook
wb = Workbook()
ws = wb.active

def db_create():
    db_cur.execute("CREATE TABLE IF NOT EXISTS Main(ID, Class, Manufacturer, ModelNumber, SerialNumber, DateAcquired, Description, Status, Location, Assembly)")
    db_con.commit()

def db_add_test():
    value = generate_id()
    data1 = str(int(generate_id())-99)
    data = [value, data1, data1, data1, data1, data1, data1, data1, data1, data1]
    db_cur.execute("INSERT INTO Main VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    db_con.commit()

def db_write():
    db_cur.execute("INSERT INTO Main VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dataBuffer)
    db_con.commit()

def db_checkout():
    db_cur.execute("UPDATE Main SET Location = ?, Assembly = ? WHERE ID = ?", [dataBuffer[8], dataBuffer[9], dataBuffer[0]])
    db_con.commit()

def db_checkin():
    db_cur.execute("UPDATE Main SET Location = ?, Assembly = ? WHERE ID = ?", ['Storage', 'N/A', dataBuffer[0]])
    db_con.commit()

def db_modify():
    db_cur.execute("UPDATE Main SET Class = ?, Manufacturer = ?, ModelNumber = ?, SerialNumber = ?, DateAcquired = ?, Description = ?, Status = ?, Location = ?, Assembly = ? WHERE ID = ?", dataBuffer)
    db_con.commit()

def db_read(rowID):
    db_cur.execute("SELECT * FROM Main WHERE ID = ?", [str(rowID)])
    return db_cur.fetchone()

def db_read_table():
    db_cur.execute("SELECT * FROM Main")
    for db_row in db_cur.fetchall():
        print(db_row)

def db_delete(rowID):
    db_cur.execute("DELETE FROM Main WHERE ID = ?", [str(rowID)])
    db_con.commit()

def generate_id():
    db_cur.execute("SELECT ID FROM Main")
    id_array = [int(str(db_row[0])) for db_row in db_cur.fetchall()]
    if len(id_array) == 0:
        next_id = 100
    else:
        next_id = max(id_array) + 1
    return str(next_id)

def add_text(root):
    input_text = []
    dataBuffer = []
    for i in range(10):
        textbox = Entry(root, width=30, font=('Arial', 14))
        textbox.grid(row=i, column=1)
        input_text.append(textbox)
        dataBuffer.append('-1')
    return input_text, dataBuffer

def exit_app():
    root.destroy()
    db_con.close()
    wb.save(wb_name)

def insert_data(input_text, dataBuffer):
    for i in range(len(input_text)):
        input_text[i].insert(END, dataBuffer[i])
    status.configure(text='Data Loaded in')

def get_data(input_text, dataBuffer):
    for i in range(len(input_text)):
        dataBuffer[i] = input_text[i].get()
    status.configure(text='Data Loaded into buffer')

def clear_data(input_text):
    for i in range(len(input_text)):
        input_text[i].delete(0, END)
    index_txt.delete(0, END)
    status.configure(text='Data Cleared')

def write_data():
    get_data(input_text, dataBuffer)
    dataBuffer[0] = generate_id()
    db_write()
    clear_data(input_text)
    status.configure(text='Writing complete')

def read_data():
    read_id = index_txt.get()
    test = db_read(read_id)
    if test:
        for i in range(len(input_text)):
            dataBuffer[i] = test[i]
        clear_data(input_text)
        insert_data(input_text, dataBuffer)
        status.configure(text='Data read')
    else:
        status.configure(text='Invalid ID')

def delete_data():
    delete_id = index_txt.get()
    test = db_read(delete_id)
    if test:
        for i in range(len(input_text)):
            dataBuffer[i] = test[i]
        clear_data(input_text)
        insert_data(input_text, dataBuffer)
        db_delete(delete_id)
        status.configure(text='Data deleted')
    else:
        status.configure(text='Invalid ID')

def export_data():
    db_cur.execute("SELECT * FROM Main")
    for db_row in db_cur.fetchall():
        parsed = str(db_row).replace("'", "").replace("(", "").replace(")", "").split(',')
        ws.append(parsed)
    wb.save(wb_name)
    status.configure(text='Data exported')

def check_out():
    get_data(input_text, dataBuffer)
    db_checkout()
    clear_data(input_text)
    status.configure(text='Item checked out')

def check_in():
    get_data(input_text, dataBuffer)
    db_checkin()
    clear_data(input_text)
    status.configure(text='Item checked in')

def modify_data():
    get_data(input_text, dataBuffer)
    db_modify()
    clear_data(input_text)
    status.configure(text='Data modified')

# UI initialization
root = Tk()
root.title('Inventory System')

# Create database table if it doesn't exist
db_create()

# Add test data to the database
db_add_test()

# Read and display all data from the database
db_read_table()

# Initialize input text boxes
input_text, dataBuffer = add_text(root)

# Status Message
status = Label(root, text="", justify=LEFT)
status.grid(row=10, column=1)

# Index Text Box
index_txt = Entry(root, width=30, font=('Arial', 14))
index_txt.grid(column=1, row=11)

# Index Label
index_lbl = Label(root, text="Index", justify=LEFT)
index_lbl.grid(row=11, column=0)

# Button Functions
button_functions = [
    ('Enter', write_data),
    ('Clear', clear_data),
    ('Read', read_data),
    ('Delete', delete_data),
    ('Modify', modify_data),
    ('Check in', check_in),
    ('Check out', check_out),
    ('Export', export_data),
    ('Exit', exit_app)
]

# Buttons
for i, (text, command) in enumerate(button_functions):
    button = Button(root, text=text, fg='black', bg='white', width=10, command=command)
    button.grid(column=2, row=i)

root.mainloop()