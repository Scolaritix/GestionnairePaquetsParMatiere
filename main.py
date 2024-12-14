import tkinter as tk
import tkinter.ttk as ttk

import customtkinter
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x300")
        self.title("Gestionnaire de paquets par matières")
        self.resizable(False, False)

        for i in range(3):
            self.columnconfigure(i, weight=1)
        for i in range(15):
            self.rowconfigure(i, weight=1)

        ctk.CTkLabel(self, text="Gestion des paquets par matière").grid(row=0, column=1)

        self.subject_list: list[str] = ["NSI", "SI", "Maths", ]
        self.subject_spinner = ctk.CTkComboBox(self, values=self.subject_list)
        self.subject_spinner.grid(row=1, column=0)


if __name__ == "__main__":
    customtkinter.set_default_color_theme("blue")
    customtkinter.set_appearance_mode("System")

    app: App = App()
    app.mainloop()
