import tkinter as tk
from tkinter import PhotoImage

class CoffeeShopUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Management UI")
        self.root.geometry("1100x720")
        self.root.configure(bg="#F8F4B4")
        
        self.load_images()
        self.create_navbar()
        self.create_header()
        self.create_categories()
        self.create_reviews()
        self.create_footer()

    def load_images(self):
        """Load image assets (replace with your actual paths)"""
        try:
            self.nav_images = {
                "home": PhotoImage(file="images/home.png"),
                "orders": PhotoImage(file="images/orders.png"),
                "menu": PhotoImage(file="images/menu.png"),
                "logout": PhotoImage(file="images/logout.png")
            }
            self.category_images = {
                "bestseller": PhotoImage(file="images/bestseller.png"),
                "drinks": PhotoImage(file="images/drinks.png"),
                "food": PhotoImage(file="images/food.png")
            }
        except Exception as e:
            print("Image loading error:", e)
            self.use_images = False
        else:
            self.use_images = True

    def create_navbar(self):
        navbar = tk.Frame(self.root, bg="#442A20", height=50)
        navbar.pack(fill="x")
        
        # Left-aligned buttons
        for key in ["home", "orders", "menu"]:
            if self.use_images:
                btn = tk.Button(navbar, image=self.nav_images[key], bg="#442A20", relief="flat")
            else:
                btn = tk.Button(navbar, text=key.capitalize(), fg="white", bg="#442A20", relief="flat")
            btn.pack(side="left", padx=10)
        
        # Right-aligned logout
        if self.use_images:
            btn = tk.Button(navbar, image=self.nav_images["logout"], bg="#442A20", relief="flat")
        else:
            btn = tk.Button(navbar, text="Logout", fg="white", bg="#442A20", relief="flat")
        btn.pack(side="right", padx=10)

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#F8F4B4")
        header_frame.pack(pady=(30, 10))
        tk.Label(header_frame, 
                text="Handcrafted Curations", 
                font=("Helvetica", 22, "bold"), 
                bg="#F8F4B4", 
                fg="#442A20").pack()

    def create_categories(self):
        cat_frame = tk.Frame(self.root, bg="#F8F4B4")
        cat_frame.pack(pady=20)
        
        for key, text in zip(["bestseller", "drinks", "food"], 
                           ["Bestseller", "Drinks", "Food"]):
            frame = tk.Frame(cat_frame, bg="#F8F4B4")
            if self.use_images:
                tk.Label(frame, image=self.category_images[key], bg="#F8F4B4").pack()
            else:
                tk.Label(frame, text=text, font=("Arial", 12, "bold"), bg="#F8F4B4").pack()
            frame.pack(side="left", padx=40)

    def create_reviews(self):
        review_frame = tk.Frame(self.root, bg="#F8F4B4")
        review_frame.pack(pady=20)
        
        reviews = [
            ("JD John D", "Amazing! Exceeded expectations.", "Feb 18, 2025"),
            ("JS Jordan S", "Exceeded my expectations", "Feb 21, 2025"),
            ("EE Emily E", "Okay, but not great.", "Feb 28, 2025")
        ]
        
        for name, comment, date in reviews:
            card = tk.Frame(review_frame, bg="white", padx=20, pady=10, relief="groove")
            tk.Label(card, text=name, font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
            tk.Label(card, text=f'"{comment}"', wraplength=250, justify="left", bg="white").pack(anchor="w")
            tk.Label(card, text=date, fg="#666666", bg="white").pack(anchor="w")
            card.pack(side="left", padx=20, ipady=5)

    def create_footer(self):
        footer = tk.Frame(self.root, bg="#442A20", height=40)
        footer.pack(fill="x", side="bottom", pady=(20, 0))
        footer_text = "Letters & Lattes | Privacy Policy | Terms | Contact Us"
        tk.Label(footer, 
                text=footer_text, 
                fg="white", 
                bg="#442A20", 
                font=("Arial", 10)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeShopUI(root)
    root.mainloop()