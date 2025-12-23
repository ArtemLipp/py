# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 14 ==========

print("\n\n=== Практическое задание 14 (Исключения) ===")

# Задание 1
print("\n--- Задание 1 ---")
def task1():
    while True:
        try:
            x = input("число: ")
            # Пробуем преобразовать в целое число
            x_int = int(x)
            if x_int > 0:
                # Выводим диапазон от 0 до x
                result = ""
                for i in range(x_int + 1):
                    result += str(i) + " "
                print(result.strip())
                break
            else:
                print("Число должно быть положительным. Попробуйте снова.")
        except ValueError:
            print(f"{x} - не число. Повторите ввод.")

print("Запуск задания 1:")
# task1()  # Раскомментировать для реального ввода

# Покажем пример работы
print("\nПример работы задания 1:")
print(">>> число: abc")
print(">>> abc - не число. Повторите ввод.")
print(">>> число: 6")
print(">>> 0 1 2 3 4 5 6")

# Задание 2
print("\n--- Задание 2 ---")
any_list = [4, 3.2, 16, 9, 13.5, 67]
print("Исходный список:", any_list)
print("\nДеление каждого элемента на его индекс:")

for index, value in enumerate(any_list):
    try:
        result = value / index
        print(f"{value} / {index} = {result}")
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {value}")

# Задание 3
print("\n--- Задание 3 ---")
def task3():
    numbers = []
    print("Введите 5 чисел:")
    
    while len(numbers) < 5:
        try:
            num = input(f"Введите число {len(numbers)+1}: ")
            # Пробуем преобразовать в число (может быть float)
            num_float = float(num)
            numbers.append(num_float)
            print(f"Добавлено: {num_float}")
        except ValueError:
            print(f"'{num}' - не число. Пропускаем.")
    
    print(f"\nЧисла в списке: {numbers}")

print("Запуск задания 3:")
# task3()  # Раскомментировать для реального ввода

# Покажем пример работы
print("\nПример работы задания 3:")
print(">>> 8")
print(">>> abc")
print(">>> 11")
print(">>> -2")
print(">>> 9")
print(">>> txt")
print(">>> 4")
print(">>> Числа в списке: [8.0, 11.0, -2.0, 9.0, 4.0]")

# Дополнительные примеры для задания 3
print("\nЕще один вариант решения (более простой):")
numbers_list = []
print("Будем вводить числа. Для завершения введите 'стоп'")

while True:
    user_input = input("Введите число (или 'стоп' для завершения): ")
    if user_input.lower() == 'стоп':
        break
    
    try:
        num = float(user_input)
        numbers_list.append(num)
        print(f"Добавлено число: {num}")
    except ValueError:
        print(f"Ошибка: '{user_input}' не является числом")

print(f"\nИтоговый список чисел: {numbers_list}")
