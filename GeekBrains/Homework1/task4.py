# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def paper_cranes_count() -> None:
    """
    The function asks user to enter how much paper cranes the kids made,
    checks if the quantity of cranes is correct and prints how much paper cranes each kid made.
    """
    numerals = {1: "одного", 2: "двух", 3: "трёх", 4: "четырёх", 5: "пятерых", 6: "шестерых",
                7: "семерых", 8: "восьмерых", 9: "девятерых", 10: "десятерых"}
    print("Введите, сколько журавликов сделали Петя, Катя и Сережа вместе и нажмите 'Enter'")
    cranes = input("(Подсказка - число должно делиться на 6): ")
    while not cranes.strip().isdigit() or int(cranes.strip()) % 6 != 0:
        print("Количество журавликов должно быть целым числом, кратным 6. Повторите ввод и нажмите 'Enter': ", end='')
        cranes = input()
    boys = int(cranes) // 6
    if boys == 1:
        crane_str = "журавлика"
    else:
        crane_str = "журавликов"
    girl = boys * 4
    if boys in numerals.keys():
        boys = numerals[boys]
    if girl in numerals.keys():
        girl = numerals[girl]
    if cranes == '0':
        print("\nПетя не сделал ни одного журавлика\nКатя не сделала ни одного журавлика\n"
              "Серёжа не сделал ни одного журавлика")
    else:
        print(f"\nПетя сделал {boys} {crane_str}\nКатя сделала {girl} {crane_str}\n"
              f"Серёжа сделал {boys} {crane_str}")


paper_cranes_count()
