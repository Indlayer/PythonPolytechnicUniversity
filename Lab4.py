# Лабораторная работа №4
# Тема: "Одномерные массивы"
# Вариант 1
# Выполнил: Тимофей Константинович

# 1. Ввод массива
n = int(input("Введите количество элементов массива: "))
array = []

print("Введите элементы массива:")
for i in range(n):
    element = float(input(f"{i + 1}-й элемент: "))
    array.append(element)

print("\nИсходный массив:", array)

# 2. Сумма отрицательных элементов
negative_sum = sum(x for x in array if x < 0)
print("Сумма отрицательных элементов:", negative_sum)

# 3. Произведение элементов между максимальным и минимальным
max_index = array.index(max(array))
min_index = array.index(min(array))

# определяем диапазон между min и max
if max_index < min_index:
    start = max_index + 1
    end = min_index
else:
    start = min_index + 1
    end = max_index

product = 1
if start < end:  # если между ними есть элементы
    for i in range(start, end):
        product *= array[i]
else:
    product = 0  # если нет элементов между ними

print("Произведение элементов между максимальным и минимальным:", product)

# 4. Сортировка массива по возрастанию
sorted_array = sorted(array)
print("Отсортированный массив по возрастанию:", sorted_array)
