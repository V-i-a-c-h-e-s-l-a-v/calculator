import tkinter as tk
from tkinter import messagebox
from math import sqrt

memory_storage = ""  # Get value from M-buttons.


def memory_add():
    """
    Command for 'M+' button to add value from Entry widget (var. 'calc') to the value
    of the global var. 'memory_storage'.

    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    memory_storage = str(eval(f"{calc.get()} + {memory_storage}"))


def memory_subtract():
    """
    Command for 'M-' button to subtract value from Entry widget (var. 'calc') from the value
    of the global var. 'memory_storage'.

    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    memory_storage = str(eval(f"{memory_storage} - {calc.get()}"))


def memory_clear():
    """
    Command for 'MC' button to clear the value of the global var. 'memory_storage' (add empty string).

    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    memory_storage = ""


def memory_recall():
    """
    Command for 'MR' button to add the value of the global var. 'memory_storage' to the Entry widget (var. 'calc')
    :return: Nothing
    """
    # TODO:  MR button replaces the current 'Entry' widget value on the new one.It'd be better to implement
    # an additional functionality. If next to digit is a math sign when using button "MR" adds the value of
    # the global var. 'memory_storage' to the 'Entry' widget value.
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
    Command for 'MS' button to pass the value of the Entry widget (var. calc) to the global var. memory_storage.
    :return: Global var. 'memory_storage'.
    """
    global memory_storage
    value = calc.get()
    # Using 'MS' button to storage digits only not digits and math signs
    # (after digit) or expression which has the math signs between digits.
    if any(item in "+-*/" for item in value[1:]):  # A negative number is possible.
        memory_storage = "0"
    else:
        memory_storage = calc.get()


def press_key(event):
    """
    Getting the keyboard buttons binds for some buttons of the GUI.
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
        messagebox.showerror("ValueError:", "Math domain error")
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
    Command of "+/-" button to switch sign of the 'Entry' widget value (method 'calc').
    :return: Nothing
    """
    # TODO: There is a bug. If the 'Entry' widget value is 'digit and sign' the function returns message 'SyntaxError'.
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, -1 * eval(value))


def basic_calculation():
    """
    Command of "=" button to complete current 'Entry' widget value (method 'calc')
    calculation and pass the result to the method 'calc'.
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
    Command of "." button.
    :param point:
    :return: Nothing
    """
    value = calc.get()
    if value[0] == "0":  # To omit the start zero.
        value = value + point
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])

    if value != "0" and value.count(".") == 0:  # Each digit can have one decimal point only
        calc.delete(0, tk.END)
        calc.insert(0, value + point)

    if any(item in "+-/*" for item in value) and value.count(".") < 2:
        calc.delete(0, tk.END)
        calc.insert(0, value + point)


def add_operation(operation):
    """
    Command of "+", "-", "*", "." buttons.
    :param operation:
    :return: Nothing
    """
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
        (len(value) - value.count(".")) >= 3
        and any(item in "+-/*" for item in value)
        and value[0] not in "+-/*"
    ):
        value = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, str(value) + operation)

    elif (
        (len(value) - value.count(".")) >= 3
        and any(item in "+-/*" for item in value)
        and value[0] in "+-/*"
    ):
        value = eval(value)
        calc.delete(0, tk.END)
        calc.insert(0, str(value) + operation)


def add_digit(digit):
    """
    Command of digit buttons.
    :param digit:
    :return: Nothing
    """
    value = calc.get()
    if value == "0":
        value = value + digit
        calc.delete(0, tk.END)
        calc.insert(0, value[1:])
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + digit)


def get_ms_button(memory_mode):
    """
    Getting "MS" button widget.
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
    Getting "MR" button widget.
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
    Getting "MR" button widget.
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
    Getting "M+" button widget.
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
    Getting "M-" button widget.
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
    Getting "sqrt" and "x^2" buttons widget.
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
    Getting "%" button widget.
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
    Getting "=" button widget.
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
    Getting "Digit" button widget.
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
    Getting "+/-" button widget.
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
    Getting "." button widget.
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
    Getting "C" button widget.
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

# Getting the keyboard buttons binds for some buttons of the GUI

root.bind("<Key>", press_key)

# Entry widget

calc = tk.Entry(root, justify=tk.RIGHT, width=15, font=("Arial", 15))
calc.grid(row=0, column=0, stick="we", columnspan=4, padx=5, pady=5)
calc.insert(0, "0")

# Memory button widgets

get_mc_button("MC").grid(row=1, column=0, sticky="we", padx=3, pady=3)
get_mr_button("MR").grid(row=1, column=1, sticky="we", padx=3, pady=3)
get_m_add_button("M+").grid(row=2, column=0, sticky="we", padx=3, pady=3)
get_m_subtract_button("M-").grid(row=2, column=1, sticky="we", padx=3, pady=3)
get_ms_button("MS").grid(row=1, column=2, sticky="wens", rowspan=2, padx=3, pady=3)


# Digit button widgets

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

# Plus/minus button widget

get_sign_button("+/-").grid(row=7, column=0, sticky="wens", padx=3, pady=3)

# Decimal point button widget

get_decimal_point_button(".").grid(row=7, column=2, sticky="wens", padx=3, pady=3)

# Clear button widget

get_clear_button("C").grid(row=1, column=3, sticky="wens", rowspan=2, padx=3, pady=3)

# Operation buttons widgets

get_operation_button("/").grid(row=3, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("*").grid(row=4, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("-").grid(row=5, column=3, sticky="wens", padx=3, pady=3)
get_operation_button("+").grid(row=6, column=3, sticky="wens", padx=3, pady=3)

# Calculations button widgets

get_calc_button("=").grid(row=7, column=3, sticky="wens", padx=3, pady=3)

# Extra math operations buttons widget

get_extra_math_operations_button("sqrt").grid(
    row=3, column=2, sticky="we", padx=3, pady=3
)
get_extra_math_operations_button("x^2").grid(
    row=3, column=1, sticky="we", padx=3, pady=3
)

# Percent button widget

get_percent_button("%").grid(row=3, column=0, sticky="we", padx=3, pady=3)

# Grid root's columns and rows configuration

for y in range(5):
    root.grid_columnconfigure(y, minsize=60)

for x in range(0, 2):
    root.grid_rowconfigure(x, minsize=30)

for x in range(3, 8):
    root.grid_rowconfigure(x, minsize=60)


root.mainloop()

if __name__ == "__main__":
    root.mainloop()
