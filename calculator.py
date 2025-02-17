import tkinter as tk
from typing import Any


class Calculator:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Калькулятор")

        self.entry = tk.Entry(self.root, font=("Arial", 18), justify="right")
        self.entry.pack(fill="both", expand=True)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"],
        ]

        for row in self.buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for text in row:
                button = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 18),
                    command=self.create_command(text),
                )
                button.pack(side="left", expand=True, fill="both")

    def create_command(self, text: str) -> Any:
        def on_button_click() -> None:
            self.on_click(text)

        return on_button_click

    def on_click(self, text: str) -> None:
        if text == "C":
            self.entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
