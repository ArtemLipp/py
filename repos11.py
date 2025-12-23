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
