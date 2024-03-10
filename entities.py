from collections import UserDict
from datetime import datetime

from exceptions import BadPhoneNumberException, BadDateException
from get_birthday import get_birthdays_per_week


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(value) == 10 and value.isnumeric():
            self.value = value
        else:
            raise BadPhoneNumberException

    def __str__(self):
        return self.value


class Birthday(Field):
    def __init__(self, value):
        try:
            v = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(v)
        except ValueError:
            raise BadDateException

    def __str__(self):
        return self.value.strftime('%d.%m.%Y')


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone_value):
        for phone in self.phones:
            if phone.value == new_phone_value:
                phone.value = new_phone_value
                break

    def remove_phone(self, phone_to_delete):
        self.phones = filter(lambda phone: phone.value != phone_to_delete, self.phones)

    def find_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone.value:
                return phone

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)} birthday: {self.birthday if self.birthday else 'not set'}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        return get_birthdays_per_week(self.data.values())
