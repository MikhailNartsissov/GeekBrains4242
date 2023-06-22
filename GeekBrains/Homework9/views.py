from text import (
    main_menu, main_menu_header, main_menu_prompt,
    main_menu_incorrect_choice, new_contact_data_request,
    get_new_contact_data_header,
                  )
from typing import Any


def menu() -> int:
    """
        Main menu function
        Returns the number of the menu item selected
    """

    print(main_menu_header)
    for key, value in enumerate(main_menu, 1):
        print(key, ". " + value)
    choice = input(main_menu_prompt)
    while not (choice.isdigit() and int(choice) in range(1, len(main_menu) + 1)):
        print(main_menu_incorrect_choice)
        for key, value in enumerate(main_menu, 1):
            print(key, ". " + value)
        choice = input(main_menu_prompt)
    choice = int(choice)
    if choice == len(main_menu):
        return 0
    return choice


def get_new_contact_data() -> dict[Any]:
    """
        Returns data of a new contact
    """
    print(get_new_contact_data_header)
    new_contact_data = {}
    for key, value in new_contact_data_request.items():
        new_contact_data[key] = input(value)
    return new_contact_data

