import numpy as np
import matplotlib.pyplot as plt
import math

print("Лабораторная работа №8 — Программирование в графическом режиме")
print("Вариант 1\n")
print("Программа строит графики двух функций:")
print("1) y(x) = 2 * Σ[ 1 / ((2n+1) * x^(2n+1)) ], вычисляется по ряду Тейлора (|x| > 1)")
print("2) z(x) = ln((x+1)/(x-1)) + b\n")

# === Ввод данных ===
print("Введите диапазон x так, чтобы |x| > 1 для всего интервала!")
print("Например: x_min = 1.1, x_max = 3.0 или x_min = -3.0, x_max = -1.1\n")

while True:
    x_min = float(input("Введите x_min: "))
    x_max = float(input("Введите x_max: "))

    if abs(x_min) <= 1 or abs(x_max) <= 1:
        print("Ошибка: диапазон должен удовлетворять |x| > 1. Попробуйте снова.\n")
    elif (x_min > 1 and x_max > 1) or (x_min < -1 and x_max < -1):
        break
    else:
        print("Ошибка: диапазон не должен пересекать область (-1; 1). Попробуйте снова.\n")

dx = float(input("Введите шаг dx (например 0.1): "))
eps = float(input("Введите точность ε (например 1e-6): "))
b = float(input("Введите параметр b: "))

# === Первая функция y(x) через ряд Тейлора ===
def y_series(x, eps):
    """Вычисляет сумму ряда для y(x) с заданной точностью ε.
       Возвращает (значение функции, количество членов ряда)."""
    n = 0
    term = 1 / ((2 * n + 1) * x ** (2 * n + 1))
    s = term
    while abs(term) > eps:
        n += 1
        term = 1 / ((2 * n + 1) * x ** (2 * n + 1))
        s += term
    return 2 * s, n + 1

# === Вторая функция z(x) ===
def z_func(x, b):
    return math.log((x + 1) / (x - 1)) + b

# === Построение точек и отчёт ===
x_vals = np.arange(x_min, x_max + dx, dx)
y_vals = []
z_vals = []
iterations = []

print("\n=== Отчёт о вычислениях для функции y(x) ===")
for x in x_vals:
    y_val, terms = y_series(x, eps)
    y_vals.append(y_val)
    z_vals.append(z_func(x, b))
    iterations.append(terms)
    print(f"x = {x:>6.2f} | y(x) = {y_val:>10.6f} | Кол-во членов ряда: {terms}")

# === Построение графиков ===
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y(x) — ряд Тейлора', color='blue', linewidth=2)
plt.plot(x_vals, z_vals, label='z(x) = ln((x+1)/(x-1)) + b', color='red', linestyle='--', linewidth=2)

plt.title("Графики функций y(x) и z(x)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Значения функций", fontsize=12)
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

# === Дополнительный вывод ===
print("\nСреднее количество членов ряда:", round(sum(iterations) / len(iterations), 2))
print("Максимальное количество членов ряда:", max(iterations))
print("Минимальное количество членов ряда:", min(iterations))
