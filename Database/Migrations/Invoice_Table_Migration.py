import mysql.connector

def create_invoice_table():
    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Kit-Accounting-DB'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Create the invoice table
        table_name = 'invoice'
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            invoice_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            organization_id INT,
            invoice_date DATE,
            invoice_result VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES user(user_id),
            FOREIGN KEY (organization_id) REFERENCES organization(organization_id)
        )
        '''.format(table_name)

        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'invoice' has been created successfully.")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def delete_invoice_table():
    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Kit-Accounting-DB'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Delete the invoice table
        table_name = 'invoice'
        delete_table_query = '''
        DROP TABLE IF EXISTS {}
        '''.format(table_name)

        cursor.execute(delete_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'invoice' has been deleted successfully.")

    except mysql.connector.Error as error:
        print("Failed to delete table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function to create the invoice table
create_invoice_table()

# Call the function to delete the invoice table
delete_invoice_table()
