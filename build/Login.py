from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
import subprocess  # Added to open registration window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Python Miniproject\build\assets\frame0")  # Your assets path

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# ---------------- WINDOW SETTINGS ----------------
window = Tk()
window.geometry("411x350")  # Slightly increased height for link space
window.configure(bg="#F2F2F2")
window.title("Login Page")
window.resizable(True, True)  # Allow resizing

canvas = Canvas(
    window,
    bg="#F2F2F2",
    height=350,
    width=411,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.pack(fill="both", expand=True)

# ---------------- LOGO ICON ----------------
logo_image = PhotoImage(file=relative_to_assets("image_1.png"))  # Replace with your logo image
canvas.create_image(
    50, 50,
    image=logo_image
)

# ---------------- LOGIN TITLE ----------------
canvas.create_text(
    90,
    38,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Poppins Bold", 20)
)

# ---------------- EMAIL LABEL ----------------
canvas.create_text(
    50,
    90,
    anchor="nw",
    text="Enter your Email",
    fill="#555555",
    font=("Poppins", 12)
)

# ---------------- EMAIL ENTRY ----------------
entry_email = Entry(
    bd=1,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=1,
    relief="solid"
)
entry_email.place(
    x=50,
    y=115,
    width=310,
    height=30
)

# ---------------- PASSWORD LABEL ----------------
canvas.create_text(
    50,
    160,
    anchor="nw",
    text="Enter your Password",
    fill="#555555",
    font=("Poppins", 12)
)

# ---------------- PASSWORD ENTRY ----------------
entry_pass = Entry(
    bd=1,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=1,
    relief="solid",
    show="*"
)
entry_pass.place(
    x=50,
    y=185,
    width=310,
    height=30
)

# ---------------- LOGIN BUTTON ----------------
def login_action():
    email = entry_email.get().strip()
    password = entry_pass.get().strip()
    if not email or not password:
        messagebox.showwarning("Input Error", "Please fill in both Email and Password.")
        return
    print(f"Email: {email}, Password: {password}")

login_btn = Button(
    text="Login",
    bg="#5B3A29",
    fg="#FFFFFF",
    font=("Poppins", 12, "bold"),
    relief="flat",
    command=login_action
)
login_btn.place(
    x=50,
    y=230,
    width=310,
    height=35
)

# ---------------- CREATE ACCOUNT LINK ----------------
def create_account():
    window.destroy()  # Close the login window
    subprocess.run(["python", "register.py"])  # Open registration form (make sure register.py exists)

link_label = Label(
    window,
    text="Don't have an account? Create one",
    fg="#5B3A29",
    bg="#F2F2F2",
    cursor="hand2",
    font=("Poppins", 10, "underline")
)
link_label.place(
    x=90,
    y=280
)
link_label.bind("<Button-1>", lambda e: create_account())  # Clickable link

# ---------------- CENTER WINDOW ----------------
window.eval('tk::PlaceWindow . center')

window.mainloop()
