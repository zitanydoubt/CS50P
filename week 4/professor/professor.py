import random


def main():
    i = 0
    score = 0
    level = get_level()
    while i < 10:
        attempts = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while attempts < 3:
            try:
                result = int(input(f"{x} + {y} = "))
                if result == (x + y):
                    i += 1
                    attempts = 3
                    score += 1
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                attempts += 1
                if attempts == 3:
                    print(f"{x} + {y} = {x+y}")
                    i += 1
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
