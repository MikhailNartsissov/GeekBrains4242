# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных
from os.path import exists, getsize


def main_menu() -> int:
    f_choice = 6
    print("\nГлавное меню:\n")
    print("1 - просмотр справочника")
    print("2 - поиск контакта в справочнике")
    print("3 - добавление контакта")
    print("4 - удаление контакта")
    print("5 - изменение контакта")
    print("0 - завершение работы\n")
    f_choice = input("Введите номер пункта меню: ")
    while not f_choice.isdigit() or int(f_choice) not in range(0, 6):
        print("Вы ввели значение, которого нет в меню. Пожалуйста, введите цифру от 0 до 5.")
        f_choice = input("Введите номер пункта меню: ")
    return int(f_choice)


choice = None
while choice != 0:
    print("*" * 200)
    choice = main_menu()
    match choice:
        case 1:
            if exists('phonebook.txt') and getsize('phonebook.txt') != 0:
                with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
                    print("\n" + "*" * 30 + "\nТелефонный справочник:\n")
                    for record in phonebook:
                        print(*record.strip().split(";"))
                    print("*" * 30 + "\n")
            else:
                print("\nТелефонный справочник пуст. Выберите пункт меню 3 для добавления данных")
        case 2:
            if exists('phonebook.txt') and getsize('phonebook.txt') != 0:
                search_str = input("\nВведите строку для поиска:")
                with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
                    found = False
                    print("\nРезультаты поиска:\n" + "*" * 30)
                    for record in phonebook:
                        if search_str.strip().lower() in record.lower():
                            print(*record.strip().split(";"))
                            found = True
                    if not found:
                        print("По вашему запросу ничего не найдено")
                    print("*" * 30 + "\n")
            else:
                print("\nТелефонный справочник пуст. Выберите пункт меню 3 для добавления данных")
        case 3:
            with open('phonebook.txt', 'a', encoding='utf-8') as phonebook:
                add_another_contact = True
                while add_another_contact:
                    contact = input("Введите имя контакта: ").strip() + ";"
                    contact += input("Введите фамилию контакта: ").strip() + ";"
                    contact += input("Введите телефонный номер контакта: ").strip() + ";"
                    contact += input("Введите комментарий: ").strip()
                    phonebook.write(contact + "\n")
                    add_another_contact = input("Добавить ещё один контакт (д/н)?")
                    if add_another_contact.strip().lower() == 'y' or add_another_contact.strip().lower() == 'д':
                        add_another_contact = True
                    else:
                        add_another_contact = False
        case 4:
            if exists('phonebook.txt') and getsize('phonebook.txt') != 0:
                search_str = input("\nВведите строку для поиска:")
                with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
                    found = False
                    new_phonebook = ""
                    for record in phonebook:
                        if search_str.strip().lower() in record.lower():
                            print(*record.strip().split(";"))
                            confirm = input("Удалить запись (д/н)? ")
                            if confirm.strip().lower() == 'y' or confirm.strip().lower() == 'д':
                                found = True
                            else:
                                new_phonebook += record + "\n"
                        else:
                            new_phonebook += record + "\n"
                    phonebook.close()
                    if found:
                        print("Удаление выполнено успешно")
                        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
                            phonebook.write(new_phonebook)
            else:
                print("\nТелефонный справочник пуст. Выберите пункт меню 3 для добавления данных")
        case 5:
            if exists('phonebook.txt') and getsize('phonebook.txt') != 0:
                search_str = input("\nВведите строку для поиска:")
                with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
                    found = False
                    new_phonebook = ""
                    for record in phonebook:
                        if search_str.strip().lower() in record.lower():
                            print(*record.strip().split(";"))
                            confirm = input("Изменить запись (д/н)? ")
                            if confirm.strip().lower() == 'y' or confirm.strip().lower() == 'д':
                                found = True
                                contact = input("Введите имя контакта: ").strip() + ";"
                                contact += input("Введите фамилию контакта: ").strip() + ";"
                                contact += input("Введите телефонный номер контакта: ").strip() + ";"
                                contact += input("Введите комментарий: ").strip() + "\n"
                                new_phonebook += contact
                            else:
                                new_phonebook += record
                        else:
                            new_phonebook += record
                    phonebook.close()
                    if found:
                        print("Изменения внесены в справочник")
                        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
                            phonebook.write(new_phonebook)
            else:
                print("\nТелефонный справочник пуст. Выберите пункт меню 3 для добавления данных")
