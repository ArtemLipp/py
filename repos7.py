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
