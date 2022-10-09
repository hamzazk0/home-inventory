# import ui package
import imp
from tkinter import *

#import excel package
from openpyxl import *

# import database package
import sqlite3

db_name = "./home-inventory/development.db"
wb_name = "./home-inventory/export.xlsx"

# connect to database with name
db_con = sqlite3.connect(db_name)

# create cursor for database
db_cur = db_con.cursor()

# create initial response
db_res = db_cur.execute("SELECT name FROM sqlite_master")
db_res.fetchone()

# initialize excel sheet
wb1 = Workbook()
ws1 = wb1.active

def db_create():
    # execute command
    # create new main table
    db_cur.execute("CREATE TABLE Main(ID, Class, Manufacturer,\
                                      Model Number, Serial Number,\
                                      Date Acquired, Description, Status, \
                                      Location, Assembly)")

def db_add_test():
    value = generate_id()
    data1 = str(int(generate_id())-99)
    data = [value, data1, data1, data1, data1,\
            data1, data1, data1, data1, data1]
    db_cur.execute("INSERT INTO Main VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    db_con.commit()

def db_write():
    db_cur.execute("INSERT INTO Main VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dataBuffer)
    db_con.commit()

def db_read(rowID):
    for db_row in db_cur.execute("SELECT * FROM Main WHERE ID = '" + str(rowID) + "'"):
        return(db_row)

def db_read_table():
    for db_row in db_cur.execute("SELECT * FROM Main"):
        print(db_row)

def db_delete(rowID):
    db_cur.execute("DELETE FROM Main WHERE ID = '" + str(rowID) + "'")
    db_con.commit()

def generate_id():
    id_array = []
    for db_row in db_cur.execute("SELECT ID FROM Main"):
        id_array.append(int(str(db_row).replace("'","").replace("(","").replace(")","").replace(',',"")))

    if(len(id_array) == 0):
        next_id = 100
    else:
        next_id = max(id_array) + 1
    return(str(next_id))

# ui initalization
root = Tk()
root.title('Inventory System')

# adding menu bar in root windows
menubar = Menu(root)
root.config(menu = menubar)

# create the file_menu
file_menu = Menu(menubar, tearoff = 0)

# add menu items to the File menu
file_menu.add_command(label = 'New')
file_menu.add_command(label = 'Open...')
file_menu.add_command(label = 'Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(label = 'Exit', command = root.destroy)

menubar.add_cascade(label = "File", menu = file_menu, underline = 0)

# create the Item menu
item_menu = Menu(menubar, tearoff = 0)

item_menu.add_command(label = 'Add')
item_menu.add_command(label = 'Remove')
item_menu.add_command(label = 'Edit')
item_menu.add_command(label = 'Read')

# add item menu to the menubar
menubar.add_cascade(label = "Item", menu = item_menu, underline = 0)

# data structures
input_text = []
dataBuffer = []

# Function to initialize 11 UI text boxes
def add_text():
    for i in range(10):
        textbox = Entry(root, width = 50)
        textbox.grid(row = i, column = 1)
        input_text.append(textbox)
        dataBuffer.append('-1')

# initalize text boxes
add_text()

# Immediately close the program
def exit_app():
    # close ui
    root.destroy()
    # database close
    db_con.close()
    # save excel sheet
    wb1.save(wb_name)

# Put data from data buffer into text boxes
def insert_data():
    # loop populate textboxes
    for i in range(len(input_text)):
        input_text[i].insert(END, dataBuffer[i])

    status.configure(text = 'Data Loaded in')

# Put data from text boxes into data buffer
def get_data():
    # loop retrieve input text
    for i in range(len(input_text)):
        dataBuffer[i] = input_text[i].get()

    status.configure(text = 'Data Loaded into buffer')

# clear text boxes        
def clear_data():
    # update status message
    for i in range(len(input_text)):
        input_text[i].delete(0,END)

    status.configure(text = 'Data Cleared')

def write_data():
    # load buffer
    get_data()

    # generate next ID
    dataBuffer[0] = generate_id()
    
    # write buffer to database
    db_write()

    # clear data
    clear_data()

    # update status
    status.configure(text = 'Writing complete')

def read_data():
    # check read id
    read_id = read_txt.get()

    # query database
    test = db_read(read_id)
    
    # copy query into data buffer
    for i in range(len(input_text)):
        dataBuffer[i] = test[i]

    # display data from buffer
    clear_data()
    insert_data()
    
    # set status
    status.configure(text = 'Data read')

def delete_data():
    # check delete id
    delete_id = delete_txt.get()

    # query database
    test = db_read(delete_id)
    
    # copy query into data buffer
    for i in range(len(input_text)):
        dataBuffer[i] = test[i]

    # display data from buffer
    clear_data()
    insert_data()

    # query database
    db_delete(delete_id)
    
    # set status
    status.configure(text = 'Data deleted')

def export_data():
    for db_row in db_cur.execute("SELECT * FROM Main"):
        parsed = str(db_row).replace("'","").replace("(","").replace(")","").split(',')
        ws1.append(parsed)

# ID
lbl1 = Label(root, text = "ID", justify = LEFT)
lbl1.grid(row = 0, column = 0)

# Class
lbl2 = Label(root, text = "Class", justify = LEFT)
lbl2.grid(row = 1, column = 0)
 
# Manufacturer
lbl4 = Label(root, text = "Manufacturer", justify = LEFT)
lbl4.grid(row = 2, column = 0)

# Model Number
lbl5 = Label(root, text = "Part Number", justify = LEFT)
lbl5.grid(row = 3, column = 0)

# Serial Number
lbl6 = Label(root, text = "Serial Number", justify = LEFT)
lbl6.grid(row = 4, column = 0)

# Date Acquired
lbl7 = Label(root, text = "Date Acquired", justify = LEFT)
lbl7.grid(row = 5, column = 0)

# Description
lbl8 = Label(root, text = "Description", justify = LEFT)
lbl8.grid(row = 6, column = 0)

# Status
lbl9 = Label(root, text = "Status", justify = LEFT)
lbl9.grid(row = 7, column = 0)

# Location
lbl10 = Label(root, text = "Location", justify = LEFT)
lbl10.grid(row = 8, column = 0)

# Assembly
lbl11 = Label(root, text = "Assembly", justify = LEFT)
lbl11.grid(row = 9, column = 0)

# Status Message
status = Label(root, text = "", justify = LEFT)
status.grid(row = 10, column = 1)

# Enter Data Button
enter_bttn = Button(root, text = "Enter", fg = "black", bg = "white", width = 10, command = write_data)
enter_bttn.grid(column = 0, row = 10)

# Read Button
read_bttn = Button(root, text = "Read", fg = "black", bg = "white", width = 10, command = read_data)
read_bttn.grid(column = 0, row = 13)

# Read text box
read_txt = Entry(root, width = 50)
read_txt.grid(column = 1, row = 13)

# Delete Button
delete_bttn = Button(root, text = "Delete", fg = "black", bg = "white", width = 10, command = delete_data)
delete_bttn.grid(column = 0, row = 14)

# Delete text box
delete_txt = Entry(root, width = 50)
delete_txt.grid(column = 1, row = 14)

# Clear Button
clear_bttn = Button(root, text = "Clear", fg = "black", bg = "white", width = 10, command = clear_data)
clear_bttn.grid(column = 0, row = 11)

# Exit Button
exit_bttn = Button(root, text = "Exit", fg = "black", bg = "white", width = 10, command = exit_app)
exit_bttn.grid(column = 0, row = 12)

# Export Button
exit_bttn = Button(root, text = "Export", fg = "black", bg = "white", width = 10, command = export_data)
exit_bttn.grid(column = 0, row = 15)


# db_create()
# db_add_test()
db_read_table()

root.mainloop()