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
        self.password = ""
        self.lenght = 6
        self.special_symbols = False
        self.master = ctk.CTk()
        self.master.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.master.title("Password generator")
        self.master.resizable(False, False)
        self.init_menu()
        self.master.mainloop()

    def lenght_slider_method(self, value) -> None:
        self.lenght = int(value)
        self.lenght_label.configure(text=f"Password lenght: {int(value)}")
    
    def symbols_slider_method(self, value) -> None:
        self.special_symbols = bool(int(value))

    def password_gen_button(self) -> None:
        self.password = self.generate_password(self.lenght, self.special_symbols)
        self.result_label.configure(text=self.password)

    def init_menu(self) -> None:
        # title frame
        self.frame_title = ctk.CTkFrame(self.master, width=400, height=80, corner_radius=10)
        self.frame_title.place(relx=0.5, rely=0.12, anchor=tk.CENTER)
        ctk.CTkLabel(self.frame_title, text="Password generator", font=("Roboto", 30)).place(
            relx=0.5, rely=0.5, anchor=tk.CENTER)
        # options frame
        self.frame_options = ctk.CTkFrame(self.master, width=400, height=200, corner_radius=10)
        self.frame_options.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
        self.lenght_label = ctk.CTkLabel(self.frame_options, text="Password lenght: 0", font=("Roboto", 20))
        self.lenght_label.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
        self.lenght_slider = ctk.CTkSlider(self.frame_options, width=300, height=20, from_=6, to=20, 
                      number_of_steps=14, command=self.lenght_slider_method)
        self.lenght_slider.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.lenght_slider.set(10)
        self.lenght_slider_method(10)
        ctk.CTkLabel(self.frame_options, text="Special symbols", font=("Roboto", 20)).place(
            relx=0.25, rely=0.6, anchor=tk.CENTER)
        self.symbols_slider = ctk.CTkSlider(self.frame_options, width=60, height=30, from_=0, to=1, 
                      number_of_steps=1, command=self.symbols_slider_method)
        self.symbols_slider.place(relx=0.25, rely=0.8, anchor=tk.CENTER)
        self.symbols_slider.set(0)
        # result frame
        self.frame_result = ctk.CTkFrame(self.master, width=400, height=60, corner_radius=10)
        self.frame_result.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.result_label = ctk.CTkLabel(self.frame_result, text="", font=("Roboto", 30))
        self.result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # buttons frame
        self.frame_buttons = ctk.CTkFrame(self.master, width=400, height=180, corner_radius=10)
        self.frame_buttons.place(relx=0.5, rely=0.82, anchor=tk.CENTER)
        ctk.CTkButton(self.frame_buttons, width=200, height=50, corner_radius=8,
                      command=self.password_gen_button, text="Generate password", font=("Roboto", 20)
                      ).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        ctk.CTkButton(self.frame_buttons, width=200, height=50, corner_radius=8,
                      command=lambda: pyperclip.copy(self.password), text="Copy to clipboard", font=("Roboto", 20)
                      ).place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        


if __name__ == "__main__":
    App()