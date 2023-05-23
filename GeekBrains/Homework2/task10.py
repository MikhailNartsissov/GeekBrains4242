# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.


def turnover_count() -> int:
    """
        The function asks user to input, which side up the coin lays at the table and returns
        minimum of eagles and tails.
    return: int: Minimum of eagles and tails.
    """
    user_input = ""
    coins = {}
    print("\nДля каждой монетки нужно ввести, какой стороной вверх она лежит.\n Давайте начнём. "
          "\nЕсли монетка лежит вверх 'орлом', нажмите 1, если 'решкой', нажмите 2.\nЧтобы завершить ввод, нажмите Q.")
    while user_input.strip().lower() not in ["q", "й"]:
        print("\nКакой стороной вверх лежит монетка?")
        user_input = input("\n(1 - 'орёл', 2 - 'решка', Q - 'закончить ввод'))")
        if user_input in ['1', '2'] and user_input in coins.keys():
            coins[user_input] += 1
        elif user_input in ['1', '2']:
            coins[user_input] = 1
        elif user_input.strip().lower() not in ["q", "й"]:
            print("\nВведено некорректное значение. Попробуйте ещё раз.")
    if len(coins) == 0:
        return 0
    return min(coins['1'], coins['2'])


print(f'\nМинимальное количество монет, которое нужно перевернуть равно {turnover_count()}')
