# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1


def parse_input(input_str: str) -> int:
    """
    The function checks if the string is digit. If it is, returns the string converted to integer,
    if not - shows user error message and asks user to input correct value.
    """
    while not input_str.strip().isdigit() or len(input_str.strip()) == 0:
        print(f"Некорректный ввод. Введённое значение {input_str} не соответствует требованиям условия задачи.")
        input_str = input("Пожалуйста, повторите ввод (в задаче используются только целые положительные числа): ")
    return int(input_str)


def occurrences_count() -> None:
    """
    The function asks user to input length of list, list elements and value for count its occurrences in the list.
    Then it counts occurrences of the value in the list fnd prints it.
    """
    list_length = parse_input(
        input("Введите количество элементов в массиве: ")
    )

    list_elements = [
        parse_input(
            input("Введите элемент массива (целое положительное число): ")
        )
        for _ in range(list_length)
    ]

    element = parse_input(
        input("Введите элемент для подсчёта количества вхождений в массив: ")
    )
    result = 0
    for item in list_elements:
        if item == element:
            result += 1
    print(f"\nКоличество вхождений элемента {element} в массив равно {result}")


if __name__ == '__main__':
    occurrences_count()
