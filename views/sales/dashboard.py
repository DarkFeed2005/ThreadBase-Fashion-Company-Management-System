import customtkinter as ctk
from utils.styles import *

class SalesDashboard(ctk.CTkFrame):
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
            ("Add Sales", self.add_sales),
            ("View Sales", self.view_sales),
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
    
    def add_sales(self):
        from views.sales.sales import AddSalesPage
        self.controller.show_frame(AddSalesPage, self.username)
    
    def view_sales(self):
        from views.sales.sales import SalesPage
        self.controller.show_frame(SalesPage, self.username)
    
    def logout(self):
        self.controller.show_login()