import tkinter as tk
import mysql.connector
from tkinter import messagebox


def register():
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

        # Get the values from the entry fields
        company_name = companyName_entry.get()
        physical_address = companyAddress_entry.get()
        phone_no = phoneNumber_entry.get()
        email = emailAddress_entry.get()
        website = link_entry.get()
        password = password_entry.get()
        confirm_password = confPassword_entry.get()

        if not company_name:
            messagebox.showerror("Error", "Please enter the company name")
            return
        if not physical_address:
            messagebox.showerror("Error", "Please enter the company address")
            return
        if not phone_no:
            messagebox.showerror("Error", "Please enter the phone number")
            return
        if not email:
            messagebox.showerror("Error", "Please enter the email address")
            return
        if not password:
            messagebox.showerror("Error", "Please enter the password")
            return
        if not confirm_password:
            messagebox.showerror("Error", "Please confirm the password")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Validate the phone number
        if not phone_no.isdigit() or len(phone_no) != 10:
            messagebox.showerror("Error", "Invalid phone number. Please enter a 10-digit number.")
            return

        # Check if the organization already exists
        check_organization_query = "SELECT * FROM organization WHERE email_address = %s AND company_name = %s"
        cursor.execute(check_organization_query, (email, company_name))
        existing_organization = cursor.fetchone()
        if existing_organization:
            messagebox.showerror("Error", "Company already exists.")
            return

        # Insert the user into the organization table
        insert_organization_query = "INSERT INTO organization (company_name, email_address, phone_no, website, physical_address, password, confirm_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        organization_data = (company_name, email, phone_no, website, physical_address, password, confirm_password)
        cursor.execute(insert_organization_query, organization_data)
        connection.commit()
        print("Company registration successful.")

    except mysql.connector.Error as error:
        print("Failed to register.py Company in MySQL: {}".format(error))

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")


register_window = tk.Tk()
register_window.geometry('600x450+350+100')
register_window.configure(bg='#0d0828')
register_window.title("register")

# Register content

companyName_label = tk.Label(register_window, text="Company Name:", font=('bold', 10), fg="white", bg="#0d0828")
companyName_label.pack()
companyName_label.place(x=90, y=70)

companyName_entry = tk.Entry(register_window)
companyName_entry.pack()
companyName_entry.place(x=90, y=95)

companyAddress_label = tk.Label(register_window, text="Company Address:", font=('bold', 10), fg="white", bg="#0d0828")
companyAddress_label.pack()
companyAddress_label.place(x=250, y=70)

companyAddress_entry = tk.Entry(register_window)
companyAddress_entry.pack()
companyAddress_entry.place(x=250, y=95)

phoneNumber_label = tk.Label(register_window, text="Phone Number:", font=('bold', 10), fg="white", bg="#0d0828")
phoneNumber_label.pack()
phoneNumber_label.place(x=90, y=130)

phoneNumber_entry = tk.Entry(register_window)
phoneNumber_entry.pack()
phoneNumber_entry.place(x=90, y=155)

emailAddress_label = tk.Label(register_window, text="Email Address:", font=('bold', 10), fg="white", bg="#0d0828")
emailAddress_label.pack()
emailAddress_label.place(x=250, y=130)

emailAddress_entry = tk.Entry(register_window)
emailAddress_entry.pack()
emailAddress_entry.place(x=250, y=155)

link_label = tk.Label(register_window, text="Website Link(optional):", font=('bold', 10), fg="white", bg="#0d0828")
link_label.pack()
link_label.place(x=90, y=190)

link_entry = tk.Entry(register_window)
link_entry.pack()
link_entry.place(x=90, y=215)

password_label = tk.Label(register_window, text="Password:", font=('bold', 10), fg="white", bg="#0d0828")
password_label.pack()
password_label.place(x=90, y=250)

password_entry = tk.Entry(register_window, show="*")
password_entry.pack()
password_entry.place(x=90, y=275)

confPassword_label = tk.Label(register_window, text="Confirm Password:", font=('bold', 10), fg="white", bg="#0d0828")
confPassword_label.pack()
confPassword_label.place(x=250, y=250)

confPassword_entry = tk.Entry(register_window, show="*")
confPassword_entry.pack()
confPassword_entry.place(x=250, y=275)

register_button = tk.Button(register_window, text="register", command=register)
register_button.pack()
register_button.place(x=200, y=350)

register_window.mainloop()