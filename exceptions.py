class BadPhoneNumberException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = 'Invalid phone number. Should be 10 digits'


class BadDateException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = 'Invalid date format. Should be DD.MM.YYYY'
