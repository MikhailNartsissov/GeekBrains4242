# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# ВНИМАНИЕ ИМПОРТ! Используется функция parse_input
# из задачи 16 домашнего задания к уроку 3: (GeekBrains/Homework3/task.16.py)


from GeekBrains.Homework3.task16 import parse_input


def power_of_numbers(a: int, b: int) -> int:
    """
        The function calculates a raised to the power of b, using recursion.
    """
    if b == 1:
        return a
    elif b == 0:
        if a == 0:
            print("Выражение 0⁰ (ноль в нулевой степени) многие учебники считают неопределённым и лишённым смысла,\n"
                  "но здесь мы будем придерживаться другой точки зрения и вернём единицу:")
        return 1
    return a * power_of_numbers(a, b - 1)


if __name__ == "__main__":
    first_number = parse_input(input("\nВведите первый аргумент (целое положительное число): "))
    second_number = parse_input(input("Введите второй аргумент (целое положительное число): "))
    print(f"\nЕсли {first_number} возвести в степень {second_number}, "
          f"получится {power_of_numbers(first_number, second_number)}")
