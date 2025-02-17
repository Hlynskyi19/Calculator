import tkinter as tk
from typing import Any


class Calculator:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.entry = tk.Entry(
            self.root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.FLAT,
            bg="#ecf0f1",
        )
        self.entry.pack(fill="both", padx=10, pady=10, ipady=10)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"],
        ]

        for row in self.buttons:
            frame = tk.Frame(self.root, bg="#2c3e50")
            frame.pack(expand=True, fill="both")
            for text in row:
                button = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 20),
                    command=self.create_command(text),
                    bg="#34495e",
                    fg="white",
                    activebackground="#16a085",
                    activeforeground="white",
                    relief=tk.FLAT,
                    bd=2,
                )
                button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

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
