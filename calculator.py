"""
Program: calculator.py
This is a basic calculator which evaluates expressions input
by the user and displays the results.
"""
import tkinter as tk

# Defines constants for font names and sizes
FONT_STYLE = ("Arial", 20)
DISPLAY_STYLE = ("Arial", 24)


class Calculator(object):
    def __init__(self):
        """Sets up the application."""
        self.window = tk.Tk()
        self.window.geometry("375x550")
        self.window.resizable(False, False)
        self.window.title("Calculator")
        self.window.iconbitmap("calcicon.ico")
        self.window.focus_force()

        # Sets the calculation display elements
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        # Creates the output display
        self.label = self.create_display_label()

        # Places all ten digits in a dictionary, with tuple values for the grid layout coordinates.
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        # Places operations in a dictionary, using Unicode values for the divide and multiply symbols.
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        # This for-loop allows buttons to fill empty space evenly.
        self.buttons_frame = self.create_buttons_frame()
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        # Calls all the other functions of the program
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.create_sqrt_button()
        self.create_square_button()
        self.bind_keys()

    def bind_keys(self):
        """Binds keys to their respective functions as defined by their dictionaries."""
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<Escape>", lambda event: self.clear())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        """Creates the clear and equals buttons."""
        self.create_clear_button()
        self.create_equals_button()

    def create_display_label(self):
        """Returns the current display as a label."""
        label = tk.Label(self.display_frame, text=self.current_expression,
                         font=DISPLAY_STYLE, anchor=tk.E, padx=24)
        label.pack(expand=True, fill="both")

        return label

    def create_display_frame(self):
        """Creates and returns the frame for the application."""
        frame = tk.Frame(self.window, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        """Adds the current value to the label."""
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        """Creates the buttons for the digits."""
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), font=FONT_STYLE,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        """Appends an operator to the end of the expression."""
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()

    def create_operator_buttons(self):
        """Creates each operator button and appends their operators."""
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, font=FONT_STYLE,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        """Clears both display labels."""
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        """Creates a button to clear both the total expression and current expression."""
        button = tk.Button(self.buttons_frame, text="C", font=FONT_STYLE, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        """Creates a square function."""
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        """Creates a square button."""
        button = tk.Button(self.buttons_frame, text="x\u00b2", font=FONT_STYLE, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        """Creates a square root function."""
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        """Creates the square root button."""
        button = tk.Button(self.buttons_frame, text="\u221ax", font=FONT_STYLE, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        """Evaluates the total expression label using the current expression."""
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        """Creates the '=' button."""
        button = tk.Button(self.buttons_frame, text="=", font=FONT_STYLE, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        """Creates and returns the frame that houses the buttons."""
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        """Updates the total_label based on the current expression."""
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.label.config(text=expression)

    def update_label(self):
        """Updates the current expression label, limiting display to 11 characters."""
        self.label.config(text=self.current_expression[:11])

    def run(self):
        """Runs the main loop."""
        self.window.mainloop()


# Entry point for the application
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
