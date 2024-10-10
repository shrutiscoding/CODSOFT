import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        tk.Label(root, text="First Number:").pack()
        self.num1_entry = tk.Entry(root, width=15)
        self.num1_entry.pack(pady=(10, 5))

      
        tk.Label(root, text="Second Number:").pack()
        self.num2_entry = tk.Entry(root, width=15)
        self.num2_entry.pack(pady=(5, 10))

      
        tk.Button(root, text="Add", command=self.add, width=10).pack(pady=5)
        tk.Button(root, text="Subtract", command=self.subtract, width=10).pack(pady=5)
        tk.Button(root, text="Multiply", command=self.multiply, width=10).pack(pady=5)
        tk.Button(root, text="Divide", command=self.divide, width=10).pack(pady=5)

        self.result_label = tk.Label(root, text="",font="Algebra")
        self.result_label.pack(pady=10)

    def add(self):
        self.calculate(lambda x, y: x + y)

    def subtract(self):
        self.calculate(lambda x, y: x - y)

    def multiply(self):
        self.calculate(lambda x, y: x * y)

    def divide(self):
        self.calculate(lambda x, y: x / y if y != 0 else "Error: Division by zero")

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = operation(num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
