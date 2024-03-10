from commands import add_contact, change_contact, show_phone, add_birthday, show_birthday, show_birthdays, show_all
from file_io import load_data, save_data
from init_error import input_error


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == 'change':
                print(change_contact(args, book))
            elif command == 'phone':
                print(show_phone(args, book))
            elif command == 'add-birthday':
                print(add_birthday(args, book))
            elif command == 'show-birthday':
                print(show_birthday(args, book))
            elif command == 'birthdays':
                print(show_birthdays(book))
            elif command == 'all':
                print(show_all(book))
            else:
                print("Invalid command.")

        except Exception as e:
            if 'message' in e.__dict__:
                print(f"Error: {e.message}")
            else:
                print('Unknown error. Please try again.')


if __name__ == "__main__":
    main()
