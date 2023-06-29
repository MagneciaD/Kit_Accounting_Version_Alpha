import tkinter as tk
from tkinter import messagebox
from tkinter import font


login_window = tk.Tk()
login_window.geometry('925x500+350+100')
login_window.configure(bg='#0d0828')
login_window.title("Login")


def validate_login(username, password):

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
        login_window.destroy()
        import home
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register_button_clicked():
    # Close the login window
    # login_window.destroy()
    import register

def on_entry_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, "end")
        username_entry.config(fg="black")

def entry_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(fg="black")

def here():
    messagebox.showinfo("OTP has been send to your email!")

def open_landing():
    landing_window = tk.Toplevel(login_window)
    landing_window.title("Landing Page")

    logout_button = tk.Button(landing_window, text="Logout", command=close_windows)
    logout_button.pack()


def close_windows():
    login_window.destroy()


# ============================ login content ==========================================================================

username_entry = tk.Entry(login_window)
username_entry.pack()
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_entry_click)
username_entry.place(x=400, y=150)

password_entry = tk.Entry(login_window)
password_entry.pack()
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", entry_click)
password_entry.place(x=400, y=200)

custom_font = ("Cambria", 12)
here_label = tk.Label(login_window, text="Forgot Password, click ", fg='white', bg='#0d0828', font=custom_font)
here_label.pack()
here_label.place(x=350, y=250)

here_button = tk.Button(login_window, text="here", command=here, fg='blue', bg='#0d0828', font=custom_font)
here_button.pack()
here_button.place(x=510, y=250)
custom_font = ("Cambria", 12)


register_button = tk.Button(login_window, text="Register", command=register_button_clicked)
register_button.pack()
register_button.place(x=430, y=327)

login_button = tk.Button(login_window, text="Login",
                         command=lambda: validate_login(username_entry.get(), password_entry.get()))
login_button.pack()
login_button.place(x=430, y=300)

login_window.protocol("WM_DELETE_WINDOW", close_windows)
login_window.mainloop()