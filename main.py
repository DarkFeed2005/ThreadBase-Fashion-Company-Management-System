import customtkinter as ctk
from views.auth.login import LoginPage
from views.auth.signup import SignupPage
from views.admin.dashboard import AdminDashboard
from views.designer.dashboard import DesignerDashboard
from views.sales.dashboard import SalesDashboard

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class FashionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fashion Management System")
        self.geometry("1000x700+380+150")
        self.resizable(False, False)

        # Container for frames
        self.container = ctk.CTkFrame(self, fg_color="#FFFFFF")
        self.container.pack(fill="both", expand=True)

        self.show_login()

    # 👤 Auth Screens
    def show_login(self):
        self.clear_frame()
        frame = LoginPage(self.container, self)
        frame.pack(expand=True, fill="both")

    def show_signup(self):
        self.clear_frame()
        frame = SignupPage(self.container, self)
        frame.pack(expand=True, fill="both")

    #  Admin Dashboard
    def show_admin_dashboard(self):
        self.clear_frame()
        frame = AdminDashboard(self.container, self)  
        frame.pack(expand=True, fill="both")

    #  Designer Dashboard
    def show_designer_dashboard(self, username):
        self.clear_frame()
        frame = DesignerDashboard(self.container, self, username)
        frame.pack(expand=True, fill="both")

    #  Sales Dashboard
    def show_sales_dashboard(self, username):
        self.clear_frame()
        frame = SalesDashboard(self.container, self, username)
        frame.pack(expand=True, fill="both")

    #  Utility
    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = FashionApp()
    app.mainloop()