from collections import UserDict


class BadPhoneNumberException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = 'Invalid phone number. Should be 10 digits'


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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone_value):
        for phone in self.phones:
            if phone.value == new_phone_value:
                phone.value = new_phone_value
                break

    def remove_phone(self, phone_to_delete):
        self.phones = filter(lambda phone: phone.value != phone_to_delete, self.phones )

    def find_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone.value:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]
