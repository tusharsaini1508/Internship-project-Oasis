import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x300")
        self.configure(bg="#e6e6e6")

        self.create_widgets()

    def create_widgets(self):
        self.label_length = tk.Label(self, text="Password Length:", bg="#e6e6e6")
        self.label_length.pack(pady=5)
        self.entry_length = tk.Entry(self)
        self.entry_length.pack(pady=5)

        self.label_complexity = tk.Label(self, text="Password Complexity:", bg="#e6e6e6")
        self.label_complexity.pack(pady=5)

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")

        self.complexity_choices = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(self, self.complexity_var, *self.complexity_choices)
        self.complexity_menu.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password, bg="blue", fg="white")
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self, text="", bg="#e6e6e6")
        self.password_label.pack(pady=5)

        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="green", fg="white")
        self.copy_button.pack(pady=5)

    def generate_password(self):
        length = self.get_length()
        complexity = self.get_complexity()

        password = self.generate_random_password(length, complexity)
        self.password_label.config(text=password)

    def get_length(self):
        try:
            length = int(self.entry_length.get())
            return length
        except ValueError:
            return 8  # Default length if user enters invalid input

    def get_complexity(self):
        complexity = self.complexity_var.get()
        if complexity == "Low":
            return string.ascii_letters
        elif complexity == "Medium":
            return string.ascii_letters + string.digits
        elif complexity == "High":
            return string.ascii_letters + string.digits + string.punctuation

    def generate_random_password(self, length, complexity):
        return ''.join(random.choice(complexity) for _ in range(length))

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)
        messagebox.showinfo("Clipboard", "Password copied to clipboard.")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
