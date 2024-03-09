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
                if s[i] =="0":
                    return False
                if s[i:].isdigit():
                    return True
            else:
                return True
    else:
        return False



main()