amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    amount = int(input("Insert Coin: "))
    if amount  in [5, 10, 25]:
        amount_due -= amount
if amount_due <= 0:
    print(f"Change Owed: {0-amount_due}")
