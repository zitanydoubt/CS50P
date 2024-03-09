def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
        str_x, str_y = fraction.split("/")
        x = int(str_x)
        y = int(str_y)
        if y > 0 and x > y: # y > 0 because otherwise ZeroDivisionError would have to be raised seperately
            raise ValueError
        return round(x / y * 100)


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
