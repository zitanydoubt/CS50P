import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if matches := re.search(r"^([1-9]|[1][0-2])\:?([0-5][0-9])? (AM|PM) to ([1-9]|[1][0-2])\:?([0-5][0-9])? (AM|PM)$", s.strip(), re.IGNORECASE):
        begin_h = int(matches.group(1))
        if matches.group(3) == "PM":
            if begin_h == 12:
                begin_h = 12
            else:
                begin_h += 12
        if begin_h == 12 and matches.group(3) == "AM":
            begin_h = 0
        try:
            begin_min = int(matches.group(2))
        except TypeError:
            begin_min = 0
        end_h = int(matches.group(4))
        if matches.group(6) == "PM":
            if end_h == 12:
                end_h = 12
            else:
                end_h += 12
        if end_h == 12 and matches.group(6) == "AM":
            end_h = 0
        try:
            end_min = int(matches.group(5))
        except TypeError:
            end_min = 0
        return (f"{begin_h:02}:{begin_min:02} to {end_h:02}:{end_min:02}")
    else:
        raise ValueError






if __name__ == "__main__":
    main()
