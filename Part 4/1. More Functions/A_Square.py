def line(integer, string):

    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)


def square(size, character):

    num = 1
    while num <= size:
        line(size, character)
        num += 1


if __name__ == "__main__":
    
    square(5, "x")