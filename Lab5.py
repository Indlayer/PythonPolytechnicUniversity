from collections import Counter
from typing import List, Optional


def read_int(prompt: str) -> int:
    """Надёжный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Нужно целое число. Попробуй ещё раз.")


def read_matrix(rows: int, cols: int) -> List[List[int]]:
    """
    Считывает целочисленную прямоугольную матрицу rows×cols.
    Ввод — построчно, элементы через пробел.
    """
    matrix: List[List[int]] = []
    for i in range(rows):
        while True:
            line = input(f"Строка {i + 1} из {rows} (ровно {cols} целых через пробел): ").strip().split()
            if len(line) != cols:
                print(f"Нужно ровно {cols} значений. Сейчас: {len(line)}.")
                continue
            try:
                row = [int(x) for x in line]
            except ValueError:
                print("Все элементы должны быть целыми числами.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(a: List[List[int]], title: str = "Матрица") -> None:
    """Красиво печатает матрицу."""
    print(f"\n{title}:")
    if not a:
        print("∅ (пусто)")
        return
    width = max(len(str(x)) for row in a for x in row)
    for row in a:
        print(" ".join(f"{x:>{width}}" for x in row))
    print()


def count_rows_without_zero(a: List[List[int]]) -> int:
    """Количество строк, не содержащих ни одного нулевого элемента."""
    return sum(1 for row in a if all(x != 0 for x in row))


def max_value_repeated(a: List[List[int]]) -> Optional[int]:
    """
    Максимальное значение среди чисел, встречающихся в матрице более одного раза.
    Если повторяющихся нет — вернёт None.
    """
    flat = [x for row in a for x in row]
    freq = Counter(flat)
    repeated = [val for val, cnt in freq.items() if cnt > 1]
    if not repeated:
        return None
    return max(repeated)


def main() -> None:
    print("Лаба №5: Двумерные массивы и функции — Вариант 1")
    m = read_int("Введите количество строк m: ")
    n = read_int("Введите количество столбцов n: ")
    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными.")
        return

    a = read_matrix(m, n)
    print_matrix(a, "Исходная матрица")

    no_zero_rows = count_rows_without_zero(a)
    max_repeated = max_value_repeated(a)

    print(f"1) Количество строк без единого нуля: {no_zero_rows}")
    if max_repeated is None:
        print("2) В матрице нет чисел, встречающихся более одного раза.")
    else:
        print(f"2) Максимальное значение среди повторяющихся чисел: {max_repeated}")


if __name__ == "__main__":
    main()
