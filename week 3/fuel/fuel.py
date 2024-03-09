def main():
    x, y = get_fuel("Fraction: ")
    fraction = round(x / y * 100)
    if fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction}%")

def get_fuel(prompt):
    while True:
        try:
            str_x, str_y = input(prompt).split("/")
            x = int(str_x)
            y = int(str_y)
            if x <= y:
                return x,y
        except (ValueError, ZeroDivisionError):
            pass



main ()