# =============================================
# ЛАБОРАТОРНАЯ РАБОТА №6 — ФАЙЛЫ
# Автор: Тимофей Константинович
# =============================================
# Задание: модифицировать программы ЛР №1, №4 и №5 так,
# чтобы ввод и вывод осуществлялись через файлы.
# =============================================

import math
from pathlib import Path
from collections import Counter
import sys

# ---------------------------------------------
# === ЛАБА №1: Линейные программы ===
# ---------------------------------------------

def lab1(input_file="lab1_input.txt", output_file="lab1_output.txt"):
    """
    Считывает значения α из файла, вычисляет z1 и z2, сохраняет в файл.
    Формат входа: числа (в радианах) через пробел или с новой строки.
    """

    path_in = Path(input_file)
    path_out = Path(output_file)

    if not path_in.exists():
        # создаём файл с примерами, если его нет
        sample = "0\n0.5236\n0.7854\n1.0472\n1.5708"
        path_in.write_text(sample, encoding="utf-8")
        print(f"Создан пример входного файла: {path_in.name}")

    # читаем входные данные
    text = path_in.read_text(encoding="utf-8")
    alphas = [float(x) for x in text.replace(",", " ").split()]

    results = []
    for alpha in alphas:
        z1 = 2 * (math.sin(3 * math.pi - 2 * alpha) ** 2) * (math.cos(5 * math.pi + 2 * alpha) ** 2)
        z2 = (1 / 4) - (1 / 4) * math.sin((5 / 2) * math.pi - 8 * alpha)
        results.append((alpha, z1, z2))

    # запись результата
    lines = ["ЛР №1 — Линейные программы (файлы)\n"]
    lines.append(f"{'α (рад)':>12}  {'z1':>15}  {'z2':>15}")
    for a, z1, z2 in results:
        lines.append(f"{a:12.6f}  {z1:15.6f}  {z2:15.6f}")
    path_out.write_text("\n".join(lines), encoding="utf-8")

    print(f"✅ Лаба 1 выполнена. Результат сохранён в {output_file}")


# ---------------------------------------------
# === ЛАБА №4: Одномерные массивы ===
# ---------------------------------------------

def lab4(input_file="lab4_input.txt", output_file="lab4_output.txt"):
    """
    Вход: числа массива через пробел или с новой строки.
    Первая строка может быть количеством элементов.
    """

    path_in = Path(input_file)
    path_out = Path(output_file)

    if not path_in.exists():
        sample = "6\n2 -4 3 -1 5 -2"
        path_in.write_text(sample, encoding="utf-8")
        print(f"Создан пример входного файла: {path_in.name}")

    tokens = path_in.read_text(encoding="utf-8").replace(",", " ").split()
    try:
        n = int(tokens[0])
        nums = list(map(float, tokens[1:1 + n]))
        if len(nums) != n:
            nums = list(map(float, tokens))
    except:
        nums = list(map(float, tokens))

    negative_sum = sum(x for x in nums if x < 0)
    max_index = nums.index(max(nums))
    min_index = nums.index(min(nums))
    start, end = (max_index + 1, min_index) if max_index < min_index else (min_index + 1, max_index)
    product = 0 if start >= end else math.prod(nums[start:end])
    sorted_nums = sorted(nums)

    lines = [
        "ЛР №4 — Одномерные массивы (файлы)\n",
        f"Исходный массив: {nums}",
        f"Сумма отрицательных элементов: {negative_sum}",
        f"Произведение между max и min: {product}",
        f"Отсортированный массив: {sorted_nums}"
    ]
    path_out.write_text("\n".join(lines), encoding="utf-8")

    print(f"✅ Лаба 4 выполнена. Результат сохранён в {output_file}")


# ---------------------------------------------
# === ЛАБА №5: Двумерные массивы ===
# ---------------------------------------------

def lab5(input_file="lab5_input.txt", output_file="lab5_output.txt"):
    """
    Формат входа:
    Первая строка: m n
    Далее — m строк по n чисел.
    """

    path_in = Path(input_file)
    path_out = Path(output_file)

    if not path_in.exists():
        sample = """3 4
1 2 3 0
4 0 5 6
7 8 9 1"""
        path_in.write_text(sample, encoding="utf-8")
        print(f"Создан пример входного файла: {path_in.name}")

    lines = [ln.strip() for ln in path_in.read_text(encoding="utf-8").splitlines() if ln.strip()]
    m, n = map(int, lines[0].split())
    matrix = [[int(x) for x in line.split()] for line in lines[1:m + 1]]

    def rows_without_zero(mat):
        return sum(1 for row in mat if all(x != 0 for x in row))

    def max_repeated(mat):
        flat = [x for row in mat for x in row]
        freq = Counter(flat)
        repeated = [val for val, cnt in freq.items() if cnt > 1]
        return max(repeated) if repeated else None

    no_zero = rows_without_zero(matrix)
    max_rep = max_repeated(matrix)

    lines = ["ЛР №5 — Двумерные массивы (файлы)\n"]
    lines.append("Исходная матрица:")
    lines.extend(" ".join(map(str, row)) for row in matrix)
    lines.append(f"\n1) Количество строк без нулей: {no_zero}")
    lines.append("2) " + (f"Максимум среди повторяющихся: {max_rep}" if max_rep else "Повторяющихся нет"))
    path_out.write_text("\n".join(lines), encoding="utf-8")

    print(f"✅ Лаба 5 выполнена. Результат сохранён в {output_file}")


# ---------------------------------------------
# === ГЛАВНОЕ МЕНЮ ===
# ---------------------------------------------

def main():
    print("ЛАБОРАТОРНАЯ №6 — Работа с файлами\n")
    print("1 — Лаба №1 (линейные программы)")
    print("2 — Лаба №4 (одномерные массивы)")
    print("3 — Лаба №5 (двумерные массивы)")
    choice = input("Выбери номер части: ")

    if choice == "1":
        lab1()
    elif choice == "2":
        lab4()
    elif choice == "3":
        lab5()
    else:
        print("Некорректный выбор.")


if __name__ == "__main__":
    main()
