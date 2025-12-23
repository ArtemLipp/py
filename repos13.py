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
