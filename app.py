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
window.title("Стильный калькулятор")
window.geometry("400x600")
window.config(bg="#1e1e1e")

# Экран ввода
entry = tk.Entry(window, width=20, font=('Arial', 30), borderwidth=0, relief="flat", justify="right", bd=10, bg="#2f2f2f", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Стиль для кнопок
button_style = {
    "font": ('Arial', 20),
    "width": 5,
    "height": 2,
    "bd": 0,
    "fg": "white",
    "relief": "flat",
    "bg": "#3a3a3a",
}

# Функция для создания кнопок
def create_button(text, row, col, width=5, height=2, color="#444"):
    button = tk.Button(window, text=text, font=('Arial', 20), width=width, height=height, bg=color, fg="white", bd=0, relief="flat",
                       command=lambda t=text: on_button_click(t) if t != "=" else on_equal())
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    button.bind("<Enter>", lambda e, b=button: b.config(bg="#4c4c4c"))
    button.bind("<Leave>", lambda e, b=button: b.config(bg=color))
    return button

# Размещение кнопок
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Размещение обычных кнопок
for (text, row, col) in buttons:
    color = "#444" if text not in ('+', '-', '*', '/', '=', '.') else "#ff914d"
    create_button(text, row, col, color=color)

# Кнопка очистки
clear_button = tk.Button(window, text='C', font=('Arial', 20), width=5, height=2, bg="#ff6f61", fg="white", bd=0, relief="flat", command=on_clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Сделаем кнопки растягивающимися по сетке
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Запуск окна
window.mainloop()
