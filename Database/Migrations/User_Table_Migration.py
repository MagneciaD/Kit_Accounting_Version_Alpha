import mysql.connector

def create_organisation_table():
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
        table_name = 'organisation'
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            org_id INT PRIMARY KEY AUTO_INCREMENT,
            company_name VARCHAR(255),
            email_address VARCHAR(255),
            password VARCHAR(255),
            company_address VARCHAR(255),
            address VARCHAR(255),
            phone_number VARCHAR(20),
            link VARCHAR(255),
            company_logo VARCHAR(255),
            timestamp TIMESTAMP
        )
        '''.format(table_name)

        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'organisation' has been created successfully.")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def delete_organisation_table():
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

        # Delete the user table
        table_name = 'organisation'
        delete_table_query = '''
        DROP TABLE IF EXISTS {}
        '''.format(table_name)

        cursor.execute(delete_table_query)

        # Commit the changes
        connection.commit()
        print("Table 'organisation' has been deleted successfully.")

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
create_organisation_table()

# Call the function to delete the user table
#delete_user_table()
