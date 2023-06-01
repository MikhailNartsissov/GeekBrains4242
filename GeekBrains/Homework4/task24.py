# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём
# кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на
# грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число
# ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# --- Внимание требуется импорт ---
# В решении используется функция парсинга из задачи №16 в папке Homework3.

from GeekBrains.Homework3.task16 import parse_input


def blueberries() -> None:
    """
        The function asks user to input number of blueberry bushes and the number of berries on each of them.
        Then it searches three consecutive bushes with maximal sum of berries and prints their numbers.
    """
    bushes_count = parse_input(
        input("Введите количество кустов черники на грядке: ")
    )
    print("\nТеперь нужно ввести количество ягод на каждом кусте по очереди.")
    blueberry = [
        parse_input(
            input("Введите количество ягод на кусте (целое положительное число): ")
        )
        for _ in range(bushes_count)
    ]
    best_harvest = (
            blueberry[0] +
            blueberry[1] +
            blueberry[2]
                    )
    best_index = 1
    for index in range(2, bushes_count-1):
        harvest = (
            blueberry[index - 1] +
            blueberry[index] +
            blueberry[index + 1]
                   )
        if harvest > best_harvest:
            best_harvest = harvest
            best_index = index
    print(f"\nМаксимальное число ягод, равное {best_harvest}, можно собрать, "
          f"если собирающий модуль находится перед грядкой номер {best_index + 1} (нумерация грядок начинается с 1).")


if __name__ == '__main__':
    blueberries()
