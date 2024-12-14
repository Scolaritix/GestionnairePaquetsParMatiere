import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk


class App:
    def __init__(self) -> None:
        self.app : ctk.CTk = ctk.CTk()
        self.app.geometry("400x600")
        self.app.title("Gestionnaire de paquets pas matières")


if __name__ == "__main__":
    ...
