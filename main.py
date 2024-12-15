import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x300")
        self.title("Gestionnaire de paquets par matières")
        self.resizable(False, False)

        self.subject_list: list[str] = ["NSI", "SI", "Maths", ]
        self.subject_spinner = ctk.CTkComboBox(self, values=self.subject_list)

        self.layout = ctk.CTkFrame(self)
        self.packet_state = ctk.CTkLabel(self.layout, text="Non-installé")

        self.install_button = ctk.CTkButton(self, text="Installer")

        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text="Gestion des paquets par matière", font=ctk.CTkFont("Calibri", 24)).pack(pady=25)
        self.subject_spinner.pack(pady=15)

        ctk.CTkLabel(self.layout, text="Etat du paquet:").pack(side=tk.LEFT, padx=20)
        self.packet_state.pack(side=tk.RIGHT, padx=20)
        self.layout.pack(ipady=15, pady=15)

        self.install_button.pack(ipadx=10, ipady=10, pady=15)


if __name__ == "__main__":
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("System")

    app: App = App()
    app.mainloop()
