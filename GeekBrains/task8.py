# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

def chocolate_piece() -> None:
    """
    The function asks user to input the dimensions of the chocolate piece and quantity of sections to cut and then
    prints if it's possible to cut necessary quantity of sections in one division
    """

    print("Введите размеры шоколадки и требуемое количество долек через точку с запятой.")
    piece_dimension = input("(Подсказка. Нужно ввести три "
                            "целых числа через точку с запятой (например 1;2;3) и нажать 'Enter'): ")

    while not len(piece_dimension.split(";")) == 3:
        print("Некорректный ввод. Пожалуйста, введите три "
              "целых числа через точку с запятой (например 1;2;3) и нажмите 'Enter'): ", end='')
        piece_dimension = input()

    while not (
            piece_dimension.split(";")[0].strip().isdigit() and
            piece_dimension.split(";")[1].strip().isdigit() and
            piece_dimension.split(";")[2].strip().isdigit()
    ):
        print("Некорректный ввод. Пожалуйста, введите три "
              "целых числа через точку с запятой (например 1;2;3) и нажмите 'Enter'): ", end='')
        piece_dimension = input()

    piece_dimension = [int(piece) for piece in piece_dimension.split(";")]
    if piece_dimension[2] < piece_dimension[0] * piece_dimension[1] and \
            (
            (piece_dimension[2] % piece_dimension[0] == 0) or
            (piece_dimension[2] % piece_dimension[1] == 0)
    ):
        result = "можно"
    else:
        result = "нельзя"
    print(f"\nКоличество долек, равное {piece_dimension[2]}, отломить от шоколадки,"
          f" размером {piece_dimension[0]}x{piece_dimension[1]}, {result}.")


chocolate_piece()
