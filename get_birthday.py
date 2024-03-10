from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(users):
    output = defaultdict(list)
    today = datetime.today().date()

    for user in users:

        if not user.birthday:
            continue

        birthday = user.birthday.value

        this_year_birthday = birthday.replace(year=today.year).date()

        if this_year_birthday < today:
            this_year_birthday = this_year_birthday.replace(year=today.year + 1)

        delta_days = (this_year_birthday - today).days

        if delta_days > 7:
            continue

        day_name = this_year_birthday.strftime('%A')

        if this_year_birthday.weekday() > 5:
            day_name = 'Next Monday' if today.weekday() == 0 else 'Monday'

        output[day_name].append(user.name.value)

    return output
