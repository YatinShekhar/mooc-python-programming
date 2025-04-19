dict1 = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in dict1:
            print(dict1[name])
        else:
            print("no number")
        
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        dict1[name] = number
        print("ok!")

    elif command == 3:
        break 

print("quitting...")