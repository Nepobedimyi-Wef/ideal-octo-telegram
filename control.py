import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
import sympy as sp

def calc():
    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Калькулятор")

            self.result_var = tk.StringVar()

            # Поле ввода для отображения результата
            self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2,
                                  width=14, borderwidth=4)
            self.entry.grid(row=0, column=0, columnspan=4)

            self.create_buttons()

        def create_buttons(self):
            # Определяем кнопки калькулятора
            buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+'
            ]

            row_val = 1
            col_val = 0

            for button in buttons:
                if button == '=':
                    btn = tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                                    command=self.calculate)
                else:
                    btn = tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                                    command=lambda b=button: self.append_to_expression(b))
                btn.grid(row=row_val, column=col_val)

                col_val += 1
                if col_val > 3:
                    col_val = 0
                    row_val += 1

        def append_to_expression(self, value):
            # Добавляем нажатую кнопку к текущему выражению
            current_text = self.result_var.get()
            new_text = current_text + value
            self.result_var.set(new_text)

        def calculate(self):
            # Вычисляем результат выражения
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Ошибка")

    if __name__ == "__main__":
        root2 = tk.Tk()  # Изменено на root2
        calculator = Calculator(root2)  # Изменено на root2
        root2.mainloop()  # Изменено на root2

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

def open():

    def solve_equation(equation_str, variable_str):
        # Определяем переменную
        variable = sp.symbols(variable_str)

        # Преобразуем строку уравнения в символьное выражение
        equation = sp.sympify(equation_str)

        # Решаем уравнение
        solutions = sp.solve(equation, variable)

        return solutions

    def on_solve():
        equation = equation_entry.get()
        variable = variable_entry.get()

        try:
            solutions = solve_equation(equation, variable)
            result = f"Решения уравнения {equation} = 0: {solutions}"
            messagebox.showinfo("Решение", result)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    # Создаем окно
    root1 = tk.Tk()
    root1.title("Решение уравнений")

    # Создаем виджеты
    equation_label = tk.Label(root1, text="Введите уравнение равное 0:")
    equation_label.pack()

    equation_entry = tk.Entry(root1, width=40)
    equation_entry.pack()

    variable_label = tk.Label(root1, text="Введите переменную:")
    variable_label.pack()

    variable_entry = tk.Entry(root1, width=10)
    variable_entry.pack()

    solve_button = tk.Button(root1, text="Решить", command=on_solve)
    solve_button.pack()
    root1.mainloop()

label = tk.Label(root, text="Введите функцию для построения графика")
label.place(x=100, y=130)

# Текстовое поле для ввода функции
entry = tk.Entry(root, width=50)
entry.place(x=100, y=160)

button = tk.Button(root, text="Выключить", height=4, width=20, fg='#000',
                   bg='#fff', activebackground='#000',
                   activeforeground='#000', cursor='hand2', command=root.destroy)
button.place(x=700, y=700)

button1 = tk.Button(root, text="Построение функции", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=on_plot_button_click)
button1.place(x=100, y=200)

button2 = tk.Button(root, text="Решение уравнения", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=open)
button2.place(x=630, y=200)

button3 = tk.Button(root, text="Калькулятор", height=15, width=40, fg='#000',
                    bg='#fff', activebackground='#000',
                    activeforeground='#000', cursor='hand2', command=calc)
button3.place(x=1160, y=200)

root.mainloop()
