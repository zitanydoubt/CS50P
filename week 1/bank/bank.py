grtng = input("Say something! ").strip().lower()

if grtng.startswith("hello"):
    print("$0")
elif grtng.startswith("h"):
    print("$20")
else:
    print("$100")