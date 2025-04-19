num = int(input("Please type in a positive number: "))

for i in range(-1 * num, num + 1):
    if i == 0:
        continue
    print(i)