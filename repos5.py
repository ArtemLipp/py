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
