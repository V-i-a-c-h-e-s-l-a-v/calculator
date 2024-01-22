import tkinter as tk
from tkinter import messagebox
from math import sqrt


def press_key(event):
    print(event)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char == "\x1b":
        clear()
    elif event.char in "+-*/.":
        add_operation(event.char)
    elif event == "\r" or "=":
        basic_calculation()
    elif event == ".":
        get_decimal_pot_button(event.char)


def extra_math_operations(operation):
    try:
        value = calc.get()
        if operation == "sqrt":
            calc.delete(0, tk.END)
            calc.insert(0, str(sqrt(float(eval(value)))))

        elif operation == "x^2":
            calc.delete(0, tk.END)
            calc.insert(0, eval(value) ** 2)
    except ValueError:
        messagebox.showerror("ValueError:", "Math domain error")
        calc.insert(0, "Error")


def percent():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(value) / 100)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, "0")


def sign_switcher():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, -1 * eval(value))


def basic_calculation():
    value = calc.get()
    if value[-1] in "+-/*":
        value = value[:-1] + value[-1] + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def add_decimal_pot(pot):
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + pot)


def add_operation(operation):
    value = calc.get()
    if value == "0" and len(value) == 1:
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)

    if value[-1] in "+-/*" and operation in "+-/*":
        calc.delete(len(value) - 1, tk.END)
        calc.insert(len(value) - 1, operation)

    if (
        len(value) >= 3
        and any(item in "+-/*" for item in value)
        and value[0] not in "+-/*"
    ):
        value = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, str(value) + operation)

    elif (
        len(value) >= 4 and any(item in "+-/*" for item in value) and value[0] in "+-/*"
    ):
        value = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, str(value) + operation)


def add_digit(digit):
    value = calc.get()
    if value == "0":
        value = value + digit
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + digit)


def get_memory_button(memory_mode):
    # TODO: It is necessary to think out of the implementation!!!

    return tk.Button(root, text=memory_mode, font=("Calibri", 10), foreground="green")


def get_operation_button(operation):
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: add_operation(operation),
    )


def get_extra_math_operations_button(operation):
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: extra_math_operations(operation),
    )


def get_percent_button(pcnt):
    return tk.Button(
        root,
        text=pcnt,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: percent(),
    )


def get_calc_button(op):
    return tk.Button(
        root,
        text=op,
        font=("Arial", 13),
        borderwidth=3,
        bg="grey",
        foreground="red",
        command=lambda: basic_calculation(),
    )


def get_digit_button(digit):
    return tk.Button(
        root,
        text=digit,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: add_digit(digit),
    )


def get_sign_button(param):
    return tk.Button(
        root,
        text=param,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: sign_switcher(),
    )


def get_decimal_pot_button(pot):
    return tk.Button(
        root,
        text=pot,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: add_decimal_pot(pot),
    )


def get_clear_button(operation):
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: clear(),
    )


root = tk.Tk()
root.geometry("240x420")
root.title("Calculator")

root.resizable(False, False)

# Getting binds for all buttons

root.bind("<Key>", press_key)

# Entry widget

calc = tk.Entry(root, justify=tk.RIGHT, width=15, font=("Arial", 15))
calc.grid(row=0, column=0, stick="we", columnspan=4, padx=5, pady=5)
calc.insert(0, "0")


# Memory button widgets

get_memory_button("MC").grid(row=1, column=0, sticky="we", padx=3, pady=3)
get_memory_button("MR").grid(row=1, column=1, sticky="we", padx=3, pady=3)
get_memory_button("M+").grid(row=1, column=2, sticky="we", padx=3, pady=3)


# Digit button widgets

get_digit_button("9").grid(row=3, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("8").grid(row=3, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("7").grid(row=3, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("6").grid(row=4, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("5").grid(row=4, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("4").grid(row=4, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("3").grid(row=5, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("2").grid(row=5, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("1").grid(row=5, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("0").grid(row=6, column=1, sticky="wens", padx=3, pady=3)

# Plus/minus button widget

get_sign_button("+/-").grid(row=6, column=0, sticky="wens", padx=3, pady=3)

# Decimal pot button widget

get_decimal_pot_button(".").grid(row=6, column=2, sticky="wens", padx=3, pady=3)

# Clear button widget

get_clear_button("C").grid(row=1, column=3, sticky="wens", padx=3, pady=3)

# Operation buttons widgets

get_operation_button("/").grid(row=2, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("*").grid(row=3, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("-").grid(row=4, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("+").grid(row=5, column=3, sticky="wens", padx=3, pady=3)

# Calculations button widgets

get_calc_button("=").grid(row=6, column=3, sticky="wens", padx=3, pady=3)

# Extra math operations buttons widget

get_extra_math_operations_button("sqrt").grid(
    row=2, column=2, sticky="we", padx=3, pady=3
)
get_extra_math_operations_button("x^2").grid(
    row=2, column=1, sticky="we", padx=3, pady=3
)

# Percent button widget

get_percent_button("%").grid(row=2, column=0, sticky="we", padx=3, pady=3)

# Grid root's columns and rows configuration

for y in range(5):
    root.grid_columnconfigure(y, minsize=60)

for x in range(7):
    root.grid_rowconfigure(x, minsize=60)

root.mainloop()

if __name__ == "__main__":
    pass
