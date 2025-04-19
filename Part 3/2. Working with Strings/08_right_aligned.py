string1 = input("Please type in a string: ")

if len(string1) < 20:
    string2 = "*"*(20 - len(string1))
    print(string2+string1)
else:
    print(string1[:20])