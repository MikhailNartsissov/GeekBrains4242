# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
# написать программу, которая проверяет, счастливый билет или нет.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

def is_lucky() -> None:
    """
    The function asks user to enter six-digit integer number,
    checks if the number is correct and prints if the sum of the first three digits is equal to the sum
    of the last three digits
    """
    print("Введите шестизначный номер билета.")
    ticket_number = input("(Подсказка. Нужно ввести целое шестизначное число и нажать 'Enter'): ")
    while not ticket_number.strip().isdigit() or len(ticket_number) != 6:
        print("Некорректный ввод. Пожалуйста, введите целое шестизначное число и нажмите 'Enter': ", end='')
        ticket_number = input()
    sum_first = 0
    sum_last = 0
    for index in range(2):
        sum_first += int(ticket_number[index])
        sum_last += int(ticket_number[index + 3])
    if sum_first == sum_last:
        print("\nПоздравляем! Вам выпал счастливый билет.")
    else:
        print("\nУвы, этот билет не подходит под определение счастливого. Попробуйте купить ещё один билет.")


is_lucky()
