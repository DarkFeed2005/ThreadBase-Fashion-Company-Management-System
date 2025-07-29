import customtkinter as ctk
from tkinter import ttk
from utils.styles import *
from database.db_operations import get_all_users, delete_user

class UsersPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=BG_COLOR)
        self.controller = controller
        
        # Header
        header = ctk.CTkFrame(self, fg_color=PRIMARY_COLOR, height=60)
        header.pack(fill="x", padx=20, pady=20)
        
        title = ctk.CTkLabel(
            header,
            text="Manage Users",
            font=TITLE_FONT,
            text_color="white"
        )
        title.pack(side="left", padx=30)
        
        back_btn = ctk.CTkButton(
            header,
            text="Back",
            width=100,
            height=35,
            font=BUTTON_FONT_SMALL,
            command=lambda: controller.show_admin_dashboard()
        )
        back_btn.pack(side="right", padx=20)
        
        # Table Frame
        table_frame = ctk.CTkFrame(self, fg_color=BG_COLOR)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Username", "Name", "Role", "Email", "Contact"),
            show="headings",
            style="Custom.Treeview"
        )
        
        # Configure columns
        columns = {
            "ID": {"width": 50, "anchor": "center"},
            "Username": {"width": 120},
            "Name": {"width": 150},
            "Role": {"width": 100},
            "Email": {"width": 200},
            "Contact": {"width": 120}
        }
        
        for col, config in columns.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, **config)
        
        # Add scrollbars
        y_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        # Action buttons
        btn_frame = ctk.CTkFrame(self, fg_color=BG_COLOR)
        btn_frame.pack(pady=20)
        
        ctk.CTkButton(
            btn_frame,
            text="Add User",
            width=120,
            height=40,
            font=BUTTON_FONT_SMALL,
            command=self.add_user
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame,
            text="Edit User",
            width=120,
            height=40,
            font=BUTTON_FONT_SMALL,
            command=self.edit_user
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame,
            text="Delete User",
            width=120,
            height=40,
            font=BUTTON_FONT_SMALL,
            fg_color="#E74C3C",
            hover_color="#C0392B",
            command=self.delete_user
        ).pack(side="left", padx=10)
        
        # Load data
        self.load_users()
    
    def load_users(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        users = get_all_users()
        for user in users:
            self.tree.insert("", "end", values=(
                user["id"],
                user["username"],
                f"{user['first_name']} {user['last_name']}",
                user["role"],
                user["email"],
                user["contact"]
            ))
    
    def add_user(self):
        from views.auth.signup import SignupPage
        self.controller.show_signup()
    
    def edit_user(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        user_id = self.tree.item(selected[0])["values"][0]
        print(f"Editing user ID: {user_id}")
        # Implement edit functionality
    
    def delete_user(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        user_id = self.tree.item(selected[0])["values"][0]
        if delete_user(user_id):
            self.load_users()