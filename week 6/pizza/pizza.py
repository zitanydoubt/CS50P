from csv import reader
import sys
from tabulate import tabulate

menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv"):
    try:
        with open (sys.argv[1]) as file:
            reader = reader(file)
            for row in reader:
                menu.append([row[0], row[1], row[2]])
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

print(tabulate(menu, headers = "firstrow", tablefmt = "grid"))
