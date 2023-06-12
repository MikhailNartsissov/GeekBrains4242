# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с
# единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# ВНИМАНИЕ в задаче используется импорт функции из предыдущего домашнего задания Homework3.task16

from typing import Callable
from GeekBrains.Homework3.task16 import parse_input


def print_operation_table(f_operation: Callable, f_num_rows: int = 6, f_num_columns: int = 6) -> None:
    """
        The function prints a table of results f_operation(x, y), where x in [1, f_num_rows]
        and y in [1, f_num_columns]
    """
    print("\nТаблица результатов:\n")
    for f_i in range(1, f_num_rows + 1):
        for f_n in range(1, f_num_columns):
            f_result = f_operation(f_i, f_n)
            if isinstance(f_result, float):
                print("\t", f"{round(f_result, 2): .2f}", end="")
            else:
                print("\t", f_result, end="")
        print("\n")


if __name__ == "__main__":
    choice_dict = {"1": lambda x, y: x + y, "2": lambda x, y: x - y, "3": lambda x, y: x * y,
                   "4": lambda x, y: x / y, "5": lambda x, y: x == y, "6": lambda x, y: x < y,
                   "7": lambda x, y: x > y, "8": lambda x, y: x <= y, "9": lambda x, y: x >= y,
                   "10": lambda x, y: x // y, "11": lambda x, y: x % y, "12": "Выход"}
    choice = input("\nВыберите бинарную операцию:\n\n1 - 'x + y'\n2 - 'x - y'\n3 - 'x * y'\n4 - 'x / y'"
                   "\n5 - 'x == y'\n6 - 'x < y'\n7 - 'x > y'\n8 - 'x <= y'\n9 - 'x >= y'"
                   "\n10 - 'x // y'\n11 - 'x % y'\n12 - Выход\n\nВведите число, соответствующее вашему выбору: ")
    while choice not in choice_dict.keys():
        print("Введено некорректное значение. Пожалуйста, введите число от 1 до 12:")
        choice = input("\nВыберите бинарную операцию:\n\n1 - 'x + y'\n2 - 'x - y'\n3 - 'x * y'\n4 - 'x / y'"
                       "\n5 - 'x == y'\n6 - 'x < y'\n7 - 'x > y'\n8 - 'x <= y'\n9 - 'x >= y'"
                       "\n10 - 'x // y'\n11 - 'x % y'\n12 - Выход")
    num_col = parse_input(input("\nВведите число столбцов: "))
    num_str = parse_input(input("\nВведите число строк: "))
    if int(choice) in range(1, 12):
        print_operation_table(choice_dict[choice], num_col, num_str)
