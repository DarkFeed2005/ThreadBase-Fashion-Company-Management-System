import customtkinter as ctk
from views.auth.login import LoginPage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FashionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fashion Management System")
        self.geometry("1200x700")
        self.resizable(False, False)
        
        # Container for all frames
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        self.show_login()
    
    def show_login(self):
        from views.auth.login import LoginPage
        self.frames = {}
        frame = LoginPage(self.container, self)
        self.frames[LoginPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__ == "__main__":
    app = FashionApp()
    app.mainloop()