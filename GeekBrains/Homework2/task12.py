# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


def suggest_number() -> None:
    """
        The function asks user to input two integer numbers. One of them is a sum of two unknown numbers, and
        another is a product of the numbers and prints numbers used as arguments in the sum and product
    """

    print("Введите сумму и произведение задуманных чисел через точку с запятой.")
    sum_product = input("(Подсказка. Нужно ввести два "
                        "целых положительных числа через точку с запятой (например 1;2) и нажать 'Enter'): ")

    while not len(sum_product.split(";")) == 2:
        print("Некорректный ввод. Пожалуйста, введите два "
              "целых положительных числа\n "
              "(первое - сумма задуманных чисел, второе - их произведение) через точку с запятой (например 1;2)\n"
              " и нажмите 'Enter'): ", end='')
        sum_product = input()

    while not (
            sum_product.split(";")[0].strip().isdigit() and
            sum_product.split(";")[1].strip().isdigit()
    ):
        print("Некорректный ввод. Пожалуйста, введите два "
              "целых положительных числа\n "
              "(первое - сумма задуманных чисел, второе - их произведение) через точку с запятой (например 1;2)\n"
              " и нажмите 'Enter'): ", end='')
        sum_product = input()

    sum_product = [int(piece) for piece in sum_product.split(";")]
    discriminant = sum_product[0] ** 2 - 4 * sum_product[1]
    if discriminant < 0:
        print("\nПетя где-то ошибся. При таких условиях задача не имеет решения.")
    if discriminant == 0:
        if sum_product[0] % 2 != 0:
            print("\nПетя задумал дробные числа.")
        else:
            print(f"\nПетя задумал числа {sum_product[0] // 2} и {sum_product[0] // 2}")
    if discriminant > 0:
        if (sum_product[0] - (sum_product[0] ** 2 - 4 * sum_product[1]) ** 0.5) % 2 != 0:
            print("\nПетя задумал дробные числа.")
        else:
            first_number = int(sum_product[0] - (sum_product[0] ** 2 - 4 * sum_product[1]) ** 0.5) // 2
            print(f"\nПетя задумал числа {first_number} и {sum_product[0] - first_number}")


suggest_number()
