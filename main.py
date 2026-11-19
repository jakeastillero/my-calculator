"""
Jake's First Calculator
A beginner-friendly calculator made with Python and Tkinter.
Tkinter is included with most standard Python installations.
"""

import tkinter as tk
from tkinter import ttk, messagebox


def calculate():
    """Read the inputs, perform the selected operation, and show the result."""
    try:
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())
        operation = operation_box.get()

        if operation == "Addition (+)":
            result = first_number + second_number
        elif operation == "Subtraction (-)":
            result = first_number - second_number
        elif operation == "Multiplication (×)":
            result = first_number * second_number
        elif operation == "Division (÷)":
            if second_number == 0:
                messagebox.showerror("Math Error", "You cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            messagebox.showwarning("Choose an operation", "Please select an operation.")
            return

        result_label.config(text=f"Result: {result:g}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number in both number fields."
        )


def clear_fields():
    """Clear both input fields and reset the result message."""
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    result_label.config(text="Result: —")
    first_entry.focus()


# Create the main application window.
window = tk.Tk()
window.title("Jake's First Calculator")
window.geometry("420x430")
window.resizable(False, False)
window.configure(bg="#f2f6fc")

# Main title.
title_label = tk.Label(
    window,
    text="MY FIRST CALCULATOR",
    font=("Arial", 19, "bold"),
    bg="#102d55",
    fg="white",
    pady=18
)
title_label.pack(fill="x")

subtitle = tk.Label(
    window,
    text="Python Beginner Project",
    font=("Arial", 10),
    bg="#f2f6fc",
    fg="#52647d"
)
subtitle.pack(pady=(12, 18))

# Calculator form.
form = tk.Frame(window, bg="white", padx=24, pady=22,
                highlightbackground="#d8e3f2", highlightthickness=1)
form.pack(fill="x", padx=25)

tk.Label(form, text="First number", font=("Arial", 11, "bold"),
         bg="white", fg="#102d55").pack(anchor="w")
first_entry = tk.Entry(form, font=("Arial", 13), relief="solid", bd=1)
first_entry.pack(fill="x", pady=(6, 14), ipady=7)

tk.Label(form, text="Operation", font=("Arial", 11, "bold"),
         bg="white", fg="#102d55").pack(anchor="w")
operation_box = ttk.Combobox(
    form,
    values=[
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    ],
    state="readonly",
    font=("Arial", 11)
)
operation_box.current(0)
operation_box.pack(fill="x", pady=(6, 14), ipady=5)

tk.Label(form, text="Second number", font=("Arial", 11, "bold"),
         bg="white", fg="#102d55").pack(anchor="w")
second_entry = tk.Entry(form, font=("Arial", 13), relief="solid", bd=1)
second_entry.pack(fill="x", pady=(6, 16), ipady=7)

button_row = tk.Frame(form, bg="white")
button_row.pack(fill="x")

calculate_button = tk.Button(
    button_row,
    text="Calculate",
    command=calculate,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
)
calculate_button.pack(side="left", expand=True, fill="x", padx=(0, 5))

clear_button = tk.Button(
    button_row,
    text="Clear",
    command=clear_fields,
    bg="#e5edf8",
    fg="#102d55",
    activebackground="#d5e2f4",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
)
clear_button.pack(side="left", expand=True, fill="x", padx=(5, 0))

result_label = tk.Label(
    window,
    text="Result: —",
    font=("Arial", 17, "bold"),
    bg="#f2f6fc",
    fg="#102d55",
    pady=18
)
result_label.pack()

footer = tk.Label(
    window,
    text="Created by Jake Astillero | BSIT-1C",
    font=("Arial", 9),
    bg="#f2f6fc",
    fg="#687990"
)
footer.pack(side="bottom", pady=12)

first_entry.focus()
window.mainloop()
