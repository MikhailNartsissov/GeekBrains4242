# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух
# считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы
# отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def vowels_count(f_string: str) -> int:
    """
        The function returns amount of vowels in string
    """
    f_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е", "a", "e", "i", "o", "u", "y"]
    f_counter = 0
    for f_letter in f_string.strip():
        if f_letter.lower() in f_vowels:
            f_counter += 1
    return f_counter


def rhyme_check(f_string: str) -> str:
    """
        The function checks amounts of vowels in each part of the input string separated from the others by spaces
        and returns "Парам пам-пам" if the amounts are equal in all parts or "Пам парам" if not.
    """
    f_list = f_string.split()
    f_is_first = True
    f_vowels = None
    for f_item in f_list:
        if f_is_first:
            f_vowels = vowels_count(f_item)
            f_is_first = False
        else:
            if vowels_count(f_item) != f_vowels:
                return "Пам парам"
    return "Парам пам-пам"


if __name__ == "__main__":
    poem = input("\nВведите текст кричалки, разделяя фразы пробелом, а слова - дефисами: ")
    print(rhyme_check(poem))
