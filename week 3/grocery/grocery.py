grocery_list = {}

while True:
    try:
        item = input().upper().strip()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

sorted_grocery_list = dict(sorted(grocery_list.items()))

for grocery, amount in sorted_grocery_list.items():
    print(amount, grocery)