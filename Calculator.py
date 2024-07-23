import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Display Entry
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click function
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))

# Functions for operations
def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Calculator Buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_values = [1, 2, 3, 4]
column_values = [0, 1, 2, 3]

for i, text in enumerate(button_texts):
    action = lambda x=text: button_click(x) if x != '+' else button_click(x)
    button = tk.Button(root, text=text, width=10, height=3, font=('Arial', 14), command=action)
    button.grid(row=row_values[i // 4], column=column_values[i % 4], padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', width=10, height=3, font=('Arial', 14), command=clear_display)
clear_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky='we')

# Equal button
equal_button = tk.Button(root, text='=', width=10, height=3, font=('Arial', 14), command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5, columnspan=2, sticky='we')

root.mainloop()
