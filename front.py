import tkinter as tk
from tkinter import messagebox

WIDTH = 1285
HEIGHT = 800

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


def create_gradient():
    # Top color
    top_r, top_g, top_b = 250, 250, 255

    # Bottom color
    bottom_r, bottom_g, bottom_b = 135, 190, 235

    for y in range(HEIGHT):

        ratio = y / HEIGHT

        r = int(top_r + (bottom_r - top_r) * ratio)
        g = int(top_g + (bottom_g - top_g) * ratio)
        b = int(top_b + (bottom_b - top_b) * ratio)

        color = f"#{r:02x}{g:02x}{b:02x}"

        canvas.create_line(
            0,
            y,
            WIDTH,
            y,
            fill=color
        )


create_gradient()


def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter your username and password."
        )
        return

    messagebox.showinfo(
        "Success",
        "Account created successfully!"
    )


def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter your username and password."
        )
        return

    messagebox.showinfo(
        "Login",
        "Login successful!"
    )


def clear_form():
    for widget in card.winfo_children():
        widget.destroy()


def show_register():

    clear_form()


    title = tk.Label(
        card,
        text="Create Account",
        font=("Arial", 23, "bold"),
        bg="white",
        fg="#172333"
    )

    title.pack(pady=(25, 2))

    subtitle = tk.Label(
        card,
        text="Sign in to continue",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )

    subtitle.pack(pady=(0, 20))



    username_label = tk.Label(
        card,
        text="Username",
        font=("Arial", 9),
        bg="white",
        fg="#344054",
        anchor="w"
    )

    username_label.pack(
        fill="x",
        padx=30
    )


    global username_entry

    username_entry = tk.Entry(
        card,
        font=("Arial", 9),
        bg="white",
        fg="#333333",
        relief="solid",
        bd=1
    )

    username_entry.pack(
        fill="x",
        padx=30,
        ipady=8,
        pady=(3, 12)
    )

    username_entry.insert(
        0,
        "Enter Username"
    )

    username_entry.config(
        fg="#a5aab1"
    )

    username_entry.bind(
        "<FocusIn>",
        lambda event: clear_placeholder(
            username_entry,
            "Enter Username"
        )
    )

    username_entry.bind(
        "<FocusOut>",
        lambda event: restore_placeholder(
            username_entry,
            "Enter Username"
        )
    )




    password_label = tk.Label(
        card,
        text="Password",
        font=("Arial", 9),
        bg="white",
        fg="#344054",
        anchor="w"
    )

    password_label.pack(
        fill="x",
        padx=30
    )



    global password_entry

    password_entry = tk.Entry(
        card,
        font=("Arial", 9),
        bg="white",
        fg="#333333",
        relief="solid",
        bd=1
    )

    password_entry.pack(
        fill="x",
        padx=30,
        ipady=8,
        pady=(3, 15)
    )

    password_entry.insert(
        0,
        "Enter Password"
    )

    password_entry.config(
        fg="#a5aab1"
    )

    password_entry.bind(
        "<FocusIn>",
        lambda event: clear_placeholder(
            password_entry,
            "Enter Password"
        )
    )

    password_entry.bind(
        "<FocusOut>",
        lambda event: restore_placeholder(
            password_entry,
            "Enter Password"
        )
    )


    

    register_button = tk.Button(
        card,
        text="Register",
        font=("Arial", 9),
        bg="#4b3cff",
        fg="white",
        activebackground="#3929e8",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=register_user
    )

    register_button.pack(
        fill="x",
        padx=30,
        ipady=8
    )


 

    bottom_frame = tk.Frame(
        card,
        bg="white"
    )

    bottom_frame.pack(
        pady=(13, 0)
    )


    text = tk.Label(
        bottom_frame,
        text="Already have an account?",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )

    text.pack(
        side="left"
    )


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

    login_button.pack(
        side="left",
        padx=2
    )




def show_login():

    clear_form()

  

    title = tk.Label(
        card,
        text="Welcome Back",
        font=("Arial", 23, "bold"),
        bg="white",
        fg="#172333"
    )

    title.pack(pady=(25, 2))


    

    subtitle = tk.Label(
        card,
        text="Sign in to continue",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )

    subtitle.pack(pady=(0, 20))


   

    username_label = tk.Label(
        card,
        text="Username",
        font=("Arial", 9),
        bg="white",
        fg="#344054",
        anchor="w"
    )

    username_label.pack(
        fill="x",
        padx=30
    )


    global username_entry

    username_entry = tk.Entry(
        card,
        font=("Arial", 9),
        bg="white",
        fg="#333333",
        relief="solid",
        bd=1
    )

    username_entry.pack(
        fill="x",
        padx=30,
        ipady=8,
        pady=(3, 12)
    )

    username_entry.insert(
        0,
        "Enter Username"
    )

    username_entry.config(
        fg="#a5aab1"
    )

    username_entry.bind(
        "<FocusIn>",
        lambda event: clear_placeholder(
            username_entry,
            "Enter Username"
        )
    )

    username_entry.bind(
        "<FocusOut>",
        lambda event: restore_placeholder(
            username_entry,
            "Enter Username"
        )
    )


    password_label = tk.Label(
        card,
        text="Password",
        font=("Arial", 9),
        bg="white",
        fg="#344054",
        anchor="w"
    )

    password_label.pack(
        fill="x",
        padx=30
    )


    global password_entry

    password_entry = tk.Entry(
        card,
        font=("Arial", 9),
        bg="white",
        fg="#333333",
        relief="solid",
        bd=1
    )

    password_entry.pack(
        fill="x",
        padx=30,
        ipady=8,
        pady=(3, 15)
    )

    password_entry.insert(
        0,
        "Enter Password"
    )

    password_entry.config(
        fg="#a5aab1"
    )

    password_entry.bind(
        "<FocusIn>",
        lambda event: clear_placeholder(
            password_entry,
            "Enter Password"
        )
    )

    password_entry.bind(
        "<FocusOut>",
        lambda event: restore_placeholder(
            password_entry,
            "Enter Password"
        )
    )


    login_button = tk.Button(
        card,
        text="Login",
        font=("Arial", 9),
        bg="#4b3cff",
        fg="white",
        activebackground="#3929e8",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=login_user
    )

    login_button.pack(
        fill="x",
        padx=30,
        ipady=8
    )


    bottom_frame = tk.Frame(
        card,
        bg="white"
    )

    bottom_frame.pack(
        pady=(13, 0)
    )

    text = tk.Label(
        bottom_frame,
        text="Don't have an account?",
        font=("Arial", 9),
        bg="white",
        fg="#8a94a3"
    )

    text.pack(
        side="left"
    )

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

    register_button.pack(
        side="left",
        padx=2
    )


def clear_placeholder(entry, placeholder):

    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(
            fg="#333333"
        )

def restore_placeholder(entry, placeholder):

    if entry.get() == "":
        entry.insert(
            0,
            placeholder
        )

        entry.config(
            fg="#a5aab1"
        )

card = tk.Frame(
    root,
    width=325,
    height=350,
    bg="white"
)

card.place(
    relx=0.5,
    rely=0.46,
    anchor="center"
)

card.pack_propagate(False)
show_register()


root.mainloop()
