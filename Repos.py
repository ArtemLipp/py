# Практическое задание 4 - Все варианты

# Вариант 1
print("=== Вариант 1 ===")

# Задание 1
num = int(input("Введите число: "))
if num < 0:
    num = -num
    print(num)
elif num == 0:
    num = 1
    print(num)
else:
    print(num)

# Задание 2
text = input("Введите строку: ")
if '.' in text or ',' in text:
    print(True)
else:
    print(False)

# Задание 3
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 % 3 == 0 and num2 % 3 == 0:
    print(True)
elif num1 % 3 == 0 or num2 % 3 == 0:
    print("Одно число делится на 3")
else:
    print(False)

# Вариант 2
print("\n=== Вариант 2 ===")

# Задание 1
num = int(input("Введите число: "))
if num > 100:
    print("*")
elif num > 0:
    print("*" * num)

# Задание 2
str1 = input("Первая строка: ")
str2 = input("Вторая строка: ")
if str1 == str2:
    print(True)
else:
    print(False)

# Задание 3
r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))
if r == 0 and g == 0 and b == 0:
    print("Чёрный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")

# Вариант 3
print("\n=== Вариант 3 ===")

# Задание 1
num = int(input("Введите число: "))
if num > 0:
    print(num-1, num, num+1)
else:
    num = 1
    print(num-1, num, num+1)

# Задание 2
filename = input("Имя файла: ")
if filename.endswith('.doc'):
    print("Word file")
elif filename.endswith('.py'):
    print("Python file")
elif filename.endswith('.txt'):
    print("Text file")
else:
    print("Неизвестный формат")

# Задание 3
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

# Вариант 4
print("\n=== Вариант 4 ===")

# Задание 1
text = 'important information in one line'
letter = input("Введите букву: ")
if letter in text:
    print(True)
else:
    print(False)

# Задание 2
side1 = float(input("Первая сторона: "))
side2 = float(input("Вторая сторона: "))
if side1 == side2:
    print("Квадрат, площадь:", side1 * side2)
else:
    print("Прямоугольник, площадь:", side1 * side2)

# Задание 3
answer = input("Как твои дела? ")
if answer in ["хорошо", "нормально", "отлично"]:
    print("😊")
elif answer in ["плохо", "не хорошо", "..."]:
    print("😢")
else:
    print("😐")

# Вариант 5
print("\n=== Вариант 5 ===")

# Задание 1
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 > num2:
    print(num1 ** num2)
elif num2 > num1:
    print(num2 ** num1)
else:
    print(num1 + num2)

# Задание 2
new_message = "Hello! How are you?"
user_answer = input("Введите ответ: ")
if new_message[0] == user_answer[0]:
    print(True)
else:
    print(False)

# Задание 3
segment1 = float(input("Длина первого отрезка: "))
segment2 = float(input("Длина второго отрезка: "))
if segment1 > segment2:
    print("Первый отрезок длиннее на", segment1 - segment2)
elif segment2 > segment1:
    print("Второй отрезок длиннее на", segment2 - segment1)
else:
    print("Отрезки равны")

# Вариант 6
print("\n=== Вариант 6 ===")

# Задание 1
text = input("Введите строку: ")
if text[0] == text[-1]:
    print(True)
else:
    print(False)

# Задание 2
num = int(input("Введите число: "))
if num % 2 == 0:
    print(num ** 2)
elif num % 3 == 0:
    print(num ** 3)
else:
    print(num * 100)

# Задание 3
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 < 0 and num2 < 0:
    print(False)
elif num1 < 0:
    num1 += 1000
    print(num1, num2)
elif num2 < 0:
    num2 += 1000
    print(num1, num2)
else:
    print(True)

# Вариант 7
print("\n=== Вариант 7 ===")

# Задание 1
text = input("Введите строку: ")
if text[-1] in ['я', 'и', 'е', 'ю']:
    print(True)
else:
    print(False)

# Задание 2
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print(True)
    else:
        print(False)
else:
    print(False)

# Задание 3
num = int(input("Введите число: "))
last_digit = num % 10
if last_digit == 0:
    print(num ** 10)
elif last_digit == 1:
    print(num % 3)
elif last_digit == 2:
    print(num // 2)
else:
    print(num ** 2)

# Вариант 8
print("\n=== Вариант 8 ===")

# Задание 1
password = input("Введите пароль: ")
if len(password) < 8 or password == "qwerty123":
    print(False)
else:
    print(True)

# Задание 2
pc_number = 777
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if (num1 < pc_number < num2) or (num2 < pc_number < num1):
    print(True)
else:
    print(False)

# Задание 3
lamp_1 = 0
lamp_2 = 0
choice = input("Какую лампочку зажечь? ")
if choice == "1":
    lamp_1 = 1
    print("Лампочка 1 горит")
elif choice == "2":
    lamp_2 = 1
    print("Лампочка 2 горит")
else:
    print("Обе лампочки не горят")

# Вариант 9
print("\n=== Вариант 9 ===")

# Задание 1
switch_1 = False
switch_2 = False
answer = input("Включить? ")
if answer == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
    print("switch_1 =", switch_1)
    print("switch_2 =", switch_2)
else:
    print("switch_1 =", switch_1)
    print("switch_2 =", switch_2)

# Задание 2
num = int(input("Введите число: "))
if num > 0:
    if num % 2 == 0:
        print(True, "even")
    else:
        print(True, "odd")
else:
    print(False)

# Задание 3
text = input("Введите строку: ")
if text.startswith('/'):
    print("command")
else:
    print("It's string")

# Вариант 10
print("\n=== Вариант 10 ===")

# Задание 1
text = input("Введите строку: ")
length = len(text)
if length == 0:
    print(None)
elif length <= 5:
    print("short")
elif 6 <= length <= 10:
    print("normal")
else:
    print("long")

# Задание 2
num = int(input("Введите число: "))
if num < 0:
    num = 1000000
    print(num)
elif num == 0:
    num = 2
    print(num ** 2)
else:
    print(num ** 3)

# Задание 3
number_1 = 10
number_2 = 100
user_num = int(input("Введите число: "))
if number_1 < user_num < number_2:
    print(True)
else:
    print(False)

# Вариант 11
print("\n=== Вариант 11 ===")

# Задание 1
prog_num = 0
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
if num1 < 0 and num2 < 0:
    prog_num = num1 + num2
    print(prog_num)
elif num1 > 0 and num2 > 0:
    prog_num = num1 - num2
    print(prog_num)
else:
    print(False)

# Задание 2
num = int(input("Введите число: "))
if num % 2 == 1:
    num += 1
    print(num)
else:
    print(True)

# Задание 3
text = input("Введите строку: ")
if len(text) > 10:
    print(text[:5])
else:
    print(text)

# Вариант 12
print("\n=== Вариант 12 ===")

# Задание 1
ru = 'a6Brдеёжзийклинопрстуфхцчищbblbэюя'
en = 'abcdefghijklmnopqrstuvwxyz'
letter = input("Введите букву: ")
if letter in ru:
    print("rus")
elif letter in en:
    print("eng")
else:
    print(None)

# Задание 2
pc_num = 10
user_num = int(input("Введите число: "))
if user_num == pc_num or user_num == pc_num-1 or user_num == pc_num+1:
    print(True)
else:
    print(False)

# Задание 3
print('(221 - 13) * 2')
correct_answer = (221 - 13) * 2
user_answer = int(input("Ваш ответ: "))
if user_answer == correct_answer:
    print(True)
elif user_answer > correct_answer:
    print(">")
else:
    print("<")
# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 5 ==========

print("=== Практическое задание 5 ===")

# Задание 1
print("\n--- Задание 1 ---")
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']

print("Исходный список:", m)

# Удаляем элементы, которые не являются названиями фигур
if 0.25 in m:
    m.remove(0.25)
if 15 in m:
    m.remove(15)
if '10' in m:
    m.remove('10')

print("Только названия фигур:", m)

# Задание 2
print("\n--- Задание 2 ---")
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print("Исходный список:", abc)

# Удаляем элементы с 1 по 4 индекс
del abc[1:5]

print("Результат:", abc)

# Задание 3
print("\n--- Задание 3 ---")
numbers = [1, 4]
print("Исходный список:", numbers)

# Добавляем недостающие цифры
numbers.insert(1, 2)
numbers.insert(2, 3)

print("Результат:", numbers)

# Задание 4
print("\n--- Задание 4 ---")
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
print("Исходный список:", mass)

# Удаляем отрицательные числа
new_mass = []
for num in mass:
    if num >= 0:
        new_mass.append(num)

# Сортируем
new_mass.sort()
print("По возрастанию:", new_mass)

new_mass.sort(reverse=True)
print("По убыванию:", new_mass)

# Задание 5
print("\n--- Задание 5 ---")
negative = []
positive = []
zeros = []

n = int(input("Введите количество чисел: "))
print("Введите числа:")

for i in range(n):
    num = int(input())
    if num < 0:
        negative.append(num)
    elif num > 0:
        positive.append(num)
    else:
        zeros.append('*')

# Сумма отрицательных
sum_neg = sum(negative)
print("Сумма отрицательных:", sum_neg)

# Среднее положительных
if len(positive) > 0:
    avg_pos = sum(positive) / len(positive)
    print("Среднее положительных:", avg_pos)
else:
    print("Положительных чисел нет")

# Обработка нулей
print("Количество нулей:", len(zeros))
print("Нули заменены на *:", zeros)

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 6 ==========

print("\n\n=== Практическое задание 6 ===")

# Задание 1
print("\n--- Задание 1 ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)

print("\nнечётные числа matrix")
odd_numbers = []
even_count = 0

for row in matrix:
    for element in row:
        if element % 2 == 1:
            odd_numbers.append(element)
            print(element, end=' ')
        else:
            even_count += 1

print("\nкол-во чётных:", even_count)

# Задание 2
print("\n--- Задание 2 ---")
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

# Создаем матрицу для ответа
answer_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]

# Перемножаем
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

print("Результат умножения:")
for row in answer_matrix:
    print(row)

print("\nСуммы строк:")
for row in answer_matrix:
    row_sum = sum(row)
    print(row, "сумма строки:", row_sum)

# Задание 3
print("\n--- Задание 3 ---")
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], 
          ['lime', 'lemon'], ['Mango', 'grapes']]

print("Элементы с заглавной буквы:")
for row in fruits:
    for fruit in row:
        if fruit[0].isupper():
            print(fruit)

# Задание 4
print("\n--- Задание 4 ---")
random_elements = [['toy', 'bee', 'cheese', 'ear'], 
                   [False, 'word', '0110110', 10], 
                   ['happiness', '(1 °□°)1 ', 'luck', None], 
                   ['car', '<- code ->', 4.7, True]]

print("Каждый второй элемент:")
for i, row in enumerate(random_elements):
    if i % 2 == 1:  # индексы 1, 3 (второй и четвертый)
        print(f"Строка {i}:", row)

# Задание 5
print("\n--- Задание 5 ---")
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = input(f"Введите значение элемента [{i}][{j}]: ")
        # Пробуем преобразовать в число
        try:
            value = int(value)
        except:
            try:
                value = float(value)
            except:
                pass
        row.append(value)
    matrix.append(row)

print("\nВаш двумерный массив:")
for row in matrix:
    print(row)

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 7 ==========

print("\n\n=== Практическое задание 7 ===")

# Задание 1
print("\n--- Задание 1 ---")
# Создаем двумерный массив как в таблице
table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]

print("начальный список")
for row in table:
    print(row)

# 1. Удаляем папки и заменяем data.accdb на data.sql
new_table = []
for row in table:
    new_row = []
    for item in row:
        if item != 'folder':
            if item == 'data.accdb':
                new_row.append('data.sql')
            else:
                new_row.append(item)
    new_table.append(new_row)

print("\nбез папок и с заменой data")
for row in new_table:
    print(row)

# 2. Все файлы .py
print("\nвсе файлы.py")
py_files = []
for row in new_table:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

for file in py_files:
    print(file, end=' ')
print()

# 3. Все файлы .js с префиксом new_
print("\nвсе new_файлы.js")
js_files = []
for row in new_table:
    for item in row:
        if item.endswith('.js'):
            js_files.append('new_' + item)

for file in js_files:
    print(file, end=' ')
print()

# Задание 2
print("\n--- Задание 2 ---")
word_numb = ["ноль", "один", "два", "три", "четыре", "пять",
             "шесть", "семь", "восемь", "девять"]

n = int(input("Введите число от 0 до 9: "))
if n <= 9:
    for i in range(n + 1):
        print(word_numb[i])
else:
    print('Введите число <= 9')

# Задание 3
print("\n--- Задание 3 ---")
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']

decimals = []
print("Десятичные числа:")
for binary in bin_sy:
    decimal = int(binary, 2)
    decimals.append(decimal)
    print(decimal)

print("Максимальное:", max(decimals))
print("Минимальное:", min(decimals))

# Задание 4
print("\n--- Задание 4 ---")
# Создаем матрицу как в задании (предположим, что слово это 'слово')
matr = [
    [1, 2, 3],
    [4, 'слово', 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matr:
    print(row)

# Заменяем слово на количество символов
for i, row in enumerate(matr):
    for j, element in enumerate(row):
        if isinstance(element, str):
            matr[i][j] = len(element)

print("\nМатрица после замены:")
for row in matr:
    print(row)

# Сумма всех элементов
total_sum = 0
for row in matr:
    for element in row:
        total_sum += element

print("Сумма всех элементов:", total_sum)

# 
# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 8 ==========

print("=== Практическое задание 8 ===")

# Задание 1
print("\n--- Задание 1 ---")
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}

print("1. Исходный словарь:")
print(my_dict)

# Убираем ключ с шестнадцатеричной системой счисления (3:'1A14C')
print("\n2. Убираем ключ с шестнадцатеричным значением (ключ 3):")
if 3 in my_dict:
    my_dict.pop(3)
print(my_dict)

# Добавляем новое значение
print("\n3. Добавляем значение 0100101 с ключом 10:")
my_dict[10] = '0100101'
print(my_dict)

# Задание 2
print("\n--- Задание 2 ---")
s1 = {'</>':13, 'script':1, '__init__':10, 'self':5, 'number_9':6, '#comment':100}

print("Исходный словарь:")
print(s1)

print("\nДобавление нового элемента:")
key = input("key: ")
value = input("value: ")
s1[key] = value

print("\nОбновленный словарь:")
print(s1)

# Задание 3
print("\n--- Задание 3 ---")
my_dict2 = {}
print("Создаем словарь из 3 элементов (ключи должны быть числами):")

while len(my_dict2) < 3:
    try:
        key_input = input(f"Введите ключ (число) для элемента {len(my_dict2)+1}: ")
        key_num = int(key_input)
        value_input = input(f"Введите значение для ключа {key_num}: ")
        my_dict2[key_num] = value_input
        print(f"Текущий словарь: {my_dict2}")
    except ValueError:
        print("Ошибка! Ключ должен быть числом. Попробуйте снова.")

print("\nИтоговый словарь из 3 элементов:")
print(my_dict2)

# Задание 4
print("\n--- Задание 4 ---")
a11_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}

print("Исходный словарь:")
print(a11_d)

# Убираем элементы с ключами 1, 101, 3
keys_to_remove = [1, 101, 3]
for key in keys_to_remove:
    if key in a11_d:
        del a11_d[key]

print("\nСловарь после удаления ключей 1, 101, 3:")
print(a11_d)

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 9 ==========

print("=== Записная книжка ===")

# Создаем словарь для записной книжки
notebook = {}

# Функция для добавления заметки
def add_note():
    global notebook  # говорим, что будем менять внешний словарь
    print("\n--- Добавление новой заметки ---")
    header = input("Header: ")
    text = input("Text: ")
    notebook[header] = text
    print(f"Заметка '{header}' добавлена!")

# Функция для чтения заметок
def read_notes():
    global notebook
    print("\n--- Чтение заметок ---")
    
    # Проверяем, есть ли заметки
    if len(notebook) == 0:
        print("Заметок нет.")
        return
    
    # Показываем все названия заметок
    print("Доступные заметки:")
    for header in notebook.keys():
        print(f"- {header}")
    
    # Просим выбрать заметку
    choice = input("\nКакую заметку прочитать? (введите название): ")
    
    # Проверяем, есть ли такая заметка
    if choice in notebook:
        print(f"\n--- {choice} ---")
        print(notebook[choice])
    else:
        print("Такой заметки нет.")

# Функция для удаления заметки
def delete_note():
    global notebook
    print("\n--- Удаление заметки ---")
    
    # Проверяем, есть ли заметки
    if len(notebook) == 0:
        print("Заметок нет.")
        return
    
    # Показываем все названия заметок
    print("Доступные заметки:")
    for header in notebook.keys():
        print(f"- {header}")
    
    # Просим выбрать заметку для удаления
    choice = input("\nКакую заметку удалить? (введите название): ")
    
    # Проверяем, есть ли такая заметка
    if choice in notebook:
        notebook.pop(choice)
        print(f"Заметка '{choice}' удалена!")
    else:
        print("Такой заметки нет.")

# Функция меню
def menu():
    while True:
        print("\n" + "="*50)
        print("МЕНЮ ЗАПИСНОЙ КНИЖКИ")
        print("[1] - Создать новую заметку")
        print("[2] - Прочитать заметки")
        print("[3] - Удалить заметку")
        print("[4] - Выход")
        print("="*50)
        
        choice = input("Ваш выбор (1-4): ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор! Введите число от 1 до 4.")

# Запускаем программу
print("Добро пожаловать в записную книжку!")
menu()

# ========== ПРИМЕР РАБОТЫ ПРОГРАММЫ ==========
print("\n\n=== Пример работы программы ===")

# Показываем выглядела работа программы
print("""
Пример работы:

[1] - Создать новую заметку
[2] - Прочитать заметки
[3] - Удалить заметку
[4] - Выход
> 1

--- Добавление новой заметки ---
Header: Мои любимые книги
Text: 1. Гарри Поттер 2. Учебник по Python
Заметка 'Мои любимые книги' добавлена!

[1] - Создать новую заметку
[2] - Прочитать заметки
[3] - Удалить заметку
[4] - Выход
> 1

--- Добавление новой заметки ---
Header: Мои пароли
Text: почта - qwerty123
Заметка 'Мои пароли' добавлена!

[1] - Создать новую заметку
[2] - Прочитать заметки
[3] - Удалить заметку
[4] - Выход
> 2

--- Чтение заметок ---
Доступные заметки:
- Мои любимые книги
- Мои пароли

Какую заметку прочитать? (введите название): Мои любимые книги

--- Мои любимые книги ---
1. Гарри Поттер 2. Учебник по Python

[1] - Создать новую заметку
[2] - Прочитать заметки
[3] - Удалить заметку
[4] - Выход
> 3

--- Удаление заметки ---
Доступные заметки:
- Мои любимые книги
- Мои пароли

Какую заметку удалить? (введите название): Мои пароли
Заметка 'Мои пароли' удалена!

[1] - Создать новую заметку
[2] - Прочитать заметки
[3] - Удалить заметку
[4] - Выход
> 4
Выход из программы. До свидания!
""")


# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 10 ==========

print("\n\n=== Практическое задание 10 ===")

# Задание 1
print("\n--- Задание 1 ---")
def upper(t):
    result = ""
    for char in t:
        if char.isupper():
            result += char + " "
    return result

print("Результат функции upper('PriVet'):")
result1 = upper('PriVet')
if result1:
    print(result1)
else:
    print("(ничего)")

# Задание 2
print("\n--- Задание 2 ---")
def punct(txt):
    signs = "!?.,()"
    count = 0
    for char in txt:
        if char in signs:
            count += 1
    return count

print("Результат функции punct('(Как дела?)'):")
print(punct('(Как дела?)'))

# Задание 3
print("\n--- Задание 3 ---")
def create_cube(x, y):
    for i in range(y):
        print("*" * x)

print("Результат функции create_cube(5, 3):")
create_cube(5, 3)

# Задание 4
print("\n--- Задание 4 ---")
def double(text):
    result = ""
    for char in text:
        result += char * 2
    return result

print("Результат функции double('строка'):")
print(double('строка'))

# Задание 5
print("\n--- Задание 5 ---")
def Constructor(details, people, cars, trees):
    # В наборе: 72 детали, 4 фигурки, 2 машины, 7 деревьев
    sets_details = details // 72
    sets_people = people // 4
    sets_cars = cars // 2
    sets_trees = trees // 7
    
    # Находим минимальное количество полных наборов
    full_sets = min(sets_details, sets_people, sets_cars, sets_trees)
    return full_sets

print("Результат функции Constructor(144, 8, 4, 14):")
print(Constructor(144, 8, 4, 14))

print("\nРезультат функции Constructor(10000, 16, 6, 2):")
print(Constructor(10000, 16, 6, 2))

# Задание 6
print("\n--- Задание 6 ---")
def create_list(length, value=0):
    result = []
    for i in range(length):
        result.append(value)
    return result

print("Результат функции create_list(5, 3):")
print(create_list(5, 3))

print("\nРезультат функции create_list(3):")
print(create_list(3))

# Задание 7
print("\n--- Задание 7 ---")
def custom_filter(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):
            if item % 7 == 0:
                total += item
    
    print(f"сумма: {total}")
    if total <= 83:
        return True
    else:
        return False

print("Результат функции custom_filter([7, 10.5, 'txt', 14, 2, 56]):")
result7 = custom_filter([7, 10.5, 'txt', 14, 2, 56])
print(result7)

# Задание 8
print("\n--- Задание 8 ---")
def square(x, y):
    # Верхняя граница
    print("_" * (x * 3 + 2))
    
    # Числа
    for i in range(y):
        row = "|"
        for j in range(x):
            row += f" {j+1} |"
        print(row)
    
    # Нижняя граница
    print("-" * (x * 3 + 2))

print("Результат функции square(2, 3):")
square(2, 3)

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 11 ==========

print("\n\n=== Практическое задание 11 ===")

def time_to_travel_around_planet(robot_speed, planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    
    pi = 3.14159
    # Длина окружности = π * диаметр
    circumference = pi * planet_diameter
    # Время = расстояние / скорость
    time = circumference / robot_speed
    
    return time

# Пример использования
print("Пример 1:")
robot_speed = 10  # км/ч
planet_diameter = 12742  # км (диаметр Земли)
robot_name = "Igor_bot V.2.0"
planet_name = "Земля"

calculation_1 = time_to_travel_around_planet(robot_speed, planet_diameter)
print(f"Роботу {robot_name} необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты {planet_name}.")

print("\nПример 2 (с ошибкой):")
result_error = time_to_travel_around_planet(0, 100)
print(result_error)

print("\nПример 3 (пользовательский ввод):")
try:
    speed = float(input("Введите скоростскорость (км/ч): "))
    diameter = float(input("Введите диаметр планеты (км): "))
    
    result = time_to_travel_around_planet(speed, diameter)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Время для объезда планеты: {result:.2f} часов")
except ValueError:
    print("Ошибка! Введите числа.")

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 12 ==========

print("=== Практическое задание 12 (Лямбда-функции) ===")

# Задание 1
print("\n--- Задание 1 ---")
# Создаем лямбда-функцию для умножения двух чисел
x = lambda a, b: a * b

print("Результат x(2, 3):")
print(x(2, 3))

# Задание 2
print("\n--- Задание 2 ---")
# Пользователь вводит количество чисел
count = int(input("Всего чисел будет: "))

# Создаем список для чисел
numbers_list = []

# Заполняем список
for i in range(count):
    try:
        num = int(input(f"Введите число {i+1}: "))
        numbers_list.append(num)
    except ValueError:
        print("Это не число! Пропускаем...")

print(f"\nВведенный список: {numbers_list}")

# Используем filter для чисел, кратных 3 и 5
# Число должно делиться и на 3, и на 5 одновременно
filtered_numbers = list(filter(lambda n: n % 3 == 0 and n % 5 == 0, numbers_list))

print(f"Числа, кратные 3 и 5: {filtered_numbers}")

# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 13 ==========

print("\n\n=== Практическое задание 13 ===")

# Задание 1
print("\n--- Задание 1 ---")
def alpha(user_string):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    print("Полный алфавит:")
    print(" ".join(alphabet))
    
    # Буквы из строки пользователя
    used_letters = ""
    for char in user_string.lower():
        if char in alphabet and char not in used_letters:
            used_letters += char
    
    print(f"\nБуквы из строки '{user_string}':")
    print(" ".join(used_letters))
    
    # Оставшиеся буквы
    remaining = ""
    for char in alphabet:
        if char not in used_letters:
            remaining += char
    
    print("\nОставшиеся буквы:")
    print(" ".join(remaining))

print("Результат alpha('пайтон'):")
alpha('пайтон')

# Задание 2
print("\n--- Задание 2 ---")
def create_calendar(month, year, days):
    print(f"\ncalendar: {month} {year}")
    print("-" * 20)
    
    # Выводим дни по 7 в строке
    day_counter = 1
    while day_counter <= days:
        row = ""
        for i in range(7):
            if day_counter <= days:
                row += str(day_counter) + " "
                day_counter += 1
            else:
                break
        print(row.strip())

print("Результат create_calendar('Randomner', 2045, 23):")
create_calendar('Randomner', 2045, 23)

# Задание 3
print("\n--- Задание 3 ---")
def bin_sys(start, end):
    total = 0
    for i in range(start, end + 1):
        binary = bin(i)[2:]  # убираем '0b' в начале
        print(binary)
        total += i
    
    print(f"сумма: {bin(total)[2:]}")

print("Результат bin_sys(3, 6):")
bin_sys(3, 6)

# Задание 4
print("\n--- Задание 4 ---")
def begin(field, row, col):
    print("Исходное поле:")
    for r in field:
        print(" ".join(r))
    
    # Заменяем элемент
    if 0 <= row < len(field) and 0 <= col < len(field[0]):
        field[row][col] = '*'
    
    print("\nПоле после изменения:")
    for r in field:
        print(" ".join(r))

# Создаем поле
field = [['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]']]

print("Результат begin(field, 1, 2):")
begin(field, 1, 2)

# Задание 5
print("\n--- Задание 5 ---")
def _numbers(n1, step=1):
    # Вычисляем значения для поля 2x2
    n2 = n1 + 1 * step
    n3 = n1 + 2 * step
    n4 = n1 + 3 * step
    
    # Выводим поле
    print(f"[{n1}] [{n2}]")
    print(f"[{n3}] [{n4}]")

print("Результат _numbers(1):")
_numbers(1)

print("\nРезультат _numbers(1, 2):")
_numbers(1, 2)

# Задание 6
print("\n--- Задание 6 ---")
def exam(text, letter):
    count = 0
    text_lower = text.lower()
    letter_lower = letter.lower()
    
    for char in text_lower:
        if char == letter_lower:
            count += 1
    
    print(f"Буква '{letter}' встречается {count} раз(а) в тексте")

print("Результат exam('My name is Sara.', 's'):")
exam('My name is Sara.', 's')
