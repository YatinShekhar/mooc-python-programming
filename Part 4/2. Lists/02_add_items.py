no_of_items = int(input("How many items? "))

n = 1
items = []
while n <= no_of_items:
    item = int(input(f"Item {n}: "))
    items.append(item)
    n += 1

print(items)