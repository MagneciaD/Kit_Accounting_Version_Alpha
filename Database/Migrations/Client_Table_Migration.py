import mysql.connector

def create_client_table():
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

        # Create the user table
        table_name = 'client'
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            org_id INT,
            email VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            address VARCHAR(255),
            phone_no VARCHAR(20),
            timestamp TIMESTAMP,
        
            FOREIGN KEY (org_id) REFERENCES organization (org_id)
        )
        '''.format(table_name)

        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()
        print("Table client' has been created successfully.")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def delete_client_table():
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

        # Delete the client table
        table_name = 'client'
        delete_table_query = '''
        DROP TABLE IF EXISTS {}
        '''.format(table_name)

        cursor.execute(delete_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'client' has been deleted successfully.")

    except mysql.connector.Error as error:
        print("Failed to delete table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function to create the user table
create_client_table()

# Call the function to delete the user table
#delete_client_table()
