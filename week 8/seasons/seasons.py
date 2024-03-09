from datetime import date, timedelta
import re
import sys
import inflect

p = inflect.engine()


def main():
    year, month, day = get_date()
    age = convert(year, month, day)
    print(age + " minutes")


def get_date():
    date = input("Date of Birth: ").strip()
    if matches := re.search(r"^(\d{4})-([0][0-9]|1[0-2])-([0-2][0-9]|3[0-1])$", date):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return year, month, day
    else:
        sys.exit("Invalid date")

def convert(y, m, d):
    today = date.today()
    birthday = date(y, m, d)
    age = today - birthday
    age_min = round(age/timedelta(minutes=1))
    return p.number_to_words(age_min, andword="").capitalize()



if __name__ == "__main__":
    main()
