x, y, z = input("Exression: ").split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = round((x + z), 1)
    print(f"result: {result}")
elif y == "-":
    result = round((x - z), 1)
    print(f"result: {result}")
elif y == "*":
    result = round((x * z), 1)
    print(f"result: {result}")
elif y == "/":
    result = round((x / z), 1)
    print(f"result: {result}")
