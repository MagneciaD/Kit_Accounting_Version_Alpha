import mysql.connector

def register_client():
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

        # Prompt the user for information
        email = input("Enter your email: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        address  = input("Enter your physical address: ")
        phone_no = input("Enter the phone number (10 digits): ")

        # Validate the phone number
        if not phone_no.isdigit() or len(phone_no) != 10:
            print("Invalid phone number. Please enter a 10-digit number.")
            return

        # Check if the user already exists
        check_client_query = "SELECT * FROM client WHERE email = %s AND phone_no = %s"
        cursor.execute(check_client_query, (email, phone_no))
        existing_client = cursor.fetchone()
        if existing_client:
            print("Client already exists in the database.")
            return

        # Insert the user into the client table
        insert_user_query = "INSERT INTO client (email, first_name, last_name, phone_no, address) VALUES (%s, %s, %s, %s, %s)"
        user_data = (email, first_name, last_name, phone_no, address)
        cursor.execute(insert_user_query, user_data)
        connection.commit()
        print("User registration successful.")

    except mysql.connector.Error as error:
        print("Failed to register user in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

def delete_user(user_id):
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

        # Check if the user exists
        check_user_query = "SELECT * FROM client WHERE user_id = %s"
        cursor.execute(check_user_query, (user_id,))
        existing_user = cursor.fetchone()
        if not existing_user:
            print("User does not exist in the database.")
            return

        # Delete the user from the client table
        delete_user_query = "DELETE FROM client WHERE user_id = %s"
        cursor.execute(delete_user_query, (user_id,))
        connection.commit()
        print("User deletion successful.")

    except mysql.connector.Error as error:
        print("Failed to delete user from MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function to register a user
register_client()

# Call the function to delete a user
user_id_to_delete = input("Enter the user ID to delete: ")
delete_user(user_id_to_delete)
