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
