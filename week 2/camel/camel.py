def main():
    camel = input("Camel Case: ")
    snake = make_snake(camel)
    print(f"Snake Case: {snake}")

def make_snake(word):
    snake_word = ""
    for index in range(len(word)):
        if word[index].isupper():
            snake_word += "_"
        snake_word += word[index].lower()
    return snake_word


main ()


