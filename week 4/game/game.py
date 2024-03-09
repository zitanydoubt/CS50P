from random import randint

while True:
    try:
        level = int(input("Level: "))
        random_number = randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess in range(1, level+1):
                    if guess < random_number:
                        print("Too small!")
                    elif guess > random_number:
                        print("Too large!")
                    elif guess == random_number:
                        print("Just right!")
                        break
                else:
                    raise ValueError
            except ValueError:
                pass
    except ValueError:
        pass
    else:
        break

