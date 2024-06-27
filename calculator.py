import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("310x420+950+300")
root.iconbitmap("letter-p.ico")
root.resizable(False, False)  # Disable window resizing


# Create an entry widget to display the input and result
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, width=16, font=('Arial', 24), borderwidth=2, relief='sunken')
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

# Function to handle button clicks (numbers and operators)
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to handle the '=' button (calculate result)
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear the entry
def button_clear():
    entry.delete(0, tk.END)

# Function to delete the last digit entered
def button_delete_last_digit():
    current_value = entry.get()
    if current_value:
        new_value = current_value[:-1]  # Remove the last character
        entry.delete(0, tk.END)         # Clear the Entry widget
        entry.insert(0, new_value)      # Insert the updated value back into the Entry widget

# List of buttons to display
buttons =[
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    ]

row_val = 1
col_val = 0

# Loop to create buttons and place them in the grid
for button in buttons:
    if button in ['=', 'All Clear', 'Delete']:
        if button == '=':
            btn = tk.Button(root, text=button, width=7, height=3, command=button_equal)
        elif button == 'All Clear':
            btn = tk.Button(root, text=button, width=7, height=3, command=button_clear)

        elif button == 'Delete':
            btn = tk.Button(root, text=button, width=7, height=3, command=button_delete_last_digit)
    else:
        btn = tk.Button(root, text=button, width=7, height=3, command=lambda b=button: button_click(b))
    
    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=(5, 5))
    
    # Adjusting column and row values for grid placement
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add clear button
clear_button = tk.Button(root, text='All Clear', width=7, height=3, command=button_clear)
clear_button.grid(row=row_val+1, column=col_val, columnspan= 4,sticky="nsew", padx=5, pady=5)

# Add delete button
clear_button = tk.Button(root, text='Delete', width=7, height=3, command=button_delete_last_digit)
clear_button.grid(row=row_val+2, column=col_val, columnspan=4, sticky="nsew",padx=5, pady=5)

# Run the application
root.mainloop()
