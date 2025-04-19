items = []
print(f"The list is now {items}")

n = 1
while True:
    operation = input("a(d)d, (r)emove or e(x)it: ")
    
    if operation == "x":
        print("Bye!")
        break
    else:
        if operation == "d":
            items.append(n)
            n += 1
        elif operation == "r":
            items.pop()
            n -= 1
        
        print(f"The list is now {items}")