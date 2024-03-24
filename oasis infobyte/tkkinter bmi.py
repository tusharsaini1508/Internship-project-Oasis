import tkinter as tk
from tkinter import messagebox

class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        self.geometry("400x200")
        self.configure(bg="#e6e6e6")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Select an Option:", bg="#e6e6e6")
        self.label.pack(pady=10)

        self.bmi_button = tk.Button(self, text="BMI Calculator", command=self.open_bmi_calculator, bg="green", fg="white")
        self.bmi_button.pack(pady=5)

    def open_bmi_calculator(self):
        bmi_calculator = BMICalculator(self)
        bmi_calculator.mainloop()

class BMICalculator(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("BMI Calculator")
        self.geometry("300x200")
        self.configure(bg="#e6e6e6")

        self.create_widgets()

    def create_widgets(self):
        self.label_weight = tk.Label(self, text="Enter your weight in kg:", bg="#e6e6e6")
        self.label_weight.pack(pady=5)
        self.entry_weight = tk.Entry(self)
        self.entry_weight.pack(pady=5)

        self.label_height = tk.Label(self, text="Enter your height in cm:", bg="#e6e6e6")
        self.label_height.pack(pady=5)
        self.entry_height = tk.Entry(self)
        self.entry_height.pack(pady=5)

        self.calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi, bg="green", fg="white")
        self.calculate_button.pack(pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get()) / 100 
            bmi = weight / (height ** 2)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
