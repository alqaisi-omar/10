import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ФИО автора")
        
        # Создание вкладок
        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Калькулятор')
        self.tabControl.add(self.tab2, text='Чекбоксы')
        self.tabControl.add(self.tab3, text='Работа с текстом')
        self.tabControl.pack(expand=1, fill="both")
        
        # Вкладка Калькулятор
        self.create_calculator()
        
        # Вкладка Чекбоксы
        self.create_checkboxes()
        
        # Вкладка Работа с текстом
        self.create_text_work()
        
    def create_calculator(self):
        # Определение переменных
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        self.operation_var = tk.StringVar()  # Переменная для хранения выбранной операции
        
        # Создание элементов интерфейса
        label1 = ttk.Label(self.tab1, text="Первое число:")
        entry1 = ttk.Entry(self.tab1, textvariable=self.num1)
        label2 = ttk.Label(self.tab1, text="Второе число:")
        entry2 = ttk.Entry(self.tab1, textvariable=self.num2)
        operation = ttk.Combobox(self.tab1, values=['+', '-', '*', '/'], textvariable=self.operation_var)
        operation.current(0)  # Установка значения по умолчанию
        calculate_btn = ttk.Button(self.tab1, text="Вычислить", command=self.calculate)
        result_label = ttk.Label(self.tab1, textvariable=self.result)
        
        # Размещение элементов на вкладке
        label1.grid(row=0, column=0, padx=5, pady=5)
        entry1.grid(row=0, column=1, padx=5, pady=5)
        label2.grid(row=1, column=0, padx=5, pady=5)
        entry2.grid(row=1, column=1, padx=5, pady=5)
        operation.grid(row=0, column=2, padx=5, pady=5)
        calculate_btn.grid(row=1, column=2, padx=5, pady=5)
        result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        
    def calculate(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            operation = self.operation_var.get()  # Получаем выбранную операцию
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            self.result.set(f"Результат: {result}")
        except ValueError:
            self.result.set("Ошибка: Введите числа")
        except ZeroDivisionError:
            self.result.set("Ошибка: Деление на ноль")
    
    def create_checkboxes(self):
        # Создание чекбоксов
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        checkbox1 = ttk.Checkbutton(self.tab2, text="Первый", variable=self.var1)
        checkbox2 = ttk.Checkbutton(self.tab2, text="Второй", variable=self.var2)
        checkbox3 = ttk.Checkbutton(self.tab2, text="Третий", variable=self.var3)
        button = ttk.Button(self.tab2, text="Показать выбор", command=self.show_choice)
        
        # Размещение элементов на вкладке
        checkbox1.grid(row=0, column=0, padx=5, pady=5)
        checkbox2.grid(row=1, column=0, padx=5, pady=5)
        checkbox3.grid(row=2, column=0, padx=5, pady=5)
        button.grid(row=3, column=0, padx=5, pady=5)
        
    def show_choice(self):
        choices = []
        if self.var1.get():
            choices.append("первый")
        if self.var2.get():
            choices.append("второй")
        if self.var3.get():
            choices.append("третий")
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
        
    def create_text_work(self):
        # Создание кнопки и привязка события к ней
        button = ttk.Button(self.tab3, text="Открыть файл", command=self.open_file)
        button.pack(padx=10, pady=10)
        
    def open_file(self):
        # Открытие файла и вывод его содержимого в сообщении
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            messagebox.showinfo("Содержимое файла", content)

# Создание и запуск приложения
app = Application()
app.mainloop()
