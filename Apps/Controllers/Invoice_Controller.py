import mysql.connector


def generate_invoice(invoice_number, invoice_date, customer_name, items):
    invoice = f"===================\n"
    invoice += f"     INVOICE\n"
    invoice += f"===================\n"
    invoice += f"Invoice Number: {invoice_number}\n"
    invoice += f"Date: {invoice_date}\n"
    invoice += f"Customer: {customer_name}\n"
    invoice += f"-------------------\n"
    invoice += f"    DESCRIPTION     |  AMOUNT\n"
    invoice += f"-------------------\n"

    total_amount = 0

    for item in items:
        description = item["description"]
        amount = item["amount"]
        invoice += f"{description:20} |  {amount:.2f}\n"
        total_amount += amount

    invoice += f"-------------------\n"
    invoice += f"TOTAL:              |  {total_amount:.2f}\n"
    invoice += f"===================\n"

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

        # Insert the invoice data into the items table
        insert_query = '''
        INSERT INTO items (user_id, name, price, qty, subtotal, qi_id, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, NOW())
        '''

        user_id = 1  # Assuming a specific user ID for the invoice
        for item in items:
            name = item["description"]
            price = item["amount"]
            qty = 1  # Assuming quantity is always 1
            subtotal = price
            qi_id = 1  # Assuming a specific invoice ID for the invoice item

            item_data = (user_id, name, price, qty, subtotal, qi_id)
            cursor.execute(insert_query, item_data)

        # Commit the changes
        connection.commit()
        print("Invoice data has been inserted into the 'items' table successfully.")

    except mysql.connector.Error as error:
        print("Failed to insert invoice data into the 'items' table in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

    return invoice


# Example usage
invoice_number = "INV-001"
invoice_date = "2023-06-23"
customer_name = "John Doe"
items = [
    {"description": "Item 1", "amount": 10.99},
    {"description": "Item 2", "amount": 5.99},
    {"description": "Item 3", "amount": 2.50},
]

invoice = generate_invoice(invoice_number, invoice_date, customer_name, items)
print(invoice)
