# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# --- Внимание требуется импорт ---
# В решении используется функция парсинга из задачи №16 в папке Homework3.

from GeekBrains.Homework3.task16 import parse_input


def set_intersect() -> None:
    """
        The function asks user to input number of elements of each set and the elements. Then it searches
        intersection of the two sets and prints it sorted.
    """
    first_set_length = parse_input(
        input("Введите количество элементов первого множества: ")
    )
    second_set_length = parse_input(
        input("Введите количество элементов второго множества: ")
    )
    print("\nТеперь нужно ввести элементы первого множества по одному.")
    first_set = {
        parse_input(
            input("Введите элемент первого множества (целое положительное число): ")
        )
        for _ in range(first_set_length)
    }
    print("\nТеперь нужно ввести элементы второго множества по одному.")
    second_set = {
        parse_input(
            input("Введите элемент второго множества (целое положительное число): ")
        )
        for _ in range(second_set_length)
    }
    print()
    print(f"\nВ обоих введённых наборах чисел встречаются следующие значения (в порядке возрастания): "
          f"{sorted(first_set&second_set)}")


if __name__ == '__main__':
    set_intersect()
