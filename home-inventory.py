# package imports
from tkinter import *
from tkinter import messagebox
import openpyxl

#excel configuration variables
invName = 'HomeInvExcel_RevT.xlsx'
priSheet = 'Main'
addSheetDis = True

# Tkinter Initialization
root = Tk()
root.title('Inventory System')
root.geometry('800x600')

# adding menu bar in root windows
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
# create a menubar
menubar = Menu(root)
root.config(menu = menubar)

# create the file_menu
file_menu = Menu(menubar, tearoff = 0)

# add menu items to the File menu
file_menu.add_command(label = 'New')
file_menu.add_command(label = 'Open...')
file_menu.add_command(label = 'Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff = 0)

file_menu.add_cascade(label = "Preferences", menu = sub_menu)

# add Exit menu item
file_menu.add_separator()
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

# create the Help menu
help_menu = Menu(menubar, tearoff = 0)

help_menu.add_command(label = 'Welcome')
help_menu.add_command(label = 'About...')

# add the Help menu to the menubar
menubar.add_cascade(label = "Help", menu = help_menu, underline = 0)

# ID
lbl1 = Label(root, text = "ID", justify = LEFT)
lbl1.grid(row = 0)

# lbl1_1 = Label(root, text = "Automatically Assigned", justify = LEFT)
# lbl1_1.grid(column = 1, row = 0)
txt1 = Entry(root, width = 50)
txt1.grid(column = 1, row = 0)

# Class
lbl2 = Label(root, text = "Class", justify = LEFT)
lbl2.grid(row = 1)

txt2 = Entry(root, width = 50)
txt2.grid(column = 1, row = 1)
 
# Item
lbl3 = Label(root, text = "Item", justify = LEFT)
lbl3.grid(row = 2)

txt3 = Entry(root, width = 50)
txt3.grid(column = 1, row = 2)
 
# Manufacturer
lbl4 = Label(root, text = "Manufacturer", justify = LEFT)
lbl4.grid(row = 3)

txt4 = Entry(root, width = 50)
txt4.grid(column = 1, row = 3)

# Part Number
lbl5 = Label(root, text = "Part Number", justify = LEFT)
lbl5.grid(row = 4)

txt5 = Entry(root, width = 50)
txt5.grid(column = 1, row = 4)

# Serial Number
lbl6 = Label(root, text = "Serial Number", justify = LEFT)
lbl6.grid(row = 5)

txt6 = Entry(root, width = 50)
txt6.grid(column = 1, row = 5)

# Date Acquired
lbl7 = Label(root, text = "Date Acquired", justify = LEFT)
lbl7.grid(row = 6)

txt7 = Entry(root, width = 50)
txt7.grid(column = 1, row = 6)

# Description
lbl8 = Label(root, text = "Description", justify = LEFT)
lbl8.grid(row = 7)

txt8 = Entry(root, width = 50)
txt8.grid(column = 1, row = 7)

# Status
lbl9 = Label(root, text = "Status", justify = LEFT)
lbl9.grid(row = 8)

txt9 = Entry(root, width = 50)
txt9.grid(column = 1, row = 8)

# Location
lbl10 = Label(root, text = "Location", justify = LEFT)
lbl10.grid(row = 9)

txt10 = Entry(root, width = 50)
txt10.grid(column = 1, row = 9)

# Included In
lbl11 = Label(root, text = "Included In", justify = LEFT)
lbl11.grid(row = 10)

txt11 = Entry(root, width = 50)
txt11.grid(column = 1, row = 10)

# Data Entered
lbl12 = Label(root, text = "", justify = LEFT)
lbl12.grid(column = 1, row = 11)

def write_data(rowData):
    # initialize excel sheet
    wb1 = openpyxl.load_workbook(invName)
    
    # get next row ID
    nextID = wb1[priSheet].max_row

    # check if assembly sheet is required
    assembly = rowData[10] #input ('Enter the Included Assembly: \n')

    if(assembly != 'N/A' and (not addSheetDis)):
        wb1.create_sheet(assembly)
        print('New assembly created\n')

    # accept general row information
    rowData[0]  = nextID
    
    # add main data to primary sheet
    wb1.active = wb1[priSheet]
    if(nextID > int(rowData[0])):
        print('write to correct row')
    else:
        print('write to new row')
    
    wb1.active.append(rowData)

    # save sheet
    wb1.save(invName)

# function to display user text when
# button is clicked
def enter_data():
    lbl12.configure(text = 'Item added')

    write_data(get_data())
    
    clear_data()
   
def exit_app():
    root.destroy()

def clear_data():
    lbl12.configure(text = 'Data Cleared')
    
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    txt9.delete(0,END)
    txt10.delete(0,END)
    txt11.delete(0,END)

def read_data():
    # initialize excel sheet
    wb1 = openpyxl.load_workbook(invName, read_only = True)
    ws1 = wb1['Main']

    rowID = int(read_txt.get()) + 1
    # read line counter
    count = 0

    # call read row
    for row in ws1.iter_rows(min_row = rowID, max_col = 11, max_row = rowID, values_only = True):
        count = count + 1
    
    # close sheet
    wb1.close()

    # clear text boxes
    clear_data()

    # populate the text boxes
    insert_data(row)

def insert_data(rowData):
    txt1.insert(END, rowData[0])
    txt2.insert(END, rowData[1])
    txt3.insert(END, rowData[2])
    txt4.insert(END, rowData[3])
    txt5.insert(END, rowData[4])
    txt6.insert(END, rowData[5])
    txt7.insert(END, rowData[6])
    txt8.insert(END, rowData[7])
    txt9.insert(END, rowData[8])
    txt10.insert(END, rowData[9])
    txt11.insert(END, rowData[10])

    lbl12.configure(text = 'Data Updated')

def get_data():
    rowID       = txt1.get()
    rowClass    = txt2.get()
    rowItem     = txt3.get()
    rowManu     = txt4.get()
    rowPN       = txt5.get()
    rowSN       = txt6.get()
    rowDate     = txt7.get()
    rowDesc     = txt8.get()
    rowStatus   = txt9.get()
    rowLoc      = txt10.get()
    rowAssm     = txt11.get()

    rowData = [rowID, rowClass, rowItem, rowManu, rowPN, rowSN, rowDate, rowDesc, rowStatus, rowLoc, rowAssm]
    return rowData

# Enter Data Button
enter_bttn = Button(root, text = "Enter", fg = "black", bg = "white", width = 10, command = enter_data)
enter_bttn.grid(column = 0, row = 11)

# Read Button
read_bttn = Button(root, text = "Read", fg = "black", bg = "white", width = 10, command = read_data)
read_bttn.grid(column = 0, row = 14)

# Read text box
read_txt = Entry(root, width = 50)
read_txt.grid(column = 1, row = 14)

# Clear Button
clear_bttn = Button(root, text = "Clear", fg = "black", bg = "white", width = 10, command = clear_data)
clear_bttn.grid(column = 0, row = 12)

# Exit Button
exit_bttn = Button(root, text = "Exit", fg = "black", bg = "white", width = 10, command = exit_app)
exit_bttn.grid(column = 0, row = 13)

# Execute Tkinter
root.mainloop()