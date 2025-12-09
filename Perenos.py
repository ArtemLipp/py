# ========== ПРАКТИЧЕСКОЕ ЗАДАНИЕ 12 ==========

print("=== Практическое задание 12 (Лямбда-функции) ===")

# Задание 1
print("\n--- Задание 1 ---")
# Создаем лямбда-функцию для умножения двух чисел
x = lambda a, b: a * b

print("Результат x(2, 3):")
print(x(2, 3))

# Покажем еще примеры
print("\nДополнительные примеры:")
print("x(5, 4) =", x(5, 4))
print("x(10, 3) =", x(10, 3))

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
