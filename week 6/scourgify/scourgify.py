import sys
from csv import (DictReader, DictWriter)

names = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv"):
    try:
        with open (sys.argv[1]) as file:
            reader = DictReader(file)
            with open (sys.argv[2], "w") as file:
                        writer = DictWriter(file, fieldnames=["first", "last", "house"])
                        writer.writeheader()
                        for row in reader:
                            last, first = row["name"].split(sep = ", ")
                            house = row["house"]
                            writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


