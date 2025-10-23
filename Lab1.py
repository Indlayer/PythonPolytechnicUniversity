import math

print("Лабораторная работа №1 — Линейные программы")
print("Вычисление значений z1 и z2\n")

# Перебираем 5 тестовых значений альфа (в радианах)
alphas = [0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2]

for alpha in alphas:
    # Формулы
    z1 = 2 * (math.sin(3 * math.pi - 2 * alpha) ** 2) * (math.cos(5 * math.pi + 2 * alpha) ** 2)
    z2 = (1 / 4) - (1 / 4) * math.sin((5 / 2) * math.pi - 8 * alpha)

    # Вывод
    print(f"α = {alpha:.4f} рад")
    print(f"z1 = {z1:.6f}")
    print(f"z2 = {z2:.6f}")
    print("-" * 30)