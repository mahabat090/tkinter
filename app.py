import tkinter as tk


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


# Создаем окно
window = tk.Tk()
window.title("Круглый калькулятор")
window.geometry("400x600")
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


# Размещение кнопок
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Размещение кнопок
for (text, row, col) in buttons:
    color = "#444" if text not in ('+', '-', '*', '/', '=', '.') else "#ff914d"
    create_round_button(text, row, col, color=color)

# Кнопка очистки
clear_button = tk.Button(window, text='C', font=('Arial', 20), width=5, height=2, bg="#ff6f61", fg="white", bd=0,
                         relief="flat", command=on_clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Настройка растягивания кнопок по сетке
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Запуск окна
window.mainloop()
