import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

       
        tk.Label(root, text="Enter password length:").pack(pady=10)
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack(pady=5)

        
        self.digits_var = tk.BooleanVar()
        self.letters_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        tk.Checkbutton(root, text="Digits", variable=self.digits_var).pack(anchor=tk.W)
        tk.Checkbutton(root, text="Letters", variable=self.letters_var).pack(anchor=tk.W)
        tk.Checkbutton(root, text="Special Characters", variable=self.special_var).pack(anchor=tk.W)

       
        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=20)

      
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            character_list = ""

           
            if self.digits_var.get():
                character_list += string.digits
            if self.letters_var.get():
                character_list += string.ascii_letters
            if self.special_var.get():
                character_list += string.punctuation
            
           
            if character_list and length > 0:
                password = ''.join(random.choice(character_list) for _ in range(length))
                self.result_label.config(text=f"Generated Password: {password}")
            else:
                messagebox.showwarning("Warning", "Please enter a valid length and select at least one character set.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
