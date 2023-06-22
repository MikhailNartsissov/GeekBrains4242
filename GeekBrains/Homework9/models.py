from json import load, dump
from typing import Any
from os.path import exists
from text import (
    record_found_message, search_string_prompt, end_of_action_message,
    not_found_message, edit_request, get_new_contact_data_header,
    new_contact_data_request,phonebook_divider, phonebook_header,
    delete_request, search_continue_request
)

# Путь до файла телефонной книги - str
path_to_phonebook = 'phonebook.json'

# Словарь для временного хранения телефонной книги
phonebook_dict = dict()


def open_phonebook():
    """
        1st point of the main menu handler
    """
    global phonebook_dict
    if exists(path_to_phonebook):
        with open(path_to_phonebook, 'r', encoding='utf-8') as phonebook:
            phonebook_dict = load(phonebook)
    else:
        print("Телефонная книга пока пуста. Добавьте хотя бы один контакт и сохраните файл.")


def save_phonebook() -> None:
    """
        2nd point of the main menu handler
    """
    global phonebook_dict
    with open(path_to_phonebook, 'w', encoding='utf-8') as phonebook:
        dump(phonebook_dict, phonebook, ensure_ascii=False)


def show_contacts():
    """
        Prints actual phonebook
    """
    global phonebook_dict
    for phonebook_record in phonebook_dict.values():
        print(phonebook_header)
        for key, value in phonebook_record.items():
            print(key, ": ", value)
        print(phonebook_divider)
    input(end_of_action_message)


def add_contact(phonebook_record: dict[Any]) -> None:
    """
        4t point of the main menu handler
    """
    global phonebook_dict
    if phonebook_dict.keys():
        new_key = max([int(key) for key in phonebook_dict.keys()]) + 1
    else:
        new_key = 0
    phonebook_dict.update({new_key: phonebook_record})


def find_contact() -> None:
    """
        5th point of the main menu handler
    """
    global phonebook_dict
    found = False
    search_string = input(search_string_prompt)
    for phonebook_record in phonebook_dict.values():
        for value in phonebook_record.values():
            if search_string in value:
                found = True
                print(record_found_message)
                print(*[value for value in phonebook_record.values()])
                search_again = input(search_continue_request)
                if search_again.strip().lower() != "д" and search_again.strip().lower() != "y":
                    return
    if not found:
        print(not_found_message)
        input(end_of_action_message)


def change_contact() -> None:
    """
        6th point of the main menu handler
    """
    global phonebook_dict
    found = False
    search_string = input(search_string_prompt)
    for phonebook_record in phonebook_dict.values():
        for value in phonebook_record.values():
            if search_string in value:
                found = True
                print(record_found_message)
                print(*[value for value in phonebook_record.values()])
                change = input(edit_request)
                if change.strip().lower() == "д" or change.strip().lower() == "y":
                    print(get_new_contact_data_header)
                    for key, data in new_contact_data_request.items():
                        phonebook_record[key] = input(data)
    if not found:
        print(not_found_message)
        input(end_of_action_message)


def delete_contact() -> None:
    """
        7th point of the main menu handler
    """
    global phonebook_dict
    found = False
    search_string = input(search_string_prompt)
    for key, phonebook_record in phonebook_dict.items():
        for value in phonebook_record.values():
            if search_string in value:
                found = True
                print(record_found_message)
                print(*[value for value in phonebook_record.values()])
                confirm_delete = input(delete_request)
                if confirm_delete.strip().lower() == "д" or confirm_delete.strip().lower() == "y":
                    phonebook_dict.pop(key)
                    return
    if not found:
        print(not_found_message)
        input(end_of_action_message)
