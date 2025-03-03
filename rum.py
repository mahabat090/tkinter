import tkinter as tk
from tkinter import ttk


# Основные функции калькулятора
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def on_clear():
    entry.delete(0, tk.END)


def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Конвертер
def convert():
    try:
        value = float(entry.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()

        if conversion_type.get() == "Валюта":
            # Пример курса для валют
            rates = {
                "USD": 1, "EUR": 0.93, "RUB": 75.5, "GBP": 0.82
            }
            result = value * rates[to_unit] / rates[from_unit]

        elif conversion_type.get() == "Длина":
            # Пример конвертации длин
            lengths = {
                "мм": 1, "см": 10, "м": 1000, "км": 1000000
            }
            result = value * lengths[to_unit] / lengths[from_unit]

        elif conversion_type.get() == "Масса":
            # Пример конвертации массы
            masses = {
                "г": 1, "кг": 1000, "т": 1000000
            }
            result = value * masses[to_unit] / masses[from_unit]

        elif conversion_type.get() == "Время":
            # Пример конвертации времени
            times = {
                "с": 1, "мин": 60, "ч": 3600, "д": 86400
            }
            result = value * times[to_unit] / times[from_unit]

        elif conversion_type.get() == "Температура":
            # Пример конвертации температуры
            if from_unit == "Цельсий" and to_unit == "Фаренгейт":
                result = (value * 9 / 5) + 32
            elif from_unit == "Фаренгейт" and to_unit == "Цельсий":
                result = (value - 32) * 5 / 9
            elif from_unit == "Цельсий" and to_unit == "Кельвин":
                result = value + 273.15
            elif from_unit == "Кельвин" and to_unit == "Цельсий":
                result = value - 273.15
            elif from_unit == "Фаренгейт" and to_unit == "Кельвин":
                result = (value - 32) * 5 / 9 + 273.15
            elif from_unit == "Кельвин" and to_unit == "Фаренгейт":
                result = (value - 273.15) * 9 / 5 + 32

        # Выводим результат
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Создаем окно
window = tk.Tk()
window.title("Калькулятор с конвертером")
window.geometry("500x700")
window.config(bg="#1e1e1e")

# Экран ввода
entry = tk.Entry(window, width=20, font=('Arial', 30), borderwidth=0, relief="flat", justify="right", bd=10,
                 bg="#2f2f2f", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


# Функция для рисования круглых кнопок с помощью Canvas
def create_round_button(text, row, col, color="#444"):
    canvas = tk.Canvas(window, width=70, height=70, bg=color, bd=0, highlightthickness=0, relief="flat")
    canvas.grid(row=row, column=col, padx=10, pady=10)

    # Рисуем круг на canvas
    canvas.create_oval(10, 10, 60, 60, fill=color, outline="white", width=2)

    # Добавляем текст
    canvas.create_text(35, 35, text=text, font=('Arial', 20), fill="white")

    # Привязываем действие к кнопке
    canvas.bind("<Button-1>", lambda event, val=text: on_button_click(val) if val != "=" else on_equal())

    return canvas


# Размещение кнопок калькулятора
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Размещение кнопок калькулятора
for (text, row, col) in buttons:
    color = "#444" if text not in ('+', '-', '*', '/', '=', '.') else "#ff914d"
    create_round_button(text, row, col, color=color)

# Кнопка очистки
clear_button = tk.Button(window, text='C', font=('Arial', 20), width=5, height=2, bg="#ff6f61", fg="white", bd=0,
                         relief="flat", command=on_clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Конвертер
conversion_type = tk.StringVar(value="Валюта")
conversion_label = tk.Label(window, text="Тип конверсии", font=('Arial', 14), fg="white", bg="#1e1e1e")
conversion_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

conversion_options = ["Валюта", "Длина", "Масса", "Время", "Температура"]
conversion_menu = ttk.Combobox(window, textvariable=conversion_type, values=conversion_options, font=('Arial', 14),
                               state="readonly")
conversion_menu.grid(row=6, column=2, columnspan=2, padx=20, pady=10)

# Поля для выбора единиц
from_unit_label = tk.Label(window, text="Из", font=('Arial', 14), fg="white", bg="#1e1e1e")
from_unit_label.grid(row=7, column=0, padx=10, pady=10)

to_unit_label = tk.Label(window, text="В", font=('Arial', 14), fg="white", bg="#1e1e1e")
to_unit_label.grid(row=7, column=2, padx=10, pady=10)

# Комбобоксы для единиц
from_unit_combobox = ttk.Combobox(window, font=('Arial', 14))
to_unit_combobox = ttk.Combobox(window, font=('Arial', 14))


# Функция обновления доступных единиц в зависимости от типа конверсии
def update_units(*args):
    if conversion_type.get() == "Валюта":
        from_unit_combobox["values"] = ["USD", "EUR", "RUB", "GBP"]
        to_unit_combobox["values"] = ["USD", "EUR", "RUB", "GBP"]
    elif conversion_type.get() == "Длина":
        from_unit_combobox["values"] = ["мм", "см", "м", "км"]
        to_unit_combobox["values"] = ["мм", "см", "м", "км"]
    elif conversion_type.get() == "Масса":
        from_unit_combobox["values"] = ["г", "кг", "т"]
        to_unit_combobox["values"] = ["г", "кг", "т"]
    elif conversion_type.get() == "Время":
        from_unit_combobox["values"] = ["с", "мин", "ч", "д"]
        to_unit_combobox["values"] = ["с", "мин", "ч", "д"]
    elif conversion_type.get() == "Температура":
        from_unit_combobox["values"] = ["Цельсий", "Фаренгейт", "Кельвин"]
        to_unit_combobox["values"] = ["Цельсий", "Фаренгейт", "Кельвин"]

# Привязываем обновление списка единиц при изменении типа конверсии
conversion_menu.bind("<<ComboboxSelected>>", update_units)

# Вызов функции обновления сразу после старта
update_units()

from_unit_combobox.grid(row=8, column=0, padx=10, pady=10)
to_unit_combobox.grid(row=8, column=2, padx=10, pady=10)

# Кнопка для конверсии
convert_button = tk.Button(window, text="Конвертировать", font=('Arial', 14), bg="#ff914d", fg="white", command=convert)
convert_button.grid(row=9, column=0, columnspan=4, padx=20, pady=20)

# Запуск окна
window.mainloop()
