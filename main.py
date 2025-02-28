import tkinter as tk
from tkinter import scrolledtext

# Создание главного окна
root = tk.Tk()
root.title("Простой чат")
root.geometry("400x500")

# Функция для отправки сообщения
def send_message():
    message = message_entry.get()
    if message:
        chat_box.config(state=tk.NORMAL)  # Разрешаем редактирование чата
        chat_box.insert(tk.END, "Вы: " + message + '\n')  # Вставляем сообщение
        chat_box.config(state=tk.DISABLED)  # Запрещаем редактирование чата
        message_entry.delete(0, tk.END)  # Очищаем поле ввода

# Создание виджетов
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=20, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10)

message_entry = tk.Entry(root, width=35)
message_entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Отправить", width=20, command=send_message)
send_button.pack(padx=10, pady=10)

# Запуск главного цикла
root.mainloop()
