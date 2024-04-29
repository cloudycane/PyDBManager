import tkinter as tk
import psycopg2
from psycopg2 import Error

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Simple Database Creation With PostgreSQL")
root.geometry("910x890")

# Not resizable window
root.resizable(False, False)

# CONNECTING TO POSTGRESQL
# Create the title label widget
title_connection_frame = tk.Frame(root, padx=10, pady=10)
title_connection_frame.grid(row=0, column=0)
title_connection = tk.Label(title_connection_frame, text="POSTGRESQL", font=("Arial", 12, "bold"))
title_connection.grid(row=0, column=0, sticky="nsew", columnspan=2)

# FRAMES
username_entry_frame = tk.Frame(root, padx=10, pady=10)
username_entry_frame.grid(row=1, column=0)

password_entry_frame = tk.Frame(root, padx=10, pady=10)
password_entry_frame.grid(row=1, column=1)

host_entry_frame = tk.Frame(root, padx=10, pady=10)
host_entry_frame.grid(row=1, column=2)

port_entry_frame = tk.Frame(root, padx=10, pady=10)
port_entry_frame.grid(row=1, column=3)

database_entry_frame = tk.Frame(root, padx=10, pady=10)
database_entry_frame.grid(row=1, column=4)

# Create the username entry widget
username_entry = tk.Entry(username_entry_frame)
username_entry.grid(row=1, column=0)

username_label = tk.Label(root, text="Username")
username_label.grid(row=2, column=0)

# Create the password entry widget
password_entry = tk.Entry(password_entry_frame)
password_entry.grid(row=1, column=1)

password_label = tk.Label(root, text="Password")
password_label.grid(row=2, column=1)

# Create a host entry widget
host_entry = tk.Entry(host_entry_frame)
host_entry.grid(row=1, column=2)

host_entry_label = tk.Label(root, text="Host Name")
host_entry_label.grid(row=2, column=2)

# Create a port entry widget
port_entry = tk.Entry(port_entry_frame)
port_entry.grid(row=1, column=3)

port_entry_label = tk.Label(root, text="Port")
port_entry_label.grid(row=2, column=3)

# Create a database entry widget

database_entry = tk.Entry(database_entry_frame)
database_entry.grid(row=1, column=4)

database_entry_label = tk.Label(root, text="Database Name")
database_entry_label.grid(row=2, column=4)

# Connection Button
def connect_to_postgreSQL():
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()
    print(f"""
        username: {username}, 
        password: {password}, 
        host: {hostname}, 
        port: {port}, 
        database_name: {database_name}
    """)
    try:
        connection = psycopg2.connect(user=username,
                                     password=password,
                                     host=hostname,
                                     port=port,
                                     database=database_name)
        cursor = connection.cursor()
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text="The database exists! You can now insert, update, and delete values from the database! ")
        label.pack()

    except (Exception, Error) as error:
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed...")


connection_button = tk.Button(text="Connect to Database", command=connect_to_postgreSQL)
connection_button.grid(row=1, column=5)


# Center the title label horizontally within its cell
#root.grid_columnconfigure((0, 0), weight=2)

# SELECTING QUERIES
select_query_frame = tk.Frame(root, padx=10, pady=10)
select_query_frame.grid(row=3, column=0)

select_query_title = tk.Label(select_query_frame, text="SELECT", font=("Arial", 12, "bold"))
select_query_title.grid(row=3, column=0)

select_entry_frame = tk.Frame(root, padx=10, pady=10)
select_entry_frame.grid(row=4, column=0)

select_entry = tk.Entry(select_entry_frame)
select_entry.grid(row=4, column=0)

select_label = tk.Label(root, text="Select (column)")
select_label.grid(row=5, column=0)

from_entry_frame = tk.Frame(root, padx=10, pady=10)
from_entry_frame.grid(row=4, column=1)

from_entry = tk.Entry(from_entry_frame)
from_entry.grid(row=4, column=1)

from_label = tk.Label(root, text="From (table name)")
from_label.grid(row=5, column=1)

where_entry_frame = tk.Frame(root, padx=10, pady=10)
where_entry_frame.grid(row=4, column=2)

where_entry = tk.Entry(where_entry_frame)
where_entry.grid(row=4, column=2)

where_label = tk.Label(root, text="Where (conditions)")
where_label.grid(row=5, column=2)

# FUNCTION TO SELECT QUERIES IN THE DATABASE

def select_query():
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()

    selected_column = select_entry.get()
    select_from_table = from_entry.get()
    select_where_condition = where_entry.get()

    print(f"""
            username: {username}, 
            password: {password}, 
            host: {hostname}, 
            port: {port}, 
            database_name: {database_name}
            
            selected column: {selected_column},
            selected from table: {select_from_table}, 
            condition: {select_where_condition}
        
        """)
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=hostname,
                                      port=port,
                                      database=database_name)
        cursor = connection.cursor()
        if select_where_condition == "":
            query = f"SELECT {selected_column} FROM {select_from_table}"
            cursor.execute(query)
            rows = cursor.fetchall()

            popup = tk.Toplevel(root)
            popup.title("PostgreSQL Selected Queries Information")
            popup.geometry("540x160")
            popup.resizable(False, False)

            label = tk.Label(popup,
                             text=f"Success!{rows}")
            label.pack()

            for row in rows:
                print(row)

            cursor.close()
            connection.close()
        else:
            query = f"SELECT {selected_column} FROM {select_from_table} WHERE {select_where_condition}"
            cursor.execute(query)

            rows = cursor.fetchall()

            popup = tk.Toplevel(root)
            popup.title("PostgreSQL Selected Queries Information")
            popup.geometry("540x160")
            popup.resizable(False, False)

            label = tk.Label(popup,
                         text=f"{rows}")
            label.pack()

            for row in rows:
                print(row)

            cursor.close()
            connection.close()

    except (Exception, Error) as error:
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed...")


select_button = tk.Button(root, text="Select query(ies)", command=select_query)
select_button.grid(row=4, column=3)

# CREATE TABLE

table_label_frame = tk.Frame(root, padx=10, pady=10)
table_label_frame.grid(row=6, column=0)

table_label = tk.Label(table_label_frame, text="CREATE TABLE", font=("Arial", 12, "bold"))
table_label.grid(row=6, column=0)

create_table_entry_frame = tk.Frame(root, padx=10, pady=10)
create_table_entry_frame.grid(row=7, column=0)

create_table_entry = tk.Entry(create_table_entry_frame)
create_table_entry.grid(row=7, column=0)

table_name_label = tk.Label(root, text="Table's Name")
table_name_label.grid(row=8, column=0)

item_1_entry_frame = tk.Frame(root, padx=10, pady=10)
item_1_entry_frame.grid(row=7, column=1)

item_1_entry = tk.Entry(item_1_entry_frame)
item_1_entry.grid(row=7, column=1)

item_1_label = tk.Label(root, text="Item 1")
item_1_label.grid(row=8, column=1)

values = ["BOOL", "REAL", "DOUBLE", "SMALLINT", "INT", "BIGINT", "NUMERIC", "VARCHAR", "TEXT", "DATE",
          "TIME", "TIMETZ", "TIMESTAMPT", "TIMESTAMPTZ", "INTERVAL", "ARRAY", "HSTORE"]

selected_option = tk.StringVar(root)
selected_option.set(values[0]) # default option

values_frame = tk.Frame(root)
values_frame.grid(row=7, column=2)
listbox = tk.Listbox(values_frame, selectmode=tk.SINGLE)
listbox.grid(row=7, column=2)

scrollbar = tk.Scrollbar(values_frame, orient=tk.VERTICAL)
scrollbar.grid(row=7, column=3)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for value in values:
    listbox.insert(tk.END, value)

primarykey = tk.Label(root, text="PRIMARY KEY")
primarykey.grid(row=7, column=3)

notnull = tk.Label(root, text="NOT NULL")
notnull.grid(row=7, column=4)

# FUNCTION TO CREATE TABLE
def create_table():
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()

    new_table_name = create_table_entry.get()
    new_item_name = item_1_entry.get()
    new_column = item_1_entry.get()
    data_type = selected_option.get()

    print(f"""
              username: {username}, 
              password: {password}, 
              host: {hostname}, 
              port: {port}, 
              database_name: {database_name}
            
             new table: {new_table_name}, 
             new item: {new_item_name}, 
             new column: {new_column}
             data type: {data_type}
             NOT NULL

          """)
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=hostname,
                                      port=port,
                                      database=database_name)
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {new_table_name} ({new_column} {data_type} PRIMARY KEY NOT NULL)"
        cursor.execute(create_table_query)
        connection.commit()

        popup = tk.Toplevel(root)
        popup.title("PostgreSQL New Table Creation Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"You have successfully created a new table.")
        label.pack()
        cursor.close()
        connection.close()

    except (Exception, Error) as error:
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed...")


create_table_button = tk.Button(root, text="Create Table", command=create_table)
create_table_button.grid(row=7, column=5)

# INSERT VALUES

insert_values_frame = tk.Frame(root, padx=20, pady=20)
insert_values_frame.grid(row=9, column=0)

insert_values_title = tk.Label(insert_values_frame, text="INSERT VALUES", font=("Arial", 12, "bold"))
insert_values_title.grid(row=9, column=0)

insert_label = tk.Label(root, text="INSERT INTO")
insert_label.grid(row=10, column=0)

insert_table_entry_frame = tk.Frame(root, padx=10, pady=10)
insert_table_entry_frame.grid(row=10, column=1)

insert_table_entry = tk.Entry(insert_table_entry_frame)
insert_table_entry.grid(row=10, column=1)

insert_table_label = tk.Label(root, text="Table's name")
insert_table_label.grid(row=11, column=1)

column_entry_frame = tk.Frame(root, padx=10, pady=10)
column_entry_frame.grid(row=9, column=2)

column1_entry = tk.Entry(column_entry_frame)
column1_entry.grid(row=9, column=2)

column1_label = tk.Label(root, text="Column 1 + values")
column1_label.grid(row=11, column=2)

column2_entry_frame = tk.Frame(root, padx=10, pady=10)
column2_entry_frame.grid(row=9, column=3)

column2_entry = tk.Entry(column2_entry_frame)
column2_entry.grid(row=9, column=3)

column2_label = tk.Label(root, text="Column 2 + values")
column2_label.grid(row=11, column=3)

column3_entry_frame = tk.Frame(root, padx=10, pady=10)
column3_entry_frame.grid(row=9, column=4)

column3_entry = tk.Entry(column3_entry_frame)
column3_entry.grid(row=9, column=4)

column3_label = tk.Label(root, text="Column 3 + values")
column3_label.grid(row=11, column=4)

# VALUES FROM COLUMNS

value_1_entry_frame = tk.Frame(root, padx=10, pady=10)
value_1_entry_frame.grid(row=10, column=2)

value_1_entry = tk.Entry(value_1_entry_frame)
value_1_entry.grid(row=10, column=2)

value_2_entry_frame = tk.Frame(root, padx=10, pady=10)
value_2_entry_frame.grid(row=10, column=3)

value_2_entry = tk.Entry(value_2_entry_frame)
value_2_entry.grid(row=10, column=3)

value_3_entry_frame = tk.Frame(root, padx=10, pady=10)
value_3_entry_frame.grid(row=10, column=4)

value_3_entry = tk.Entry(value_3_entry_frame)
value_3_entry.grid(row=10, column=4)

# INSERT BUTTON FUNCTION

def insert_values():
    # Get connection details
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()

    # Get values for insertion
    table_name = insert_table_entry.get()
    column1 = column1_entry.get()
    column2 = column2_entry.get()
    column3 = column3_entry.get()

    value1 = value_1_entry.get()
    value2 = value_2_entry.get()
    value3 = value_3_entry.get()

    # Establish connection to the database
    try:
        connection = psycopg2.connect(
            user=username,
            password=password,
            host=hostname,
            port=port,
            database=database_name
        )

        # Create a cursor object
        cursor = connection.cursor()

        insert_query = f'''INSERT INTO {table_name} ({column1}, {column2}, {column3}) VALUES ({value1}, {value2}, {value3})'''
        cursor.execute(insert_query)
        connection.commit()
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"You have successfully inserted some values to the database.")
        label.pack()


    except psycopg2.Error as e:
        # Handle exceptions
        print("Error:", e)
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()

# Insert Button
insert_button = tk.Button(root, text="Insert", command=insert_values)
insert_button.grid(row=11, column=5)

# UPDATE
update_values_frame = tk.Frame(root, padx=20, pady=20)
update_values_frame.grid(row=12, column=0)
update_values_label = tk.Label(update_values_frame, text="UPDATE VALUES", font=("Arial", 12, "bold"))
update_values_label.grid(row=12, column=0)

update_label = tk.Label(root, text="UPDATE")
update_label.grid(row=13, column=0)

update_entry_frame = tk.Frame(root, padx=10, pady=10)
update_entry_frame.grid(row=13, column=1)

update_entry = tk.Entry(update_entry_frame)
update_entry.grid(row=13, column=1)

table_update_label = tk.Label(root, text="Table's name")
table_update_label.grid(row=14, column=1)

set_label = tk.Label(root, text="SET")
set_label.grid(row=13, column=2)

column_update_frame = tk.Frame(root, padx=10, pady=10)
column_update_frame.grid(row=13, column=3)

column_update = tk.Entry(column_update_frame)
column_update.grid(row=13, column=3)

column_update_label = tk.Label(root, text="column = (value + conditions)")
column_update_label.grid(row=14, column=3)

update_values_entry_frame = tk.Frame(root, padx=10, pady=10)
update_values_entry_frame.grid(row=13, column=4)

update_values_entry = tk.Entry(update_values_entry_frame)
update_values_entry.grid(row=13, column=4)

condition_update_label = tk.Label(root, text="Where (conditions)")
condition_update_label.grid(row=14, column=4)

# UPDATE FUNCTION
def update_values():
    # Get connection details
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()

    table_update = update_entry.get()
    update_column = column_update.get()
    condition_update = update_values_entry.get()

    # Establish connection to the database
    try:
        connection = psycopg2.connect(
            user=username,
            password=password,
            host=hostname,
            port=port,
            database=database_name
        )

        # Create a cursor object
        cursor = connection.cursor()

        update_query = f'''UPDATE {table_update} SET {update_column} WHERE {condition_update}'''

        cursor.execute(update_query)
        connection.commit()

        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"You have successfully updated some values to the database.")
        label.pack()


    except psycopg2.Error as e:
        # Handle exceptions
        print("Error:", e)
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()
        
    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()

update_button = tk.Button(root, text="Update", command=update_values)
update_button.grid(row=13, column=5)

# DELETE VALUES

delete_values_label_frame = tk.Frame(root, padx=20, pady=20)
delete_values_label_frame.grid(row=15, column=0)

delete_values_label = tk.Label(delete_values_label_frame, text="DELETE VALUES", font=("Arial", 12, "bold"))
delete_values_label.grid(row=15, column=0)

delete_from_label = tk.Label(root, text="DELETE FROM")
delete_from_label.grid(row=16, column=0)

delete_from_table_entry_frame = tk.Frame(root, padx=10, pady=10)
delete_from_table_entry_frame.grid(row=16, column=1)

delete_from_table_entry = tk.Entry(delete_from_table_entry_frame)
delete_from_table_entry.grid(row=16, column=1)

delete_from_table_label = tk.Label(root, text="Table's Name")
delete_from_table_label.grid(row=17, column=1)

delete_where_label = tk.Label(root, text="WHERE")
delete_where_label.grid(row=16, column=2)

delete_where_entry_frame = tk.Frame(root, padx=10, pady=10)
delete_where_entry_frame.grid(row=16, column=3)

delete_where_entry = tk.Entry(delete_where_entry_frame)
delete_where_entry.grid(row=16, column=3)

delete_where_entry_label = tk.Label(root, text="column + conditions")
delete_where_entry_label.grid(row=17, column=3)

# DELETE VALUES FUNCTION

def delete_values():
    # Get connection details
    username = username_entry.get()
    password = password_entry.get()
    hostname = host_entry.get()
    port = port_entry.get()
    database_name = database_entry.get()

    table_delete = delete_from_table_entry.get()
    where_delete = delete_where_entry.get()

    # Establish connection to the database
    try:
        connection = psycopg2.connect(
            user=username,
            password=password,
            host=hostname,
            port=port,
            database=database_name
        )

        # Create a cursor object
        cursor = connection.cursor()

        delete_query = f'''DELETE FROM {table_delete} WHERE {where_delete}'''
        cursor.execute(delete_query)
        connection.commit()

        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"You have successfully deleted some values to the database.")
        label.pack()


    except psycopg2.Error as e:
        # Handle exceptions
        print("Error:", e)
        print("Error:", e)
        popup = tk.Toplevel(root)
        popup.title("PostgreSQL Connection Information")
        popup.geometry("540x80")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"Error while connecting to PostgreSQL")
        label.pack()

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()


delete_button = tk.Button(root, text="Delete", command=delete_values)
delete_button.grid(row=16, column=4)

# Run the Tkinter event loop
root.mainloop()
