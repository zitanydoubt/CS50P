import validators

email = input("Whats your email adress? ").strip().lower()
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
