import inflect
p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

print("\nAdieu, adieu, to", p.join(names))
