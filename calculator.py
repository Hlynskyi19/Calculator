import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")

        self.entry = tk.Entry(
            root, width=20, font=("Arial", 18), bd=5, relief=tk.GROOVE
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, col in buttons:
            button = tk.Button(
                self.root, text=text, font=("Arial", 14), width=5, height=2
            )
            button.grid(row=row, column=col, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
