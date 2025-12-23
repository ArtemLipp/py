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
