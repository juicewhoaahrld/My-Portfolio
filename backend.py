import os
import tkinter as tk
from tkinter import messagebox


WIDTH = 1285
HEIGHT = 800
ACCOUNTS_FILE = "accounts.txt"

BACKGROUND_IMAGE_PATH = "background.jpg"

root = tk.Tk()
root.title("Login and Register")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)


def set_background():
    """Loads, resizes, and displays a background image on the Canvas."""
    global bg_image  

    if os.path.exists(BACKGROUND_IMAGE_PATH):
        try:
            
            raw_img = Image.open(BACKGROUND_IMAGE_PATH)
            resized_img = raw_img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
            bg_image = ImageTk.PhotoImage(resized_img)

            canvas.create_image(0, 0, image=bg_image, anchor="nw")
        except Exception as e:
            print(f"Error loading background image: {e}")
            canvas.config(bg="#87CEEB")
    else:
       
        canvas.config(bg="#87CEEB")


set_background()



def load_accounts():
    """Reads all accounts from accounts.txt into a list of dicts."""
    accounts = []
    if not os.path.exists(ACCOUNTS_FILE):
        return accounts

    with open(ACCOUNTS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 6:
                    accounts.append({
                        "username": parts[0],
                        "password": parts[1],
                        "first_name": parts[2],
                        "last_name": parts[3],
                        "age": parts[4],
                        "email": parts[5]
                    })
    return accounts


def save_account(username, password, first_name, last_name, age, email):
    """Appends a new user account to accounts.txt."""
    with open(ACCOUNTS_FILE, "a") as f:
        f.write(f"{username},{password},{first_name},{last_name},{age},{email}\n")


# Event Handlers
def register_user():
    fields = [
        (first_name_entry, "Enter First Name"),
        (last_name_entry, "Enter Last Name"),
        (age_entry, "Enter Age"),
        (email_entry, "Enter Email"),
        (username_entry, "Enter Username"),
        (password_entry, "Enter Password")
    ]

    values = {}
    for entry, placeholder in fields:
        val = entry.get().strip()
        if val == "" or val == placeholder:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return
        values[placeholder] = val

    username = values["Enter Username"]
    email = values["Enter Email"]

    
    accounts = load_accounts()
    for acc in accounts:
        if acc["username"].lower() == username.lower():
            messagebox.showerror("Error", "Username already exists. Please pick another.")
            return
        if acc["email"].lower() == email.lower():
            messagebox.showerror("Error", "An account with this email already exists.")
            return

    save_account(
        username,
        values["Enter Password"],
        values["Enter First Name"],
        values["Enter Last Name"],
        values["Enter Age"],
        email
    )

    messagebox.showinfo("Success", "Account created successfully!")
    show_login()


def login_user():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username in ("", "Enter Username") or password in ("", "Enter Password"):
        messagebox.showwarning("Missing Information", "Please enter your username and password.")
        return

    accounts = load_accounts()
    for acc in accounts:
        if acc["username"] == username and acc["password"] == password:
            show_dashboard(acc["first_name"])
            return

    messagebox.showerror("Login Failed", "Invalid username or password.")


def recover_password():
    email = email_entry.get().strip()

    if email in ("", "Enter Email"):
        messagebox.showwarning("Missing Information", "Please enter your registered email address.")
        return

    accounts = load_accounts()
    for acc in accounts:
        if acc["email"].lower() == email.lower():
            messagebox.showinfo(
                "Password Recovery",
                f"Account Found!\n\nUsername: {acc['username']}\nPassword: {acc['password']}"
            )
            show_login()
            return

    messagebox.showerror("Not Found", "No account found with that email address.")



def clear_placeholder(entry, placeholder, is_password=False):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="#333333")
        if is_password:
            entry.config(show="*")


def restore_placeholder(entry, placeholder, is_password=False):
    if entry.get() == "":
        if is_password:
            entry.config(show="")
        entry.insert(0, placeholder)
        entry.config(fg="#a5aab1")


def clear_form():
    for widget in card.winfo_children():
        widget.destroy()


def create_input_field(parent, label_text, placeholder, is_password=False):
    label = tk.Label(
        parent,
        text=label_text,
        font=("Arial", 8),
        bg="white",
        fg="#344054",
        anchor="w"
    )
    label.pack(fill="x", padx=30)

    entry = tk.Entry(
        parent,
        font=("Arial", 9),
        bg="white",
        fg="#a5aab1",
        relief="solid",
        bd=1
    )
    entry.pack(fill="x", padx=30, ipady=5, pady=(2, 8))
    entry.insert(0, placeholder)

    entry.bind("<FocusIn>", lambda e: clear_placeholder(entry, placeholder, is_password))
    entry.bind("<FocusOut>", lambda e: restore_placeholder(entry, placeholder, is_password))

    return entry



def show_dashboard(first_name):
    clear_form()
    card.config(height=280)

    welcome_label = tk.Label(
        card,
        text=f"Welcome {first_name}",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#172333"
    )
    welcome_label.pack(pady=(45, 5))

    subtext = tk.Label(
        card,
        text="You have successfully logged in to your account.",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    subtext.pack(pady=(0, 30))

    logout_button = tk.Button(
        card,
        text="Log Out",
        font=("Arial", 9, "bold"),
        bg="#e63946",
        fg="white",
        activebackground="#c52838",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=show_login
    )
    logout_button.pack(fill="x", padx=40, ipady=8)


def show_register():
    clear_form()
    card.config(height=520)

    title = tk.Label(
        card,
        text="Create Account",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#172333"
    )
    title.pack(pady=(15, 2))

    subtitle = tk.Label(
        card,
        text="Fill in your details to get started",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    subtitle.pack(pady=(0, 10))

    global first_name_entry, last_name_entry, age_entry, email_entry, username_entry, password_entry

    first_name_entry = create_input_field(card, "First Name", "Enter First Name")
    last_name_entry = create_input_field(card, "Last Name", "Enter Last Name")
    age_entry = create_input_field(card, "Age", "Enter Age")
    email_entry = create_input_field(card, "Email", "Enter Email")
    username_entry = create_input_field(card, "Username", "Enter Username")
    password_entry = create_input_field(card, "Password", "Enter Password", is_password=True)

    register_button = tk.Button(
        card,
        text="Register",
        font=("Arial", 9, "bold"),
        bg="#4b3cff",
        fg="white",
        activebackground="#3929e8",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=register_user
    )
    register_button.pack(fill="x", padx=30, ipady=6, pady=(5, 0))

    bottom_frame = tk.Frame(card, bg="white")
    bottom_frame.pack(pady=(8, 0))

    text = tk.Label(
        bottom_frame,
        text="Already have an account?",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    text.pack(side="left")

    login_button = tk.Button(
        bottom_frame,
        text="Login",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="#3425d5",
        activeforeground="#3425d5",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=show_login
    )
    login_button.pack(side="left", padx=2)


def show_login():
    clear_form()
    card.config(height=350)

    title = tk.Label(
        card,
        text="Welcome Back",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#172333"
    )
    title.pack(pady=(20, 2))

    subtitle = tk.Label(
        card,
        text="Sign in to continue",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    subtitle.pack(pady=(0, 15))

    global username_entry, password_entry

    username_entry = create_input_field(card, "Username", "Enter Username")
    password_entry = create_input_field(card, "Password", "Enter Password", is_password=True)

    forgot_btn = tk.Button(
        card,
        text="Forgot Password?",
        font=("Arial", 8),
        bg="white",
        fg="#3425d5",
        activeforeground="#3425d5",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=show_forgot_password
    )
    forgot_btn.pack(anchor="e", padx=30, pady=(0, 10))

    login_button = tk.Button(
        card,
        text="Login",
        font=("Arial", 9, "bold"),
        bg="#4b3cff",
        fg="white",
        activebackground="#3929e8",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=login_user
    )
    login_button.pack(fill="x", padx=30, ipady=6)

    bottom_frame = tk.Frame(card, bg="white")
    bottom_frame.pack(pady=(12, 0))

    text = tk.Label(
        bottom_frame,
        text="Don't have an account?",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    text.pack(side="left")

    register_button = tk.Button(
        bottom_frame,
        text="Register",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="#3425d5",
        activeforeground="#3425d5",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=show_register
    )
    register_button.pack(side="left", padx=2)


def show_forgot_password():
    clear_form()
    card.config(height=300)

    title = tk.Label(
        card,
        text="Reset Password",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#172333"
    )
    title.pack(pady=(25, 2))

    subtitle = tk.Label(
        card,
        text="Enter your email to recover password",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )
    subtitle.pack(pady=(0, 20))

    global email_entry
    email_entry = create_input_field(card, "Registered Email", "Enter Email")

    submit_button = tk.Button(
        card,
        text="Recover Password",
        font=("Arial", 9, "bold"),
        bg="#4b3cff",
        fg="white",
        activebackground="#3929e8",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=recover_password
    )
    submit_button.pack(fill="x", padx=30, ipady=6, pady=(10, 0))

    bottom_frame = tk.Frame(card, bg="white")
    bottom_frame.pack(pady=(15, 0))

    back_button = tk.Button(
        bottom_frame,
        text="Back to Login",
        font=("Arial", 9, "bold"),
        bg="white",
        fg="#3425d5",
        activeforeground="#3425d5",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=show_login
    )
    back_button.pack()



card = tk.Frame(
    root,
    width=340,
    height=520,
    bg="white"
)
card.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)
card.pack_propagate(False)

show_register()

root.mainloop()