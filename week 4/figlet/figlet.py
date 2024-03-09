import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont (font=random.choice(fonts))
    print(figlet.renderText(input("Input: ")))

elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "-font":
    try:
        figlet.setFont (font=sys.argv[2])
    except IndexError:
        sys.exit("Invalid usage")
    else:
        print(figlet.renderText(input("Input: ")))
else:
    sys.exit("Invalid usage")

