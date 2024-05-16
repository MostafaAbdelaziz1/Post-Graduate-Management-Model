import customtkinter as ctk
import pyodbc
from prettytable import PrettyTable
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import tkinter as tk

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER="SERVER_NAME";'
    r'DATABASE="DB_NAME";'
    'trusted_connection=yes;'
)


def create_scrollable_frame(parent):
    canvas = tk.Canvas(parent)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollable_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw', width=canvas.cget('width'))
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind('<Configure>', lambda e: canvas.itemconfig('all', width=e.width))
    return scrollable_frame


def insert_query():
    table = insert_table_entry.get()
    data = insert_data_entry.get()

    try:
        data_pairs = data.split(',')
        columns = []
        values = []
        for pair in data_pairs:
            key_value = pair.strip().split('=')
            if len(key_value) != 2:
                raise ValueError("Each data entry must be in the format 'column=value'.")
            columns.append(key_value[0].strip())
            values.append(key_value[1].strip())

        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()

            placeholders = ', '.join(['?' for _ in values])
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully.")
    except pyodbc.Error as e:
        print(f"Database Error: {e}")
        messagebox.showerror("Database Error", f"Insert failed: {str(e)}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
        messagebox.showerror("Input Error", f"Insert failed: {str(ve)}")
    except Exception as e:
        print(f"General Error: {e}")
        messagebox.showerror("Error", f"Insert failed: {str(e)}")


def select_query():
    table = table_entry.get()
    condition = select_condition_entry.get()

    result_textbox.delete('1.0', 'end')

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            if condition:
                query = f"SELECT * FROM {table} WHERE {condition}"
            else:
                query = f"SELECT * FROM {table}"
            cursor.execute(query)

            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                messagebox.showinfo('Notice', "No data found.  Please check your entry.\n")
                return

            for row in rows:
                row_data = ' | '.join(f"{col}: {str(val)}" for col, val in zip(columns, row))
                result_textbox.insert('end', f"{row_data}\n")
                result_textbox.insert('end', '\n')
    except pyodbc.Error as e:
        print(f"Database Error: {e}")
        messagebox.showerror("Database Error", f"Delete failed: {str(e)}")
    except Exception as e:
        print(f"General Error: {e}")
        messagebox.showerror("Error", f"Delete failed: {str(e)}")


def update_query():
    table = table_update_entry.get()
    condition = old_values_entry.get()
    new_values = new_values_entry.get()
    if not condition:
        messagebox.showinfo("Notice", "Please enter a condition to update specific rows.")
        return

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            query = f"UPDATE {table} SET {new_values} WHERE {condition}"
            cursor.execute(query)
            rows_updated = cursor.rowcount
            conn.commit()
            if rows_updated > 0:
                messagebox.showinfo("Success", f"Updated successfully. Rows affected: {rows_updated}")
            else:
                messagebox.showinfo("Notice", "No rows were updated. Please check your query.")
    except pyodbc.Error as e:
        print(f"Database Error: {e}")
        messagebox.showerror("Database Error", f"Update failed: {str(e)}")
    except Exception as e:
        print(f"General Error: {e}")
        messagebox.showerror("Error", f"Update failed: {str(e)}")


def delete_query():
    table = table_entry.get()
    condition = select_condition_entry.get()
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            if condition:
                query = f"DELETE FROM {table} WHERE {condition}"
                cursor.execute(query)
                rows_deleted = cursor.rowcount
                conn.commit()
                if rows_deleted > 0:
                    messagebox.showinfo("Success", f"Deleted successfully. Rows affected: {rows_deleted}")
                else:
                    messagebox.showinfo("Notice", "No rows were deleted. Please check your query.")
            else:
                messagebox.showinfo("Notice", "Please enter a condition to delete specific rows.")
    except pyodbc.Error as e:
        print(f"Database Error: {e}")
        messagebox.showerror("Database Error", f"Delete failed: {str(e)}")
    except Exception as e:
        print(f"General Error: {e}")
        messagebox.showerror("Error", f"Delete failed: {str(e)}")


def clear_fields():
    table_entry.delete(0, 'end')
    select_condition_entry.delete(0, 'end')
    table_update_entry.delete(0, 'end')
    new_values_entry.delete(0, 'end')
    old_values_entry.delete(0, 'end')
    insert_table_entry.delete(0, 'end')
    insert_data_entry.delete(0, 'end')
    result_textbox.delete('1.0', 'end')


app = ctk.CTk()

app.title("Automation Application")
app.geometry('1000x700')

main_frame = create_scrollable_frame(app)

header_frame = ctk.CTkFrame(main_frame)
header_frame.pack(pady=50)

image_path = r'PATH/TO/YOUR/IMAGE.jpg'
original_image = Image.open(image_path)

label_width = int(original_image.width * (50 / original_image.height))
resized_image = original_image.resize((label_width, 50), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

image_label = ctk.CTkLabel(header_frame, image=photo)
image_label.grid(row=0, column=0)

title_label = ctk.CTkLabel(header_frame, text='Master Admission', font=('Century gothic', 30))
title_label.grid(row=0, column=1, padx=20)

first_section_frame = ctk.CTkFrame(main_frame)
first_section_frame.pack(pady=10)

table_label = ctk.CTkLabel(first_section_frame, text="Enter a table", font=('Century gothic', 20))
table_label.grid(row=0, column=0, padx=10, pady=10)

table_entry = ctk.CTkEntry(first_section_frame)
table_entry.grid(row=0, column=1, padx=10, pady=10)

select_condition_label = ctk.CTkLabel(first_section_frame, text="Enter a condition (optional)",
                                      font=('Century gothic', 20))
select_condition_label.grid(row=3, column=0, padx=10, pady=10)

select_condition_entry = ctk.CTkEntry(first_section_frame)
select_condition_entry.grid(row=3, column=1, padx=10, pady=10)

select_update_frame = ctk.CTkFrame(main_frame)
select_update_frame.pack(pady=10)

select_button = ctk.CTkButton(select_update_frame, text="Select", command=select_query)
select_button.grid(row=0, column=0, padx=10, pady=10)

delete_button = ctk.CTkButton(select_update_frame, text="Delete", command=delete_query)
delete_button.grid(row=0, column=1, padx=10, pady=10)

second_section_frame = ctk.CTkFrame(main_frame)
second_section_frame.pack(pady=10)

table_update_label = ctk.CTkLabel(second_section_frame, text="Enter table to update", font=('Century gothic', 20))
table_update_label.grid(row=0, column=0, padx=10, pady=10)

table_update_entry = ctk.CTkEntry(second_section_frame)
table_update_entry.grid(row=0, column=1, padx=10, pady=10)

old_values_label = ctk.CTkLabel(second_section_frame, text="Enter old values", font=('Century gothic', 20))
old_values_label.grid(row=1, column=0, padx=10, pady=10)

old_values_entry = ctk.CTkEntry(second_section_frame)
old_values_entry.grid(row=1, column=1, padx=10, pady=10)

old_values_syntax_label = ctk.CTkLabel(second_section_frame, text="'any_column_name=column_value'",
                                       font=('Century gothic', 12))
old_values_syntax_label.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

new_values_label = ctk.CTkLabel(second_section_frame, text="Enter new values", font=('Century gothic', 20))
new_values_label.grid(row=3, column=0, padx=10, pady=10)

new_values_entry = ctk.CTkEntry(second_section_frame)
new_values_entry.grid(row=3, column=1, padx=10, pady=10)

new_values_syntax_label = ctk.CTkLabel(second_section_frame, text="'column_name=new_column_value'",
                                       font=('Century gothic', 12))
new_values_syntax_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

update_button = ctk.CTkButton(main_frame, text="Update", command=update_query)
update_button.pack(pady=10)

insert_section_frame = ctk.CTkFrame(main_frame)
insert_section_frame.pack(pady=10)

insert_table_label = ctk.CTkLabel(insert_section_frame, text="Enter table to insert data", font=('Century gothic', 20))
insert_table_label.grid(row=0, column=0, padx=10, pady=10)

insert_table_entry = ctk.CTkEntry(insert_section_frame)
insert_table_entry.grid(row=0, column=1, padx=10, pady=10)

insert_data_label = ctk.CTkLabel(insert_section_frame, text="Enter data to insert", font=('Century gothic', 20))
insert_data_label.grid(row=1, column=0, padx=10, pady=10)

insert_data_entry = ctk.CTkEntry(insert_section_frame)
insert_data_entry.grid(row=1, column=1, padx=10, pady=10)

insert_data_syntax_label = ctk.CTkLabel(insert_section_frame, text="'column1=value1, column2=value2, ...'",
                                        font=('Century gothic', 12))
insert_data_syntax_label.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

insert_button = ctk.CTkButton(main_frame, text="Insert", command=insert_query)
insert_button.pack(pady=10)

results_frame = ctk.CTkFrame(main_frame)
results_frame.pack(fill='both', expand=True, pady=10)

result_textbox = ctk.CTkTextbox(results_frame, width=400, height=200, wrap='none', font=('Century gothic', 20))
result_textbox.pack(side='left', fill='both', expand=True)

clear_button = ctk.CTkButton(main_frame, text="Clear", command=clear_fields)
clear_button.pack(pady=10)

app.mainloop()
