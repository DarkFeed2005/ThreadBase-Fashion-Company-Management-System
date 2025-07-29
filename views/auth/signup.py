from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkRadioButton, StringVar
from CTkMessagebox import CTkMessagebox
from utils.styles import *
from database.db_operations import add_user

class SignupPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=1000, height=700)
        self.grid_columnconfigure(0, weight=1)

        # Main Container Frame
        self.container = CTkFrame(self, width=800, height=620, fg_color="white")
        self.container.pack_propagate(False)
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        CTkLabel(self.container, text="Create Account", font=("Arial Bold", 28), text_color="#601E88").pack(pady=(30, 10))

        # Form Section
        self.form_frame = CTkFrame(self.container, fg_color="white")
        self.form_frame.pack(pady=10)

        fields = [
            ("First Name", "first_name"),
            ("Last Name", "last_name"),
            ("Username", "username"),
            ("Password", "password"),
            ("Email", "email"),
            ("Contact", "contact"),
            ("Address", "address"),
            ("NIC", "nic")
        ]

        self.entries = {}
        for i, (label_text, field_name) in enumerate(fields):
            CTkLabel(self.form_frame, text=label_text, font=("Arial Bold", 14), text_color="#601E88").grid(row=i, column=0, sticky="w", padx=(10, 0), pady=(8, 2))
            entry = CTkEntry(self.form_frame, width=300, fg_color="#EEEEEE", border_color="#601E88", text_color="#000000")
            if field_name == "password":
                entry.configure(show="•")
            entry.grid(row=i, column=1, padx=10, pady=4)
            self.entries[field_name] = entry

        # Role Selection
        CTkLabel(self.form_frame, text="Role", font=("Arial Bold", 14), text_color="#601E88").grid(row=len(fields), column=0, sticky="w", padx=(10, 0), pady=(10, 0))
        self.role_var = StringVar(value="Designer")

        roles = ["Admin", "Designer", "Sales Manager"]
        for idx, role in enumerate(roles):
            CTkRadioButton(self.form_frame, text=role, variable=self.role_var, value=role, font=("Arial", 12)).grid(row=len(fields), column=1+idx, padx=6, sticky="w")

        # Divider
        CTkLabel(self.form_frame, text="", height=2, fg_color="#ddd").grid(row=len(fields)+1, columnspan=4, sticky="ew", pady=15)

        # Buttons
        button_row = len(fields)+2
        CTkButton(self.form_frame, text="Sign Up", width=140, fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
                  command=self.register_user).grid(row=button_row, column=0, padx=10, pady=10)

        CTkButton(self.form_frame, text="Back to Login", width=140, fg_color="#EEEEEE", hover_color="#919191", text_color="#601E88",
                  font=("Arial Bold", 12), command=lambda: self.controller.show_login()).grid(row=button_row, column=1, padx=10, pady=10)

    def show_feedback(self, title, message, icon="info"):
        CTkMessagebox(title=title, message=message, icon=icon)

    def register_user(self):
        user_data = {field: entry.get() for field, entry in self.entries.items()}
        user_data["role"] = self.role_var.get()

        if any(not value for value in user_data.values()):
            self.show_feedback("Error", "All fields are required!", icon="cancel")
            return

        if add_user(user_data):
            self.show_feedback("Success", "Account created successfully!", icon="check")
            self.controller.show_login()
        else:
            self.show_feedback("Error", "Failed to create account!", icon="cancel")