import pickle

from entities import AddressBook

filename = "phonebook.dat"


def save_data(data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_data():
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
