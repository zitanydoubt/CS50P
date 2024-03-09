import sys
from PIL import (Image, ImageOps)
from os import path

def main():
    try:
        check(sys.argv)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        make_shirt(sys.argv[1], sys.argv[2])

def check(input):
    if len(input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(input) > 3:
        sys.exit("Too many command-line arguments")
    elif path.splitext(input[1])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    elif path.splitext(input[2])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    elif path.splitext(input[1])[1] != path.splitext(input[2])[1]:
        sys.exit("Input and output have different extensions")

def make_shirt(input, output):
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(input) as im:
        im_resize = ImageOps.fit(im, size)
        im_resize.paste(shirt, shirt)
        im_resize.save(output)

if __name__ == "__main__":
    main()
