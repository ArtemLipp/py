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
