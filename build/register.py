from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\1_MINIPROJECT\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# --- Validation Function ---
def validate_register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Input Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
    else:
        messagebox.showinfo("Success", f"Account created for {username}!")


window = Tk()
window.geometry("1440x1024")
window.configure(bg="#3E2723")
window.title("Register")

canvas = Canvas(
    window,
    bg="#3E2723",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# --- Center Light Box ---
canvas.create_rectangle(
    500, 200, 940, 700,
    fill="#F3EFEF",
    outline=""
)

# --- Header Text ---
canvas.create_text(
    720, 230,
    text="Create an account",
    fill="#000000",
    font=("Poppins", 24, "bold"),
    anchor="center"
)

# --- Labels ---
canvas.create_text(
    550, 300,
    anchor="w",
    text="Enter your Username",
    fill="#666666",
    font=("Poppins", 14)
)

canvas.create_text(
    550, 390,
    anchor="w",
    text="Enter your Password",
    fill="#666666",
    font=("Poppins", 14)
)

canvas.create_text(
    550, 480,
    anchor="w",
    text="Confirm your Password",
    fill="#666666",
    font=("Poppins", 14)
)

# --- Entry Fields ---
username_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    font=("Poppins", 12),
    relief="flat"
)
username_entry.place(x=550, y=330, width=340, height=35)

password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    font=("Poppins", 12),
    relief="flat",
    show='*'
)
password_entry.place(x=550, y=420, width=340, height=35)

confirm_password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    font=("Poppins", 12),
    relief="flat",
    show='*'
)
confirm_password_entry.place(x=550, y=510, width=340, height=35)

# --- Register Button ---
register_button = Button(
    text="Register",
    font=("Poppins", 12, "bold"),
    bg="#3E2723",  # Dark brown
    fg="#FFFFFF",
    activebackground="#5D4037",
    activeforeground="#FFFFFF",
    relief="flat",
    command=validate_register
)
register_button.place(x=650, y=580, width=120, height=40)

window.resizable(False, False)
window.mainloop()
