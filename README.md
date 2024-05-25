# Post-Graduate-Management-Model

This project is a Python application that uses the 'customtkinter' library to create a graphical user interface (GUI) for interacting with a SQL Server database. The application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on the database through a user-friendly interface.

## Libraries Used
1. customtkinter (ctk): A custom Tkinter library for creating modern GUI applications.
2. tkinter (tk): The standard Python interface to the Tk GUI toolkit.
3. pyodbc: A Python library for accessing databases using ODBC (Open Database Connectivity).
4. prettytable: Used for creating ASCII tables, though not directly used in the provided code.
5. PIL (Pillow): Used for image processing.

## Functions
create_scrollable_frame(parent)
Creates a scrollable frame within a given parent widget. This is useful for displaying content that exceeds the visible area.

insert_query()
Handles the insertion of data into a specified table. The function:

  1. Retrieves the table name and data from user input.
  2. Parses the input data into column-value pairs.
  3. Constructs an SQL INSERT query and executes it.
  4. Shows success or error messages based on the outcome.


select_query()
Handles data retrieval from a specified table. The function:

  1. Retrieves the table name and optional condition from user input.
  2. Constructs an SQL SELECT query and executes it.
  3. Displays the results in a textbox widget.
  4. Shows messages if there are no results or if an error occurs.


update_query()
Handles updating data in a specified table. The function:

  1. Retrieves the table name, condition, and new values from user input.
  2. Constructs an SQL UPDATE query and executes it.
  3. Shows success or error messages based on the outcome.


delete_query()
Handles deletion of data from a specified table. The function:

  1. Retrieves the table name and condition from user input.
  2. Constructs an SQL DELETE query and executes it.
  3. Shows success or error messages based on the outcome.


clear_fields()
Clears all input fields and the result textbox.


## GUI Layout

- The main window of the application is created using customtkinter with a specified title and geometry.
- Various frames and widgets are created and packed into the main window to form sections for different operations:
    - Header Frame: Displays an image and title.
    - First Section Frame: For entering table name and condition for SELECT and DELETE operations.
    - Select/Update Frame: Contains buttons for SELECT and DELETE operations.
    - Second Section Frame: For entering details for the UPDATE operation.
    - Insert Section Frame: For entering details for the INSERT operation.
    - Results Frame: Displays query results in a textbox.
    - Clear Button: Clears all fields and results.


## Main Application Loop

The app.mainloop() call starts the Tkinter event loop, allowing the GUI to wait for user interactions.
