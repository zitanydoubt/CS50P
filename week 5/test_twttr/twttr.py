def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    twttr = ""
    for letter in word:
        if letter not in vowel:
            twttr += letter
    return twttr

if __name__ == "__main__":
    main()
