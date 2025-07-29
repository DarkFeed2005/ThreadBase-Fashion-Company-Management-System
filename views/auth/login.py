from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkCheckBox
from CTkMessagebox import CTkMessagebox 
from PIL import Image, ImageTk, ImageSequence
from utils.styles import *
from database.db_operations import verify_user
import os

class LoginPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent , fg_color=BG_COLOR
)
        self.controller = controller
        self.configure(width=1000, height=700)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Left – Animated GIF
        self.left_frame = CTkFrame(self, width=650, height=600)
        self.left_frame.pack_propagate(False)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.load_gif("assets/animated.gif", size=(800, 900))

        # Right – Login Form
        self.right_frame = CTkFrame(self, width=400, height=700 , fg_color=BG_COLOR)
        self.right_frame.pack_propagate(False)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.create_form_widgets()

    def load_gif(self, gif_path, size=(800, 1000)):
        gif = Image.open(gif_path)
        self.frames = [
            ImageTk.PhotoImage(frame.copy().convert("RGBA").resize(size, Image.Resampling.LANCZOS))
            for frame in ImageSequence.Iterator(gif)
        ]
        self.anim_index = 0
        self.gif_label = CTkLabel(self.left_frame, text="")
        self.gif_label.pack(expand=True)
        self.animate()

    def animate(self):
        self.gif_label.configure(image=self.frames[self.anim_index])
        self.anim_index = (self.anim_index + 1) % len(self.frames)
        self.after(100, self.animate)

    def create_form_widgets(self):
        logo = CTkImage(light_image=Image.open("assets/logo.png"), size=(120, 120))
        CTkLabel(self.right_frame, image=logo, text="").pack(pady=(40, 10))

        CTkLabel(self.right_frame, text="Welcome Back!",
                 font=("Arial Bold", 28), text_color="#601E88").pack(anchor="w", padx=25)
        CTkLabel(self.right_frame, text="Sign in to your account",
                 font=("Arial Bold", 12), text_color="#7E7E7E").pack(anchor="w", padx=25, pady=(0, 25))

        email_icon = CTkImage(light_image=Image.open("assets/email-icon.png"), size=(20, 20))
        CTkLabel(self.right_frame, text="  User Name:", font=("Arial Bold", 14),
                 text_color="#601E88", image=email_icon, compound="left").pack(anchor="w", padx=25)
        self.username = CTkEntry(self.right_frame, width=225, fg_color="#EEEEEE",
                                 border_color="#601E88", text_color="#000000")
        self.username.pack(anchor="w", padx=25, pady=(0, 15))

        password_icon = CTkImage(light_image=Image.open("assets/password-icon.png"), size=(17, 17))
        CTkLabel(self.right_frame, text="  Password:", font=("Arial Bold", 14),
                 text_color="#601E88", image=password_icon, compound="left").pack(anchor="w", padx=25)
        self.password = CTkEntry(self.right_frame, width=225, fg_color="#EEEEEE",
                                 border_color="#601E88", text_color="#000000", show="•")
        self.password.pack(anchor="w", padx=25, pady=(0, 15))

        self.remember_me = CTkCheckBox(self.right_frame, text="Remember me",
                                       font=("Arial Bold", 12), text_color="#601E88")
        self.remember_me.pack(anchor="w", padx=25)

        CTkButton(self.right_frame, text="Login", fg_color="#601E88", hover_color="#2A78C6",
                  font=("Arial Bold", 18), text_color="#ffffff", width=225,
                  command=self.authenticate).pack(anchor="w", padx=25, pady=(20, 0))

        forgot_pass = CTkLabel(self.right_frame, text="Forgot password?",
                               font=("Arial Bold", 11), text_color="#601E88", cursor="hand2")
        forgot_pass.pack(anchor="w", padx=25, pady=(10, 0))
        forgot_pass.bind("<Button-1>", lambda e: self.controller.show_forgot_password())

        signup_icon = CTkImage(light_image=Image.open("assets/signup-icon.png"), size=(17, 17))
        CTkButton(self.right_frame, text="Haven’t an account?", fg_color="#EEEEEE", hover_color="#919191",
                  font=("Arial Bold", 11), text_color="#601E88", width=225,
                  image=signup_icon, command=lambda: self.controller.show_signup()).pack(anchor="w", padx=25, pady=(10, 0))

    def authenticate(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            CTkMessagebox(title="Error", message="Please enter both username and password!", icon="cancel")
            return

        user = verify_user(username, password)

        if user:
            role = user["role"]
            if role == "Admin":
                self.controller.show_admin_dashboard()
            elif role == "Designer":
                self.controller.show_designer_dashboard(user["username"])
            elif role == "Sales Manager":
                self.controller.show_sales_dashboard(user["username"])
        else:
            CTkMessagebox(title="Login Failed", message="Invalid username or password", icon="cancel")