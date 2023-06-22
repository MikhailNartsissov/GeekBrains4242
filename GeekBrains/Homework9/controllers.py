from views import menu, get_new_contact_data
from models import (
    open_phonebook, save_phonebook, add_contact, find_contact,
    change_contact, show_contacts, delete_contact
)


def start_main_app() -> None:
    """
        Starts main menu function
    """
    choice = menu()
    while choice != 0:
        match choice:
            case 1:
                open_phonebook()
            case 2:
                save_phonebook()
            case 3:
                show_contacts()
            case 4:
                add_contact(get_new_contact_data())
            case 5:
                find_contact()
            case 6:
                change_contact()
            case 7:
                delete_contact()
        choice = menu()
