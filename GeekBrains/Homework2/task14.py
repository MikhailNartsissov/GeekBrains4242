# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

from math import log2


def powers_of_two() -> None:
    """
    The function asks user to input positive integer number and prints integer powers of 2
    which are not more than the number
    """
    number = input("Введите целое положительное число и нажмите 'Enter': ")
    while not number.strip().isdigit():
        print("Некорректный ввод. Пожалуйста, введите целое положительное число и нажмите 'Enter': ", end='')
        number = input()
    if number == '0':
        max_power = 0
    else:
        max_power = int(log2(int(number))) + 1
    result = [(power, 2 ** power) for power in range(max_power)]
    print(f"\nЦелые степени 2, не превосходящие {number}:")
    for item in result:
        print(f"2 в степени {item[0]} равно {item[1]}")


powers_of_two()
