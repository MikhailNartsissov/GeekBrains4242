# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
def sum_of_digits() -> None:
    """
    The function asks user to enter three-digit integer number,
    checks if the number is correct and prints sum of the digits of the number
    """
    three_digits_number = input("Введите трехзначное целое число и нажмите 'Enter': ")
    while not three_digits_number.strip().isdigit() or len(three_digits_number) != 3:
        print("Некорректный ввод. Пожалуйста, введите целое трехзначное число и нажмите 'Enter': ", end='')
        three_digits_number = input()
    result = 0
    for digit in three_digits_number:
        result += int(digit)
    print(f"\nСумма цифр введённого числа равна {result}")


sum_of_digits()
