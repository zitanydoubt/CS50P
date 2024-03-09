def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
        for i in range(2, len(s)):
            if s[i].isdigit():
                if s[i] == "0":
                    return False
                for j in range(i + 1, len(s)):
                    if s[j].isalpha():
                        return False
                else:
                    return True
            else:
                return True
        return True # returns two-letter plate true
    else:
        return False



if __name__ == "__main__":
    main()
