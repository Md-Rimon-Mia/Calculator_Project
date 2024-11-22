import tkinter as tk


class Calculation:
    def __init__(self):
        self.result = ""

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error"
        else:
            return num1 / num2


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create the Calculation object to perform operations
        self.calculation = Calculation()

        # Display Entry widget
        self.entry = tk.Entry(self.root, width=30, borderwidth=5, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout for calculator
        self.create_buttons()

    def create_buttons(self):
        # Button definitions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons and add them to grid
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=3, font=('Arial', 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        current_text = self.entry.get()

        if char == 'C':  # Clear button
            self.entry.delete(0, tk.END)
        elif char == '=':  # Equals button, calculate result
            try:
                # Safe evaluation using eval function (can be dangerous in other contexts)
                result = self.evaluate_expression(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:  # Any other button (numbers or operators)
            self.entry.insert(tk.END, char)

    def evaluate_expression(self, expression):
        # Evaluate expression using simple calculation methods
        try:
            if '+' in expression:
                num1, num2 = map(float, expression.split('+'))
                return self.calculation.add(num1, num2)
            elif '-' in expression:
                num1, num2 = map(float, expression.split('-'))
                return self.calculation.subtract(num1, num2)
            elif '*' in expression:
                num1, num2 = map(float, expression.split('*'))
                return self.calculation.multiply(num1, num2)
            elif '/' in expression:
                num1, num2 = map(float, expression.split('/'))
                return self.calculation.divide(num1, num2)
            else:
                return float(expression)  # If it's just a number
        except Exception:
            return "Error"


# Create the main window (root) and pass it to the CalculatorApp class
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()

