# Home Inventory Management System Documentation

## Introduction

**Disclaimer: this documentation was generated using OpenAI's ChatGPT 3.5.**

This documentation provides an overview of the Home Inventory Management System code, which is a Python application designed to manage home inventory data. The system uses the tkinter library for the graphical user interface (GUI), openpyxl for Excel file operations, and sqlite3 for database management. The code allows users to perform various operations such as adding items, modifying item details, deleting items, checking items in and out, exporting data to Excel, querying the database, and more.
Requirements

## Prerequisites

To run the Home Inventory Management System, you need the following requirements:

- Python: The code is written in Python and requires Python installed on the system.
- tkinter: The tkinter library comes pre-installed with most Python distributions.
- openpyxl: Install this library using pip install openpyxl to perform Excel file operations.
- sqlite3: The sqlite3 library comes built-in with Python and provides support for SQLite databases.

## Code Structure

The code is organized into functions that handle specific tasks, such as database operations, GUI setup, data manipulation, etc. The main functions in the code include:

- db_create(): Creates the initial main table in the SQLite database.
- db_add_test(): Inserts test data into the main table for initial testing purposes.
- db_write(): Writes data from the data buffer to the main table in the database.
- db_checkout(): Updates the location and assembly fields of an item to check it out.
- db_checkin(): Updates the location and assembly fields of an item to check it in.
- db_modify(): Updates an item's details in the main table.
- db_read(rowID): Reads data from the main table based on the provided rowID.
- db_read_table(): Reads and displays all data from the main table.
- db_delete(rowID): Deletes an item from the main table based on the provided rowID.
- generate_id(): Generates the next unique ID for new items based on existing IDs in the main table.
- db_query(): Executes a custom SQL query provided by the user and exports the results to an Excel file.

The code also includes several functions related to the GUI setup and user interactions, such as adding, clearing, reading, deleting, and modifying data in the GUI text boxes.
GUI Layout

The GUI is built using tkinter and consists of several elements:

- Ten input text boxes for the user to enter item details like ID, Class, Manufacturer, etc.
- Buttons for various actions, such as Enter, Clear, Read, Delete, Modify, Check-in, Check-out, Export, and Exit.
- An index text box to input the ID for read, delete, and modify operations.
- A SQL query text box to input custom queries for the database.
- A status label to display the current status of operations.

## Usage

To use the Home Inventory Management System, follow these steps:

- Run the Python script containing the code.
- The GUI window will open, displaying ten input text boxes and buttons for various operations.
- Enter item details into the text boxes.
- Click the "Enter" button to add the item to the database.
- Click the "Read" button and provide an item ID to retrieve item details from the database.
- Click the "Delete" button and provide an item ID to remove the item from the database.
- Click the "Modify" button to update item details in the database.
- Click the "Check-in" button to change an item's location and assembly status.
- Click the "Check-out" button to check out an item and update its location and assembly status.
- Click the "Export" button to export all items in the database to an Excel file.
- Use the "SQL" text box to input custom SQL queries and click the "Query" button to execute the query and export the results to an Excel file.
- Click the "Clear" button to clear the input text boxes.
- Click the "Exit" button to close the application and disconnect from the database.

## Conclusion

The Home Inventory Management System is a Python application that allows users to manage their home inventory. With a graphical user interface, users can easily add, read, modify, and delete items from the inventory database. The system also offers the ability to check-in and check-out items, export inventory data to Excel files, and execute custom SQL queries for more advanced operations.
