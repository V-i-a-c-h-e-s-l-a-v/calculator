import tkinter as tk
from tkinter import messagebox
from math import sqrt

memory_storage = "0"  # Gets the value from M-buttons. Default value is '0'.


def memory_add():
    """
    Command for the 'M+' button: add value from the Entry widget (var. 'calc') to the value
    stored in the global var. 'memory_storage'.

    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    value = calc.get()
    if value[-1] in "+-/*":
        # Global var. 'memory_storage' should only be assigned a numerical value.
        messagebox.showerror("Error", "SyntaxError")
    else:
        memory_storage = str(eval(f"{value} + {memory_storage}"))


def memory_subtract():
    """
    Command for the 'M-' button: subtract current value of the Entry widget (var. 'calc') from the value
    stored in the global var. 'memory_storage'.

    :return: Global var. 'memory_storage'.
    """

    global memory_storage
    value = calc.get()
    if value[-1] in "+-/*":
        # Global var. 'memory_storage' should only be assigned a numerical value.
        messagebox.showerror("Error", "SyntaxError")
    else:
        memory_storage = str(eval(f"{value} - {calc.get()}"))


def memory_clear():
    """
    Command for the 'MC' button: reset the value of the global var. 'memory_storage' (set default value: '0').

    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    memory_storage = "0"


def memory_recall():
    """
    Command for the 'MR' button: add the value of the global var. 'memory_storage' to the Entry widget (var. 'calc')
    :return: Nothing
    """

    global memory_storage
    value = calc.get()

    if value == "0" and memory_storage:
        value = value + memory_storage
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])
    elif value[-1] in "+-*/":
        calc.delete(0, tk.END)
        calc.insert(0, value + memory_storage)
    else:
        calc.delete(0, tk.END)
        calc.insert(0, memory_storage)


def memory_store():
    """
    Command for the 'MS' button: transfer the value from the Entry widget (var. calc) to the global var. memory_storage.
    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    value = calc.get()
    # Global var. 'memory_storage' should only be assigned a numerical value.
    if value[-1] in "+-/*":
        # Global var. 'memory_storage' should only be assigned a numerical value.
        messagebox.showerror("Error", "SyntaxError")
    else:
        memory_storage = calc.get()


def press_key(event):
    """
    Retrieving the keyboard buttons binds for certain buttons in the GUI.
    :param event: Event means pressing of the keyboard button.
    :return: Nothing
    """
    print(event)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char == ".":
        add_decimal_point(event.char)
    elif event.char in "+-*/":
        add_operation(event.char)
    elif event.keysym == "Escape":
        clear()
    elif event.keysym in ["Return", "KP_Enter", "equal"]:
        basic_calculation()


def extra_math_operations(operation):
    """
    Command for 'sqrt' and 'x^2' buttons.

    :param operation:
    :return: Nothing
    """
    try:
        value = calc.get()
        if operation == "sqrt":
            calc.delete(0, tk.END)
            calc.insert(0, str(sqrt(float(eval(value)))))

        elif operation == "x^2":
            calc.delete(0, tk.END)
            calc.insert(0, eval(value) ** 2)
    except ValueError:
        messagebox.showerror("ValueError:", "mathematical domain error")
        calc.insert(0, "Error")


def percent():
    """
    Command for '%' button.
    :return:
    """
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(value) / 100)


def clear():
    """
    Command of "C" button to clear value of the 'Entry' widget (method 'calc').
    :return:
    """
    calc.delete(0, tk.END)
    calc.insert(0, "0")


def sign_switcher():
    """
    Command for the "+/-" button: switch negative/positive symbols of the 'Entry' widget value (method 'calc').
    :return: Nothing
    """

    value = calc.get()
    if len(value) >= 2 and value[-1] in "+-/*":
        # Otherwise the func. 'eval' returns "SyntaxError" and  interrupt the script execution.
        messagebox.showerror("Error", "SyntaxError")
    else:
        calc.delete(0, tk.END)
        calc.insert(0, -1 * eval(value))


def basic_calculation():
    """
    Command for the "=" button: complete current 'Entry' widget value (method 'calc')
    calculation and assign the result to the method 'calc'.

    :return: Nothing
    """
    try:
        value = calc.get()
        if value[-1] in "+-/*":
            value = value[:-1] + value[-1] + value[:-1]
            calc.delete(0, tk.END)
            calc.insert(0, eval(value))

        calc.delete(0, tk.END)
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showerror("Error", "ZeroDivisionError")


def add_decimal_point(point):
    """
    Command for the "." button.
    :param point:
    :return: Nothing
    """
    value = calc.get()
    if value[0] == "0":  # To omit the start zero.
        value = value + point
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])

    if (
        value != "0" and value.count(".") == 0
    ):  # Each digit should have one decimal point.
        calc.delete(0, tk.END)
        calc.insert(0, value + point)

    if any(item in "+-/*" for item in value) and value.count(".") < 2:
        calc.delete(0, tk.END)
        calc.insert(0, value + point)


def add_operation(operation):
    """
    Command for the "+", "-", "*", "." buttons.

    :param operation:
    :return: Nothing
    """

    value = calc.get()
    if value == "0" and len(value) == 1:
        # The first symbol of the expression must be a digit only.
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)

    if value[-1] in "+-/*" and operation in "+-/*":
        # The symbol next to any mathematical operation must be a digit. The preceding mathematical
        # symbol will be replaced with the current one.
        calc.delete(len(value) - 1, tk.END)
        calc.insert(len(value) - 1, operation)

    if (
        (len(value) - value.count(".")) >= 3
        and any(item in "+-/*" for item in value)
        and value[0] not in "+-/*"
    ):
        # An expression like '2 + 5 +' should evaluate to '7. The decimal point is excluded from the calculation of the
        # expression length.
        value = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, str(value) + operation)


def add_digit(digit):
    """
    Command for the digit buttons.
    :param digit:
    :return: Nothing
    """
    value = calc.get()
    if value[0] == "0":  # To omit the start zero.
        value = value + digit
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + digit)


def get_ms_button(memory_mode):
    """
    Retrieving the "MS" button widget.
    :param memory_mode:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=memory_mode,
        font=("Calibri", 10),
        foreground="green",
        command=lambda: memory_store(),
    )


def get_mr_button(memory_mode):
    """
    Retrieving the "MR" button widget.
    :param memory_mode:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=memory_mode,
        font=("Calibri", 10),
        foreground="green",
        command=lambda: memory_recall(),
    )


def get_mc_button(memory_mode):
    """
    Retrieving the "MR" button widget.
    :param memory_mode:
    :return: Tkinter button widget.
    """

    return tk.Button(
        root,
        text=memory_mode,
        font=("Calibri", 10),
        foreground="green",
        command=lambda: memory_clear(),
    )


def get_m_add_button(memory_mode):
    """
    Retrieving the "M+" button widget.
    :param memory_mode:
    :return: Tkinter button widget.
    """

    return tk.Button(
        root,
        text=memory_mode,
        font=("Calibri", 10),
        foreground="green",
        command=lambda: memory_add(),
    )


def get_m_subtract_button(memory_mode):
    """
    Retrieving the "M-" button widget.
    :param memory_mode:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=memory_mode,
        font=("Calibri", 10),
        foreground="green",
        command=lambda: memory_subtract(),
    )


def get_operation_button(operation):
    """
    Getting "+", "-", "*", "/" buttons widget.
    :param operation:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: add_operation(operation),
    )


def get_extra_math_operations_button(operation):
    """
    Retrieving "sqrt" and "x^2" buttons widget.
    :param operation:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: extra_math_operations(operation),
    )


def get_percent_button(pcnt):
    """
    Retrieving  the "%" button widget.
    :param pcnt:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=pcnt,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: percent(),
    )


def get_calc_button(op):
    """
    GRetrieving the "=" button widget.
    :param op:
    :return: Tkinter button widget.
    """
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
    """
    Retrieving the "Digit" button widget.
    :param digit:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=digit,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: add_digit(digit),
    )


def get_sign_button(param):
    """
    Retrieving the "+/-" button widget.
    :param param:
    :return: Tkinter button widget.
    """

    return tk.Button(
        root,
        text=param,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: sign_switcher(),
    )


def get_decimal_point_button(point):
    """
    Retrieving the "." button widget.
    :param point:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=point,
        font=("Arial", 13),
        borderwidth=3,
        foreground="blue",
        command=lambda: add_decimal_point(point),
    )


def get_clear_button(operation):
    """
    Retrieving "C" button widget.
    :param operation:
    :return: Tkinter button widget.
    """
    return tk.Button(
        root,
        text=operation,
        font=("Calibri", 13),
        borderwidth=3,
        foreground="red",
        command=lambda: clear(),
    )


root = tk.Tk()
root.geometry("240x400")
root.title("Calculator")

root.resizable(False, False)

# Retrieving the keyboard buttons binds for some buttons of the GUI.

root.bind("<Key>", press_key)

# Entry widget.

calc = tk.Entry(root, justify=tk.RIGHT, width=15, font=("Arial", 15))
calc.grid(row=0, column=0, stick="we", columnspan=4, padx=5, pady=5)
calc.insert(0, "0")

# Memory button widgets.

get_mc_button("MC").grid(row=1, column=0, sticky="we", padx=3, pady=3)
get_mr_button("MR").grid(row=1, column=1, sticky="we", padx=3, pady=3)
get_m_add_button("M+").grid(row=2, column=0, sticky="we", padx=3, pady=3)
get_m_subtract_button("M-").grid(row=2, column=1, sticky="we", padx=3, pady=3)
get_ms_button("MS").grid(row=1, column=2, sticky="wens", rowspan=2, padx=3, pady=3)


# Digit button widgets.

get_digit_button("9").grid(row=4, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("8").grid(row=4, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("7").grid(row=4, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("6").grid(row=5, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("5").grid(row=5, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("4").grid(row=5, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("3").grid(row=6, column=2, sticky="wens", padx=3, pady=3)
get_digit_button("2").grid(row=6, column=1, sticky="wens", padx=3, pady=3)
get_digit_button("1").grid(row=6, column=0, sticky="wens", padx=3, pady=3)

get_digit_button("0").grid(row=7, column=1, sticky="wens", padx=3, pady=3)

# Plus/minus button widget.

get_sign_button("+/-").grid(row=7, column=0, sticky="wens", padx=3, pady=3)

# Decimal point button widget.

get_decimal_point_button(".").grid(row=7, column=2, sticky="wens", padx=3, pady=3)

# Clear button widget.

get_clear_button("C").grid(row=1, column=3, sticky="wens", rowspan=2, padx=3, pady=3)

# Operation buttons widgets.

get_operation_button("/").grid(row=3, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("*").grid(row=4, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("-").grid(row=5, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("+").grid(row=6, column=3, sticky="wens", padx=3, pady=3)

# Calculations button widgets.

get_calc_button("=").grid(row=7, column=3, sticky="wens", padx=3, pady=3)

# Extra mathematical operations buttons widget.

get_extra_math_operations_button("sqrt").grid(
    row=3, column=2, sticky="we", padx=3, pady=3
)
get_extra_math_operations_button("x^2").grid(
    row=3, column=1, sticky="we", padx=3, pady=3
)

# Percent button widget.

get_percent_button("%").grid(row=3, column=0, sticky="we", padx=3, pady=3)

# Grid root's columns and rows configuration.

for y in range(5):
    root.grid_columnconfigure(y, minsize=60)

for x in range(0, 2):
    root.grid_rowconfigure(x, minsize=30)

for x in range(3, 8):
    root.grid_rowconfigure(x, minsize=60)


root.mainloop()

if __name__ == "__main__":
    root.mainloop()
