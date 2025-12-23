# Практическое задание 16: Консольная игра "Лабиринт"

import random

def maze_game():
    print("Начинаем игру. Повороты: [a]-Налево, [w]-Прямо, [d]-Направо")
    
    # Счётчики поворотов
    left_count = 0
    right_count = 0
    straight_count = 0
    total_moves = 0
    
    while True:
        move = input("Куда идти? ").strip().lower()
        
        # Проверка на корректный ввод
        if move not in ['a', 'w', 'd']:
            print("Ошибка: такой кнопки нет. Используйте a, w или d.")
            continue
        
        total_moves += 1
        
        # Обработка хода
        if move == 'a':
            left_count += 1
            print("Повернул налево.", end=" ")
        elif move == 'd':
            right_count += 1
            print("Повернул направо.", end=" ")
        elif move == 'w':
            straight_count += 1
            print("Пошёл прямо.", end=" ")
        
        # Проверка на выход (вероятность 1 к 10)
        if random.randint(1, 10) == 1:
            print("Выход найден. Ты выиграл.")
            print(f"Для того, чтобы найти выход ты {left_count} раз повернул налево, "
                  f"{straight_count} раз пошёл прямо и {right_count} раз повернул направо.")
            print(f"Всего сделано ходов: {total_moves}")
            break
        else:
            print("Выхода пока нет...")

# Запуск игры
if __name__ == "__main__":
    maze_game()






# Практическое задание 17: Сборка фигуры

import random
import time

# Функция "загрузка" (дополнительное задание)
def loading_simulator():
    print("Загрузка...")
    for i in range(1, 101):
        print(f"\rПрогресс: {i}%", end="")
        time.sleep(0.02)  # небольшая задержка для эффекта
    print("\nЗагрузка завершена!")

# Элементы для фигур (простые примеры)
figures = [
    # Фигура 1: Квадрат
    {
        "target": [
            " *** ",
            "*   *",
            "*   *",
            " *** "
        ],
        "parts": [
            ["  *  ", " * * ", "*   *", " * * ", "  *  "],
            ["*   *", " * * ", "  *  ", " * * ", "*   *"],
            [" *** ", "*   *", "*   *", "*   *", " *** "],
            ["  *  ", " *** ", "* * *", " *** ", "  *  "]
        ]
    },
    # Фигура 2: Стрелка
    {
        "target": [
            "  *  ",
            " *** ",
            "*****",
            "  *  ",
            "  *  "
        ],
        "parts": [
            ["  *  ", "  *  ", "*****", "  *  ", "  *  "],
            [" *** ", "* * *", "  *  ", "* * *", " *** "],
            ["*****", " *** ", "  *  ", " *** ", "*****"],
            ["  *  ", " * * ", "*   *", " * * ", "  *  "]
        ]
    }
]

def generate_figure(parts):
    """Генерирует случайную фигуру из частей"""
    figure = []
    for part_set in parts:
        figure.append(random.choice(part_set))
    return figure

def print_figure(fig):
    """Печатает фигуру построчно"""
    for line in fig:
        print(line)

def check_win(current, target):
    """Проверяет, собрана ли фигура"""
    return current == target

def figure_game():
    # Вызываем загрузку
    loading_simulator()
    print("\n" + "="*30)
    
    # Случайный выбор фигуры
    fig_data = random.choice(figures)
    target_fig = fig_data["target"]
    parts = fig_data["parts"]
    
    print("Должна получиться такая фигура:")
    print_figure(target_fig)
    print("\nС помощью кнопок 1,2,3,4 меняйте направление элементов фигуры.")
    
    # Начальная случайная фигура
    current_fig = generate_figure(parts)
    
    attempts = 0
    while not check_win(current_fig, target_fig):
        attempts += 1
        print(f"\nПопытка #{attempts}")
        print("Текущая фигура:")
        print_figure(current_fig)
        
        try:
            choice = int(input("\nВыберите элемент для изменения (1-4): "))
            if choice < 1 or choice > 4:
                print("Ошибка: введите число от 1 до 4")
                continue
            
            # Меняем выбранный элемент
            current_fig[choice-1] = random.choice(parts[choice-1])
            
        except ValueError:
            print("Ошибка: введите число!")
    
    print("\n" + "="*30)
    print("Поздравляем! Вы собрали фигуру!")
    print_figure(current_fig)
    print(f"Всего попыток: {attempts}")

# Запуск игры
if __name__ == "__main__":
    figure_game()
