# Post-Graduate-Management-Model

This project is about college automation for post-graduate studies.


This project is a Python application that uses the 'customtkinter' library to create a graphical user interface (GUI) for interacting with a SQL Server database. The application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on the database through a user-friendly interface. Here's a detailed breakdown of the project code:

## Libraries Used
customtkinter (ctk): A custom Tkinter library for creating modern GUI applications.
pyodbc: A Python library for accessing databases using ODBC (Open Database Connectivity).
prettytable: Used for creating ASCII tables, though not directly used in the provided code.
tkinter.messagebox: Provides message box functions for Tkinter applications.
PIL (Pillow): Used for image processing.
tkinter (tk): The standard Python interface to the Tk GUI toolkit.
Connection String
The connection string conn_str is defined to connect to a SQL Server database using ODBC Driver 17.
Functions
create_scrollable_frame(parent)
Creates a scrollable frame within a given parent widget. This is useful for displaying content that exceeds the visible area.

insert_query()
Handles the insertion of data into a specified table. The function:

Retrieves the table name and data from user input.
Parses the input data into column-value pairs.
Constructs an SQL INSERT query and executes it.
Shows success or error messages based on the outcome.
select_query()
Handles data retrieval from a specified table. The function:

Retrieves the table name and optional condition from user input.
Constructs an SQL SELECT query and executes it.
Displays the results in a textbox widget.
Shows messages if there are no results or if an error occurs.
update_query()
Handles updating data in a specified table. The function:

Retrieves the table name, condition, and new values from user input.
Constructs an SQL UPDATE query and executes it.
Shows success or error messages based on the outcome.
delete_query()
Handles deletion of data from a specified table. The function:

Retrieves the table name and condition from user input.
Constructs an SQL DELETE query and executes it.
Shows success or error messages based on the outcome.
clear_fields()
Clears all input fields and the result textbox.

GUI Layout
The main window of the application is created using customtkinter with a specified title and geometry.
Various frames and widgets are created and packed into the main window to form sections for different operations:
Header Frame: Displays an image and title.
First Section Frame: For entering table name and condition for SELECT and DELETE operations.
Select/Update Frame: Contains buttons for SELECT and DELETE operations.
Second Section Frame: For entering details for the UPDATE operation.
Insert Section Frame: For entering details for the INSERT operation.
Results Frame: Displays query results in a textbox.
Clear Button: Clears all fields and results.
Main Application Loop
The app.mainloop() call starts the Tkinter event loop, allowing the GUI to wait for user interactions.
