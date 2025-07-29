import customtkinter as ctk
from utils.styles import *

class AdminDashboard(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=BG_COLOR)
        self.controller = controller
        self.nav_buttons = {}

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header Bar
        header = ctk.CTkFrame(self, fg_color=PRIMARY_COLOR, height=60)
        header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        title = ctk.CTkLabel(
            header,
            text="🧶 ThreadBase Admin Dashboard",
            font=TITLE_FONT,
            text_color="white"
        )
        title.pack(side="left", padx=30)

        # Sidebar Navigation
        sidebar = ctk.CTkFrame(self, fg_color=CARD_COLOR, width=180)
        sidebar.grid(row=1, column=0, sticky="ns", padx=(10, 5), pady=(0, 10))

        nav_items = [
            ("Dashboard", self.show_stats),
            ("Manage Users", self.show_users),
            ("Manage Designs", self.show_designs),
            ("View Sales", self.show_sales),
            ("Logout", self.logout)
        ]

        for label, command in nav_items:
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                width=160,
                font=BUTTON_FONT,
                fg_color="transparent",
                hover_color=SECONDARY_COLOR,
                command=lambda l=label, c=command: self.activate_nav(l, c)
            )
            btn.pack(pady=8)
            self.nav_buttons[label] = btn

        # Main Content Area
        self.main_content = ctk.CTkFrame(self, fg_color=BG_COLOR)
        self.main_content.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=(0, 10))

        self.activate_nav("Dashboard", self.show_stats)  # Fixed default nav

    def activate_nav(self, label, callback):
        for name, btn in self.nav_buttons.items():
            btn.configure(fg_color="transparent", text_color="black")
        if label in self.nav_buttons:
            self.nav_buttons[label].configure(fg_color=PRIMARY_COLOR, text_color="white")
        self.clear_main()
        callback()

    def clear_main(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_stats(self):
        stats = {
            "👥 Total Users": "72",
            "🎨 Total Designs": "134",
            "💰 Total Sales": "Rs. 1,250,000",
            "⏳ Pending Payments": "Rs. 225,000"
        }

        stats_frame = ctk.CTkFrame(self.main_content, fg_color=BG_COLOR)
        stats_frame.pack(pady=20, padx=20, fill="both", expand=True)

        for label, value in stats.items():
            card = ctk.CTkFrame(stats_frame, fg_color=CARD_COLOR)
            card.pack(pady=10, padx=10, fill="x")

            ctk.CTkLabel(card, text=label, font=LABEL_FONT).pack(anchor="w", padx=20, pady=5)
            ctk.CTkLabel(card, text=value, font=("Helvetica Neue", 20, "bold"), text_color=PRIMARY_COLOR).pack(anchor="w", padx=20)

    def show_users(self):
        from views.admin.users import UsersPage
        self.controller.show_frame(UsersPage)

    def show_designs(self):
        from views.admin.designs import DesignsPage
        self.controller.show_frame(DesignsPage)

    def show_sales(self):
        from views.sales.sales import SalesPage
        self.controller.show_frame(SalesPage)

    def logout(self):
        confirm = ctk.CTkToplevel(self)
        confirm.title("Confirm Logout")
        confirm.geometry("300x150")
        confirm.transient(self)
        confirm.grab_set()

        ctk.CTkLabel(confirm, text="Are you sure you want to logout?", font=LABEL_FONT).pack(pady=20)

        button_frame = ctk.CTkFrame(confirm)
        button_frame.pack(pady=10)

        # Yes → go to login screen
        ctk.CTkButton(
            button_frame,
            text="Yes",
            command=lambda: [confirm.destroy(), self.controller.show_login()]
        ).pack(side="left", padx=20)

        # Cancel
        ctk.CTkButton(button_frame, text="Cancel", command=confirm.destroy).pack(side="right", padx=20)