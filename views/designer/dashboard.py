import customtkinter as ctk
from utils.styles import *

class DesignerDashboard(ctk.CTkFrame):
    def __init__(self, parent, controller, username):
        super().__init__(parent, fg_color=BG_COLOR)
        self.controller = controller
        self.username = username
        
        # Header
        header = ctk.CTkFrame(self, fg_color=PRIMARY_COLOR, height=80)
        header.pack(fill="x", padx=20, pady=20)
        
        title = ctk.CTkLabel(
            header,
            text=f"Welcome, {username}",
            font=TITLE_FONT,
            text_color="white"
        )
        title.pack(side="left", padx=30)
        
        # Navigation buttons
        nav_frame = ctk.CTkFrame(self, fg_color=BG_COLOR)
        nav_frame.pack(pady=30)
        
        buttons = [
            ("Add Designs", self.add_designs),
            ("View Designs", self.view_designs),
            ("Logout", self.logout)
        ]
        
        for text, command in buttons:
            btn = ctk.CTkButton(
                nav_frame,
                text=text,
                width=200,
                height=50,
                font=BUTTON_FONT,
                command=command
            )
            btn.pack(pady=15)
    
    def add_designs(self):
        from views.designer.designs import AddDesignPage
        self.controller.show_frame(AddDesignPage, self.username)
    
    def view_designs(self):
        from views.designer.designs import ViewDesignsPage
        self.controller.show_frame(ViewDesignsPage, self.username)
    
    def logout(self):
        self.controller.show_login()