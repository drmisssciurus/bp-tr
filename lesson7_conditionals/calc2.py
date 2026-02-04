import tkinter as tk


def calculator(number1, number2, action):
    if action != "+" and action != "-" and action != "*" and action != "/":
        return "Error: wrong action"
    if type(number1) != float and type(number1) != int:
        return "Error: wrong number1 type"
    if type(number2) != float and type(number2) != int:
        return "Error: wrong number2 type"
    if action == "/":
        if number2 == 0:
            return "Error: number2=0"
        return number1 / number2
    if action == "+":
        return number1 + number2
    if action == "-":
        return number1 - number2
    if action == "*":
        return number1 * number2


# ====== GUI ======

root = tk.Tk()
root.title("Простой калькулятор")

# Состояние калькулятора
display_var = tk.StringVar(value="0")  # то, что видим на экране
first_number = None                    # первое число
current_action = None                  # операция: + - * /
should_reset_input = False             # флаг: очистить ли ввод перед следующей цифрой


def set_display(text: str):
    """Установить текст на экране."""
    display_var.set(text)


def on_digit(digit: str):
    """Нажатие на кнопку цифры."""
    global should_reset_input
    text = display_var.get()

    if should_reset_input or text.startswith("Error"):
        # если только что показывали результат или ошибку — начинаем ввод заново
        text = ""
        should_reset_input = False

    if text == "0":
        text = digit  # заменяем ведущий ноль
    else:
        text += digit

    set_display(text)


def on_dot():
    """Кнопка точки (.)"""
    global should_reset_input
    text = display_var.get()

    if should_reset_input or text.startswith("Error"):
        text = "0"
        should_reset_input = False

    if "." not in text:
        text += "."
        set_display(text)


def on_clear():
    """Сброс всего."""
    global first_number, current_action, should_reset_input
    first_number = None
    current_action = None
    should_reset_input = False
    set_display("0")


def on_action_click(action: str):
    """Нажали + - * /"""
    global first_number, current_action, should_reset_input
    text = display_var.get()

    try:
        first_number = float(text)
    except ValueError:
        set_display("Error: number1")
        first_number = None
        current_action = None
        should_reset_input = True
        return

    current_action = action
    should_reset_input = True  # следующее число начнём вводить с нуля


def on_equal():
    """Нажали ="""
    global first_number, current_action, should_reset_input

    if first_number is None or current_action is None:
        return  # нечего считать

    text = display_var.get()
    try:
        second_number = float(text)
    except ValueError:
        set_display("Error: number2")
        first_number = None
        current_action = None
        should_reset_input = True
        return

    res = calculator(first_number, second_number, current_action)
    set_display(str(res))

    # если была ошибка — сбрасываем, если число — можно продолжать считать дальше
    if isinstance(res, (int, float, float.__class__)):
        first_number = res
    else:
        first_number = None
    current_action = None
    should_reset_input = True


# ====== ВИДЖЕТ ЭКРАНА ======
display = tk.Entry(root, textvariable=display_var,
                   width=20, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


# ====== КНОПКИ ======

# Первая строка: C  /  *  -
btn_clear = tk.Button(root, text="C", width=5, command=on_clear)
btn_div   = tk.Button(root, text="/", width=5, command=lambda: on_action_click("/"))
btn_mul   = tk.Button(root, text="*", width=5, command=lambda: on_action_click("*"))
btn_minus = tk.Button(root, text="-", width=5, command=lambda: on_action_click("-"))

btn_clear.grid(row=1, column=0, padx=5, pady=5)
btn_div.grid(row=1, column=1, padx=5, pady=5)
btn_mul.grid(row=1, column=2, padx=5, pady=5)
btn_minus.grid(row=1, column=3, padx=5, pady=5)

# Вторая строка: 7 8 9 +
btn_7 = tk.Button(root, text="7", width=5, command=lambda: on_digit("7"))
btn_8 = tk.Button(root, text="8", width=5, command=lambda: on_digit("8"))
btn_9 = tk.Button(root, text="9", width=5, command=lambda: on_digit("9"))
btn_plus = tk.Button(root, text="+", width=5, command=lambda: on_action_click("+"))

btn_7.grid(row=2, column=0, padx=5, pady=5)
btn_8.grid(row=2, column=1, padx=5, pady=5)
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_plus.grid(row=2, column=3, padx=5, pady=5)

# Третья строка: 4 5 6 =
btn_4 = tk.Button(root, text="4", width=5, command=lambda: on_digit("4"))
btn_5 = tk.Button(root, text="5", width=5, command=lambda: on_digit("5"))
btn_6 = tk.Button(root, text="6", width=5, command=lambda: on_digit("6"))
btn_eq = tk.Button(root, text="=", width=5, command=on_equal)

btn_4.grid(row=3, column=0, padx=5, pady=5)
btn_5.grid(row=3, column=1, padx=5, pady=5)
btn_6.grid(row=3, column=2, padx=5, pady=5)
btn_eq.grid(row=3, column=3, padx=5, pady=5)

# Четвёртая строка: 1 2 3
btn_1 = tk.Button(root, text="1", width=5, command=lambda: on_digit("1"))
btn_2 = tk.Button(root, text="2", width=5, command=lambda: on_digit("2"))
btn_3 = tk.Button(root, text="3", width=5, command=lambda: on_digit("3"))

btn_1.grid(row=4, column=0, padx=5, pady=5)
btn_2.grid(row=4, column=1, padx=5, pady=5)
btn_3.grid(row=4, column=2, padx=5, pady=5)

# Пятая строка: 0 .
btn_0 = tk.Button(root, text="0", width=12, command=lambda: on_digit("0"))
btn_dot = tk.Button(root, text=".", width=5, command=on_dot)

btn_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
btn_dot.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
