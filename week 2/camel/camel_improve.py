camel = input("Camel Case: ")
print("Snake Case: ", end="")

for character in camel:
    if character.isupper():
            print("_" + character.lower(), end="")

    else:
        print(character, end="")

print ()