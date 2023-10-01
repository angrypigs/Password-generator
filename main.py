import tkinter as tk
import customtkinter as ctk
import random
import math
from itertools import chain
import pyperclip


class PasswordGenerator:

    def __init__(self) -> None:
        self.LETTERS_BIG = [chr(x) for x in range(65, 91)]
        self.LETTERS_SMALL = [chr(x) for x in range(97, 123)]
        self.NUMBERS = [chr(x) for x in range(48, 58)]
        self.SYMBOLS = "!@#$%^&*()"

    def round_normal(self, number: float) -> int:
        return math.floor(number) if number-math.floor(number)<0.5 else math.ceil(number)

    def generate_password(self, lenght: int, special_symbols: bool = False) -> str:
        LETTERS_SMALL = random.sample(
            self.LETTERS_SMALL, self.round_normal(lenght*random.uniform(0.2, 0.5)))
        NUMBERS = random.sample(
            self.NUMBERS, self.round_normal(lenght*random.uniform(0.12, 0.27)))
        SYMBOLS = random.sample(
            self.SYMBOLS, self.round_normal(lenght*random.uniform(0.08, 0.18))) if (
                special_symbols) else []
        LETTERS_BIG = random.sample(
            self.LETTERS_BIG, lenght-len(LETTERS_SMALL)-len(NUMBERS)-len(SYMBOLS))
        return "".join(sorted(chain(LETTERS_BIG, LETTERS_SMALL, NUMBERS, SYMBOLS),
                             key=lambda x: random.random()))

class App(PasswordGenerator):

    def __init__(self) -> None:
        PasswordGenerator.__init__(self)
        self.WIDTH = 500
        self.HEIGHT = 700
        self.master = ctk.CTk()
        self.master.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.master.title("Password generator")
        self.master.resizable(False, False)
        self.init_menu()
        self.master.mainloop()

    def init_menu(self) -> None:
        self.frame_title = ctk.CTkFrame(self.master, width=400, height=80, corner_radius=10)
        self.frame_title.place(relx=0.5, rely=0.12, anchor=tk.CENTER)
        self.frame_options = ctk.CTkFrame(self.master, width=400, height=200, corner_radius=10)
        self.frame_options.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
        self.frame_result = ctk.CTkFrame(self.master, width=400, height=250, corner_radius=10)
        self.frame_result.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


if __name__ == "__main__":
    App()