def main():
    t = convert(input("What time is it? "))

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)
    z = round(x + (y / 60), 2)
    return z


if __name__ == "__main__":
    main()


