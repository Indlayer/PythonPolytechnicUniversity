#1 часть задания

import math

x = float(input("Введите значение x: "))

if -9 <= x <= -6:
    y = -3 + math.sqrt(9 - (x + 6)**2)
elif -6 < x <= 0:
    y = math.sqrt(9 - (x + 3)**2)
elif 0 < x <= 3:
    y = -x + 3
elif 3 < x <= 9:
    y = 0.5 * x - 1.5
else:
    y = "Нет значения (x вне диапазона [-9, 9])"

print("Значение функции y =", y)

#2 часть задания

x = float(input("Введите координату X: "))
y = float(input("Введите координату Y: "))
R = float(input("Введите значение R: "))

# Проверяем, находится ли точка внутри круга
inside_circle = x**2 + y**2 <= R**2

# Проверяем первый сектор (0°–45°)
sector_1 = x >= 0 and y >= 0 and y <= x

# Проверяем третий сектор (180°–225°)
sector_3 = x <= 0 and y <= 0 and y >= x

if inside_circle and (sector_1 or sector_3):
    print("Точка находится в закрашенной области.")
else:
    print("Точка находится вне закрашенной области.")
