# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5


from task16 import parse_input


def nearest_count() -> None:
    """
    The function asks user to input length of list, list elements and value for count its occurrences in the list.
    Then it returns the element of the list nearest to the value.
    """
    list_length = parse_input(
        input("Введите количество элементов в массиве: ")
    )
    if list_length == 0:
        print("\nБлижайший по значению к данному элемент массива невозможно найти, поскольку количество элементов"
              " массива равно нулю.")
        return None

    list_elements = [
        parse_input(
            input("Введите элемент массива (целое положительное число): ")
        )
        for _ in range(list_length)
    ]

    element = parse_input(
        input("Введите значение для поиска элемента массива, ближайшего к данному значению: ")
    )

    result = list_elements[0]
    difference = abs(list_elements[0] - element)

    for item in list_elements[1:]:
        if abs(item - element) < difference:
            result = item
            difference = abs(item - element)

    print(f"\nБлижайший по значению к {element} элемент массива равен {result}")


if __name__ == '__main__':
    nearest_count()
