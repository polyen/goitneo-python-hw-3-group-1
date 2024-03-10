def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and/or phone please."
        except KeyError:
            return "Enter correct user name"
        except IndexError:
            return "Unknown name"

    return inner
