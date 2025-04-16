import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def plot_function(func_str, x_range=(-10, 10), num_points=1000):
    # Создаем массив значений x
    x = np.linspace(x_range[0], x_range[1], num_points)

    # Используем eval для вычисления значений функции
    try:
        y = eval(func_str)
    except Exception as e:
        print(f"Ошибка при вычислении функции: {e}")
        return

    # Строим график
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'y = {func_str}')
    plt.title('График функции')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

def on_plot_button_click():
    func_input = entry.get()  # Получаем текст из текстового поля
    plot_function(func_input)

root = tk.Tk()
root.title("World of Math")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Текстовое поле для ввода функции
entry = tk.Entry(root, width=50)
entry.place(x=100, y=100)

button = tk.Button(root, text="Выключить", height=4, width=20, fg='#000',
                   bg='#fff', activebackground='#000',
                   activeforeground='#000', cursor='hand2', command=root.destroy)
button.place(x=700, y=700)

button1 = tk.Button(root, text="Построение функции", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=on_plot_button_click)
button1.place(x=100, y=200)

button2 = tk.Button(root, text="Homyak", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=root.destroy)
button2.place(x=630, y=200)

button3 = tk.Button(root, text="Faster", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=root.destroy)
button3.place(x=1160, y=200)

root.mainloop()
