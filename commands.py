from entities import Record
from init_error import input_error


@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name, phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, book):
    name, phone = args
    record = book.find(name)
    record.change_phone(phone)
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name, *rest = args
    record = contacts.find(name)

    return ', '.join(record.phones)


@input_error
def show_all(book):
    output = ''
    for record in book:
        output += str(book[record]) + '\n'

    return output


def add_birthday(args, book):
    name, birthday = args
    user = book.find(name)
    user.add_birthday(birthday)
    return "Birthday added."


def show_birthday(args, book):
    name, *rest = args
    user = book.find(name)
    return str(user.birthday)


def show_birthdays(book):
    birthdays = book.get_birthdays_per_week()
    return '\n'.join([f"{day}: {', '.join(birthdays[day])}" for day in birthdays])

