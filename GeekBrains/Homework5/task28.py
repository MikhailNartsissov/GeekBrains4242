# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
# ВНИМАНИЕ ИМПОРТ! Используется функция parse_input
# из задачи 16 домашнего задания к уроку 3: (GeekBrains/Homework3/task.16.py)

from GeekBrains.Homework3.task16 import parse_input


def sum_of_numbers(a: int, b: int) -> int:
    """
        The function calculates sum a and b, using recursion.
    """
    if b == 0:
        return a
    return a + sum_of_numbers(1, b - 1)


if __name__ == "__main__":
    first_number = parse_input(input("\nВведите первый аргумент (целое неотрицательное число): "))
    second_number = parse_input(input("Введите второй аргумент (целое неотрицательное число): "))
    print(f"\nЕсли {first_number} сложить с {second_number}, "
          f"получится {sum_of_numbers(first_number, second_number)}")
