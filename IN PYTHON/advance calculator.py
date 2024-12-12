import math
import tkinter as tk
from tkinter import messagebox

def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "pow": math.pow,
            "pi": math.pi,
            "e": math.e
        })
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def on_calculate():
    expression = entry.get()
    result = calculate_expression(expression)
    result_label.config(text=f"Result: {result}")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x300")
root.resizable(True, True)

# Input field
entry = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", font=("Arial", 12), command=on_calculate)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), command=clear)
clear_button.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

# Info label
info_label = tk.Label(root, text="Supported functions: +, -, *, /, pow, sqrt, log, sin, cos, tan", font=("Arial", 10), wraplength=350, justify='center')
info_label.pack(pady=10)

# Run the application
root.mainloop()
