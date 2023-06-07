# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def create_list(num_elements: int, f_border: int) -> list[int]:
    f_result = [randint(1, f_border) for _ in range(num_elements)]
    print(f"\nИсходный список: {f_result}")
    return f_result


def get_bounds(f_border: int) -> (int, int):
    left_border = randint(0, f_border)
    right_border = randint(1, f_border)
    while left_border >= right_border:
        left_border = randint(0, f_border)
    print(f"Левая граница: {left_border}\t Правая граница: {right_border}")
    return left_border, right_border


def elem_in_bounds(f_list: list[int], left_bound: int, right_bound: int) -> None:
    f_result = {index: f_list[index] for index in range(len(f_list)) if left_bound <= f_list[index] <= right_bound}
    if f_result:
        print(f"\nЗаданному диапазону принадлежат элементы:")
        for key in f_result.keys():
            print(f"Индекс элемента в исходном списке: {key}\tЗначение элемента: {f_result[key]}")
    else:
        print("Элементов, принадлежащих заданному диапазону, в списке нет.")


if __name__ == "__main__":
    list_len = randint(2, 20)
    border = randint(2, 50)
    elem_in_bounds(create_list(list_len, border), *get_bounds(border))
