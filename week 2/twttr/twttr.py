word = input("Input: ")
vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
print("Output: ", end="")
for letter in word:
    if letter in vowel:
        print("", end="")
    else:
        print(letter, end="")
print()