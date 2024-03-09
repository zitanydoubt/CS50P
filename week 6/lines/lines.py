import sys

counter = 0

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py"):
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.isspace():
                    continue
                else:
                    counter += 1
    else:
        sys.exit("Not a Python file")
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(counter)
