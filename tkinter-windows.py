from tkinter import *

WINDOW_WIDTH = 250
WINDOW_HEIGHT = 320

def submit():
    # Function to handle the submit button click event
    print('pressed submit')

def open_item_window():
    # Function to open the second window
    item_window = Toplevel(window)
    item_window.title('Add Item')
    item_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Create labels and entry widgets in the second window
    for i in range(9):
        label_text = StringVar()
        label_text.set(label_texts[i])

        label = Label(item_window, textvariable=label_text, justify='left')
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = Entry(item_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry_list.append(entry)

    # Create the submit button in the second window
    submit_button = Button(item_window, text='Submit', command=submit)
    submit_button.grid(row=9, column=1, padx=10, pady=10)

    # Create the exit button for the window
    exit_button = Button(item_window, text='Exit', command=item_window.destroy)
    exit_button.grid(row=9, column=0, padx=10, pady=10)

def open_read_window():
    # Function to open the second window
    read_window = Toplevel(window)
    read_window.title('Read Item')
    read_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Create labels and entry widgets in the second window
    for i in range(9):
        label_text = StringVar()
        label_text.set(label_texts[i])

        label = Label(read_window, textvariable=label_text, justify='left')
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

        entry = Entry(read_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry_list.append(entry)

    # Create the submit button in the second window
    submit_button = Button(read_window, text='Submit', command=submit)
    submit_button.grid(row=9, column=1, padx=10, pady=10)

    # Create the exit button for the window
    exit_button = Button(read_window, text='Exit', command=read_window.destroy)
    exit_button.grid(row=9, column=0, padx=10, pady=10)

def open_getID_window():
    # Function to open the third window
    getID_window = Toplevel(window)
    getID_window.title('Get ID')
    getID_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Create the label for getting ID
    enterID_label = Label(getID_window, text='Enter Item ID')
    enterID_label.grid(row=0, column=0, padx=10, pady=5)

    # Create the text box for getting ID
    enterID_text = Entry(getID_window)
    enterID_text.grid(row=1, column=0, padx=10, pady=5)

    button_functions = [
        ('Read', open_read_window),
        ('Modify', open_read_window),
        ('Check In', open_read_window),
        ('Check Out', open_read_window),
        ('Delete', open_delete_window)]

    # Buttons
    for i, (text, command) in enumerate(button_functions):
        button = Button(getID_window, text=text, fg='black', bg='white', width=10, command=command)
        button.grid(row=i+2, column=0, padx=10, pady=5)

    # Create the submit button in the third window
    submit_button = Button(getID_window, text='Submit', command=submit)
    submit_button.grid(row=i+3, column=0, padx=10, pady=10)

    # Create the exit button for the window
    exit_button = Button(getID_window, text='Exit', command=getID_window.destroy)
    exit_button.grid(row=i+3, column=1, padx=10, pady=10)

def open_delete_window():
    # Function to open the fourth window
    delete_window = Toplevel(window)
    delete_window.title('Item Deleted')

    # Create the text box for deleted
    delete_text = Label(delete_window, text='Item Deleted')
    delete_text.grid(row=0, column=0, padx=10, pady=5)

    # Create the submit button in the fourth window
    delete_button = Button(delete_window, text='Okay', command=delete_window.destroy)
    delete_button.grid(row=1, column=0, padx=10, pady=10)

def exit_window():
    window.destroy()

# Create the main window
window = Tk()
window.title('Inventory Database')
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create a list to hold the labels and entry widgets
entry_list = []
label_texts = [
    'Class', 'Manufacturer', 'Model Number',
    'Serial Number', 'Date Acquired', 'Description',
    'Status', 'Location', 'Assembly']

# Create the open button in the main window
button_functions = [
    ('Add Item', open_item_window),
    ('Modify Item', open_getID_window),
    ('Export', open_delete_window),
    ('Exit', exit_window)]

# Buttons
for i, (text, command) in enumerate(button_functions):
    button = Button(window, text=text, fg='black', bg='white', width=10, command=command)
    button.grid(column=0, row=i, padx=10, pady=5, sticky='w')

# Start the Tkinter event loop
window.mainloop()