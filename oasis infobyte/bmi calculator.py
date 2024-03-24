class MeasurementConverter:
    def __init__(self):
        pass
    
    def kg_to_lb(self, kg):
        return kg * 2.20462
    
    def lb_to_kg(self, lb):
        return lb / 2.20462
    
    def cm_to_ft(self, cm):
        return cm / 30.48
    
    def ft_to_cm(self, ft):
        return ft * 30.48
    
    def main(self):
        choice = int(input("""Enter the conversion you want to perform:
                            1. Kilograms to Pounds
                            2. Pounds to Kilograms
                            3. Centimeters to Feet
                            4. Feet to Centimeters\n"""))
        
        if choice == 1:
            kg = float(input("Enter weight in kilograms: "))
            print("Weight in pounds:", self.kg_to_lb(kg))
        elif choice == 2:
            lb = float(input("Enter weight in pounds: "))
            print("Weight in kilograms:", self.lb_to_kg(lb))
        elif choice == 3:
            cm = float(input("Enter height in centimeters: "))
            print("Height in feet:", self.cm_to_ft(cm))
        elif choice == 4:
            ft = float(input("Enter height in feet: "))
            print("Height in centimeters:", self.ft_to_cm(ft))
        else:
            print("Invalid choice")

class BMIConverter:
    def __init__(self):
        pass
    
    def main_bmi(self):
        choice = int(input("""Enter the system for entering height and weight:
                            1. Kilograms and Centimeters
                            2. Pounds and Feet\n"""))
        if choice == 1:
            self.kg_cm()
        elif choice == 2:
            self.pound_foot()
        else:
            print("Invalid choice")

    def kg_cm(self):
        kg = float(input("Enter your weight in kg: "))
        cm = float(input("Enter your height in cm: "))
        main_h = cm / 100
        main_h_square = main_h * main_h
        bmi = kg / main_h_square
        print("Your BMI is:", bmi)
        print("""
            Underweight = <18.5
            Normal weight = 18.5–24.9
            Overweight = 25–29.9
            Obesity = BMI of 30 or greater""")

    def pound_foot(self):
        pound = float(input("Enter your weight in pounds: "))
        foot = float(input("Enter your height in feet: "))
        main_foot = foot * 12
        final_foot = main_foot * main_foot
        weight_height = pound / final_foot
        bmi = weight_height * 703
        print("Your BMI is:", bmi)
        print("""
            Underweight = <18.5
            Normal weight = 18.5–24.9
            Overweight = 25–29.9
            Obesity = BMI of 30 or greater""")

choice = int(input("""Enter your choice
                    1 for MeasurementConverter
                    2 for BMIConverter\n"""))

if choice == 1:
    converter = MeasurementConverter()
    converter.main()
elif choice == 2:
    bmi_converter = BMIConverter()
    bmi_converter.main_bmi()
else:
    print("Invalid choice")
